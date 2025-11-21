# 02-40-11 – EFB Software

## Purpose

This folder contains documentation, source code, and certification assets for the Electronic Flight Bag (EFB) software, an iOS/iPadOS application that provides pilots with digital tools for flight operations, performance calculations, weight & balance, weather visualization, and electronic document viewing.

---

## Scope

The EFB Software subsystem includes:

- **iOS/iPadOS Application**: Native Swift/SwiftUI application for iPad
- **Performance Module**: Takeoff, landing, and cruise performance calculations
- **Weight & Balance Module**: Real-time W&B calculations with H₂ fuel integration
- **Weather Display Module**: Graphical weather overlays and METAR/TAF display
- **Document Viewer**: S1000D and ATA iSpec 2200 document viewing with offline caching
- **Offline-First Architecture**: Full functionality without network connectivity
- **DO-178C Certification**: Level C/D software assurance for safety-critical functions

---

## Folder Organization

### Documentation Files

- **[02-40-11-001_EFB_App_Architecture.md](02-40-11-001_EFB_App_Architecture.md)**: Overall EFB app architecture covering layers, modules, on-device storage, and synchronization mechanisms
- **[02-40-11-002_iOS_Application_Design.md](02-40-11-002_iOS_Application_Design.md)**: iOS-specific design including Swift/SwiftUI patterns, navigation, offline-first principles, and OS integration
- **[02-40-11-003_Offline_Data_Sync.md](02-40-11-003_Offline_Data_Sync.md)**: Offline data synchronization architecture with conflict resolution, delta sync, queues, and error handling
- **[02-40-11-004_Performance_Module.md](02-40-11-004_Performance_Module.md)**: EFB performance module features, algorithms, interfaces, and UX flows
- **[02-40-11-005_Weight_Balance_Module.md](02-40-11-005_Weight_Balance_Module.md)**: W&B module logic, data inputs, safety checks, and ground system integration
- **[02-40-11-006_Weather_Display_Module.md](02-40-11-006_Weather_Display_Module.md)**: Weather visualization features including layers, time sliders, hazards, and performance constraints
- **[02-40-11-007_Document_Viewer.md](02-40-11-007_Document_Viewer.md)**: Document viewer capabilities for S1000D/ATA docs with search, annotations, and offline caching
- **[02-40-11-008_User_Interface_Guidelines.md](02-40-11-008_User_Interface_Guidelines.md)**: EFB-specific UI/UX guidelines for readability, dark mode, input constraints, and safety cues
- **[02-40-11-009_DO_178C_Evidence.md](02-40-11-009_DO_178C_Evidence.md)**: [DO-178C](https://www.rtca.org/content/standards-guidance-materials) evidence structure including plans, standards, reviews, and verification
- **[02-40-11-010_Testing_Strategy.md](02-40-11-010_Testing_Strategy.md)**: Testing strategy covering unit, UI, system tests, device matrix, and regression testing

### ASSETS Folder Structure

The **[ASSETS/](ASSETS/)** folder contains source code, UI designs, and certification assets:

#### Source_Code/
- **ios_app/**: Root folder for iOS app codebase
  - Swift/SwiftUI project structure
  - Xcode workspace and schemes
  - App targets (main app, extensions)
  - Configuration files (Info.plist, entitlements)
  
- **shared_logic/**: Cross-platform business logic
  - Domain models
  - Calculation engines
  - Reusable algorithms
  - Can be shared with Android or web clients in the future
  
- **unit_tests/**: Unit test projects
  - XCTest test suites
  - Test fixtures and mocks
  - Coverage targets (>80% for non-UI code)

#### UI_Designs/
- **02-40-11-A-101_UI_Mockups.figma**: Figma design file with all EFB UI screens and design system
- **02-40-11-A-102_UI_Mockups.pdf**: Exported PDF of UI mockups for reviews and offline access
- **02-40-11-A-103_Style_Guide.pdf**: Complete style guide including colors, typography, controls, and layout rules

#### Certification/
- **02-40-11-A-501_DO_178C_Package.pdf**: Aggregated [DO-178C](https://www.rtca.org/content/standards-guidance-materials) evidence package
  - Software Development Plan (SDP)
  - Software Verification Plan (SVP)
  - Software Configuration Management Plan (SCMP)
  - Software Quality Assurance Plan (SQAP)
  - Software Accomplishment Summary (SAS)
  
- **02-40-11-A-502_Test_Coverage_Report.html**: HTML report with test coverage analysis and results

---

## Key Features

### Performance Calculations
- **Takeoff Performance**: Runway required, V-speeds, climb gradients
- **Landing Performance**: Landing distance, approach speeds, go-around performance
- **Cruise Optimization**: Cost index optimization, altitude selection, step climbs
- **BWB-Specific Models**: Custom aerodynamic models for Blended Wing Body configuration
- **H₂ Fuel Considerations**: Performance adjustments for hydrogen propulsion characteristics

See [02-40-13 Performance Calculator](../02-40-13_Performance_Calculator/) for the calculation engine details.

### Weight & Balance
- **Load Calculation**: Passenger, cargo, fuel weights with station positions
- **CG Envelope Checking**: Real-time CG position verification against limits
- **H₂ Fuel Integration**: Cryogenic hydrogen mass properties and tank configuration
- **Visual CG Display**: Graphical CG position on envelope chart
- **What-If Scenarios**: Pre-flight load planning with multiple configurations

See [02-40-14 Weight & Balance System](../02-40-14_Weight_Balance_System/) for the W&B engine details.

### Weather Display
- **METAR/TAF**: Decoded text and graphical display
- **Graphical Overlays**: Radar, satellite, winds aloft, turbulence, icing
- **Time Slider**: Scrub through forecast timeline
- **Route Weather**: Weather along planned route with significant weather flagged
- **Offline Caching**: Pre-download weather for offline ops

See [02-40-17 Weather Data Processor](../02-40-17_Weather_Data_Processor/) for weather data processing details.

### Document Viewer
- **S1000D Support**: Native rendering of S1000D data modules
- **ATA iSpec 2200**: Support for ATA iSpec 2200 format
- **PDF Viewer**: Embedded PDF rendering for charts and manuals
- **Search**: Full-text search across all documents
- **Annotations**: Pilot notes and highlights (synced across devices)
- **Offline Access**: Full document library available offline

---

## Technology Stack

### Development
- **Language**: Swift 5.9+
- **UI Framework**: SwiftUI 5.0+
- **Minimum iOS**: iOS 16.0+
- **IDE**: Xcode 15+
- **Dependency Management**: Swift Package Manager

### Data Persistence
- **Core Data**: Local structured data storage
- **CloudKit**: iCloud synchronization (optional)
- **File System**: Document and cache storage

### Networking
- **URLSession**: HTTP/HTTPS networking
- **Combine**: Reactive networking layer
- **Background Transfer**: Large file downloads

### Testing
- **XCTest**: Unit and UI testing
- **XCUITest**: End-to-end UI automation
- **Testflight**: Beta distribution

---

## Integration Points

### Backend Services
- **API Gateway** ([02-40-12](../02-40-12_Backend_Services/)): Authentication, data sync
- **Data Service**: Flight data, aircraft configuration, aeronautical data
- **Weather Service** ([02-40-17](../02-40-17_Weather_Data_Processor/)): METAR, TAF, graphical products
- **Document Service**: Electronic document distribution

### On-Board Systems
- **ACARS/SITA** ([02-40-16](../02-40-16_Dispatch_Interface/)): Datalink communication
- **AFDX Network**: Integration with on-board avionics (via gateway)
- **FMS**: Flight plan synchronization (read-only)

### Calculation Engines
- **Performance Calculator** ([02-40-13](../02-40-13_Performance_Calculator/)): Embedded calculation library
- **Weight & Balance** ([02-40-14](../02-40-14_Weight_Balance_System/)): Embedded W&B calculation library

---

## Offline-First Architecture

The EFB app is designed to function fully offline, synchronizing when connectivity is available:

### Data Synchronization
- **Delta Sync**: Only changed data is synchronized
- **Conflict Resolution**: Last-write-wins with user override option
- **Queue Management**: Outgoing changes queued for upload
- **Bandwidth Optimization**: Compressed payloads, incremental updates

### Cached Content
- **Aeronautical Database**: Complete AIRAC cycle data (updated every 28 days)
- **Weather Products**: Last 6 hours of weather data
- **Documents**: Full aircraft manuals and procedures
- **Flight Plans**: Recent and upcoming flight plans

### Background Sync
- **Opportunistic Sync**: Sync when Wi-Fi available
- **Scheduled Sync**: Daily sync of large datasets (during charging)
- **Push Notifications**: Server-initiated sync for critical updates

---

## Certification Status

### DO-178C Software Level

The EFB software contains components at different certification levels per [DO-178C](https://www.rtca.org/content/standards-guidance-materials):

- **Level C** (Major failure condition):
  - Performance calculations used for dispatch decisions
  - Weight & balance calculations
  - Fuel calculations
  
- **Level D** (Minor failure condition):
  - Weather display
  - Document viewer
  - General UI and navigation

### Certification Evidence

Complete [DO-178C](https://www.rtca.org/content/standards-guidance-materials) evidence package includes:

1. **Planning**: SDP, SVP, SCMP, SQAP
2. **Requirements**: High-level and low-level requirements with traceability
3. **Design**: Software architecture and detailed design documents
4. **Implementation**: Source code with coding standards compliance
5. **Verification**: Test cases, test procedures, test results
6. **Configuration Management**: Version control, change management
7. **Quality Assurance**: Independent verification, process audits

See [02-40-11-009_DO_178C_Evidence.md](02-40-11-009_DO_178C_Evidence.md) for details.

---

## Development Workflow

### 1. Requirements
- Captured in Jira/GitHub Issues
- Linked to high-level requirements
- Traceability matrix maintained

### 2. Design
- UI mockups in Figma
- Architecture decisions in ADRs
- Detailed design in code comments

### 3. Implementation
- Follow [Swift Style Guide](https://github.com/raywenderlich/swift-style-guide)
- Code review required (2 approvals for Level C code)
- SwiftLint checks on every commit

### 4. Testing
- Unit tests (>80% coverage)
- UI tests for critical flows
- Device testing matrix (iPad Pro, iPad Air, iPad mini)
- Performance testing (startup time, memory usage)

### 5. Certification Review
- Independent verification for Level C code
- Traceability review
- Test coverage analysis

### 6. Release
- Testflight beta distribution
- Production release via Apple App Store (enterprise distribution)

---

## UI/UX Guidelines

### Design Principles
- **Clarity**: Information hierarchy optimized for at-a-glance comprehension
- **Safety**: Critical information prominently displayed with appropriate color coding
- **Efficiency**: Minimal taps to access frequently used features
- **Consistency**: Familiar iOS patterns and conventions
- **Accessibility**: Support for VoiceOver, Dynamic Type, high contrast

### Dark Mode
- Full dark mode support for night operations
- Automatic switching based on time of day or ambient light
- Red lighting mode for night vision preservation

### Input Methods
- Touch-optimized controls (minimum 44pt tap targets)
- Keyboard support for data entry
- Apple Pencil support for annotations
- External keyboard shortcuts for power users

See [02-40-11-008_User_Interface_Guidelines.md](02-40-11-008_User_Interface_Guidelines.md) for complete guidelines.

---

## Status

- **Development**: In Progress
- **Certification Level**: DO-178C Level C/D (in process)
- **Last Updated**: 2025-11-21
- **Owner**: AMPEL360 EFB Team

---

## References

### Standards and Regulations
- [DO-178C](https://www.rtca.org/content/standards-guidance-materials) – Software Considerations in Airborne Systems
- [DO-278A](https://www.rtca.org/content/standards-guidance-materials) – CNS/ATM Software Integrity Assurance
- [EASA CS-25.1309](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes) – Equipment, Systems, and Installations
- [FAA AC 120-76D](https://www.faa.gov/regulations_policies/advisory_circulars/) – Authorization for Use of Electronic Flight Bags

### Internal Documentation
- [02-40-00-001 Software Architecture Overview](../02-40-00-001_Software_Architecture_Overview.md)
- [02-40-00-004 Software Development Standards](../02-40-00-004_Software_Development_Standards.md)
- [02-40-13 Performance Calculator](../02-40-13_Performance_Calculator/)
- [02-40-14 Weight & Balance System](../02-40-14_Weight_Balance_System/)

### External Resources
- [Swift API Design Guidelines](https://swift.org/documentation/api-design-guidelines/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui)

---

## Document Control

- **Generated with the assistance of AI (GitHub Copilot), prompted by Amedeo Pelliccia**.
- **Status**: DRAFT – Subject to human review and approval.
- **Human approver**: _[to be completed]_.
- **Repository**: `AMPEL360-BWB-H2-Hy-E`
- **Last AI update**: _2025-11-21_.

---

**End of Document**
