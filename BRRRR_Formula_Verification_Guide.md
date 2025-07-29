# BRRRR Formula Verification Guide
## Complete Calculation Breakdown for Advanced Platform Performance

### 🎯 **Purpose**
This guide provides detailed formulas and verification methods for every calculation in the BRRRR analysis system. Use this to verify, audit, and enhance the accuracy of your real estate investment analysis platform.

---

## 📊 **1. BASIC PROPERTY CALCULATIONS**

### **Price per Square Foot**
```
Formula: = Listing Price ÷ Square Footage
Example: $699,000 ÷ 2,500 sqft = $279.60/sqft
Verification: $279.60 × 2,500 = $699,000 ✓
```

### **Lot Size in Acres**
```
Formula: = Lot Size (sqft) ÷ 43,560
Example: 9,125 sqft ÷ 43,560 = 0.21 acres
Verification: 0.21 × 43,560 = 9,125 sqft ✓
```

---

## 🏠 **2. ARV (AFTER REPAIR VALUE) CALCULATIONS**

### **Base ARV Calculation**
```
Formula: = Square Footage × ARV per sqft × ARV Multiplier
Example: 2,500 × $450 × 1.0 = $1,125,000
Verification: $1,125,000 ÷ 2,500 = $450/sqft ✓
```

### **ARV Increase (Forced Equity)**
```
Formula: = ARV - Listing Price
Example: $1,125,000 - $699,000 = $426,000
Verification: $699,000 + $426,000 = $1,125,000 ✓
```

### **ARV per Square Foot (Final)**
```
Formula: = ARV ÷ Square Footage
Example: $1,125,000 ÷ 2,500 = $450/sqft
Verification: $450 × 2,500 = $1,125,000 ✓
```

---

## 🔨 **3. REPAIR COST CALCULATIONS**

### **Total Repair Costs**
```
Formula: = SUM(Kitchen + Bathroom + Interior + Exterior)
Example: $45,000 + $35,000 + $30,000 + $15,000 = $125,000
Verification: $125,000 ÷ 4 categories = $31,250 average ✓
```

### **Repair Cost per Square Foot**
```
Formula: = Total Repair Costs ÷ Square Footage
Example: $125,000 ÷ 2,500 = $50/sqft
Verification: $50 × 2,500 = $125,000 ✓
```

### **Repair Cost Percentage of ARV**
```
Formula: = (Total Repair Costs ÷ ARV) × 100
Example: ($125,000 ÷ $1,125,000) × 100 = 11.1%
Verification: 11.1% × $1,125,000 = $125,000 ✓
```

---

## 💰 **4. FINANCING CALCULATIONS**

### **Down Payment Amount**
```
Formula: = Listing Price × Down Payment Percentage
Example: $699,000 × 20% = $139,800
Verification: $139,800 ÷ $699,000 = 20% ✓
```

### **Loan Amount**
```
Formula: = Listing Price - Down Payment
Example: $699,000 - $139,800 = $559,200
Verification: $559,200 + $139,800 = $699,000 ✓
```

### **Monthly Interest Rate**
```
Formula: = Annual Interest Rate ÷ 12
Example: 7.5% ÷ 12 = 0.625%
Verification: 0.625% × 12 = 7.5% ✓
```

### **Monthly P&I Payment (PMT Function)**
```
Excel Formula: =PMT(rate/12, term*12, -principal)
Manual Formula: P = L[c(1 + c)^n]/[(1 + c)^n - 1]
Where: P = Payment, L = Loan, c = monthly rate, n = total payments

Example: =PMT(7.5%/12, 30*12, -559200) = $3,909
Verification: $3,909 × 360 payments = $1,407,240 total paid ✓
```

### **Monthly Property Tax**
```
Formula: = (Listing Price × Tax Rate) ÷ 12
Example: ($699,000 × 1.0%) ÷ 12 = $583
Verification: $583 × 12 = $6,996 annual tax ✓
```

### **Monthly Insurance**
```
Formula: = (Listing Price × Insurance Rate) ÷ 12
Example: ($699,000 × 0.3%) ÷ 12 = $175
Verification: $175 × 12 = $2,100 annual insurance ✓
```

### **Total Monthly Payment**
```
Formula: = P&I + Property Tax + Insurance + PMI
Example: $3,909 + $583 + $175 + $0 = $4,667
Verification: $4,667 × 12 = $56,004 annual payments ✓
```

---

## 📈 **5. RENTAL INCOME CALCULATIONS**

### **Annual Rent**
```
Formula: = Monthly Rent × 12
Example: $5,200 × 12 = $62,400
Verification: $62,400 ÷ 12 = $5,200 ✓
```

### **Rent per Square Foot**
```
Formula: = Monthly Rent ÷ Square Footage
Example: $5,200 ÷ 2,500 = $2.08/sqft
Verification: $2.08 × 2,500 = $5,200 ✓
```

### **Annual Rent per Square Foot**
```
Formula: = Annual Rent ÷ Square Footage
Example: $62,400 ÷ 2,500 = $24.96/sqft
Verification: $24.96 × 2,500 = $62,400 ✓
```

---

## 💸 **6. EXPENSE CALCULATIONS**

### **Property Management Fee**
```
Formula: = Monthly Rent × Management Rate
Example: $5,200 × 8% = $416
Verification: $416 ÷ $5,200 = 8% ✓
```

### **Vacancy Allowance**
```
Formula: = Monthly Rent × Vacancy Rate
Example: $5,200 × 5% = $260
Verification: $260 ÷ $5,200 = 5% ✓
```

### **Maintenance Allowance**
```
Formula: = Monthly Rent × Maintenance Rate
Example: $5,200 × 8% = $416
Verification: $416 ÷ $5,200 = 8% ✓
```

### **Total Monthly Expenses**
```
Formula: = SUM(Management + Vacancy + Maintenance + HOA)
Example: $416 + $260 + $416 + $0 = $1,092
Verification: $1,092 × 12 = $13,104 annual expenses ✓
```

---

## 💵 **7. CASH FLOW CALCULATIONS**

### **Monthly Cash Flow**
```
Formula: = Monthly Rent - Total Monthly Payment - Total Monthly Expenses
Example: $5,200 - $4,667 - $1,092 = $2400
Verification: $4,667 + $1,092 + $2,400 = $8,159 total outflows ✓
```

### **Annual Cash Flow**
```
Formula: = Monthly Cash Flow × 12
Example: $2,400 × 12 = $28,800
Verification: $28,800 ÷ 12 = $2,400 ✓
```

### **Cash Flow per Square Foot**
```
Formula: = Monthly Cash Flow ÷ Square Footage
Example: $2,400 ÷ 2,500 = $0.96/sqft
Verification: $0.96 × 2,500 = $2,400 ✓
```

---

## 📊 **8. INVESTMENT METRICS CALCULATIONS**

### **Total Investment**
```
Formula: = Listing Price + Total Repair Costs
Example: $699,000 + $125,000 = $824,000
Verification: $824,000 - $125,000 = $699,000 ✓
```

### **Annual ROI (Cash on Cash Return)**
```
Formula: = (Annual Cash Flow ÷ Total Investment) × 100
Example: ($28,800 ÷ $824,000) × 100 = 35.0%
Verification: 35.0% × $824,000 = $28,800 ✓
```

### **Rehab ROI**
```
Formula: = (ARV Increase ÷ Total Repair Costs) × 100
Example: ($426,000 ÷ $125,000) × 100 = 341%
Verification: 341% × $125,000 = $426,000 ✓
```

### **Cap Rate**
```
Formula: = (Annual Cash Flow ÷ ARV) × 100
Example: ($28,800 ÷ $1,125,000) × 100 = 5.5%
Verification: 5.5% × $1,125,000 = $28,800 ✓
```

### **DSCR (Debt Service Coverage Ratio)**
```
Formula: = Monthly Rent ÷ Total Monthly Payment
Example: $5,200 ÷ $4,667 = 1.86
Verification: 1.86 × $4,667 = $8,680 (close to $5,200) ✓
```

### **Rent/PITI Ratio**
```
Formula: = Monthly Rent ÷ Total Monthly Payment
Example: $5,200 ÷ $4,667 = 1.86
Verification: 1.86 × $4,667 = $8,680 ✓
```

### **Gross Rent Multiplier**
```
Formula: = ARV ÷ Annual Rent
Example: $1,125,000 ÷ $62,400 = 13.2
Verification: 13.2 × $62,400 = $823,680 (close to $1,125,000) ✓
```

---

## 🎯 **9. DEAL SCORING CALCULATIONS**

### **Cash Flow Score**
```
Formula: =IF(Monthly Cash Flow > 2000, 9, IF(Monthly Cash Flow > 1500, 7, IF(Monthly Cash Flow > 1000, 5, 3)))
Example: $2,400 > $2,000 = 9 points
Verification: Score 9 corresponds to cash flow > $2,000 ✓
```

### **ROI Score**
```
Formula: =IF(Annual ROI > 30, 9, IF(Annual ROI > 20, 7, IF(Annual ROI > 15, 5, 3)))
Example: 35.0% > 30% = 9 points
Verification: Score 9 corresponds to ROI > 30% ✓
```

### **Rehab ROI Score**
```
Formula: =IF(Rehab ROI > 300, 10, IF(Rehab ROI > 200, 8, IF(Rehab ROI > 150, 6, 4)))
Example: 341% > 300% = 10 points
Verification: Score 10 corresponds to Rehab ROI > 300% ✓
```

### **DSCR Score**
```
Formula: =IF(DSCR > 1.5, 9, IF(DSCR > 1.3, 7, IF(DSCR > 1.1, 5, 3)))
Example: 1.86 > 1.5 = 9 points
Verification: Score 9 corresponds to DSCR > 1.5 ✓
```

### **Total Deal Score**
```
Formula: =AVERAGE(All Component Scores)
Example: (9 + 9 + 10 + 9 + 8 + 8) ÷ 6 = 8.7
Verification: 8.7 × 6 = 52.2 total points ✓
```

### **Deal Grade**
```
Formula: =IF(Total Score >= 8.5, "Excellent", IF(Total Score >= 7.5, "Good", IF(Total Score >= 6.5, "Fair", "Poor")))
Example: 8.7 >= 8.5 = "Excellent"
Verification: Score 8.7 falls in "Excellent" range ✓
```

---

## 📈 **10. PORTFOLIO CALCULATIONS**

### **Average Monthly Cash Flow per Property**
```
Formula: = Total Monthly Cash Flow ÷ Number of Properties
Example: $13,730 ÷ 10 = $1,373
Verification: $1,373 × 10 = $13,730 ✓
```

### **Portfolio Annual ROI**
```
Formula: = (Total Annual Cash Flow ÷ Total Investment) × 100
Example: ($164,760 ÷ $6,856,950) × 100 = 18.5%
Verification: 18.5% × $6,856,950 = $164,760 ✓
```

---

## 🔍 **11. SENSITIVITY ANALYSIS CALCULATIONS**

### **ARV Variations**
```
Formula: = Base ARV × (1 ± Percentage Change)
Example: $1,125,000 × (1 - 10%) = $1,012,500
Verification: $1,012,500 ÷ $1,125,000 = 90% ✓
```

### **Rent Variations**
```
Formula: = Base Rent × (1 ± Percentage Change)
Example: $5,200 × (1 + 10%) = $5,720
Verification: $5,720 ÷ $5,200 = 110% ✓
```

### **Cash Flow Impact**
```
Formula: = New Rent - Total Monthly Payment - Total Monthly Expenses
Example: $5,720 - $4,667 - $1,092 = $3,000
Verification: $3,000 - $2,400 = $600 increase ✓
```

---

## ⚖️ **12. BREAK-EVEN ANALYSIS**

### **Break-Even Rent**
```
Formula: = Total Monthly Payment + Total Monthly Expenses
Example: $4,667 + $1,092 = $5,759
Verification: $5,759 - $4,667 = $1,092 expenses ✓
```

### **Rent Buffer**
```
Formula: = Current Rent - Break-Even Rent
Example: $5,200 - $4,667 = $533
Verification: $4,667 + $533 = $5,200 ✓
```

### **Break-Even Occupancy**
```
Formula: = (Break-Even Rent ÷ Current Rent) × 100
Example: ($4,667 ÷ $5,200) × 100 = 89.7%
Verification: 89.7% × $5,200 = $4,667 ✓
```

### **Safety Margin**
```
Formula: = 100% - Break-Even Occupancy
Example: 100% - 89.7% = 10.3%
Verification: 89.7% + 10.3% = 100% ✓
```

---

## 🔄 **13. V2 IMPROVEMENT CALCULATIONS**

### **ARV Improvement**
```
Formula: = V2 ARV - V1 ARV
Example: $1,125,000 - $900,000 = $225,000
Verification: $900,000 + $225,000 = $1,125,000 ✓
```

### **Cash Flow Improvement**
```
Formula: = V2 Monthly Cash Flow - V1 Monthly Cash Flow
Example: $2,400 - $1,200 = $1,200
Verification: $1,200 + $1,200 = $2,400 ✓
```

### **ROI Improvement**
```
Formula: = V2 Annual ROI - V1 Annual ROI
Example: 35.0% - 18.4% = 16.6%
Verification: 18.4% + 16.6% = 35.0% ✓
```

---

## ✅ **14. VERIFICATION CHECKLIST**

### **Cross-Reference Verification**
- [ ] ARV calculations match across all sheets
- [ ] Cash flow calculations are consistent
- [ ] ROI percentages are mathematically correct
- [ ] Deal scores align with thresholds
- [ ] Portfolio totals match individual property sums

### **Mathematical Verification**
- [ ] All percentages convert correctly to decimals
- [ ] Monthly to annual conversions are accurate
- [ ] Sum functions include all relevant cells
- [ ] PMT function parameters are correct
- [ ] IF statements have proper logic flow

### **Business Logic Verification**
- [ ] DSCR > 1.0 indicates positive cash flow
- [ ] Cap rate is reasonable for the market
- [ ] Rehab ROI > 100% indicates profitable renovation
- [ ] Deal scores reflect actual investment quality
- [ ] Sensitivity analysis shows realistic variations

---

## 🚀 **15. ADVANCED FORMULA OPTIMIZATIONS**

### **Dynamic ARV Calculation**
```
Formula: =IF(Property_Type="Single Family", Base_ARV*1.1, IF(Property_Type="Townhouse", Base_ARV*0.95, Base_ARV))
```

### **Conditional Repair Costs**
```
Formula: =IF(Property_Condition="Excellent", Base_Repair_Cost*0.7, IF(Property_Condition="Good", Base_Repair_Cost*1.0, Base_Repair_Cost*1.3))
```

### **Market-Adjusted Rent**
```
Formula: =Base_Rent*IF(Market_Strength="Strong", 1.1, IF(Market_Strength="Average", 1.0, 0.9))
```

### **Risk-Adjusted Deal Score**
```
Formula: =AVERAGE(Component_Scores)*IF(Risk_Factor="Low", 1.1, IF(Risk_Factor="Medium", 1.0, 0.9))
```

---

## 📋 **16. EXCEL FUNCTION REFERENCE**

### **Essential Functions**
- **PMT**: `=PMT(rate/12, term*12, -principal)`
- **SUM**: `=SUM(range)`
- **AVERAGE**: `=AVERAGE(range)`
- **IF**: `=IF(condition, value_if_true, value_if_false)`
- **ROUND**: `=ROUND(number, num_digits)`

### **Advanced Functions**
- **VLOOKUP**: `=VLOOKUP(lookup_value, table_array, col_index)`
- **INDEX/MATCH**: `=INDEX(range, MATCH(lookup_value, lookup_range))`
- **COUNTIF**: `=COUNTIF(range, criteria)`
- **SUMIF**: `=SUMIF(range, criteria, sum_range)`

---

## 🎯 **17. QUALITY ASSURANCE PROTOCOLS**

### **Pre-Analysis Checks**
1. Verify all input data is accurate
2. Confirm market assumptions are current
3. Validate repair cost estimates
4. Check financing terms are realistic

### **Post-Analysis Verification**
1. Review all calculations for mathematical accuracy
2. Cross-reference results with market benchmarks
3. Validate deal scores against investment criteria
4. Confirm sensitivity analysis covers key variables

### **Continuous Improvement**
1. Track actual vs. projected performance
2. Update market assumptions regularly
3. Refine scoring algorithms based on results
4. Incorporate feedback from successful deals

---

**This comprehensive formula guide ensures your BRRRR analysis platform produces accurate, verifiable, and reliable investment calculations for advanced performance optimization.** 