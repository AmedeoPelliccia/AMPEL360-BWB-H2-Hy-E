/**
 * Digital Twin Viewer Module
 * Handles 3D visualization and interaction with digital twin
 */

class DigitalTwinViewer {
    constructor() {
        this.twinData = null;
        this.syncStatus = 'disconnected';
        this.simulationRunning = false;
    }

    /**
     * Initialize digital twin viewer
     */
    async initialize(containerId) {
        const container = document.getElementById(containerId);
        if (!container) {
            console.error('Digital twin container not found');
            return;
        }

        // In production, this would initialize Three.js or similar 3D library
        console.log('Initializing digital twin viewer...');
        
        // Simulate loading
        container.innerHTML = `
            <div class="twin-loading">
                <div class="spinner"></div>
                <p>Loading digital twin model...</p>
            </div>
        `;

        setTimeout(() => {
            this.renderTwinView(container);
        }, 2000);
    }

    /**
     * Render digital twin view
     */
    renderTwinView(container) {
        container.innerHTML = `
            <div class="twin-viewport">
                <div class="twin-placeholder">
                    <svg width="100%" height="400" viewBox="0 0 800 400">
                        <!-- Door outline -->
                        <rect x="250" y="50" width="300" height="300" 
                              fill="#e3f2fd" stroke="#1976d2" stroke-width="3"/>
                        
                        <!-- Window -->
                        <rect x="350" y="100" width="100" height="120" 
                              fill="#bbdefb" stroke="#1976d2" stroke-width="2"/>
                        
                        <!-- Latches (8 points) -->
                        <circle cx="260" cy="100" r="8" fill="#4CAF50"/>
                        <circle cx="260" cy="175" r="8" fill="#4CAF50"/>
                        <circle cx="260" cy="250" r="8" fill="#4CAF50"/>
                        <circle cx="260" cy="325" r="8" fill="#4CAF50"/>
                        <circle cx="540" cy="100" r="8" fill="#4CAF50"/>
                        <circle cx="540" cy="175" r="8" fill="#4CAF50"/>
                        <circle cx="540" cy="250" r="8" fill="#4CAF50"/>
                        <circle cx="540" cy="325" r="8" fill="#4CAF50"/>
                        
                        <!-- Hinges -->
                        <rect x="230" y="90" width="20" height="30" fill="#757575"/>
                        <rect x="230" y="280" width="20" height="30" fill="#757575"/>
                        
                        <!-- Seals (color-coded) -->
                        <line x1="250" y1="50" x2="550" y2="50" 
                              stroke="#4CAF50" stroke-width="6" opacity="0.7"/>
                        <line x1="250" y1="350" x2="550" y2="350" 
                              stroke="#FFC107" stroke-width="6" opacity="0.7"/>
                        <line x1="250" y1="50" x2="250" y2="350" 
                              stroke="#4CAF50" stroke-width="6" opacity="0.7"/>
                        <line x1="550" y1="50" x2="550" y2="350" 
                              stroke="#4CAF50" stroke-width="6" opacity="0.7"/>
                        
                        <!-- Labels -->
                        <text x="400" y="30" text-anchor="middle" fill="#333" font-size="16" font-weight="bold">
                            Door L1 Forward - Digital Twin
                        </text>
                        <text x="620" y="100" fill="#333" font-size="12">
                            ● Latch Engaged
                        </text>
                        <text x="620" y="120" fill="#4CAF50" font-size="12">
                            ● Seal Good
                        </text>
                        <text x="620" y="140" fill="#FFC107" font-size="12">
                            ● Seal Degraded
                        </text>
                    </svg>
                </div>
                
                <div class="twin-info">
                    <h4>Digital Twin Status</h4>
                    <table class="info-table">
                        <tr>
                            <td>Sync Status:</td>
                            <td><span id="twin-sync-status" class="status-badge yellow">Synchronizing...</span></td>
                        </tr>
                        <tr>
                            <td>Last Sync:</td>
                            <td id="twin-last-sync">--</td>
                        </tr>
                        <tr>
                            <td>Model Version:</td>
                            <td>v2.1.0</td>
                        </tr>
                        <tr>
                            <td>Accuracy:</td>
                            <td>98.5%</td>
                        </tr>
                    </table>
                    
                    <h4>Component Status</h4>
                    <div class="component-status">
                        <div class="component-item">
                            <span class="status-indicator green">●</span>
                            <span>Latch System: Optimal</span>
                        </div>
                        <div class="component-item">
                            <span class="status-indicator yellow">●</span>
                            <span>Aft Seal: 81% (Degraded)</span>
                        </div>
                        <div class="component-item">
                            <span class="status-indicator green">●</span>
                            <span>Actuator: Normal</span>
                        </div>
                        <div class="component-item">
                            <span class="status-indicator green">●</span>
                            <span>Sensors: Calibrated</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    /**
     * Synchronize digital twin with physical door
     */
    async syncWithAircraft() {
        console.log('Synchronizing digital twin...');
        
        const statusBadge = document.getElementById('twin-sync-status');
        const lastSyncText = document.getElementById('twin-last-sync');
        
        if (statusBadge) {
            statusBadge.textContent = 'Syncing...';
            statusBadge.className = 'status-badge yellow';
        }

        return new Promise((resolve) => {
            setTimeout(() => {
                this.syncStatus = 'synced';
                
                if (statusBadge) {
                    statusBadge.textContent = 'Synchronized';
                    statusBadge.className = 'status-badge green';
                }
                
                if (lastSyncText) {
                    lastSyncText.textContent = new Date().toLocaleString();
                }
                
                console.log('Digital twin synchronized');
                resolve(true);
            }, 2000);
        });
    }

    /**
     * Run simulation
     */
    async runSimulation(scenarioId = 'default') {
        console.log(`Running simulation: ${scenarioId}`);
        
        this.simulationRunning = true;
        
        // Simulate running a what-if scenario
        return new Promise((resolve) => {
            setTimeout(() => {
                const results = {
                    scenario: scenarioId,
                    timestamp: new Date().toISOString(),
                    predictions: [
                        {
                            parameter: 'Aft Seal Degradation',
                            current: '81%',
                            predicted_30d: '78%',
                            predicted_90d: '72%',
                            action_required: 'Replace before 90 days'
                        },
                        {
                            parameter: 'Latch Wear',
                            current: '98%',
                            predicted_30d: '97.5%',
                            predicted_90d: '96%',
                            action_required: 'None'
                        }
                    ],
                    confidence: 0.92
                };
                
                this.simulationRunning = false;
                console.log('Simulation complete', results);
                resolve(results);
            }, 3000);
        });
    }

    /**
     * Show historical data
     */
    showHistory(timeRange = '30d') {
        console.log(`Loading history: ${timeRange}`);
        
        // In production, this would query historical database
        const historyData = {
            timeRange: timeRange,
            dataPoints: [
                {
                    date: '2025-10-01',
                    sealPressureAft: 8.5,
                    healthScore: 95.2
                },
                {
                    date: '2025-10-15',
                    sealPressureAft: 8.2,
                    healthScore: 92.1
                },
                {
                    date: '2025-11-01',
                    sealPressureAft: 7.9,
                    healthScore: 88.5
                },
                {
                    date: '2025-11-03',
                    sealPressureAft: 7.8,
                    healthScore: 87.3
                }
            ]
        };

        // Display history (simplified)
        alert(`History loaded: ${historyData.dataPoints.length} data points over ${timeRange}\n\nSeal pressure trend: Declining from 8.5 to 7.8 psi\nHealth score trend: Declining from 95.2% to 87.3%`);
    }

    /**
     * Compare actual vs predicted
     */
    compareActualVsPredicted() {
        // Get current sensor data from CAOS
        if (!caos.connected) {
            alert('CAOS not connected. Cannot compare data.');
            return;
        }

        const comparison = {
            latchForce: {
                actual: caos.sensorData.latchForce,
                predicted: 280,
                deviation: ((caos.sensorData.latchForce - 280) / 280 * 100).toFixed(2)
            },
            sealPressureAft: {
                actual: caos.sensorData.sealPressure.aft,
                predicted: 9.0,
                deviation: ((caos.sensorData.sealPressure.aft - 9.0) / 9.0 * 100).toFixed(2)
            }
        };

        console.log('Comparison results:', comparison);
        return comparison;
    }
}

// Global digital twin instance
const digitalTwin = new DigitalTwinViewer();

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Initialize when digital twin tab is shown
    const twinSection = document.getElementById('digital-twin');
    if (twinSection) {
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.target.classList.contains('active')) {
                    digitalTwin.initialize('twin-viewer');
                }
            });
        });
        
        observer.observe(twinSection, {
            attributes: true,
            attributeFilter: ['class']
        });
    }
});

// Global functions for button onclick handlers
function syncTwin() {
    digitalTwin.syncWithAircraft().then(() => {
        alert('Digital twin synchronized successfully!');
    });
}

function runSimulation() {
    digitalTwin.runSimulation().then((results) => {
        alert(`Simulation complete!\n\nConfidence: ${(results.confidence * 100).toFixed(1)}%\n\nKey findings:\n- Aft seal replacement needed within 90 days\n- Latch system healthy`);
    });
}

function showHistory() {
    digitalTwin.showHistory('30d');
}
