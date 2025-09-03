# 📖 AFH Property Matching Service - Complete Manual

**The Definitive Guide to Operating Your AFH Property Matching System**

## Table of Contents

1. [System Overview](#system-overview)
2. [Installation & Configuration](#installation--configuration)
3. [Daily Operations](#daily-operations)
4. [Property Search & Scoring](#property-search--scoring)
5. [User Management](#user-management)
6. [Compliance & Legal](#compliance--legal)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Features](#advanced-features)
9. [Maintenance & Updates](#maintenance--updates)
10. [Best Practices](#best-practices)

---

## System Overview

### What This System Does

The AFH Property Matching Service is a comprehensive platform that:

1. **Searches Properties**: Daily automated searches across King, Pierce, Thurston, and Lewis counties
2. **Scores AFH Potential**: Uses a 100-point algorithm based on Washington State requirements
3. **Sends Alerts**: Email notifications for high-potential properties
4. **Provides Resources**: Curated dashboard with all AFH ecosystem links
5. **Ensures Compliance**: Built-in regulatory compliance and legal safeguards

### System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   MLS Data      │───▶│  Search Engine   │───▶│  AFH Scoring    │
│   (RESO API)    │    │  (Python)        │    │  Algorithm      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   County APIs   │───▶│  Notification    │───▶│  User Dashboard │
│   (Permits)     │    │  System          │    │  (Web)          │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### Key Components

- **Property Search Engine**: Python-based system with automated scheduling
- **AFH Scoring Algorithm**: 100-point system based on Washington State requirements
- **Notification System**: Email/SMS alerts for high-potential properties
- **Resource Dashboard**: Curated links to all AFH ecosystem resources
- **Compliance Framework**: Built-in regulatory compliance and legal safeguards

---

## Installation & Configuration

### Prerequisites

#### System Requirements
- **Operating System**: macOS 10.15+, Windows 10+, or Linux
- **Python**: Version 3.8 or higher
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 10GB free disk space
- **Network**: Stable internet connection for API access

#### Required Accounts
- **MLS Access**: NWMLS broker license or MLS GRID subscription
- **Email Account**: Gmail or other SMTP-compatible email
- **County Access**: Optional access to county permit systems

### Installation Steps

#### 1. Download and Extract
```bash
# Download the system files
wget https://github.com/your-repo/afh-property-matching/archive/main.zip
unzip main.zip
cd afh-property-matching-main
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv afh_env

# Activate virtual environment
# On macOS/Linux:
source afh_env/bin/activate
# On Windows:
afh_env\Scripts\activate
```

#### 3. Install Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

#### 4. Configure System
```bash
# Copy configuration template
cp config.json.example config.json

# Edit configuration file
nano config.json  # or use your preferred editor
```

### Configuration Details

#### MLS API Configuration
```json
{
  "mls_api": {
    "base_url": "https://api.mlsgrid.com/v2",
    "api_key": "YOUR_ACTUAL_API_KEY_HERE",
    "rate_limit": 1000,
    "timeout": 30,
    "broker_license": "YOUR_LICENSE_NUMBER",
    "nwmls_member_id": "YOUR_MEMBER_ID"
  }
}
```

#### Email Configuration
```json
{
  "email": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "your_email@gmail.com",
    "password": "your_app_password_here",
    "use_tls": true
  }
}
```

#### Search Criteria Configuration
```json
{
  "search_criteria": {
    "min_afh_score": 40,
    "high_potential_score": 60,
    "max_price": 800000,
    "min_bedrooms": 2,
    "min_bathrooms": 1.5,
    "min_sqft": 1200,
    "min_lot_size": 0.1,
    "max_age": 50,
    "target_counties": ["Lewis", "Thurston", "Pierce", "King"]
  }
}
```

### Testing Installation

#### 1. Test Basic Functionality
```bash
# Test imports
python -c "import requests, schedule, json; print('✅ Dependencies working')"

# Test configuration
python -c "import json; print(json.load(open('config.json')))"
```

#### 2. Test MLS API Access
```bash
# Test API connectivity
python afh_property_search_system.py --test-api
```

#### 3. Test Email System
```bash
# Test email notifications
python afh_property_search_system.py --test-email
```

---

## Daily Operations

### Starting the System

#### Manual Start
```bash
# Activate virtual environment
source afh_env/bin/activate

# Start the system
python afh_property_search_system.py
```

#### Automated Start (Recommended)
```bash
# Set up cron job for daily 6:00 AM PST searches
crontab -e

# Add this line:
0 6 * * * cd /path/to/afh-property-matching && /path/to/python afh_property_search_system.py
```

### Daily Workflow

#### 1. System Startup (6:00 AM PST)
- Check MLS API connectivity
- Verify email system status
- Load configuration settings
- Initialize logging system

#### 2. Property Search (6:05 AM PST)
- Query MLS data for each target county
- Apply rambler/single-level filters
- Retrieve property details and photos
- Cross-reference with county permit data

#### 3. AFH Scoring (6:15 AM PST)
- Apply scoring algorithm to each property
- Classify readiness level (ready/approved/potential)
- Identify key features and potential issues
- Generate confidence scores

#### 4. Alert Generation (6:20 AM PST)
- Filter high-potential properties (score ≥60)
- Create HTML email with property details
- Include county parcel viewer links
- Send to subscribed users

#### 5. Data Storage (6:25 AM PST)
- Save search results to timestamped files
- Update property status tracking
- Maintain compliance audit trail
- Generate daily summary reports

### Monitoring System Health

#### Check System Status
```bash
# View real-time logs
tail -f afh_search.log

# Check recent search results
ls -la afh_search_results_*.json

# View system status
python afh_property_search_system.py --status
```

#### Key Metrics to Monitor
- **API Response Times**: Should be <2 seconds
- **Search Success Rate**: Should be >95%
- **Email Delivery Rate**: Should be >98%
- **System Uptime**: Should be >99%

---

## Property Search & Scoring

### Search Criteria

#### Property Type Filters
- **Property Type**: Single-family residential
- **Subtype**: Ranch, rambler, single-level
- **Keywords**: "single level", "rambler", "no stairs", "one level"
- **Status**: Active listings only

#### Geographic Filters
- **Counties**: Lewis, Thurston, Pierce, King
- **Price Range**: Up to $800,000 (configurable)
- **Lot Size**: Minimum 0.1 acres
- **Age**: Maximum 50 years old

#### AFH-Specific Filters
- **Bedrooms**: Minimum 2 (prefer 3+)
- **Bathrooms**: Minimum 1.5 (prefer 2+)
- **Square Footage**: Minimum 1,200 sq ft
- **Accessibility**: Single-level or ramp-accessible

### AFH Scoring Algorithm

#### Scoring Components (100-point scale)

##### 1. Bedroom Requirements (20 points)
- **3+ bedrooms**: 20 points
- **2 bedrooms**: 10 points
- **<2 bedrooms**: 0 points

*Rationale: AFHs need 3+ bedrooms for 6 residents plus caregiver quarters*

##### 2. Bathroom Requirements (15 points)
- **2+ bathrooms**: 15 points
- **1.5 bathrooms**: 10 points
- **<1.5 bathrooms**: 0 points

*Rationale: DSHS requires adequate bathroom facilities for residents*

##### 3. Square Footage (15 points)
- **2000+ sq ft**: 15 points
- **1500-1999 sq ft**: 10 points
- **1200-1499 sq ft**: 5 points
- **<1200 sq ft**: 0 points

*Rationale: Adequate space for 6 residents plus common areas*

##### 4. Lot Size (10 points)
- **0.25+ acres**: 10 points
- **0.15-0.24 acres**: 5 points
- **0.1-0.14 acres**: 2 points
- **<0.1 acres**: 0 points

*Rationale: Space for ramps, parking, and accessibility features*

##### 5. Single-Level Design (25 points)
- **Confirmed rambler**: 25 points
- **Potential single-level**: 15 points
- **Multi-level**: 0 points

*Rationale: Single-level design is ideal for AFH operations*

##### 6. Construction Age (10 points)
- **2000+**: 10 points
- **1980-1999**: 5 points
- **1960-1979**: 2 points
- **<1960**: 0 points

*Rationale: Newer construction more likely to meet current codes*

##### 7. Accessibility Features (15 points)
- **Mentioned in listing**: 15 points
- **Not mentioned**: 0 points

*Rationale: Existing accessibility features reduce conversion costs*

##### 8. Medical Proximity (5 points)
- **Near medical facilities**: 5 points
- **Other locations**: 0 points

*Rationale: Proximity to medical care is important for AFH operations*

### Readiness Classification

#### AFH-Ready (80-100 points)
- Existing AFH permits or licenses
- Accessibility features already installed
- Meets all DSHS requirements
- Ready for immediate operation

#### WABO-Approved (60-79 points)
- Single-level design confirmed
- Good potential for AFH conversion
- May need minor modifications
- Likely to pass WABO inspection

#### AFH-Potential (40-59 points)
- Requires assessment and modifications
- May need significant changes
- Feasible but higher conversion costs
- Requires professional evaluation

### Customizing the Scoring Algorithm

#### Adjusting Weights
```json
{
  "afh_scoring_weights": {
    "bedrooms": 25,              // Increase bedroom importance
    "bathrooms": 20,             // Increase bathroom importance
    "square_footage": 15,        // Keep current
    "lot_size": 10,              // Keep current
    "single_level": 20,          // Decrease single-level importance
    "construction_age": 5,       // Decrease age importance
    "accessibility_features": 20, // Increase accessibility importance
    "medical_proximity": 5       // Keep current
  }
}
```

#### Adding New Criteria
```python
def _calculate_afh_potential(self, beds, baths, sqft, lot_size, year_built, remarks, address):
    # ... existing code ...
    
    # Add new criteria: proximity to public transportation
    transit_keywords = ['bus', 'transit', 'metro', 'light rail']
    if any(keyword in remarks.lower() for keyword in transit_keywords):
        score += 5
        features.append("Public transportation access")
    
    return score, readiness_level, features
```

---

## User Management

### User Types

#### 1. Basic Subscribers
- **Access**: Daily property alerts
- **Features**: Email notifications, basic dashboard
- **Cost**: $99/month
- **Limits**: Up to 5 property alerts per day

#### 2. Professional Subscribers
- **Access**: Unlimited property alerts + county permit data
- **Features**: Advanced filtering, priority support
- **Cost**: $199/month
- **Limits**: No daily limits

#### 3. Enterprise Subscribers
- **Access**: Custom integrations + priority support
- **Features**: API access, custom reporting
- **Cost**: $399/month
- **Limits**: Custom based on needs

### User Onboarding

#### 1. Registration Process
```python
def register_user(email, user_type, preferences):
    # Validate email address
    if not validate_email(email):
        return {"error": "Invalid email address"}
    
    # Create user profile
    user_profile = {
        "email": email,
        "user_type": user_type,
        "preferences": preferences,
        "created_date": datetime.now(),
        "status": "active"
    }
    
    # Save to database
    save_user_profile(user_profile)
    
    # Send welcome email
    send_welcome_email(email, user_type)
    
    return {"success": "User registered successfully"}
```

#### 2. Preference Configuration
```json
{
  "user_preferences": {
    "target_counties": ["King", "Pierce"],
    "max_price": 600000,
    "min_afh_score": 70,
    "property_types": ["rambler", "ranch"],
    "notification_frequency": "daily",
    "email_format": "html"
  }
}
```

### User Communication

#### Email Templates

##### Daily Alert Template
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .property { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .property-header { font-weight: bold; color: #2c5aa0; }
        .afh-score { background-color: #e8f4fd; padding: 5px; border-radius: 3px; }
        .ready { background-color: #d4edda; }
        .approved { background-color: #fff3cd; }
        .potential { background-color: #f8d7da; }
    </style>
</head>
<body>
    <h2>🏠 AFH Property Search Results</h2>
    <p>Found <strong>{total_properties}</strong> new properties with AFH potential.</p>
    
    <!-- Property listings -->
    
    <hr>
    <p><small>
        This automated search uses licensed MLS data and complies with NWMLS Data Use Policy.
        Always verify property details and consult with local building officials before making offers.
    </small></p>
</body>
</html>
```

##### Weekly Summary Template
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .summary-stats { background-color: #f8f9fa; padding: 20px; border-radius: 5px; }
        .stat-item { display: inline-block; margin: 10px; text-align: center; }
        .stat-number { font-size: 24px; font-weight: bold; color: #2c5aa0; }
        .stat-label { font-size: 14px; color: #666; }
    </style>
</head>
<body>
    <h2>📊 Weekly AFH Property Search Summary</h2>
    
    <div class="summary-stats">
        <div class="stat-item">
            <div class="stat-number">{total_properties}</div>
            <div class="stat-label">Properties Found</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{high_potential}</div>
            <div class="stat-label">High Potential</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">{avg_score}</div>
            <div class="stat-label">Average Score</div>
        </div>
    </div>
    
    <!-- Weekly highlights -->
    
</body>
</html>
```

---

## Compliance & Legal

### Regulatory Compliance

#### Washington State Requirements
- **WAC 388-76**: Adult Family Home Minimum Licensing Requirements
- **RCW 70.128**: Adult Family Homes statute
- **DSHS Guidelines**: Department of Social and Health Services requirements
- **WABO Standards**: Washington Association of Building Officials

#### Key Compliance Points
1. **Capacity Limits**: Default 6 residents, 7-8 with special approval
2. **Evacuation Standards**: 5-minute total evacuation time
3. **Insurance Requirements**: $500K per occurrence, $1M aggregate
4. **Building Codes**: 2021 IRC R330 compliance
5. **Accessibility**: ADA compliance and elder-care design principles

### Data Compliance

#### MLS Data Usage
- **NWMLS Data Use Policy**: Strict compliance required
- **Rate Limits**: Respect API rate limits (typically 1,000/day)
- **Display Rules**: Follow IDX/VOW participant rules
- **Data Retention**: 30-day maximum for search results

#### Prohibited Practices
- **No Scraping**: Redfin/Zillow automated access prohibited
- **No Bulk Downloads**: Mass data extraction not allowed
- **No Resale**: Cannot resell MLS data to third parties
- **No Unlicensed Display**: Cannot show data to unlicensed users

### Legal Safeguards

#### Terms of Service
```markdown
## AFH Property Matching Service - Terms of Service

### 1. Service Description
This service provides property matching for Adult Family Home providers in Washington State using licensed MLS data and county permit information.

### 2. User Responsibilities
- Users must verify all property information independently
- Users must consult with local building officials before making offers
- Users must comply with all applicable laws and regulations
- Users must not rely solely on automated scoring for property decisions

### 3. Data Accuracy
- Property information is provided "as is" from MLS and county sources
- We do not guarantee the accuracy of property details
- Users must verify all information before making decisions
- We are not responsible for errors in third-party data sources

### 4. Compliance Requirements
- Users must comply with all MLS data use policies
- Users must respect rate limits and usage guidelines
- Users must not attempt to scrape or bulk download data
- Users must maintain appropriate licenses for data access

### 5. Limitation of Liability
- Service provided for informational purposes only
- Not responsible for property purchase decisions
- Not responsible for licensing or regulatory compliance
- Not responsible for third-party data accuracy
```

#### Privacy Policy
```markdown
## Privacy Policy

### 1. Information Collection
- Email addresses for notifications
- Search preferences and criteria
- Usage statistics and analytics
- No personal property information stored

### 2. Information Use
- Send property alerts and notifications
- Improve service quality and features
- Comply with legal and regulatory requirements
- Provide customer support

### 3. Information Sharing
- No personal information shared with third parties
- Aggregate statistics may be used for marketing
- Information may be shared if required by law
- Information may be shared with MLS providers for compliance

### 4. Data Security
- All data encrypted in transit and at rest
- Access controls and authentication required
- Regular security audits and monitoring
- Incident response procedures in place

### 5. User Rights
- Right to access personal information
- Right to correct inaccurate information
- Right to delete personal information
- Right to opt-out of communications
```

---

## Troubleshooting

### Common Issues

#### 1. MLS API Authentication Error
```
Error: 401 Unauthorized
```

**Symptoms:**
- API requests return 401 status code
- "Invalid API key" error messages
- No property data retrieved

**Solutions:**
1. Verify API key in config.json is correct
2. Check if API key has expired
3. Confirm MLS GRID subscription is active
4. Contact MLS GRID support if issues persist

**Prevention:**
- Set up API key expiration monitoring
- Implement automatic key rotation
- Monitor API usage and limits

#### 2. Email Sending Failed
```
Error: SMTPAuthenticationError
```

**Symptoms:**
- Email notifications not sent
- SMTP authentication errors
- "Invalid credentials" messages

**Solutions:**
1. Check Gmail username/password in config.json
2. Ensure app password is used (not regular password)
3. Verify 2-factor authentication is enabled
4. Test SMTP connection manually

**Prevention:**
- Use app passwords for email authentication
- Monitor email delivery rates
- Set up email delivery monitoring

#### 3. No Properties Found
```
Warning: No properties found in [County]
```

**Symptoms:**
- Search returns empty results
- No properties match criteria
- County-specific search failures

**Solutions:**
1. Check internet connection
2. Verify MLS API is accessible
3. Review search criteria (may be too restrictive)
4. Check county-specific filters

**Prevention:**
- Implement fallback search criteria
- Monitor search success rates
- Set up alerting for empty results

#### 4. County API Errors
```
Warning: Error checking permits for [Address]
```

**Symptoms:**
- County permit checks fail
- API timeout errors
- Invalid response formats

**Solutions:**
1. Check county API status
2. Verify API endpoints are correct
3. Implement retry logic for failed requests
4. Use fallback data sources

**Prevention:**
- Monitor county API availability
- Implement circuit breaker patterns
- Set up health checks for county systems

### Diagnostic Tools

#### System Health Check
```bash
# Run comprehensive system check
python afh_property_search_system.py --health-check

# Check specific components
python afh_property_search_system.py --check-mls-api
python afh_property_search_system.py --check-email
python afh_property_search_system.py --check-county-apis
```

#### Log Analysis
```bash
# View error logs only
grep "ERROR" afh_search.log

# View recent activity
tail -20 afh_search.log

# Search for specific issues
grep "MLS API" afh_search.log
grep "Email" afh_search.log
grep "County" afh_search.log
```

#### Performance Monitoring
```bash
# Check system performance
python afh_property_search_system.py --performance-check

# Monitor resource usage
top -p $(pgrep -f afh_property_search_system.py)

# Check disk space
df -h
```

### Getting Help

#### Self-Service Resources
1. **Documentation**: Check this manual and other guides
2. **Log Files**: Review system logs for error messages
3. **Configuration**: Verify all settings are correct
4. **Testing**: Run diagnostic tools and tests

#### Professional Support
1. **Email Support**: support@afhmatcher.com
2. **Phone Support**: (425) 555-0123 (business hours)
3. **Emergency Support**: Available for critical issues
4. **Consulting Services**: Custom implementation help

---

## Advanced Features

### Custom Search Filters

#### Advanced Property Criteria
```python
def advanced_property_search(county, custom_criteria):
    """
    Advanced property search with custom criteria
    """
    base_filters = {
        "StateOrProvince": "WA",
        "City": county,
        "PropertySubType": "Single Family Residential",
        "StandardStatus": "Active"
    }
    
    # Add custom criteria
    if custom_criteria.get("min_price"):
        base_filters["ListPrice"] = f"ge {custom_criteria['min_price']}"
    
    if custom_criteria.get("max_price"):
        base_filters["ListPrice"] = f"le {custom_criteria['max_price']}"
    
    if custom_criteria.get("min_bedrooms"):
        base_filters["BedroomsTotal"] = f"ge {custom_criteria['min_bedrooms']}"
    
    if custom_criteria.get("min_bathrooms"):
        base_filters["BathroomsTotalInteger"] = f"ge {custom_criteria['min_bathrooms']}"
    
    return base_filters
```

#### Custom Scoring Weights
```python
def custom_scoring_weights(user_preferences):
    """
    Customize scoring weights based on user preferences
    """
    base_weights = {
        "bedrooms": 20,
        "bathrooms": 15,
        "square_footage": 15,
        "lot_size": 10,
        "single_level": 25,
        "construction_age": 10,
        "accessibility_features": 15,
        "medical_proximity": 5
    }
    
    # Adjust weights based on user preferences
    if user_preferences.get("prioritize_accessibility"):
        base_weights["accessibility_features"] = 25
        base_weights["single_level"] = 20
    
    if user_preferences.get("prioritize_size"):
        base_weights["square_footage"] = 25
        base_weights["lot_size"] = 15
    
    return base_weights
```

### API Integration

#### REST API Endpoints
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/properties/search', methods=['POST'])
def search_properties():
    """
    API endpoint for property search
    """
    data = request.get_json()
    
    # Validate input
    if not data.get('county'):
        return jsonify({"error": "County is required"}), 400
    
    # Perform search
    searcher = AFHPropertySearcher()
    properties = searcher.search_rambler_properties(data['county'])
    
    # Filter results
    if data.get('min_score'):
        properties = [p for p in properties if p.afh_potential_score >= data['min_score']]
    
    # Return results
    return jsonify({
        "properties": [p.__dict__ for p in properties],
        "total": len(properties)
    })

@app.route('/api/properties/score', methods=['POST'])
def score_property():
    """
    API endpoint for property scoring
    """
    data = request.get_json()
    
    # Validate input
    required_fields = ['beds', 'baths', 'sqft', 'lot_size', 'year_built', 'remarks', 'address']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    
    # Calculate score
    searcher = AFHPropertySearcher()
    score, readiness_level, features = searcher._calculate_afh_potential(
        data['beds'], data['baths'], data['sqft'], 
        data['lot_size'], data['year_built'], 
        data['remarks'], data['address']
    )
    
    return jsonify({
        "score": score,
        "readiness_level": readiness_level,
        "features": features
    })
```

#### Webhook Integration
```python
@app.route('/webhook/property-update', methods=['POST'])
def property_update_webhook():
    """
    Webhook for property updates
    """
    data = request.get_json()
    
    # Validate webhook signature
    if not verify_webhook_signature(request):
        return jsonify({"error": "Invalid signature"}), 401
    
    # Process property update
    property_id = data.get('property_id')
    update_type = data.get('update_type')
    
    if update_type == 'status_change':
        # Handle status change
        handle_property_status_change(property_id, data.get('new_status'))
    
    elif update_type == 'price_change':
        # Handle price change
        handle_property_price_change(property_id, data.get('new_price'))
    
    return jsonify({"status": "success"})
```

### Database Integration

#### SQLite Database Setup
```python
import sqlite3
from datetime import datetime

class AFHDatabase:
    def __init__(self, db_path="afh_properties.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Properties table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mls_id TEXT UNIQUE,
                address TEXT,
                county TEXT,
                price REAL,
                beds INTEGER,
                baths REAL,
                sqft INTEGER,
                lot_size REAL,
                year_built INTEGER,
                afh_score INTEGER,
                readiness_level TEXT,
                key_features TEXT,
                listing_url TEXT,
                created_date TIMESTAMP,
                updated_date TIMESTAMP
            )
        ''')
        
        # Search results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS search_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                search_date TIMESTAMP,
                county TEXT,
                total_properties INTEGER,
                high_potential_count INTEGER,
                avg_score REAL
            )
        ''')
        
        # User preferences table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_preferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                target_counties TEXT,
                max_price REAL,
                min_afh_score INTEGER,
                notification_frequency TEXT,
                created_date TIMESTAMP,
                updated_date TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_property(self, property_data):
        """Save property to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO properties 
            (mls_id, address, county, price, beds, baths, sqft, lot_size, 
             year_built, afh_score, readiness_level, key_features, 
             listing_url, created_date, updated_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            property_data.mls_id,
            property_data.address,
            property_data.county,
            property_data.price,
            property_data.beds,
            property_data.baths,
            property_data.sqft,
            property_data.lot_size,
            property_data.year_built,
            property_data.afh_potential_score,
            property_data.afh_readiness_level,
            ','.join(property_data.key_features),
            property_data.listing_url,
            datetime.now(),
            datetime.now()
        ))
        
        conn.commit()
        conn.close()
    
    def get_properties_by_county(self, county, limit=50):
        """Get properties by county"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM properties 
            WHERE county = ? 
            ORDER BY afh_score DESC 
            LIMIT ?
        ''', (county, limit))
        
        results = cursor.fetchall()
        conn.close()
        
        return results
```

---

## Maintenance & Updates

### Regular Maintenance Tasks

#### Daily Tasks
- **System Health Check**: Verify all components are working
- **Log Review**: Check for errors or warnings
- **Performance Monitoring**: Monitor response times and resource usage
- **Backup Verification**: Ensure data backups are successful

#### Weekly Tasks
- **Configuration Review**: Check all settings are correct
- **User Feedback Review**: Process user feedback and suggestions
- **Performance Analysis**: Analyze system performance metrics
- **Security Audit**: Review security logs and access patterns

#### Monthly Tasks
- **Dependency Updates**: Update Python packages and dependencies
- **Configuration Backup**: Backup all configuration files
- **User Statistics**: Generate user usage statistics
- **Compliance Review**: Review regulatory compliance status

#### Quarterly Tasks
- **System Upgrade**: Plan and execute system upgrades
- **Security Assessment**: Conduct comprehensive security assessment
- **Performance Optimization**: Optimize system performance
- **Documentation Update**: Update all documentation

### Update Procedures

#### System Updates
```bash
# 1. Backup current system
cp -r afh-property-matching afh-property-matching-backup-$(date +%Y%m%d)

# 2. Download latest version
git pull origin main

# 3. Update dependencies
pip install -r requirements.txt --upgrade

# 4. Test system
python afh_property_search_system.py --test

# 5. Restart system
sudo systemctl restart afh-property-matching
```

#### Configuration Updates
```bash
# 1. Backup configuration
cp config.json config.json.backup

# 2. Update configuration
nano config.json

# 3. Validate configuration
python -c "import json; json.load(open('config.json'))"

# 4. Restart system
python afh_property_search_system.py --restart
```

### Monitoring and Alerting

#### System Monitoring
```python
import psutil
import time
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        self.thresholds = {
            'cpu_percent': 80,
            'memory_percent': 85,
            'disk_percent': 90
        }
    
    def check_system_health(self):
        """Check system health metrics"""
        health_status = {
            'timestamp': datetime.now(),
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_percent': psutil.disk_usage('/').percent,
            'status': 'healthy'
        }
        
        # Check thresholds
        if health_status['cpu_percent'] > self.thresholds['cpu_percent']:
            health_status['status'] = 'warning'
            self.send_alert('High CPU usage detected')
        
        if health_status['memory_percent'] > self.thresholds['memory_percent']:
            health_status['status'] = 'warning'
            self.send_alert('High memory usage detected')
        
        if health_status['disk_percent'] > self.thresholds['disk_percent']:
            health_status['status'] = 'critical'
            self.send_alert('Low disk space detected')
        
        return health_status
    
    def send_alert(self, message):
        """Send system alert"""
        # Implementation for sending alerts
        pass
```

#### Log Monitoring
```python
import re
from datetime import datetime, timedelta

class LogMonitor:
    def __init__(self, log_file="afh_search.log"):
        self.log_file = log_file
        self.error_patterns = [
            r'ERROR',
            r'CRITICAL',
            r'Exception',
            r'Traceback'
        ]
    
    def check_recent_errors(self, hours=24):
        """Check for recent errors in logs"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        errors = []
        
        with open(self.log_file, 'r') as f:
            for line in f:
                # Parse timestamp and check if recent
                timestamp_match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line)
                if timestamp_match:
                    log_time = datetime.strptime(timestamp_match.group(1), '%Y-%m-%d %H:%M:%S')
                    if log_time > cutoff_time:
                        # Check for error patterns
                        for pattern in self.error_patterns:
                            if re.search(pattern, line):
                                errors.append(line.strip())
                                break
        
        return errors
```

---

## Best Practices

### System Administration

#### Security Best Practices
1. **Regular Updates**: Keep all software and dependencies updated
2. **Access Control**: Use strong passwords and multi-factor authentication
3. **Network Security**: Use firewalls and VPNs for remote access
4. **Data Encryption**: Encrypt sensitive data at rest and in transit
5. **Audit Logging**: Maintain comprehensive audit logs

#### Performance Best Practices
1. **Resource Monitoring**: Monitor CPU, memory, and disk usage
2. **Caching**: Implement caching for frequently accessed data
3. **Database Optimization**: Optimize database queries and indexes
4. **Load Balancing**: Use load balancing for high-traffic scenarios
5. **CDN Usage**: Use content delivery networks for static content

#### Backup Best Practices
1. **Regular Backups**: Schedule automated daily backups
2. **Multiple Locations**: Store backups in multiple locations
3. **Backup Testing**: Regularly test backup restoration
4. **Version Control**: Use version control for all code changes
5. **Documentation**: Document all backup and recovery procedures

### User Experience

#### Communication Best Practices
1. **Clear Messaging**: Use clear, concise language in all communications
2. **Timely Updates**: Provide timely updates on system status
3. **User Feedback**: Actively seek and respond to user feedback
4. **Documentation**: Maintain comprehensive user documentation
5. **Support**: Provide multiple channels for user support

#### Service Quality
1. **Reliability**: Maintain high system uptime and reliability
2. **Performance**: Ensure fast response times and efficient operations
3. **Accuracy**: Maintain high accuracy in property scoring and data
4. **Compliance**: Ensure strict compliance with all regulations
5. **Innovation**: Continuously improve and innovate the service

### Business Operations

#### Customer Service
1. **Response Time**: Respond to customer inquiries within 24 hours
2. **Problem Resolution**: Resolve issues quickly and effectively
3. **Proactive Communication**: Communicate proactively about issues
4. **User Education**: Provide education and training resources
5. **Feedback Integration**: Integrate user feedback into service improvements

#### Compliance Management
1. **Regular Audits**: Conduct regular compliance audits
2. **Documentation**: Maintain comprehensive compliance documentation
3. **Training**: Provide regular compliance training for staff
4. **Monitoring**: Monitor compliance metrics and indicators
5. **Reporting**: Provide regular compliance reports to stakeholders

---

## Conclusion

This manual provides comprehensive guidance for operating the AFH Property Matching Service. By following these procedures and best practices, you can ensure reliable, compliant, and effective operation of the system.

### Key Takeaways

1. **System Setup**: Proper installation and configuration are critical for success
2. **Daily Operations**: Consistent daily operations ensure reliable service delivery
3. **Compliance**: Strict adherence to regulations and legal requirements is essential
4. **User Management**: Effective user management drives customer satisfaction
5. **Maintenance**: Regular maintenance ensures long-term system reliability

### Next Steps

1. **Review Documentation**: Familiarize yourself with all documentation
2. **Set Up System**: Follow installation and configuration procedures
3. **Test Operations**: Conduct thorough testing before going live
4. **Monitor Performance**: Implement monitoring and alerting systems
5. **Continuous Improvement**: Regularly review and improve operations

For additional support or questions, refer to the troubleshooting section or contact our support team.

---

*This manual is regularly updated to reflect system improvements and regulatory changes. Please check for updates regularly.*
