# NWMLS Broker Setup Guide for AFH Property Search

## Your Advantage as a Registered Broker

Since you're already a registered real estate broker with NWMLS access, you have several advantages:

1. **Existing Data Access**: You likely already have access to NWMLS listing data
2. **Reduced Costs**: May not need additional MLS GRID subscription
3. **Faster Setup**: Can leverage existing broker credentials
4. **Compliance**: Already familiar with NWMLS data use policies

## Step-by-Step Setup Process

### 1. Check Your Current NWMLS Access

#### Log into your NWMLS broker portal:
- **URL**: https://www.nwmls.com/
- **Check for**: API access, data export capabilities, RESO Web API availability

#### Look for these features in your broker dashboard:
- [ ] API access or developer tools
- [ ] Data export options
- [ ] RESO Web API credentials
- [ ] Rate limits and usage policies

### 2. Contact NWMLS for API Access

#### Email Template:
```
Subject: RESO Web API Access Request for AFH Property Matching Service

Dear NWMLS Support Team,

I am a registered real estate broker (License #: [YOUR_LICENSE_NUMBER]) 
and would like to request access to the RESO Web API for a specialized 
property matching service focused on Adult Family Home (AFH) providers.

Project Details:
- Service: AFH Property Matching Platform
- Purpose: Help prospective AFH providers find suitable properties
- Compliance: Will follow all NWMLS Data Use Compliance Policy requirements
- Data Usage: Licensed use only, no scraping or unauthorized access

Please provide:
1. RESO Web API access credentials
2. Rate limits and usage guidelines
3. Required compliance documentation
4. Any additional fees or requirements

Thank you for your assistance.

Best regards,
[YOUR_NAME]
[YOUR_BROKERAGE]
[CONTACT_INFORMATION]
```

### 3. Alternative: MLS GRID Access

If direct NWMLS API access isn't available, use MLS GRID:

#### Registration Process:
1. **Visit**: https://www.mlsgrid.com/
2. **Click**: "Get Started" or "Sign Up"
3. **Select**: "Real Estate Professional"
4. **Provide**:
   - Your NWMLS broker license number
   - Brokerage information
   - Contact details
   - Project description (AFH property matching)

#### Required Information:
- **Brokerage Name**: [YOUR_BROKERAGE]
- **License Number**: [YOUR_LICENSE]
- **NWMLS Member ID**: [YOUR_MEMBER_ID]
- **Project Type**: "Property Matching Service"
- **Target Market**: "Adult Family Home Providers"

### 4. Data License Agreement

#### Key Points to Review:
- **Data Usage**: Licensed use only for your AFH matching service
- **Display Rules**: Must comply with IDX/VOW participant rules
- **Rate Limits**: Typically 1,000 calls per day
- **Data Retention**: 30-day maximum for search results
- **Compliance**: Regular audits and usage monitoring

#### Sign and Return:
- Review all terms carefully
- Sign electronically or print and return
- Keep copy for your records
- Note any specific compliance requirements

### 5. API Credentials Setup

#### Once Approved:
1. **Receive**: API key and base URL
2. **Test**: API connectivity with sample queries
3. **Configure**: Rate limiting and error handling
4. **Document**: Usage patterns and compliance measures

#### Update Your Config:
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

## Compliance Requirements

### NWMLS Data Use Policy Compliance

#### Required Practices:
- ✅ **Licensed Use Only**: Use data only for licensed purposes
- ✅ **Rate Limiting**: Respect API rate limits (typically 1,000/day)
- ✅ **Data Display**: Follow IDX/VOW display rules
- ✅ **User Authentication**: Verify user credentials before data access
- ✅ **Audit Logging**: Maintain logs of all data usage
- ✅ **Data Retention**: Delete data after 30 days maximum

#### Prohibited Practices:
- ❌ **Unauthorized Access**: No scraping or bulk data collection
- ❌ **Data Resale**: Cannot resell MLS data to third parties
- ❌ **Consumer Site Scraping**: No Redfin/Zillow scraping
- ❌ **Bulk Downloads**: No mass data extraction
- ❌ **Unlicensed Display**: Cannot show data to unlicensed users

### Implementation Checklist

#### Technical Requirements:
- [ ] API authentication working
- [ ] Rate limiting implemented
- [ ] Error handling configured
- [ ] Audit logging enabled
- [ ] Data retention policy set
- [ ] User authentication system
- [ ] Compliance monitoring

#### Legal Requirements:
- [ ] Data License Agreement signed
- [ ] NWMLS compliance policy reviewed
- [ ] User terms of service created
- [ ] Privacy policy implemented
- [ ] Professional liability insurance
- [ ] Regular compliance audits scheduled

## Testing Your Setup

### 1. API Connectivity Test
```python
import requests

def test_mls_api():
    headers = {
        'Authorization': f'Bearer {YOUR_API_KEY}',
        'Accept': 'application/json'
    }
    
    response = requests.get(
        'https://api.mlsgrid.com/v2/Property',
        headers=headers,
        params={'top': 1}
    )
    
    if response.status_code == 200:
        print("✅ API access working")
        return True
    else:
        print(f"❌ API error: {response.status_code}")
        return False
```

### 2. Sample Query Test
```python
def test_property_search():
    # Test search for rambler properties in King County
    params = {
        'filter': "StateOrProvince eq 'WA' and City eq 'Seattle' and PropertySubType eq 'Single Family Residential'",
        'top': 5
    }
    
    response = requests.get(
        'https://api.mlsgrid.com/v2/Property',
        headers=headers,
        params=params
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Found {len(data.get('value', []))} properties")
        return True
    else:
        print(f"❌ Search error: {response.status_code}")
        return False
```

## Next Steps

1. **Complete API Setup**: Get your credentials and test connectivity
2. **Update Configuration**: Modify config.json with your API details
3. **Test Search System**: Run the AFH property search system
4. **Verify Compliance**: Ensure all requirements are met
5. **Document Usage**: Keep records of all data access

## Support Contacts

### NWMLS Support:
- **Phone**: (425) 820-9200
- **Email**: support@nwmls.com
- **Website**: https://www.nwmls.com/contact

### MLS GRID Support:
- **Phone**: (425) 820-9200
- **Email**: support@mlsgrid.com
- **Website**: https://www.mlsgrid.com/support

## Cost Expectations

### Potential Costs:
- **NWMLS Direct API**: May be included in existing subscription
- **MLS GRID**: ~$500/year for basic access
- **Additional Features**: May have extra costs for advanced features
- **Compliance Tools**: May need additional monitoring tools

### Cost Savings:
- **No Additional Broker License**: You already have this
- **Existing Relationships**: May get better rates as current member
- **Bulk Usage**: May qualify for volume discounts

---

*This guide is specifically tailored for your situation as an existing NWMLS broker. Your existing relationship with NWMLS should significantly streamline the setup process.*
