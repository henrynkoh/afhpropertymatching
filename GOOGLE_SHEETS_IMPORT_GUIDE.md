# 📊 Google Sheets Import Guide - BRRRR Calculator

## 🎯 Complete Step-by-Step Import Instructions

This guide will walk you through importing the BRRRR calculator into Google Sheets in under 5 minutes.

---

## 🚀 Step 1: Access Google Sheets

### Open Google Sheets
1. **Go to**: [sheets.google.com](https://sheets.google.com)
2. **Sign in** with your Google account
3. **Click** "Blank" to create a new spreadsheet

### Alternative: Use Existing Sheet
- Open any existing Google Sheets document
- We'll import the calculator into a new sheet

---

## 📥 Step 2: Import the CSV File

### Method 1: Direct Import
1. **Download** the `BRRRR_Google_Sheets_Calculator.csv` file
2. **In Google Sheets**: File → Import
3. **Upload** the CSV file
4. **Choose settings**:
   - Import location: "Replace current sheet"
   - Separator type: "Comma"
5. **Click** "Import data"

### Method 2: Copy-Paste Method
1. **Open** the CSV file in a text editor
2. **Select all** content (Ctrl+A)
3. **Copy** (Ctrl+C)
4. **In Google Sheets**: Select cell A1
5. **Paste** (Ctrl+V)

---

## ⚙️ Step 3: Format the Calculator

### Apply Formatting
1. **Select** all data (Ctrl+A)
2. **Format** → Number → Automatic
3. **Adjust** column widths to fit content
4. **Apply** basic formatting:
   - Headers: Bold, background color
   - Input cells: Yellow background
   - Calculated cells: Green background

### Color Coding (Optional)
1. **Input Cells**: Select cells B2-B15, fill with light yellow
2. **Calculated Cells**: Select formula cells, fill with light green
3. **Headers**: Select row headers, make bold with background color

---

## 🔧 Step 4: Verify Formulas

### Check Key Calculations
1. **Total Investment**: Should be =B2+B15
2. **ARV Increase**: Should be =B18-B2
3. **Rehab ROI**: Should be =(B18-B2-B15)/B15*100
4. **Monthly PITI**: Should be =PMT(B24/12,B25*12,-B27)
5. **Monthly Cash Flow**: Should be =B32-B29-B33

### Test Calculations
1. **Change** purchase price in cell B2
2. **Verify** all calculations update automatically
3. **Check** that formulas are working correctly

---

## 📊 Step 5: Customize for Your Property

### Update Property Information
1. **Property Address**: Cell B2
2. **Purchase Price**: Cell B3
3. **Square Feet**: Cell B5
4. **Bedrooms/Bathrooms**: Cells B7-B8
5. **Year Built**: Cell B9

### Update Market Data
1. **Interest Rate**: Cell B24
2. **Monthly Rent**: Cell B32
3. **Renovation Costs**: Cells B11-B16
4. **Other Expenses**: Cell B33

### Update Comparable Data
1. **Comparable Sales**: Rows 85-88
2. **Rental Comparables**: Rows 92-95
3. **Market Data**: Rows 78-82

---

## 🎨 Step 6: Add Visual Enhancements

### Create Dashboard
1. **Insert** new sheet called "Dashboard"
2. **Copy** key metrics from main sheet
3. **Add** charts and visual elements
4. **Link** to main calculation sheet

### Add Charts (Optional)
1. **Select** data for charts
2. **Insert** → Chart
3. **Choose** chart type (pie, bar, line)
4. **Customize** colors and labels

---

## 🔒 Step 7: Protect Formulas

### Lock Calculated Cells
1. **Select** all cells with formulas
2. **Right-click** → Protect range
3. **Add** description: "Calculated cells - do not edit"
4. **Set** permissions as needed

### Allow Input Cell Editing
1. **Select** input cells (B2-B15)
2. **Right-click** → Protect range
3. **Allow** editing for yourself
4. **Restrict** editing for others if needed

---

## 📱 Step 8: Mobile Optimization

### Test Mobile View
1. **Open** Google Sheets app on phone
2. **Navigate** to your calculator
3. **Test** input and calculations
4. **Adjust** formatting if needed

### Mobile-Friendly Tips
- Use larger font sizes for mobile
- Ensure touch-friendly cell sizes
- Test all interactive elements

---

## 🔄 Step 9: Save and Share

### Save Your Work
1. **File** → Save
2. **Name** your calculator: "BRRRR Calculator - [Property Address]"
3. **Choose** location in Google Drive

### Share with Team
1. **Click** "Share" button
2. **Add** email addresses
3. **Set** permissions:
   - Viewer: Can view only
   - Commenter: Can comment
   - Editor: Can edit
4. **Send** invitation

---

## 🎯 Step 10: Start Analyzing

### Your First Analysis
1. **Enter** property details in input cells
2. **Watch** calculations update automatically
3. **Review** key metrics in summary section
4. **Check** deal score and recommendations

### Test Different Scenarios
1. **Change** purchase price
2. **Adjust** renovation costs
3. **Modify** rental income
4. **Update** interest rates
5. **Compare** different scenarios

---

## 🛠️ Troubleshooting

### Common Issues

#### Formulas Not Working
- **Check**: Cell formatting (should be "Automatic")
- **Verify**: No extra spaces in formulas
- **Ensure**: All referenced cells have values

#### Import Errors
- **Try**: Different separator types (comma vs semicolon)
- **Check**: File encoding (should be UTF-8)
- **Verify**: No special characters in data

#### Calculation Errors
- **Check**: All input cells have values
- **Verify**: Interest rate is in decimal format (8.00 not 8)
- **Ensure**: No division by zero

### Getting Help
- **Google Sheets Help**: [support.google.com/docs](https://support.google.com/docs)
- **Formula Reference**: [support.google.com/docs/answer/3093319](https://support.google.com/docs/answer/3093319)
- **Community Forum**: [productforums.google.com/forum/#!forum/docs](https://productforums.google.com/forum/#!forum/docs)

---

## 📋 Quick Reference

### Key Cells to Update
- **B2**: Property Address
- **B3**: Purchase Price
- **B5**: Square Feet
- **B7-B8**: Bedrooms/Bathrooms
- **B11-B16**: Renovation Costs
- **B24**: Interest Rate
- **B32**: Monthly Rent

### Important Formulas
- **Total Investment**: =B3+B15
- **Monthly PITI**: =PMT(B24/12,B25*12,-B27)
- **Monthly Cash Flow**: =B32-B29-B33
- **Deal Score**: =SUMPRODUCT(B42:B48,C42:C48)

### Color Legend
- **Yellow**: Input cells (change these)
- **Green**: Calculated cells (automatic)
- **Blue**: Summary and assessment
- **Orange**: Sensitivity analysis

---

## 🎉 Success Checklist

- [ ] CSV file imported successfully
- [ ] All formulas working correctly
- [ ] Property information updated
- [ ] Market data customized
- [ ] Formatting applied
- [ ] Mobile view tested
- [ ] File saved and shared
- [ ] First analysis completed

---

**Congratulations! Your BRRRR calculator is now ready for professional property analysis.**

*This guide ensures you can import and customize the calculator for any property in any market.* 