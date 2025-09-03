# AFH Property Search System - Setup Instructions

## Prerequisites

### System Requirements
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 10GB free disk space
- Internet connection for API access
- Email account for notifications (Gmail recommended)

### Required Accounts & Licenses

#### 1. MLS Data Access
- **MLS GRID License**: Required for NWMLS data access
- **Cost**: ~$500/year for basic access
- **Application**: Contact MLS GRID directly
- **API Key**: Will be provided after license approval

#### 2. Email Service
- **Gmail Account**: For sending notifications
- **App Password**: Required for SMTP authentication
- **Setup**: Enable 2-factor authentication, generate app password

#### 3. County API Access (Optional)
- **King County**: Free public API access
- **Pierce County**: Free public API access  
- **Thurston County**: Contact county for API access
- **Lewis County**: Free public API access

## Installation Steps

### 1. Clone or Download Files
```bash
# Create project directory
mkdir afh-property-search
cd afh-property-search

# Copy all provided files to this directory:
# - afh_property_search_system.py
# - config.json
# - requirements.txt
# - AFH_BUSINESS_BLUEPRINT.md
```

### 2. Install Python Dependencies
```bash
# Create virtual environment (recommended)
python -m venv afh_env
source afh_env/bin/activate  # On Windows: afh_env\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configure System Settings

#### Edit config.json
```json
{
  "mls_api": {
    "base_url": "https://api.mlsgrid.com/v2",
    "api_key": "YOUR_ACTUAL_MLS_GRID_API_KEY",
    "rate_limit": 1000,
    "timeout": 30
  },
  "email": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "your_actual_email@gmail.com",
    "password": "your_actual_app_password",
    "use_tls": true
  },
  "email_recipients": [
    "provider1@example.com",
    "provider2@example.com"
  ]
}
```

#### Gmail App Password Setup
1. Go to Google Account settings
2. Enable 2-factor authentication
3. Go to "App passwords"
4. Generate password for "Mail"
5. Use this password in config.json

### 4. Test Installation
```bash
# Test basic functionality
python afh_property_search_system.py --test

# Check configuration
python -c "import json; print(json.load(open('config.json')))"
```

### 5. Set Up Daily Automation

#### Option A: Cron Job (Linux/Mac)
```bash
# Edit crontab
crontab -e

# Add daily search at 6:00 AM PST
0 6 * * * cd /path/to/afh-property-search && /path/to/python afh_property_search_system.py
```

#### Option B: Windows Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger: Daily at 6:00 AM
4. Set action: Start program
5. Program: python.exe
6. Arguments: afh_property_search_system.py
7. Start in: C:\path\to\afh-property-search

#### Option C: AWS Lambda (Recommended for Production)
1. Package the application
2. Upload to AWS Lambda
3. Set CloudWatch Events trigger for daily execution
4. Configure environment variables for API keys

## Usage Instructions

### Manual Search
```bash
# Run single search
python afh_property_search_system.py --search

# Search specific county
python afh_property_search_system.py --county King

# Test email notifications
python afh_property_search_system.py --test-email
```

### Automated Daily Search
```bash
# Start the scheduler (runs continuously)
python afh_property_search_system.py

# The system will:
# 1. Search all counties at 6:00 AM PST daily
# 2. Score properties for AFH potential
# 3. Send email alerts for high-potential properties
# 4. Save results to timestamped JSON files
```

### Monitoring & Logs
```bash
# View real-time logs
tail -f afh_search.log

# Check recent search results
ls -la afh_search_results_*.json

# View system status
python afh_property_search_system.py --status
```

## Configuration Options

### Search Criteria
Edit the `search_criteria` section in config.json:
```json
{
  "search_criteria": {
    "min_afh_score": 40,        // Minimum score to include
    "high_potential_score": 60, // Score for email alerts
    "max_price": 800000,        // Maximum property price
    "min_bedrooms": 2,          // Minimum bedrooms
    "min_bathrooms": 1.5,       // Minimum bathrooms
    "min_sqft": 1200,           // Minimum square footage
    "min_lot_size": 0.1,        // Minimum lot size (acres)
    "max_age": 50,              // Maximum home age (years)
    "target_counties": ["Lewis", "Thurston", "Pierce", "King"]
  }
}
```

### AFH Scoring Weights
Customize the scoring algorithm:
```json
{
  "afh_scoring_weights": {
    "bedrooms": 20,              // Weight for bedroom count
    "bathrooms": 15,             // Weight for bathroom count
    "square_footage": 15,        // Weight for home size
    "lot_size": 10,              // Weight for lot size
    "single_level": 25,          // Weight for single-level design
    "construction_age": 10,      // Weight for home age
    "accessibility_features": 15, // Weight for accessibility
    "medical_proximity": 5       // Weight for medical proximity
  }
}
```

### Notification Settings
```json
{
  "notifications": {
    "daily_alerts": true,           // Send daily email alerts
    "weekly_summary": true,         // Send weekly summary
    "high_potential_immediate": true, // Immediate alerts for high scores
    "email_format": "html",         // Email format (html/text)
    "include_county_links": true    // Include county parcel viewer links
  }
}
```

## Troubleshooting

### Common Issues

#### 1. MLS API Authentication Error
```
Error: 401 Unauthorized
```
**Solution**: Verify API key in config.json is correct and active

#### 2. Email Sending Failed
```
Error: SMTPAuthenticationError
```
**Solution**: 
- Check Gmail username/password
- Ensure app password is used (not regular password)
- Verify 2-factor authentication is enabled

#### 3. No Properties Found
```
Warning: No properties found in [County]
```
**Solution**:
- Check internet connection
- Verify MLS API is accessible
- Review search criteria (may be too restrictive)

#### 4. County API Errors
```
Warning: Error checking permits for [Address]
```
**Solution**:
- County APIs may be temporarily unavailable
- Check county website for API status
- System will continue without permit data

### Log Analysis
```bash
# View error logs only
grep "ERROR" afh_search.log

# View recent activity
tail -20 afh_search.log

# Search for specific county
grep "King County" afh_search.log
```

### Performance Optimization

#### For High Volume
- Increase `rate_limit` in config.json
- Use multiple API keys (if allowed)
- Implement caching for county permit data
- Use database instead of JSON files for results

#### For Low Resources
- Reduce `top` parameter in API queries
- Increase search intervals
- Limit to fewer counties
- Use lighter email templates

## Security Considerations

### API Key Protection
- Never commit API keys to version control
- Use environment variables for production
- Rotate keys regularly
- Monitor API usage for anomalies

### Data Privacy
- Property data is stored locally only
- No personal information is collected
- Email addresses are used only for notifications
- Comply with local data protection laws

### System Security
- Keep Python and dependencies updated
- Use virtual environments
- Monitor system logs for suspicious activity
- Implement firewall rules if running on server

## Support & Maintenance

### Regular Maintenance Tasks
1. **Weekly**: Review search results and scoring accuracy
2. **Monthly**: Update MLS API keys if required
3. **Quarterly**: Review and update search criteria
4. **Annually**: Renew MLS licenses and subscriptions

### Getting Help
- Check logs first for error messages
- Review this documentation
- Test individual components separately
- Contact MLS GRID support for API issues
- Consult county websites for permit system updates

### Updates & Improvements
- Monitor MLS API changes
- Update scoring algorithm based on results
- Add new counties as needed
- Implement user feedback for improvements

## Compliance Reminders

### MLS Data Usage
- ✅ Use only licensed MLS data feeds
- ✅ Comply with NWMLS Data Use Policy
- ✅ Respect rate limits and usage terms
- ❌ Never scrape consumer websites (Redfin, Zillow)

### Washington State Regulations
- ✅ Follow WAC 388-76 requirements
- ✅ Use official DSHS resources
- ✅ Comply with county permit systems
- ❌ Don't provide legal advice (refer to official sources)

### Data Protection
- ✅ Protect user email addresses
- ✅ Secure API keys and credentials
- ✅ Follow data retention policies
- ❌ Don't share property data with third parties

---

*For additional support or questions, refer to the AFH_BUSINESS_BLUEPRINT.md for comprehensive business context and regulatory requirements.*
