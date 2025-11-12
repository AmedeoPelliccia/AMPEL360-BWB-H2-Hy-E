/**
 * CAOS Integration Module
 * Handles real-time communication with CAOS system
 */

class CAOSIntegration {
    constructor() {
        this.connected = false;
        this.aircraftId = null;
        this.wsConnection = null;
        this.sensorData = {};
        this.alerts = [];
    }

    /**
     * Connect to CAOS system
     */
    async connect(aircraftId) {
        this.aircraftId = aircraftId;
        
        try {
            // Simulate WebSocket connection to CAOS system
            console.log(`Connecting to CAOS for aircraft ${aircraftId}...`);
            
            // In production, this would be:
            // this.wsConnection = new WebSocket(`wss://caos.ampel360.com/aircraft/${aircraftId}`);
            
            // Simulate connection
            setTimeout(() => {
                this.connected = true;
                this.updateConnectionStatus();
                this.startDataStream();
            }, 1000);
            
        } catch (error) {
            console.error('CAOS connection failed:', error);
            this.updateConnectionStatus(false);
        }
    }

    /**
     * Update connection status indicator
     */
    updateConnectionStatus(isConnected = true) {
        const indicator = document.getElementById('caos-connection');
        if (!indicator) return;

        const light = indicator.querySelector('.status-light');
        const text = indicator.querySelector('span:last-child');

        if (isConnected && this.connected) {
            light.className = 'status-light green';
            text.textContent = 'CAOS: Connected';
        } else {
            light.className = 'status-light red';
            text.textContent = 'CAOS: Disconnected';
        }
    }

    /**
     * Start receiving sensor data stream
     */
    startDataStream() {
        // Simulate real-time sensor data
        setInterval(() => {
            this.sensorData = {
                latchForce: 280 + Math.random() * 10,
                sealPressure: {
                    forward: 8.9 + Math.random() * 0.2,
                    aft: 7.8 + Math.random() * 0.2,
                    upper: 8.5 + Math.random() * 0.2,
                    lower: 8.6 + Math.random() * 0.2
                },
                cycles: 15247,
                vibration: 0.3 + Math.random() * 0.1,
                temperature: 22 + Math.random() * 2,
                timestamp: new Date().toISOString()
            };

            this.updateDashboard();
        }, 2000);
    }

    /**
     * Update CAOS dashboard with latest data
     */
    updateDashboard() {
        // Update sensor data display
        const sensorDataDiv = document.getElementById('sensor-data');
        if (sensorDataDiv) {
            sensorDataDiv.innerHTML = `
                <table class="sensor-table">
                    <tr>
                        <td>Latch Force:</td>
                        <td>${this.sensorData.latchForce.toFixed(1)} lbf</td>
                        <td><span class="status-indicator green">●</span></td>
                    </tr>
                    <tr>
                        <td>Seal Pressure (Fwd):</td>
                        <td>${this.sensorData.sealPressure.forward.toFixed(2)} psi</td>
                        <td><span class="status-indicator green">●</span></td>
                    </tr>
                    <tr>
                        <td>Seal Pressure (Aft):</td>
                        <td>${this.sensorData.sealPressure.aft.toFixed(2)} psi</td>
                        <td><span class="status-indicator yellow">●</span></td>
                    </tr>
                    <tr>
                        <td>Seal Pressure (Upper):</td>
                        <td>${this.sensorData.sealPressure.upper.toFixed(2)} psi</td>
                        <td><span class="status-indicator green">●</span></td>
                    </tr>
                    <tr>
                        <td>Seal Pressure (Lower):</td>
                        <td>${this.sensorData.sealPressure.lower.toFixed(2)} psi</td>
                        <td><span class="status-indicator green">●</span></td>
                    </tr>
                    <tr>
                        <td>Cycles:</td>
                        <td>${this.sensorData.cycles}</td>
                        <td><span class="status-indicator green">●</span></td>
                    </tr>
                    <tr>
                        <td>Vibration:</td>
                        <td>${this.sensorData.vibration.toFixed(2)} g</td>
                        <td><span class="status-indicator green">●</span></td>
                    </tr>
                </table>
            `;
        }

        // Update health gauge
        this.updateHealthGauge();

        // Update predictions
        this.updatePredictions();

        // Update alerts
        this.updateAlerts();
    }

    /**
     * Update system health gauge
     */
    updateHealthGauge() {
        const canvas = document.getElementById('health-gauge');
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const healthScore = this.calculateHealthScore();

        // Simple gauge visualization
        canvas.width = 200;
        canvas.height = 200;

        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw gauge
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = 80;

        // Background arc
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0.75 * Math.PI, 2.25 * Math.PI);
        ctx.lineWidth = 20;
        ctx.strokeStyle = '#e0e0e0';
        ctx.stroke();

        // Health score arc
        const endAngle = 0.75 * Math.PI + (healthScore / 100) * 1.5 * Math.PI;
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0.75 * Math.PI, endAngle);
        ctx.lineWidth = 20;
        ctx.strokeStyle = healthScore > 90 ? '#4CAF50' : healthScore > 75 ? '#FFC107' : '#F44336';
        ctx.stroke();

        // Text
        ctx.fillStyle = '#333';
        ctx.font = 'bold 32px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(`${healthScore.toFixed(1)}%`, centerX, centerY);
        ctx.font = '14px Arial';
        ctx.fillText('Health Score', centerX, centerY + 30);
    }

    /**
     * Calculate overall health score
     */
    calculateHealthScore() {
        // Simplified health calculation
        const sealHealth = (
            (this.sensorData.sealPressure.forward / 9.0) * 0.25 +
            (this.sensorData.sealPressure.aft / 9.0) * 0.25 +
            (this.sensorData.sealPressure.upper / 9.0) * 0.25 +
            (this.sensorData.sealPressure.lower / 9.0) * 0.25
        ) * 100;

        const latchHealth = Math.min((this.sensorData.latchForce / 280) * 100, 100);
        const vibrationHealth = Math.max(100 - (this.sensorData.vibration / 0.5) * 100, 0);

        return (sealHealth * 0.5 + latchHealth * 0.3 + vibrationHealth * 0.2);
    }

    /**
     * Update predictive maintenance display
     */
    updatePredictions() {
        const predictionsDiv = document.getElementById('predictions');
        if (!predictionsDiv) return;

        // Simulate predictive maintenance calculations
        const aftSealLife = Math.floor((this.sensorData.sealPressure.aft - 7.0) / 0.012); // Remaining FH
        
        predictionsDiv.innerHTML = `
            <div class="prediction-item">
                <div class="prediction-title">Aft Seal Replacement</div>
                <div class="prediction-value">${aftSealLife} FH</div>
                <div class="prediction-confidence">Confidence: 92%</div>
            </div>
            <div class="prediction-item">
                <div class="prediction-title">Latch Inspection</div>
                <div class="prediction-value">450 FH</div>
                <div class="prediction-confidence">Confidence: 88%</div>
            </div>
        `;
    }

    /**
     * Update alerts display
     */
    updateAlerts() {
        const alertsDiv = document.getElementById('alerts');
        if (!alertsDiv) return;

        // Check for alert conditions
        this.alerts = [];
        
        if (this.sensorData.sealPressure.aft < 8.0) {
            this.alerts.push({
                level: 'CAUTION',
                message: 'Aft seal pressure degraded',
                time: new Date().toLocaleTimeString(),
                action: 'Schedule inspection within 100 FH'
            });
        }

        if (this.alerts.length === 0) {
            alertsDiv.innerHTML = '<p class="no-alerts">No active alerts</p>';
        } else {
            alertsDiv.innerHTML = this.alerts.map(alert => `
                <div class="alert-item alert-${alert.level.toLowerCase()}">
                    <div class="alert-header">
                        <span class="alert-level">${alert.level}</span>
                        <span class="alert-time">${alert.time}</span>
                    </div>
                    <div class="alert-message">${alert.message}</div>
                    <div class="alert-action">${alert.action}</div>
                </div>
            `).join('');
        }
    }

    /**
     * Run diagnostic
     */
    async runDiagnostic(type) {
        console.log(`Running ${type} diagnostic...`);
        
        return new Promise((resolve) => {
            setTimeout(() => {
                const results = {
                    type: type,
                    timestamp: new Date().toISOString(),
                    status: 'COMPLETED',
                    findings: [
                        {
                            system: 'Latch System',
                            status: 'OPTIMAL',
                            details: 'All 8 latches engaged, force within limits'
                        },
                        {
                            system: 'Seal Pressure',
                            status: 'DEGRADED',
                            details: 'Aft seal at 81% effectiveness',
                            recommendation: 'Schedule seal inspection'
                        },
                        {
                            system: 'Actuation',
                            status: 'NORMAL',
                            details: 'Opening time: 4.2 seconds'
                        },
                        {
                            system: 'Sensors',
                            status: 'CALIBRATED',
                            details: 'All sensors responding, no drift detected'
                        }
                    ]
                };
                resolve(results);
            }, 2000);
        });
    }

    /**
     * Disconnect from CAOS
     */
    disconnect() {
        if (this.wsConnection) {
            this.wsConnection.close();
        }
        this.connected = false;
        this.updateConnectionStatus(false);
    }
}

// Global CAOS instance
const caos = new CAOSIntegration();

// Auto-connect when aircraft is selected
document.addEventListener('DOMContentLoaded', () => {
    const aircraftSelector = document.getElementById('aircraft');
    if (aircraftSelector) {
        aircraftSelector.addEventListener('change', (e) => {
            if (e.target.value) {
                caos.connect(e.target.value);
            } else {
                caos.disconnect();
            }
        });
    }
});
