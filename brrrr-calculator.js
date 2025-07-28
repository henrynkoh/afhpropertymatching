// BRRRR Calculator Engine
class BRRRRCalculator {
    constructor() {
        this.results = {};
    }

    // Calculate all BRRRR metrics
    calculateBRRRR(propertyData) {
        const {
            purchasePrice,
            arv,
            rehabCosts,
            monthlyRent,
            propertyType,
            propertyAddress,
            mlsNumber,
            propertyNotes
        } = propertyData;

        // Basic calculations
        const totalInvestment = purchasePrice + rehabCosts;
        const arvIncrease = arv - purchasePrice;
        const rehabROI = (arvIncrease / rehabCosts) * 100;

        // Monthly expenses calculation
        const monthlyExpenses = this.calculateMonthlyExpenses(purchasePrice, arv, propertyType);
        
        // Cash flow calculation
        const monthlyCashFlow = monthlyRent - monthlyExpenses.total;
        const annualCashFlow = monthlyCashFlow * 12;

        // ROI calculation
        const annualAppreciation = arv * 0.08; // 8% annual appreciation
        const totalAnnualReturn = annualCashFlow + annualAppreciation;
        const roi = (totalAnnualReturn / totalInvestment) * 100;

        // Rent/PITI ratio
        const rentPitiRatio = monthlyRent / monthlyExpenses.piti;

        // DSCR (Debt Service Coverage Ratio)
        const annualNOI = monthlyRent * 12;
        const annualDebtService = monthlyExpenses.piti * 12;
        const dscr = annualNOI / annualDebtService;

        // Cap rate
        const capRate = (annualNOI / arv) * 100;

        // Refinance analysis
        const refinanceAnalysis = this.calculateRefinance(totalInvestment, arv, propertyType);

        // Risk assessment
        const riskScore = this.calculateRiskScore(propertyData, {
            rentPitiRatio,
            dscr,
            capRate,
            rehabROI
        });

        // Deal score
        const dealScore = this.calculateDealScore({
            roi,
            rentPitiRatio,
            dscr,
            capRate,
            rehabROI,
            riskScore
        });

        // Store results
        this.results = {
            propertyData,
            calculations: {
                totalInvestment,
                arvIncrease,
                rehabROI,
                monthlyExpenses,
                monthlyCashFlow,
                annualCashFlow,
                roi,
                rentPitiRatio,
                dscr,
                capRate,
                refinanceAnalysis,
                riskScore,
                dealScore
            },
            timestamp: new Date().toISOString(),
            analysisId: this.generateAnalysisId()
        };

        return this.results;
    }

    // Calculate monthly expenses
    calculateMonthlyExpenses(purchasePrice, arv, propertyType) {
        const loanAmount = purchasePrice * 0.8; // 80% LTV
        const interestRate = this.getInterestRate(propertyType);
        const monthlyPayment = this.calculateMortgage(loanAmount, interestRate, 30);
        
        const propertyTax = (arv * 0.012) / 12; // 1.2% annual property tax
        const insurance = (arv * 0.005) / 12; // 0.5% annual insurance
        const maintenance = monthlyPayment * 0.1; // 10% of mortgage for maintenance
        const propertyManagement = monthlyPayment * 0.1; // 10% for property management

        return {
            mortgage: monthlyPayment,
            propertyTax,
            insurance,
            maintenance,
            propertyManagement,
            piti: monthlyPayment + propertyTax + insurance,
            total: monthlyPayment + propertyTax + insurance + maintenance + propertyManagement
        };
    }

    // Calculate mortgage payment
    calculateMortgage(principal, annualRate, years) {
        const monthlyRate = annualRate / 12 / 100;
        const numberOfPayments = years * 12;
        
        if (monthlyRate === 0) return principal / numberOfPayments;
        
        return principal * (monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments)) / 
               (Math.pow(1 + monthlyRate, numberOfPayments) - 1);
    }

    // Get interest rate based on property type
    getInterestRate(propertyType) {
        const rates = {
            'single-family': 7.0,
            'duplex': 7.2,
            'triplex': 7.5,
            'quadplex': 7.8,
            'mixed-use': 8.0,
            'commercial': 8.5
        };
        return rates[propertyType] || 7.5;
    }

    // Calculate refinance analysis
    calculateRefinance(totalInvestment, arv, propertyType) {
        const refinanceLTV = this.getRefinanceLTV(propertyType);
        const refinanceAmount = arv * refinanceLTV;
        const cashOut = refinanceAmount - totalInvestment;
        
        return {
            refinanceAmount,
            cashOut,
            refinanceLTV,
            isPositive: cashOut > 0
        };
    }

    // Get refinance LTV based on property type
    getRefinanceLTV(propertyType) {
        const ltvRates = {
            'single-family': 0.75,
            'duplex': 0.75,
            'triplex': 0.70,
            'quadplex': 0.70,
            'mixed-use': 0.65,
            'commercial': 0.60
        };
        return ltvRates[propertyType] || 0.70;
    }

    // Calculate risk score
    calculateRiskScore(propertyData, metrics) {
        let riskScore = 50; // Start with neutral score

        // Rent/PITI ratio risk
        if (metrics.rentPitiRatio < 1.0) riskScore += 20;
        else if (metrics.rentPitiRatio > 1.5) riskScore -= 10;

        // DSCR risk
        if (metrics.dscr < 1.2) riskScore += 15;
        else if (metrics.dscr > 2.0) riskScore -= 10;

        // Cap rate risk
        if (metrics.capRate < 6) riskScore += 10;
        else if (metrics.capRate > 12) riskScore -= 5;

        // Rehab ROI risk
        if (metrics.rehabROI < 100) riskScore += 15;
        else if (metrics.rehabROI > 200) riskScore -= 5;

        // Property type risk
        if (propertyData.propertyType === 'mixed-use') riskScore += 10;
        if (propertyData.propertyType === 'commercial') riskScore += 15;

        return Math.max(0, Math.min(100, riskScore));
    }

    // Calculate deal score
    calculateDealScore(metrics) {
        let score = 50; // Start with neutral score

        // ROI scoring
        if (metrics.roi > 15) score += 20;
        else if (metrics.roi > 10) score += 15;
        else if (metrics.roi > 5) score += 10;
        else if (metrics.roi < 0) score -= 20;

        // Rent/PITI scoring
        if (metrics.rentPitiRatio > 1.5) score += 15;
        else if (metrics.rentPitiRatio > 1.2) score += 10;
        else if (metrics.rentPitiRatio < 1.0) score -= 15;

        // DSCR scoring
        if (metrics.dscr > 2.0) score += 10;
        else if (metrics.dscr > 1.5) score += 5;
        else if (metrics.dscr < 1.2) score -= 10;

        // Cap rate scoring
        if (metrics.capRate > 10) score += 10;
        else if (metrics.capRate > 8) score += 5;
        else if (metrics.capRate < 5) score -= 5;

        // Risk adjustment
        score -= (metrics.riskScore / 10);

        return Math.max(0, Math.min(10, score));
    }

    // Generate unique analysis ID
    generateAnalysisId() {
        return 'brrrr_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    // Format currency
    formatCurrency(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0
        }).format(amount);
    }

    // Format percentage
    formatPercentage(value) {
        return new Intl.NumberFormat('en-US', {
            style: 'percent',
            minimumFractionDigits: 1,
            maximumFractionDigits: 1
        }).format(value / 100);
    }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BRRRRCalculator;
} 