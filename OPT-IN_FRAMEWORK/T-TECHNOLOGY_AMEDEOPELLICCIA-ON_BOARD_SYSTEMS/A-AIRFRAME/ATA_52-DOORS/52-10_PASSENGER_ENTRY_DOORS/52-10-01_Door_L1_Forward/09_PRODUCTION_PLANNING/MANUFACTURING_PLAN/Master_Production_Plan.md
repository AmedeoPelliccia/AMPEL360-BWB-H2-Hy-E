# Master Production Plan - Door L1 Forward

**Document:** AMPEL360-52-10-01-PROD-PLAN  
**Status:** PRELIMINARY CONCEPT  
**Date:** 2025-11-03  
**Revision:** Draft 1.0

---

## 1. PRODUCTION CONCEPT

### Manufacturing Philosophy
- **Composite sandwich construction** with CFRP facesheets and Nomex honeycomb core
- **Autoclave cure process** for high-quality, void-free laminates
- **Modular assembly approach** for flexibility and quality
- **Lean manufacturing principles** to minimize waste and maximize efficiency

### Production Flow
```
Material Receiving → Kitting → Layup → Cure → Trim → Assembly → Test → Delivery
     ↓                  ↓         ↓       ↓       ↓        ↓        ↓        ↓
   (Day 1)           (Day 2)   (Day 3) (Day 4) (Day 5)  (Day 8)  (Day 10) (Day 12)
```

### Key Characteristics
- **Cycle time:** 12 working days per unit (steady state)
- **Takt time:** 3.75 days per unit (at 8 units/month)
- **Work-in-process:** 4-6 units typical
- **Quality gates:** 5 major inspection points

---

## 2. CAPACITY PLANNING

### Rate Targets

| Year | Phase | Units/Month | Units/Year | Shifts | Workforce |
|------|-------|-------------|------------|--------|-----------|
| 2026 | Prototype | 0.5 | 6 | 1 | 12 |
| 2027 | LRIP | 2 | 24 | 1 | 15 |
| 2028 | FRP | 8 | 96 | 2 | 25 |
| 2029 | Steady | 8 | 96 | 2 | 22 |

### Critical Path: Autoclave

**Autoclave Capacity Analysis:**
- **Cure cycle:** 8 hours (includes ramp, dwell, cooldown)
- **Capacity:** 2 doors per run (or 4 panels)
- **Setup time:** 2 hours between runs
- **Availability:** 85% (maintenance, holidays)
- **Operating schedule:** 2 shifts, 5 days/week

**Calculations:**
- Available hours/month: 160 hrs/shift × 2 shifts × 0.85 = 272 hours
- Cycle time with setup: 10 hours per run
- Max runs/month: 272 / 10 = 27 runs
- Max doors/month: 27 × 2 = 54 doors (theoretical maximum)
- **Planned:** 16 doors/month (2-shift operation, 30% buffer)

### Bottleneck Analysis

| Process | Capacity | Constraint | Mitigation |
|---------|----------|------------|------------|
| Autoclave | 54 doors/mo | PRIMARY | Service contract with backup |
| Layup | 32 doors/mo | Secondary | Add technicians if needed |
| Trim/drill | 40 doors/mo | None | Adequate capacity |
| Assembly | 28 doors/mo | Potential | Optimize fixtures |
| Inspection | 36 doors/mo | None | Adequate capacity |

---

## 3. WORK BREAKDOWN

### Labor Hours per Unit

| Operation | Hours | Skill Level | Headcount | Cost/Unit |
|-----------|-------|-------------|-----------|-----------|
| Material prep | 4 | Basic | 1 | $120 |
| Layup | 16 | Advanced | 2 | $640 |
| Bagging | 4 | Intermediate | 1 | $120 |
| Cure operation | 2 | Basic | 1 | $60 |
| Trimming | 8 | Advanced | 1 | $320 |
| Assembly | 12 | Intermediate | 2 | $360 |
| Inspection | 6 | Advanced | 1 | $300 |
| **Total** | **52** | Mixed | **9** | **$1,920** |

### Learning Curve

**Assumptions:**
- **Learning rate:** 90% (10% improvement per doubling)
- **First unit:** 52 hours (prototype conditions)
- **Plateau:** 30 hours (steady state, unit 50+)

**Projected Labor Hours:**
| Unit | Hours | Cumulative Avg |
|------|-------|----------------|
| 1 | 52.0 | 52.0 |
| 2 | 46.8 | 49.4 |
| 4 | 42.1 | 45.7 |
| 8 | 37.9 | 42.2 |
| 16 | 34.1 | 39.0 |
| 32 | 30.7 | 36.1 |
| 50 | 30.0 | 34.5 |

---

## 4. FACILITY REQUIREMENTS

### Space Allocation

| Area | Size (m²) | Purpose | Environmental |
|------|-----------|---------|---------------|
| Clean room | 200 | Layup operations | Class 100,000; 23±2°C |
| Autoclave | 100 | Cure + equipment | Standard shop |
| Trim/drill | 150 | Machining ops | Standard shop |
| Assembly | 200 | Integration | Standard shop |
| Storage | 300 | Material/WIP | Climate controlled |
| Quality | 50 | Inspection | Class 100,000 |
| Offices | 100 | Engineering/admin | Standard |
| Utilities | 100 | Support systems | - |
| **Total** | **1,200** | **Minimum** | Multiple zones |

### Layout Principles
- **U-shaped flow** to minimize transport
- **Clean-to-dirty progression** (layup → trim → assembly)
- **Material storage adjacent** to consumption points
- **Quality lab central** for all operations
- **Autoclave external** (service provider initially)

---

## 5. INVESTMENT REQUIREMENTS

### Capital Equipment

| Item | Cost ($k) | Lead Time | Qty | Total |
|------|-----------|-----------|-----|-------|
| Cure mold | 250 | 16 weeks | 1 | 250 |
| Assembly fixtures | 75 | 10 weeks | 1 | 75 |
| Trim fixtures | 30 | 6 weeks | 1 | 30 |
| Drill templates | 20 | 6 weeks | 1 | 20 |
| Material handling | 50 | 8 weeks | 1 | 50 |
| Inspection tools | 45 | 6 weeks | 1 | 45 |
| Clean room setup | 100 | 12 weeks | 1 | 100 |
| IT/documentation | 30 | 4 weeks | 1 | 30 |
| **Total** | **600** | **16 weeks** | - | **600** |

*Note: Autoclave via service provider initially ($2,000/run)*

### Operating Costs (Annual at 8 units/month)

| Category | Annual ($k) | Per Unit |
|----------|-------------|----------|
| Labor | 180 | 1,875 |
| Materials | 720 | 7,500 |
| Autoclave service | 190 | 2,000 |
| Tooling maintenance | 50 | 520 |
| Facility | 120 | 1,250 |
| Quality/test | 40 | 420 |
| Overhead | 100 | 1,040 |
| **Total** | **1,400** | **14,605** |

---

## 6. PRODUCTION CONTROL

### Production Schedule
- **Monthly planning cycle** with weekly updates
- **Material lead time:** 8-12 weeks
- **Build schedule:** Rolling 6-month plan
- **Flexibility:** ±1 unit variance permitted

### Quality Control Points
1. **Material receiving:** Certificate of conformance check
2. **Post-layup:** Visual inspection, photo documentation
3. **Post-cure:** Dimensional check, NDT scan
4. **Post-trim:** Dimensional verification
5. **Final assembly:** Function test, leak test

### Key Performance Indicators
| KPI | Target | Measurement |
|-----|--------|-------------|
| On-time delivery | >95% | Monthly |
| First-pass yield | >90% | Per lot |
| Scrap rate | <5% | Monthly |
| Rework rate | <10% | Per unit |
| Safety incidents | 0 | Continuous |
| Cost variance | ±5% | Monthly |

---

## 7. RISK MITIGATION

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| Autoclave availability | HIGH | Medium | Backup service provider contract |
| Material shortage | HIGH | Low | 3-month safety stock |
| Quality issues | MEDIUM | High | Rigorous process control |
| Skill shortage | MEDIUM | High | Cross-training program |
| Tool damage | HIGH | Low | Spare critical tooling |
| Design changes | HIGH | Medium | Change control discipline |
| Supplier failure | HIGH | Low | Dual sourcing where possible |
| Funding delays | HIGH | Medium | Phased investment approach |

---

## 8. PRODUCTION RAMP STRATEGY

### Phase 1: Prototype (2026)
- **Goal:** Prove manufacturing processes
- **Rate:** 0.5 units/month (6/year)
- **Focus:** Process refinement, documentation
- **Investment:** Minimal tooling, service providers

### Phase 2: LRIP (2027)
- **Goal:** Demonstrate stable production
- **Rate:** 2 units/month (24/year)
- **Focus:** Quality system, supplier stabilization
- **Investment:** Production tooling, facility setup

### Phase 3: FRP (2028)
- **Goal:** Achieve full rate capability
- **Rate:** 8 units/month (96/year)
- **Focus:** Efficiency, cost reduction
- **Investment:** Automation, capacity expansion

### Phase 4: Steady State (2029+)
- **Goal:** Maintain rate, continuous improvement
- **Rate:** 8 units/month sustained
- **Focus:** Lean practices, cost optimization
- **Investment:** Technology upgrades as needed

---

## 9. ASSUMPTIONS AND DEPENDENCIES

### Key Assumptions
- Design frozen by Q2 2026
- Funding secured by Q3 2026
- Suppliers qualified by Q4 2026
- Facility ready by Q1 2027
- First prototype build Q4 2026
- Autoclave services available as needed
- Workforce can be recruited and trained

### Critical Dependencies
1. **Design maturity:** Must complete professional FEA
2. **Prototype validation:** GVT damping ≥3% required
3. **Certification progress:** Type design approval track
4. **Supplier readiness:** Long-lead items procurement
5. **Facility availability:** Clean room and autoclave access
6. **Funding:** $600k capital + operating costs

---

## 10. NEXT STEPS

### Immediate Actions (Next 3 Months)
- [ ] Complete professional structural analysis
- [ ] Refine manufacturing cost estimates
- [ ] Identify candidate manufacturing facilities
- [ ] Engage potential autoclave service providers
- [ ] Develop detailed tooling designs
- [ ] Create manufacturing process FMEA

### Short Term (3-6 Months)
- [ ] Secure design freeze commitment
- [ ] Finalize tooling specifications
- [ ] Request quotes from suppliers
- [ ] Develop quality system framework
- [ ] Create training curriculum
- [ ] Build business case for investment

### Medium Term (6-12 Months)
- [ ] Procure long-lead tooling
- [ ] Qualify suppliers
- [ ] Establish facility agreements
- [ ] Hire and train core team
- [ ] Build first prototype article
- [ ] Validate manufacturing processes

---

**Document Control:**
- **Approval:** Pending
- **Distribution:** Production Planning Team
- **Review Cycle:** Quarterly
- **Next Update:** 2026-Q1 or upon major change
