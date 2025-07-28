// BRRRR Storage System using localStorage
class BRRRRStorage {
    constructor() {
        this.storageKey = 'brrrr_analyses';
        this.statsKey = 'brrrr_stats';
        this.initializeStorage();
    }

    // Initialize storage if it doesn't exist
    initializeStorage() {
        if (!localStorage.getItem(this.storageKey)) {
            localStorage.setItem(this.storageKey, JSON.stringify([]));
        }
        if (!localStorage.getItem(this.statsKey)) {
            localStorage.setItem(this.statsKey, JSON.stringify({
                totalAnalyses: 0,
                totalProperties: 0,
                totalVideos: 0,
                totalDeals: 0,
                lastUpdated: new Date().toISOString()
            }));
        }
    }

    // Save analysis result
    saveAnalysis(analysisResult) {
        try {
            const analyses = this.getAllAnalyses();
            analyses.push(analysisResult);
            localStorage.setItem(this.storageKey, JSON.stringify(analyses));
            
            // Update statistics
            this.updateStats(analysisResult);
            
            return true;
        } catch (error) {
            console.error('Error saving analysis:', error);
            return false;
        }
    }

    // Get all analyses
    getAllAnalyses() {
        try {
            const analyses = localStorage.getItem(this.storageKey);
            return analyses ? JSON.parse(analyses) : [];
        } catch (error) {
            console.error('Error retrieving analyses:', error);
            return [];
        }
    }

    // Get analysis by ID
    getAnalysisById(analysisId) {
        const analyses = this.getAllAnalyses();
        return analyses.find(analysis => analysis.analysisId === analysisId);
    }

    // Get recent analyses (last 10)
    getRecentAnalyses(limit = 10) {
        const analyses = this.getAllAnalyses();
        return analyses
            .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
            .slice(0, limit);
    }

    // Delete analysis
    deleteAnalysis(analysisId) {
        try {
            const analyses = this.getAllAnalyses();
            const filteredAnalyses = analyses.filter(analysis => analysis.analysisId !== analysisId);
            localStorage.setItem(this.storageKey, JSON.stringify(filteredAnalyses));
            
            // Update statistics
            this.updateStats();
            
            return true;
        } catch (error) {
            console.error('Error deleting analysis:', error);
            return false;
        }
    }

    // Clear all analyses
    clearAllAnalyses() {
        try {
            localStorage.setItem(this.storageKey, JSON.stringify([]));
            localStorage.setItem(this.statsKey, JSON.stringify({
                totalAnalyses: 0,
                totalProperties: 0,
                totalVideos: 0,
                totalDeals: 0,
                lastUpdated: new Date().toISOString()
            }));
            return true;
        } catch (error) {
            console.error('Error clearing analyses:', error);
            return false;
        }
    }

    // Update statistics
    updateStats(newAnalysis = null) {
        try {
            const analyses = this.getAllAnalyses();
            const stats = {
                totalAnalyses: analyses.length,
                totalProperties: analyses.length,
                totalVideos: analyses.filter(a => a.propertyData.youtubeUrl).length,
                totalDeals: analyses.filter(a => a.calculations.dealScore >= 7).length,
                lastUpdated: new Date().toISOString()
            };
            
            localStorage.setItem(this.statsKey, JSON.stringify(stats));
            return stats;
        } catch (error) {
            console.error('Error updating stats:', error);
            return null;
        }
    }

    // Get statistics
    getStats() {
        try {
            const stats = localStorage.getItem(this.statsKey);
            return stats ? JSON.parse(stats) : {
                totalAnalyses: 0,
                totalProperties: 0,
                totalVideos: 0,
                totalDeals: 0,
                lastUpdated: new Date().toISOString()
            };
        } catch (error) {
            console.error('Error retrieving stats:', error);
            return {
                totalAnalyses: 0,
                totalProperties: 0,
                totalVideos: 0,
                totalDeals: 0,
                lastUpdated: new Date().toISOString()
            };
        }
    }

    // Search analyses
    searchAnalyses(query) {
        const analyses = this.getAllAnalyses();
        const searchTerm = query.toLowerCase();
        
        return analyses.filter(analysis => {
            const address = analysis.propertyData.propertyAddress.toLowerCase();
            const mls = analysis.propertyData.mlsNumber.toLowerCase();
            const notes = analysis.propertyData.propertyNotes.toLowerCase();
            
            return address.includes(searchTerm) || 
                   mls.includes(searchTerm) || 
                   notes.includes(searchTerm);
        });
    }

    // Filter analyses by deal score
    filterByDealScore(minScore = 0, maxScore = 10) {
        const analyses = this.getAllAnalyses();
        return analyses.filter(analysis => {
            const score = analysis.calculations.dealScore;
            return score >= minScore && score <= maxScore;
        });
    }

    // Filter analyses by property type
    filterByPropertyType(propertyType) {
        const analyses = this.getAllAnalyses();
        return analyses.filter(analysis => 
            analysis.propertyData.propertyType === propertyType
        );
    }

    // Export analyses to JSON
    exportAnalyses() {
        try {
            const analyses = this.getAllAnalyses();
            const exportData = {
                analyses,
                exportDate: new Date().toISOString(),
                totalCount: analyses.length
            };
            
            const blob = new Blob([JSON.stringify(exportData, null, 2)], {
                type: 'application/json'
            });
            
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `brrrr_analyses_${new Date().toISOString().split('T')[0]}.json`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            
            return true;
        } catch (error) {
            console.error('Error exporting analyses:', error);
            return false;
        }
    }

    // Import analyses from JSON
    importAnalyses(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            
            reader.onload = (e) => {
                try {
                    const importData = JSON.parse(e.target.result);
                    const analyses = importData.analyses || [];
                    
                    // Validate analyses structure
                    const validAnalyses = analyses.filter(analysis => 
                        analysis.propertyData && analysis.calculations
                    );
                    
                    // Merge with existing analyses
                    const existingAnalyses = this.getAllAnalyses();
                    const mergedAnalyses = [...existingAnalyses, ...validAnalyses];
                    
                    localStorage.setItem(this.storageKey, JSON.stringify(mergedAnalyses));
                    this.updateStats();
                    
                    resolve({
                        success: true,
                        imported: validAnalyses.length,
                        total: mergedAnalyses.length
                    });
                } catch (error) {
                    reject(new Error('Invalid file format'));
                }
            };
            
            reader.onerror = () => reject(new Error('Error reading file'));
            reader.readAsText(file);
        });
    }

    // Get storage usage
    getStorageUsage() {
        try {
            const analyses = localStorage.getItem(this.storageKey);
            const stats = localStorage.getItem(this.statsKey);
            
            const analysesSize = new Blob([analyses]).size;
            const statsSize = new Blob([stats]).size;
            const totalSize = analysesSize + statsSize;
            
            return {
                analysesSize,
                statsSize,
                totalSize,
                totalSizeKB: (totalSize / 1024).toFixed(2)
            };
        } catch (error) {
            console.error('Error calculating storage usage:', error);
            return null;
        }
    }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = BRRRRStorage;
} 