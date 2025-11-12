# I - Infrastructures

**CRITICAL NOTE:** This axis of the OPT-IN framework contains all the technical data, standards, and procedures for the **off-board ecosystem** that supports the AMPEL360 aircraft. It defines the "world" in which the aircraft operates.

## Scope and Purpose
The `I-INFRASTRUCTURES` domain governs everything required on the ground to enable safe and efficient flight operations, maintenance, and training. This includes:

-   **Flight & Ground Operations:** The manuals and procedures used by flight crews and ground personnel (ATA 02, ATA 10).
-   **Ground Support Equipment (GSE):** The specifications, manuals, and certification for all specialized and general tooling (ATA 03, ATA 13).
-   **Infrastructure Standards:** The normative standards that airports, energy suppliers, and GSE manufacturers must adhere to for global interoperability (ATA 85-90).
-   **Training Infrastructure:** The technical basis for flight simulators used for crew training and certification (ATA 115, ATA 116).

## Governance
-   **Single Source of Truth:** This repository is the authoritative source for all ground-based operational and support requirements.
-   **Version Control & Integrity:** All documents and data are under strict revision control, with filenames, metadata sidecars (`.meta.yaml`), and CI validation enforcing compliance and data integrity.
-   **Interface Control:** This axis formally defines the physical, electrical, and data interfaces between the aircraft (defined in `T-TECHNOLOGY`) and the ground environment.

## Hyperlinked Index

-   [`ATA_02-OPERATIONS_INFORMATION`](./ATA_02-OPERATIONS_INFORMATION/): Flight Crew Operating Manual (FCOM), QRH, MEL, etc.
-   [`ATA_03-SUPPORT_INFORMATION_GSE`](./ATA_03-SUPPORT_INFORMATION_GSE/): Manuals and certifications for all Ground Support Equipment.
-   [`ATA_10-PARKING_MOORING_STORAGE_RTS`](./ATA_10-PARKING_MOORING_STORAGE_RTS/): Procedures for non-operational aircraft handling.
-   [`ATA_13-HARDWARE_AND_GENERAL_TOOLS`](./ATA_13-HARDWARE_AND_GENERAL_TOOLS/): Catalogs for standard hardware and common tools.
-   [`ATA_85-90-INFRASTRUCTURE_INTERFACE_STANDARDS`](./ATA_85-90-INFRASTRUCTURE_INTERFACE_STANDARDS/): Normative standards for airport and energy infrastructure.
-   [`ATA_115-FLIGHT_SIMULATOR_SYSTEMS`](./ATA_115-FLIGHT_SIMULATOR_SYSTEMS/): Technical basis for the Full Flight Simulator (FFS).
-   [`ATA_116-FLIGHT_SIMULATOR_CUING_SYSTEM`](./ATA_116-FLIGHT_SIMULATOR_CUING_SYSTEM/): Visual, motion, and aural systems for the FFS.
