# ⚡ AFH Property Matching Service - Quickstart Guide

**Get Your AFH Property Matching System Running in 15 Minutes!**

## 🚀 Quick Start Checklist

- [ ] **Download & Install** (5 minutes)
- [ ] **Configure Settings** (5 minutes)
- [ ] **Test System** (3 minutes)
- [ ] **Run First Search** (2 minutes)

**Total Time: 15 minutes**

---

## Step 1: Download & Install (5 minutes)

### Download the System
```bash
# Download the system files
wget https://github.com/your-repo/afh-property-matching/archive/main.zip
unzip main.zip
cd afh-property-matching-main
```

### Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv afh_env

# Activate virtual environment
# On macOS/Linux:
source afh_env/bin/activate
# On Windows:
afh_env\Scripts\activate
```

### Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

**✅ Installation Complete!**

---

## Step 2: Configure Settings (5 minutes)

### Edit Configuration File
```bash
# Copy configuration template
cp config.json.example config.json

# Edit configuration file
nano config.json  # or use your preferred editor
```

### Essential Settings

#### 1. MLS API Configuration
```json
{
  "mls_api": {
    "api_key": "YOUR_ACTUAL_API_KEY_HERE"
  }
}
```

**How to Get API Key:**
1. Contact NWMLS or MLS GRID
2. Provide your broker license information
3. Sign the Data License Agreement
4. Receive your API credentials

#### 2. Email Configuration
```json
{
  "email": {
    "username": "your_email@gmail.com",
    "password": "your_app_password_here"
  }
}
```

**How to Set Up Gmail App Password:**
1. Go to Google Account settings
2. Enable 2-factor authentication
3. Go to "App passwords"
4. Generate password for "Mail"
5. Use this password in config.json

#### 3. Email Recipients
```json
{
  "email_recipients": [
    "provider1@example.com",
    "provider2@example.com"
  ]
}
```

**✅ Configuration Complete!**

---

## Step 3: Test System (3 minutes)

### Test Basic Functionality
```bash
# Test imports
python -c "import requests, schedule, json; print('✅ Dependencies working')"
```

### Test Configuration
```bash
# Test configuration
python -c "import json; print(json.load(open('config.json')))"
```

### Test MLS API Access
```bash
# Test API connectivity
python afh_property_search_system.py --test-api
```

### Test Email System
```bash
# Test email notifications
python afh_property_search_system.py --test-email
```

**✅ System Tests Complete!**

---

## Step 4: Run First Search (2 minutes)

### Start the System
```bash
# Start the system
python afh_property_search_system.py
```

### Run Test Search
```bash
# Search King County
python afh_property_search_system.py --county King
```

### Check Results
```bash
# View latest results
ls -la afh_search_results_*.json
cat afh_search_results_*.json | head -20
```

**✅ First Search Complete!**

---

## 🎯 What You Should See

### Successful Installation
```
✅ Dependencies working
✅ Configuration loaded
✅ API access working
✅ Email system working
```

### Successful Search
```
2025-09-02 23:45:00,123 - INFO - Starting AFH property search
2025-09-02 23:45:01,456 - INFO - Searching for rambler properties in King County
2025-09-02 23:45:05,789 - INFO - Found 25 potential rambler properties in King
2025-09-02 23:45:10,012 - INFO - Scoring properties for AFH potential
2025-09-02 23:45:15,345 - INFO - Found 8 high-potential properties (score >= 60)
2025-09-02 23:45:20,678 - INFO - Sending email alerts to 3 recipients
2025-09-02 23:45:25,901 - INFO - Search completed successfully
```

### Sample Results
```json
{
  "search_date": "2025-09-02T23:45:00",
  "total_properties": 25,
  "properties": [
    {
      "address": "123 Main Street, Seattle",
      "county": "King",
      "price": 650000,
      "beds": 4,
      "baths": 2.5,
      "sqft": 2400,
      "afh_score": 85,
      "readiness_level": "ready",
      "key_features": ["Single-level design", "4 bedrooms", "2.5 bathrooms"]
    }
  ]
}
```

---

## 🚨 Troubleshooting

### Common Issues & Quick Fixes

#### Issue: "ImportError: cannot import name 'MimeText'"
**Fix:**
```bash
# The import issue has been fixed in the latest version
# If you still see this error, update the file:
sed -i 's/MimeText/MIMEText/g' afh_property_search_system.py
sed -i 's/MimeMultipart/MIMEMultipart/g' afh_property_search_system.py
```

#### Issue: "401 Unauthorized" API Error
**Fix:**
1. Check your API key in config.json
2. Verify your MLS GRID subscription is active
3. Contact MLS GRID support if issues persist

#### Issue: "SMTPAuthenticationError"
**Fix:**
1. Use Gmail app password, not regular password
2. Enable 2-factor authentication
3. Check username/password in config.json

#### Issue: "No properties found"
**Fix:**
1. Check internet connection
2. Verify API is accessible
3. Review search criteria (may be too restrictive)

---

## 🎯 Next Steps

### Immediate Actions
1. **Set Up Automation**: Configure daily 6:00 AM PST searches
2. **Add More Users**: Add email recipients for notifications
3. **Customize Search**: Adjust search criteria for your needs
4. **Monitor Results**: Check daily search results and scores

### Set Up Daily Automation
```bash
# Set up cron job for daily 6:00 AM PST searches
crontab -e

# Add this line:
0 6 * * * cd /path/to/afh-property-matching && /path/to/python afh_property_search_system.py
```

### Customize Search Criteria
```json
{
  "search_criteria": {
    "min_afh_score": 50,
    "high_potential_score": 70,
    "max_price": 600000,
    "min_bedrooms": 3,
    "min_bathrooms": 2
  }
}
```

---

## 📚 Learn More

### Complete Documentation
- **[Manual](AFH_MANUAL.md)**: Complete system operation guide
- **[Tutorial](AFH_TUTORIAL.md)**: Step-by-step learning guide
- **[Business Blueprint](AFH_BUSINESS_BLUEPRINT.md)**: Business strategy and planning
- **[Setup Instructions](setup_instructions.md)**: Detailed installation guide

### Key Resources
- **Live Dashboard**: [https://ttdhezcf.gensparkspace.com/](https://ttdhezcf.gensparkspace.com/)
- **NWMLS Broker Setup**: [nwmls_broker_setup.md](nwmls_broker_setup.md)
- **Compliance Guide**: Built into the system

### Support
- **Email Support**: support@afhmatcher.com
- **Documentation**: All guides available in your system
- **Community**: GitHub Discussions for user support

---

## 🎉 Congratulations!

You've successfully set up your AFH Property Matching Service! 

### What You've Accomplished
- ✅ Installed and configured the system
- ✅ Tested all components
- ✅ Run your first property search
- ✅ Verified email notifications

### What's Next
1. **Explore the Live Dashboard**: [https://ttdhezcf.gensparkspace.com/](https://ttdhezcf.gensparkspace.com/)
2. **Read the Complete Manual**: [AFH_MANUAL.md](AFH_MANUAL.md)
3. **Follow the Tutorial**: [AFH_TUTORIAL.md](AFH_TUTORIAL.md)
4. **Set Up Daily Automation**: Configure automated searches
5. **Start Adding Users**: Begin building your subscriber base

### Your System is Ready!
- **Daily Searches**: Automated property searches across 4 counties
- **AFH Scoring**: 100-point algorithm based on Washington State requirements
- **Email Alerts**: Automated notifications for high-potential properties
- **Compliance**: Built-in regulatory compliance and legal safeguards

**Happy Property Matching! 🏠✨**

---

*This quickstart guide gets you up and running quickly. For complete system mastery, follow the [Tutorial](AFH_TUTORIAL.md) and [Manual](AFH_MANUAL.md).*
