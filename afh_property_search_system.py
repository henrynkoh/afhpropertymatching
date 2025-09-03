#!/usr/bin/env python3
"""
Washington State AFH Property Search System
Automated daily search for rambler-style homes suitable for AFH conversion
in Lewis, Thurston, Pierce, and King counties.

Compliance Notes:
- Uses licensed MLS data feeds via RESO Web API
- Respects NWMLS Data Use Compliance Policy
- No scraping of Redfin/Zillow (prohibited by ToS)
- County permit verification via official APIs where available

Author: AFH Property Matching Service
Date: 2024
"""

import requests
import json
import logging
import schedule
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('afh_search.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class PropertyMatch:
    """Data structure for AFH potential property matches"""
    address: str
    city: str
    county: str
    price: float
    beds: int
    baths: float
    sqft: int
    lot_size: float
    year_built: int
    property_type: str
    afh_potential_score: int  # 1-100
    afh_readiness_level: str  # "ready", "approved", "potential"
    key_features: List[str]
    county_permit_status: Optional[str]
    mls_id: str
    listing_url: str
    last_updated: datetime

class AFHPropertySearcher:
    """
    Main class for searching and scoring properties for AFH potential
    """
    
    def __init__(self, config_file: str = "config.json"):
        """Initialize the searcher with configuration"""
        self.config = self._load_config(config_file)
        self.counties = ["Lewis", "Thurston", "Pierce", "King"]
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AFH-Property-Search/1.0 (Compliant MLS Data User)'
        })
        
    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file {config_file} not found. Using defaults.")
            return {
                "mls_api": {
                    "base_url": "https://api.mlsgrid.com/v2",
                    "api_key": "YOUR_MLS_GRID_API_KEY"
                },
                "email": {
                    "smtp_server": "smtp.gmail.com",
                    "smtp_port": 587,
                    "username": "your_email@gmail.com",
                    "password": "your_app_password"
                },
                "county_apis": {
                    "king_county": "https://gis.kingcounty.gov/arcgis/rest/services",
                    "pierce_county": "https://pals.piercecountywa.gov/publicgis/rest/services",
                    "thurston_county": "https://services.arcgis.com/your_thurston_endpoint",
                    "lewis_county": "https://parcels.lewiscountywa.gov/api"
                }
            }
    
    def search_rambler_properties(self, county: str) -> List[PropertyMatch]:
        """
        Search for rambler-style properties in specified county
        Uses licensed MLS data feed via RESO Web API
        """
        logger.info(f"Searching for rambler properties in {county} County")
        
        # RESO Web API query parameters for rambler/single-level homes
        query_params = {
            "select": "ListingId,ListPrice,BedroomsTotal,BathroomsTotalInteger,LivingArea,"
                     "LotSizeAcres,YearBuilt,PropertyType,StreetName,City,StateOrProvince,"
                     "PostalCode,PropertySubType,StandardStatus,ListingContractDate,"
                     "ModificationTimestamp,PublicRemarks,UnparsedAddress",
            "filter": f"StateOrProvince eq 'WA' and City eq '{county}' and "
                     f"(PropertySubType eq 'Single Family Residential' or "
                     f"PropertySubType eq 'Ranch') and "
                     f"(PublicRemarks contains 'single level' or "
                     f"PublicRemarks contains 'rambler' or "
                     f"PublicRemarks contains 'no stairs' or "
                     f"PropertySubType eq 'Ranch') and "
                     f"StandardStatus eq 'Active'",
            "orderby": "ModificationTimestamp desc",
            "top": 50
        }
        
        try:
            # Make authenticated request to MLS GRID API
            response = self.session.get(
                f"{self.config['mls_api']['base_url']}/Property",
                params=query_params,
                headers={
                    'Authorization': f"Bearer {self.config['mls_api']['api_key']}",
                    'Accept': 'application/json'
                },
                timeout=30
            )
            response.raise_for_status()
            
            data = response.json()
            properties = []
            
            for listing in data.get('value', []):
                property_match = self._create_property_match(listing, county)
                if property_match:
                    properties.append(property_match)
            
            logger.info(f"Found {len(properties)} potential rambler properties in {county}")
            return properties
            
        except requests.RequestException as e:
            logger.error(f"Error searching properties in {county}: {e}")
            return []
    
    def _create_property_match(self, listing: Dict, county: str) -> Optional[PropertyMatch]:
        """Convert MLS listing to PropertyMatch object with AFH scoring"""
        try:
            # Extract basic property information
            address = listing.get('UnparsedAddress', 'Address not available')
            price = float(listing.get('ListPrice', 0))
            beds = int(listing.get('BedroomsTotal', 0))
            baths = float(listing.get('BathroomsTotalInteger', 0))
            sqft = int(listing.get('LivingArea', 0))
            lot_size = float(listing.get('LotSizeAcres', 0))
            year_built = int(listing.get('YearBuilt', 0))
            property_type = listing.get('PropertySubType', '')
            remarks = listing.get('PublicRemarks', '')
            mls_id = listing.get('ListingId', '')
            
            # Calculate AFH potential score
            afh_score, readiness_level, key_features = self._calculate_afh_potential(
                beds, baths, sqft, lot_size, year_built, remarks, address
            )
            
            # Only include properties with reasonable AFH potential (score >= 40)
            if afh_score < 40:
                return None
            
            # Check county permit status
            permit_status = self._check_county_permit_status(address, county)
            
            return PropertyMatch(
                address=address,
                city=county,
                county=county,
                price=price,
                beds=beds,
                baths=baths,
                sqft=sqft,
                lot_size=lot_size,
                year_built=year_built,
                property_type=property_type,
                afh_potential_score=afh_score,
                afh_readiness_level=readiness_level,
                key_features=key_features,
                county_permit_status=permit_status,
                mls_id=mls_id,
                listing_url=f"https://www.nwmls.com/listing/{mls_id}",
                last_updated=datetime.now()
            )
            
        except (ValueError, KeyError) as e:
            logger.warning(f"Error processing listing {listing.get('ListingId', 'unknown')}: {e}")
            return None
    
    def _calculate_afh_potential(self, beds: int, baths: float, sqft: int, 
                               lot_size: float, year_built: int, 
                               remarks: str, address: str) -> tuple:
        """
        Calculate AFH potential score based on Washington State requirements
        Based on WAC 388-76 and WABO AFH Building Inspection Checklist
        """
        score = 0
        features = []
        readiness_level = "potential"
        
        # Bedroom requirements (minimum 3 for 6 residents)
        if beds >= 3:
            score += 20
            features.append(f"{beds} bedrooms")
        elif beds >= 2:
            score += 10
            features.append(f"{beds} bedrooms (may need addition)")
        
        # Bathroom requirements (minimum 2 for 6 residents)
        if baths >= 2:
            score += 15
            features.append(f"{baths} bathrooms")
        elif baths >= 1.5:
            score += 10
            features.append(f"{baths} bathrooms (may need upgrade)")
        
        # Square footage (adequate space for 6 residents)
        if sqft >= 2000:
            score += 15
            features.append(f"{sqft:,} sq ft")
        elif sqft >= 1500:
            score += 10
            features.append(f"{sqft:,} sq ft (adequate)")
        
        # Lot size (space for ramps, parking, accessibility)
        if lot_size >= 0.25:  # 1/4 acre
            score += 10
            features.append(f"{lot_size:.2f} acre lot")
        elif lot_size >= 0.15:
            score += 5
            features.append(f"{lot_size:.2f} acre lot")
        
        # Single-level/rambler indicators
        rambler_keywords = ['single level', 'rambler', 'ranch', 'no stairs', 
                           'one level', 'single story']
        if any(keyword in remarks.lower() for keyword in rambler_keywords):
            score += 25
            features.append("Single-level design")
            readiness_level = "approved"  # Higher potential if confirmed single-level
        
        # Age of construction (newer homes more likely to meet current codes)
        if year_built >= 2000:
            score += 10
            features.append(f"Built {year_built}")
        elif year_built >= 1980:
            score += 5
            features.append(f"Built {year_built}")
        
        # Accessibility features mentioned
        accessibility_keywords = ['wheelchair', 'accessible', 'handicap', 'ada', 
                                'wide door', 'ramp', 'grab bar']
        if any(keyword in remarks.lower() for keyword in accessibility_keywords):
            score += 15
            features.append("Accessibility features")
            readiness_level = "ready"  # Highest potential if accessibility features exist
        
        # Proximity to medical facilities (heuristic based on address)
        medical_areas = ['olympia', 'tacoma', 'seattle', 'bellevue', 'kent', 
                        'federal way', 'auburn', 'renton', 'kirkland']
        if any(area in address.lower() for area in medical_areas):
            score += 5
            features.append("Near medical facilities")
        
        return score, readiness_level, features
    
    def _check_county_permit_status(self, address: str, county: str) -> Optional[str]:
        """
        Check county permit records for AFH-related permits
        Uses official county APIs where available
        """
        try:
            if county == "King":
                return self._check_king_county_permits(address)
            elif county == "Pierce":
                return self._check_pierce_county_permits(address)
            elif county == "Thurston":
                return self._check_thurston_county_permits(address)
            elif county == "Lewis":
                return self._check_lewis_county_permits(address)
        except Exception as e:
            logger.warning(f"Error checking permits for {address} in {county}: {e}")
        
        return None
    
    def _check_king_county_permits(self, address: str) -> Optional[str]:
        """Check King County permit records"""
        # Implementation would use King County's official API
        # This is a placeholder for the actual API integration
        return "Permit check available via King County Parcel Viewer"
    
    def _check_pierce_county_permits(self, address: str) -> Optional[str]:
        """Check Pierce County permit records"""
        # Implementation would use Pierce County's PALS system
        return "Permit check available via Pierce County PALS"
    
    def _check_thurston_county_permits(self, address: str) -> Optional[str]:
        """Check Thurston County permit records"""
        # Implementation would use Thurston County's permit system
        return "Permit check available via Thurston County Permits"
    
    def _check_lewis_county_permits(self, address: str) -> Optional[str]:
        """Check Lewis County permit records"""
        # Implementation would use Lewis County's parcel system
        return "Permit check available via Lewis County Parcels"
    
    def send_daily_alerts(self, properties: List[PropertyMatch]):
        """Send daily email alerts with new property matches"""
        if not properties:
            logger.info("No new properties to alert about")
            return
        
        # Group properties by county
        county_groups = {}
        for prop in properties:
            if prop.county not in county_groups:
                county_groups[prop.county] = []
            county_groups[prop.county].append(prop)
        
        # Create email content
        subject = f"AFH Property Alerts - {len(properties)} New Matches Found"
        body = self._create_email_body(county_groups)
        
        # Send email to configured recipients
        recipients = self.config.get('email_recipients', [])
        for recipient in recipients:
            self._send_email(recipient, subject, body)
        
        logger.info(f"Sent alerts to {len(recipients)} recipients about {len(properties)} properties")
    
    def _create_email_body(self, county_groups: Dict[str, List[PropertyMatch]]) -> str:
        """Create HTML email body with property listings"""
        html = """
        <html>
        <head>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .county-section { margin-bottom: 30px; }
                .property { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
                .property-header { font-weight: bold; color: #2c5aa0; }
                .property-details { margin: 10px 0; }
                .afh-score { background-color: #e8f4fd; padding: 5px; border-radius: 3px; }
                .ready { background-color: #d4edda; }
                .approved { background-color: #fff3cd; }
                .potential { background-color: #f8d7da; }
            </style>
        </head>
        <body>
            <h2>🏠 AFH Property Search Results</h2>
            <p>Found <strong>{total_properties}</strong> new properties with AFH potential across {county_count} counties.</p>
        """.format(
            total_properties=sum(len(props) for props in county_groups.values()),
            county_count=len(county_groups)
        )
        
        for county, properties in county_groups.items():
            html += f"""
            <div class="county-section">
                <h3>📍 {county} County ({len(properties)} properties)</h3>
            """
            
            for prop in properties:
                score_class = prop.afh_readiness_level
                html += f"""
                <div class="property">
                    <div class="property-header">{prop.address}</div>
                    <div class="property-details">
                        <strong>${prop.price:,.0f}</strong> | {prop.beds} bed, {prop.baths} bath | {prop.sqft:,} sq ft
                        <br>Built {prop.year_built} | {prop.lot_size:.2f} acres
                        <br><span class="afh-score {score_class}">AFH {prop.afh_readiness_level.upper()} - Score: {prop.afh_potential_score}/100</span>
                        <br>Key Features: {', '.join(prop.key_features)}
                        <br><a href="{prop.listing_url}" target="_blank">View Listing</a>
                    </div>
                </div>
                """
            
            html += "</div>"
        
        html += """
            <hr>
            <p><small>
                This automated search uses licensed MLS data and complies with NWMLS Data Use Policy.
                Always verify property details and consult with local building officials before making offers.
                <br><a href="https://ttdhezcf.gensparkspace.com/">View Full AFH Resource Dashboard</a>
            </small></p>
        </body>
        </html>
        """
        
        return html
    
    def _send_email(self, recipient: str, subject: str, body: str):
        """Send email notification"""
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.config['email']['username']
            msg['To'] = recipient
            
            html_part = MIMEText(body, 'html')
            msg.attach(html_part)
            
            with smtplib.SMTP(self.config['email']['smtp_server'], 
                            self.config['email']['smtp_port']) as server:
                server.starttls()
                server.login(self.config['email']['username'], 
                           self.config['email']['password'])
                server.send_message(msg)
            
            logger.info(f"Email sent to {recipient}")
            
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {e}")
    
    def run_daily_search(self):
        """Main method to run daily property search across all counties"""
        logger.info("Starting daily AFH property search")
        
        all_properties = []
        
        for county in self.counties:
            properties = self.search_rambler_properties(county)
            all_properties.extend(properties)
        
        # Filter for high-potential properties (score >= 60)
        high_potential = [p for p in all_properties if p.afh_potential_score >= 60]
        
        if high_potential:
            logger.info(f"Found {len(high_potential)} high-potential properties")
            self.send_daily_alerts(high_potential)
        else:
            logger.info("No high-potential properties found today")
        
        # Save results to database/file for tracking
        self._save_search_results(all_properties)
        
        return all_properties
    
    def _save_search_results(self, properties: List[PropertyMatch]):
        """Save search results for tracking and analysis"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"afh_search_results_{timestamp}.json"
        
        results = {
            "search_date": datetime.now().isoformat(),
            "total_properties": len(properties),
            "counties_searched": self.counties,
            "properties": [
                {
                    "address": p.address,
                    "county": p.county,
                    "price": p.price,
                    "beds": p.beds,
                    "baths": p.baths,
                    "sqft": p.sqft,
                    "afh_score": p.afh_potential_score,
                    "readiness_level": p.afh_readiness_level,
                    "key_features": p.key_features,
                    "mls_id": p.mls_id,
                    "listing_url": p.listing_url
                }
                for p in properties
            ]
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
            logger.info(f"Search results saved to {filename}")
        except Exception as e:
            logger.error(f"Failed to save results: {e}")

def main():
    """Main execution function"""
    searcher = AFHPropertySearcher()
    
    # Schedule daily search at 6:00 AM PST
    schedule.every().day.at("06:00").do(searcher.run_daily_search)
    
    logger.info("AFH Property Search System started. Daily searches scheduled for 6:00 AM PST.")
    logger.info("Press Ctrl+C to stop.")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logger.info("AFH Property Search System stopped.")

if __name__ == "__main__":
    main()
