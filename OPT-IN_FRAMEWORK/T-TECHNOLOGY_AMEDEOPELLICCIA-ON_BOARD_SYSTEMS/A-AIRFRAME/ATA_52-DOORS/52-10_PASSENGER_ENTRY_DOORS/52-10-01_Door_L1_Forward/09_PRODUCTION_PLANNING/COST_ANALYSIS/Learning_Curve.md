# Learning Curve Analysis - Door L1 Forward

**Document:** AMPEL360-52-10-01-LEARNING  
**Date:** 2025-11-03  
**Status:** DRAFT

---

## 1. LEARNING CURVE OVERVIEW

### Theory
Manufacturing learning curves reflect the improvement in production efficiency as experience is gained. Labor hours typically decrease by a fixed percentage with each doubling of cumulative production.

### Assumptions for Door L1 Forward
- **Learning rate:** 90% (10% improvement per doubling)
- **First unit:** 52 hours (prototype conditions)
- **Steady state:** 30 hours (achieved around unit 50)
- **Basis:** Industry standards for aerospace composite structures

---

## 2. LABOR HOUR PROJECTIONS

### Cumulative Units vs. Hours

| Unit | Hours | Hours Saved | Cumulative Avg | Total Hours |
|------|-------|-------------|----------------|-------------|
| 1 | 52.0 | 0.0 | 52.0 | 52 |
| 2 | 46.8 | 5.2 | 49.4 | 99 |
| 4 | 42.1 | 4.7 | 45.7 | 183 |
| 8 | 37.9 | 4.2 | 42.2 | 337 |
| 16 | 34.1 | 3.8 | 39.0 | 624 |
| 32 | 30.7 | 3.4 | 36.1 | 1,154 |
| 50 | 30.0 | 0.7 | 34.5 | 1,723 |
| 64 | 30.0 | 0.0 | 33.8 | 2,161 |
| 96 | 30.0 | 0.0 | 32.9 | 3,161 |

### Learning Curve Formula
- **T(n) = T(1) × n^b**
- Where: b = log(learning rate) / log(2)
- For 90% curve: b = log(0.9) / log(2) = -0.152
- **T(n) = 52 × n^(-0.152)**

---

## 3. PRODUCTION PHASE ANALYSIS

### Prototype Phase (Units 1-6)
- **Average hours:** 45 hours/unit
- **Total hours:** 270 hours
- **Duration:** 2026 Q4
- **Labor cost:** $1,800/unit average
- **Characteristics:**
  - High variability
  - Significant rework
  - Process refinement
  - Documentation creation

### LRIP Phase (Units 7-30)
- **Average hours:** 36 hours/unit
- **Total hours:** 864 hours
- **Duration:** 2027
- **Labor cost:** $1,440/unit average
- **Characteristics:**
  - Process stabilization
  - Reduced rework
  - Workforce training
  - Supplier stabilization

### FRP Phase (Units 31-96)
- **Average hours:** 30 hours/unit
- **Total hours:** 1,980 hours
- **Duration:** 2028
- **Labor cost:** $1,200/unit average
- **Characteristics:**
  - Steady state achieved
  - Consistent quality
  - Minimal rework
  - Continuous improvement

---

## 4. COST IMPLICATIONS

### Direct Labor Cost Reduction

| Phase | Units | Avg Hours | Labor Rate | Cost/Unit | Total Cost |
|-------|-------|-----------|------------|-----------|------------|
| Prototype | 1-6 | 45 | $40/hr | $1,800 | $10,800 |
| LRIP | 7-30 | 36 | $40/hr | $1,440 | $34,560 |
| FRP | 31-96 | 30 | $40/hr | $1,200 | $79,200 |
| **Total** | **96** | **33.3** | **$40/hr** | **$1,332** | **$124,560** |

### Total Unit Cost Evolution

| Unit Range | Labor | Material | Overhead | Total | Target |
|------------|-------|----------|----------|-------|--------|
| 1-6 | $1,800 | $8,000 | $2,200 | $12,000 | N/A |
| 7-30 | $1,440 | $7,800 | $2,000 | $11,240 | $11,000 |
| 31-50 | $1,200 | $7,500 | $1,800 | $10,500 | $10,000 |
| 51+ | $1,200 | $7,200 | $1,600 | $10,000 | $9,500 |

*Material costs reduce through volume discounts and design optimizations*  
*Overhead reduces through asset utilization and process efficiency*

---

## 5. FACTORS AFFECTING LEARNING

### Positive Factors
- **Training program:** Accelerates skill development
- **Process standardization:** Reduces variability
- **Tooling improvements:** Easier, faster operations
- **Supplier maturity:** Better material quality, fewer delays
- **Design stability:** No changes disrupting flow

### Negative Factors
- **Workforce turnover:** Loss of experience
- **Design changes:** Require relearning
- **Production gaps:** Skills fade during downtime
- **Quality issues:** Increase rework, slow progress
- **Supplier problems:** Disrupt rhythm

---

## 6. LEARNING CURVE MANAGEMENT

### Tracking
- **Actual hours recorded** for each unit
- **Compare to projected** learning curve
- **Identify deviations** and root causes
- **Update projections** based on actual performance

### Improvement Actions
- If learning slower than expected:
  - Increase training intensity
  - Review work instructions for clarity
  - Investigate tool or material issues
  - Add experienced personnel
- If learning faster than expected:
  - Document best practices
  - Share across other programs
  - Update standards

### Risk Mitigation
- **Buffer in schedule** for slower learning
- **Cost reserve** for higher early labor
- **Mentorship program** to accelerate
- **Process audits** to identify improvement opportunities

---

## 7. COMPARISON TO INDUSTRY

### Aerospace Composite Structures
- **Typical learning rates:** 85-95%
- **Complex assemblies:** 90-95%
- **Simple parts:** 85-90%
- **Door L1 Forward:** 90% (moderate complexity)

### Benchmarking
| Program | Type | Learning Rate | Notes |
|---------|------|---------------|-------|
| A350 composite wings | Large structure | 92% | Reference: public data |
| 787 composite fuselage | Large structure | 90% | Reference: public data |
| F-35 composite doors | Similar size | 88% | Reference: industry experience |
| **Door L1 Forward** | **Medium structure** | **90%** | **Conservative estimate** |

---

## 8. FINANCIAL IMPACT

### Investment Payback
- Higher early costs due to learning curve
- Prototype phase: Cost overrun expected
- LRIP phase: Approaching target costs
- FRP phase: Profitable steady state

### Break-Even Analysis
- **Fixed costs:** $600k (tooling, facilities)
- **Variable costs:** $10,000/unit (steady state)
- **Selling price:** $15,000/unit (assumed)
- **Break-even:** ~120 units cumulative
- **Payback period:** ~18 months after FRP start

### Profitability Projection
| Year | Units | Revenue | Costs | Profit | Cumulative |
|------|-------|---------|-------|--------|------------|
| 2026 | 6 | $90k | $672k | -$582k | -$582k |
| 2027 | 24 | $360k | $870k | -$510k | -$1,092k |
| 2028 | 96 | $1,440k | $1,165k | $275k | -$817k |
| 2029 | 96 | $1,440k | $1,060k | $380k | -$437k |
| 2030 | 96 | $1,440k | $1,000k | $440k | $3k |

*Assumes development costs amortized over first 120 units*

---

## 9. RECOMMENDATIONS

### Near-Term (Prototype Phase)
1. **Accept higher costs** - Don't pressure for speed
2. **Focus on quality** - Build right processes from start
3. **Document everything** - Capture lessons learned
4. **Train thoroughly** - Invest in workforce development

### Medium-Term (LRIP Phase)
1. **Standardize processes** - Lock in best practices
2. **Optimize tooling** - Make improvements based on experience
3. **Build supplier partnerships** - Stabilize supply chain
4. **Implement SPC** - Control critical parameters

### Long-Term (FRP Phase)
1. **Continuous improvement** - Never stop getting better
2. **Cross-training** - Build flexible workforce
3. **Technology upgrades** - Consider automation where justified
4. **Cost reduction initiatives** - Target $9,500/unit by unit 50

---

## 10. MONITORING AND REPORTING

### Monthly Metrics
- Actual hours vs. projected
- Learning curve adherence
- Cost per unit trend
- Efficiency improvements

### Quarterly Review
- Update learning curve model
- Revise cost projections
- Identify improvement actions
- Report to management

### Annual Planning
- Set targets for next year
- Budget based on updated curve
- Resource planning
- Investment decisions

---

**Document Control:**
- **Version:** Draft 1.0
- **Owner:** Manufacturing Engineering
- **Review:** Quarterly with actual data
