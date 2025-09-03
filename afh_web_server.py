#!/usr/bin/env python3
"""
AFH Property Matching Service - Local Web Server
Runs the AFH Property Matching Service on localhost:3010
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

class AFHHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler for AFH Property Matching Service"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            # Serve the main AFH hub
            self.path = '/MASTER_AFH_ANALYZER_HUB.html'
        elif self.path == '/afh-dashboard':
            # Serve the AFH dashboard
            self.path = '/MASTER_AFH_ANALYZER_HUB.html'
        elif self.path == '/property-search':
            # Serve property search demo
            self.path = '/afh_property_search_demo.html'
        elif self.path == '/api/properties':
            # Mock API endpoint for property data
            self.send_property_api_response()
            return
        elif self.path == '/api/afh-score':
            # Mock API endpoint for AFH scoring
            self.send_afh_score_api_response()
            return
        
        return super().do_GET()
    
    def send_property_api_response(self):
        """Send mock property data API response"""
        import json
        
        mock_properties = [
            {
                "id": 1,
                "address": "123 Main St, Kent, WA 98032",
                "county": "King",
                "price": 485000,
                "beds": 4,
                "baths": 2,
                "sqft": 1850,
                "lot_size": 7200,
                "year_built": 1975,
                "property_type": "Single Family",
                "afh_score": 88,
                "afh_potential": "High",
                "features": ["Single Story", "Large Lot", "No Steps", "Wide Doorways"],
                "mls_id": "MLS123456",
                "listing_url": "https://example.com/property/1",
                "last_updated": "2024-01-15T10:30:00Z"
            },
            {
                "id": 2,
                "address": "456 Oak Ave, Renton, WA 98058",
                "county": "King",
                "price": 520000,
                "beds": 3,
                "baths": 2,
                "sqft": 1650,
                "lot_size": 8500,
                "year_built": 1980,
                "property_type": "Single Family",
                "afh_score": 92,
                "afh_potential": "Excellent",
                "features": ["Rambler Style", "Level Entry", "Large Lot", "ADA Potential"],
                "mls_id": "MLS789012",
                "listing_url": "https://example.com/property/2",
                "last_updated": "2024-01-15T11:15:00Z"
            },
            {
                "id": 3,
                "address": "789 Pine St, Auburn, WA 98002",
                "county": "King",
                "price": 445000,
                "beds": 4,
                "baths": 3,
                "sqft": 1950,
                "lot_size": 9000,
                "year_built": 1978,
                "property_type": "Single Family",
                "afh_score": 85,
                "afh_potential": "High",
                "features": ["Single Story", "Large Lot", "Updated Kitchen", "Accessible Bathroom"],
                "mls_id": "MLS345678",
                "listing_url": "https://example.com/property/3",
                "last_updated": "2024-01-15T12:00:00Z"
            }
        ]
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(mock_properties).encode())
    
    def send_afh_score_api_response(self):
        """Send mock AFH scoring API response"""
        import json
        
        mock_score = {
            "property_id": 1,
            "afh_score": 88,
            "afh_potential": "High",
            "score_breakdown": {
                "property_type": 20,
                "accessibility": 18,
                "lot_size": 15,
                "bedrooms": 12,
                "bathrooms": 10,
                "year_built": 8,
                "location": 5
            },
            "recommendations": [
                "Install grab bars in bathrooms",
                "Add wheelchair ramp to front entrance",
                "Consider widening doorways to 36 inches",
                "Install emergency call system"
            ],
            "estimated_conversion_cost": 15000,
            "estimated_roi": 285000,
            "compliance_status": "85% compliant with AFH requirements"
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(mock_score).encode())

def start_afh_server(port=3010):
    """Start the AFH Property Matching Service web server"""
    
    print("🏠 AFH Property Matching Service - Starting Web Server")
    print("=" * 60)
    
    # Check if required files exist
    required_files = [
        'MASTER_AFH_ANALYZER_HUB.html',
        'index.html'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"⚠️  Warning: Missing files: {', '.join(missing_files)}")
        print("   Some features may not work properly.")
    
    # Create the server
    try:
        with socketserver.TCPServer(("", port), AFHHTTPRequestHandler) as httpd:
            print(f"🚀 Server starting on http://localhost:{port}")
            print(f"📊 AFH Dashboard: http://localhost:{port}/afh-dashboard")
            print(f"🔍 Property Search: http://localhost:{port}/property-search")
            print(f"📡 API Endpoints:")
            print(f"   - Properties: http://localhost:{port}/api/properties")
            print(f"   - AFH Scoring: http://localhost:{port}/api/afh-score")
            print()
            print("🎯 Available Features:")
            print("   ✅ AFH Property Analysis Hub")
            print("   ✅ Property Search & Filtering")
            print("   ✅ AFH Scoring Algorithm")
            print("   ✅ County-Specific Resources")
            print("   ✅ Compliance Checking")
            print("   ✅ Investment Analysis")
            print()
            print("📱 Open your browser and navigate to:")
            print(f"   🌐 http://localhost:{port}")
            print()
            print("⏹️  Press Ctrl+C to stop the server")
            print("=" * 60)
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{port}')
                print("🌐 Browser opened automatically")
            except:
                print("💡 Please open your browser manually")
            
            print()
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use!")
            print(f"   Try a different port or stop the process using port {port}")
            print(f"   To find what's using the port: lsof -i :{port}")
        else:
            print(f"❌ Error starting server: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    # Get port from command line argument or use default
    port = 3010
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 3010.")
    
    start_afh_server(port)
