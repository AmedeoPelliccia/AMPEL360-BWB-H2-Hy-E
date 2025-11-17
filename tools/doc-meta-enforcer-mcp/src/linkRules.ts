/*
 * Copyright 2025 AMPEL360 Project Contributors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Link Rules for AMPEL360 Documentation
 * 
 * This module defines regex patterns and replacements for automatically
 * hyperlinking standards, regulations, and internal references in
 * AMPEL360 documentation.
 */

export interface LinkRule {
  pattern: RegExp;
  replacement: string; // markdown with $1, $2 etc.
  description: string;
}

export const linkRules: LinkRule[] = [
  // Note: Order matters! More specific patterns should come before general ones
  // to avoid unwanted nested replacements.
  
  // ========== Internal References - ATA Chapters (First, most specific) ==========
  
  {
    pattern: /(?<!\[)\b(ATA_00-GENERAL)\b(?!\]\()/g,
    replacement: "[$1](../O-ORGANIZATION/ATA_00-GENERAL/README.md)",
    description: "ATA 00 - General"
  },
  {
    pattern: /(?<!\[)\b(ATA_01-MAINTENANCE_POLICY_INFORMATION)\b(?!\]\()/g,
    replacement: "[$1](../O-ORGANIZATION/ATA_01-MAINTENANCE_POLICY_INFORMATION/README.md)",
    description: "ATA 01 - Maintenance Policy Information"
  },
  {
    pattern: /(?<!\[)\b(ATA_02-OPERATIONS_INFORMATION)\b(?!\]\()/g,
    replacement: "[$1](../I-INFRASTRUCTURES/ATA_02-OPERATIONS_INFORMATION/README.md)",
    description: "ATA 02 - Operations Information"
  },
  {
    pattern: /(?<!\[)\b(ATA_04-AIRWORTHINESS_LIMITATIONS)\b(?!\]\()/g,
    replacement: "[$1](../O-ORGANIZATION/ATA_04-AIRWORTHINESS_LIMITATIONS/README.md)",
    description: "ATA 04 - Airworthiness Limitations"
  },
  {
    pattern: /(?<!\[)\b(ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS)\b(?!\]\()/g,
    replacement: "[$1](../O-ORGANIZATION/ATA_05-TIME_LIMITS_MAINTENANCE_CHECKS/README.md)",
    description: "ATA 05 - Time Limits / Maintenance Checks"
  },
  {
    pattern: /(?<!\[)\b(ATA_28-FUEL_SAF_CRYOGENIC_H2)\b(?!\]\()/g,
    replacement: "[$1](../T-TECHNOLOGY_AMEDEOPELLICCIA/C2-CIRCULAR_CRYOGENICS_SYSTEMS/ATA_28-FUEL_SAF_CRYOGENIC_H2/README.md)",
    description: "ATA 28 - Fuel (SAF & Cryogenic H2)"
  },
  {
    pattern: /(?<!\[)\b(ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS)\b(?!\]\()/g,
    replacement: "[$1](../N-NEURAL_NETWORKS_USERS_TRACEABILITY/ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS/README.md)",
    description: "ATA 95 - Digital Product Passport & Neural Networks"
  },

  // ========== Internal References - ATA 95 Design Assemblies ==========
  
  {
    pattern: /(?<!\[)\b(95-00-04-A\d{3})\b(?!\]\()/g,
    replacement: "[$1](../95-00_GENERAL/95-00-04_Design/ASSETS/ASSEMBLIES/**/$1_*.md)",
    description: "ATA 95 Design Assembly reference (A-series)"
  },
  {
    pattern: /(?<!\[)\b(95-00-04-P\d{3})\b(?!\]\()/g,
    replacement: "[$1](../95-00_GENERAL/95-00-04_Design/ASSETS/PARTS/**/$1_*.md)",
    description: "ATA 95 Design Part reference (P-series)"
  },
  {
    pattern: /(?<!\[)\b(95-00-04-I\d{3})\b(?!\]\()/g,
    replacement: "[$1](../95-00_GENERAL/95-00-04_Design/ASSETS/INSTALLATIONS/**/$1_*.md)",
    description: "ATA 95 Design Installation reference (I-series)"
  },

  // ========== Internal References - Requirements ==========
  
  {
    pattern: /(?<!\[)\b(RQ-\d{2}-\d{2}-\d{3})\b(?!\]\()/g,
    replacement: "[$1](../../REQUIREMENTS/$1/README.md)",
    description: "Internal requirement reference (RQ-XX-XX-XXX pattern)"
  },
  
  // ========== Internal References - OPT-IN Framework Axes ==========
  
  {
    pattern: /(?<!\[)\b(T-TECHNOLOGY_AMEDEOPELLICCIA)\b(?!\]\()/g,
    replacement: "[$1](../../OPT-IN_FRAMEWORK/T-TECHNOLOGY_AMEDEOPELLICCIA/README.md)",
    description: "OPT-IN Framework - Technology Axis"
  },
  {
    pattern: /(?<!\[)\b(N-NEURAL_NETWORKS_USERS_TRACEABILITY)\b(?!\]\()/g,
    replacement: "[$1](../../OPT-IN_FRAMEWORK/N-NEURAL_NETWORKS_USERS_TRACEABILITY/README.md)",
    description: "OPT-IN Framework - Neural Networks & Traceability Axis"
  },
  {
    pattern: /(?<!\[)\b(I-INFRASTRUCTURES)\b(?!\]\()/g,
    replacement: "[$1](../../OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/README.md)",
    description: "OPT-IN Framework - Infrastructures Axis"
  },
  {
    pattern: /(?<!\[)\b(O-ORGANIZATION)\b(?!\]\()/g,
    replacement: "[$1](../../OPT-IN_FRAMEWORK/O-ORGANIZATION/README.md)",
    description: "OPT-IN Framework - Organization Axis"
  },
  {
    pattern: /(?<!\[)\b(P-PROGRAM)\b(?!\]\()/g,
    replacement: "[$1](../../OPT-IN_FRAMEWORK/P-PROGRAM/README.md)",
    description: "OPT-IN Framework - Program Axis"
  },

  // ========== Aviation Standards & Regulations ==========
  
  {
    pattern: /(?<!\[)\b(EASA\s+CS-25)\b(?!\]\()/g,
    replacement: "[$1](https://www.easa.europa.eu/en/document-library/certification-specifications/cs-25-large-aeroplanes)",
    description: "EASA Certification Specifications for Large Aeroplanes"
  },
  {
    pattern: /(?<!\[)\b(FAA\s+(?:14\s+CFR\s+)?Part\s+25|FAR\s+25)\b(?!\]\()/g,
    replacement: "[$1](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25)",
    description: "FAA Federal Aviation Regulations Part 25"
  },
  {
    pattern: /(?<!\[)\b(ICAO\s+Annex\s+6)\b(?!\]\()/g,
    replacement: "[$1](https://www.icao.int/safety/airnavigation/Pages/annex-6.aspx)",
    description: "ICAO Annex 6 - Operation of Aircraft"
  },
  {
    pattern: /(?<!\[)\b(ICAO\s+Annex\s+8)\b(?!\]\()/g,
    replacement: "[$1](https://www.icao.int/safety/airnavigation/Pages/annex-8.aspx)",
    description: "ICAO Annex 8 - Airworthiness of Aircraft"
  },

  // ========== AI & Data Regulations ==========
  
  {
    pattern: /(?<!\[)\b(EU\s+AI\s+Act)\b(?!\]\()/g,
    replacement: "[$1](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689)",
    description: "EU Artificial Intelligence Act"
  },
  {
    pattern: /(?<!\[)\b(EASA\s+AI\s+Roadmap)\b(?!\]\()/g,
    replacement: "[$1](https://www.easa.europa.eu/en/research-development/artificial-intelligence)",
    description: "EASA AI Roadmap"
  },
  {
    pattern: /(?<!\[)\b(GDPR)\b(?!\]\()/g,
    replacement: "[$1](https://gdpr-info.eu/)",
    description: "General Data Protection Regulation"
  },

  // ========== Technical Standards ==========
  
  {
    pattern: /(?<!\[)\b(S1000D)\b(?!\]\()/g,
    replacement: "[$1](http://www.s1000d.org/)",
    description: "S1000D Technical Publications Standard"
  },
  {
    pattern: /(?<!\[)\b(ATA\s+iSpec\s+2200)\b(?!\]\()/g,
    replacement: "[$1](https://www.ata.org/resources/specifications)",
    description: "ATA iSpec 2200 Information Standards"
  },
  {
    pattern: /(?<!\[)\b(ARP4754A)\b(?!\]\()/g,
    replacement: "[$1](https://www.sae.org/standards/content/arp4754a/)",
    description: "SAE ARP4754A - Development of Civil Aircraft Systems"
  },
  {
    pattern: /(?<!\[)\b(ARP4761)\b(?!\]\()/g,
    replacement: "[$1](https://www.sae.org/standards/content/arp4761/)",
    description: "SAE ARP4761 - Safety Assessment Process"
  },
  {
    pattern: /(?<!\[)\b(DO-178C)\b(?!\]\()/g,
    replacement: "[$1](https://www.rtca.org/content/standards-guidance-materials)",
    description: "RTCA DO-178C - Software Considerations in Airborne Systems"
  },
  {
    pattern: /(?<!\[)\b(DO-254)\b(?!\]\()/g,
    replacement: "[$1](https://www.rtca.org/content/standards-guidance-materials)",
    description: "RTCA DO-254 - Design Assurance for Airborne Electronic Hardware"
  },
  {
    pattern: /(?<!\[)\b(DO-326A)\b(?!\]\()/g,
    replacement: "[$1](https://www.rtca.org/content/standards-guidance-materials)",
    description: "RTCA DO-326A - Airworthiness Security Process Specification"
  },
  {
    pattern: /(?<!\[)\b(ED-202A)\b(?!\]\()/g,
    replacement: "[$1](https://www.eurocae.net/)",
    description: "EUROCAE ED-202A - Airworthiness Security Process Specification"
  },

  // ========== ISO Standards ==========
  
  {
    pattern: /(?<!\[)\b(ISO\s+15926)\b(?!\]\()/g,
    replacement: "[$1](https://www.iso.org/standard/29556.html)",
    description: "ISO 15926 - Industrial automation systems and integration"
  },
  {
    pattern: /(?<!\[)\b(ISO\s+9001)\b(?!\]\()/g,
    replacement: "[$1](https://www.iso.org/iso-9001-quality-management.html)",
    description: "ISO 9001 - Quality Management Systems"
  },
  {
    pattern: /(?<!\[)\b(ISO\s+14001)\b(?!\]\()/g,
    replacement: "[$1](https://www.iso.org/iso-14001-environmental-management.html)",
    description: "ISO 14001 - Environmental Management Systems"
  },

  // ========== Internal References - Requirements ==========
  
  {
    pattern: /(?<!\[)\b(RQ-\d{2}-\d{2}-\d{3})\b(?!\]\()/g,
    replacement: "[$1](../../REQUIREMENTS/$1/README.md)",
    description: "Internal requirement reference (RQ-XX-XX-XXX pattern)"
  },
  
];

/**
 * Apply all link rules to the given text
 * 
 * This function applies link rules while avoiding double-linking by:
 * 1. Extracting existing markdown links and replacing with placeholders
 * 2. Applying each rule and protecting newly-created links immediately
 * 3. Restoring all placeholders at the end
 * 
 * @param text - The input text to process
 * @returns The text with hyperlinks added
 */
export function applyLinkRules(text: string): string {
  const links: string[] = [];
  const markdownLinkPattern = /\[([^\]]+)\]\(([^)]+)\)/g;
  
  // Step 1: Protect existing markdown links
  let processed = text.replace(markdownLinkPattern, (match) => {
    const index = links.length;
    links.push(match);
    return `__MDLINK_${index}__`;
  });

  // Step 2: Apply each link rule, protecting newly-created links immediately
  for (const rule of linkRules) {
    // Apply the rule
    processed = processed.replace(rule.pattern, rule.replacement);
    
    // Immediately protect the newly-created links
    processed = processed.replace(markdownLinkPattern, (match) => {
      const index = links.length;
      links.push(match);
      return `__MDLINK_${index}__`;
    });
  }

  // Step 3: Restore all protected links
  processed = processed.replace(/__MDLINK_(\d+)__/g, (_, index) => {
    return links[parseInt(index, 10)];
  });

  return processed;
}

/**
 * Check if text already contains a hyperlink for the given pattern
 * This helps avoid double-linking
 */
function isAlreadyLinked(text: string, position: number): boolean {
  // Look backwards for '[' and forwards for ']('
  const before = text.substring(Math.max(0, position - 100), position);
  const after = text.substring(position, Math.min(text.length, position + 100));
  
  const openBracket = before.lastIndexOf('[');
  const closeBracket = after.indexOf('](');
  
  return openBracket !== -1 && closeBracket !== -1;
}
