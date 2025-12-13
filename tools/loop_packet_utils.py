#!/usr/bin/env python3
"""
Loop Packet Common Utilities

Shared functions and constants for Loop Packet management tools.
"""

from pathlib import Path
from typing import Dict, Tuple


# CSV Column definitions
CSV_COLUMNS = [
    'bb_id', 'artifact_name', 'body_summary', 'brain_summary',
    'body_ata', 'brain_ata', 'dal', 'brain_type',
    'dpp_id', 'image_id', 'sbom_ref', 'bom_ref',
    'am_ref', 'dv_ref', 'om_class', 'oav_ref', 'dt_ref',
    'loop_packet_path',
    'am_status', 'dv_status', 'dpp_status', 'om_status', 'oav_status', 'dt_status',
    'next_gate', 'last_truth_snapshot_id', 'notes'
]


def get_repo_paths(script_dir: Path = None) -> Dict[str, Path]:
    """
    Get standard repository paths.
    
    Args:
        script_dir: Directory where the calling script is located (usually __file__.parent)
                   If None, uses current working directory's parent
    
    Returns:
        Dictionary with paths: repo_root, register_base, loops_base, register_path
    """
    if script_dir is None:
        script_dir = Path.cwd()
    
    repo_root = script_dir.parent if script_dir.name == 'tools' else script_dir
    
    register_base = (
        repo_root / "OPT-IN_FRAMEWORK" / "N-NEURAL_NETWORKS_USERS_TRACEABILITY" /
        "ATA_95-DIGITAL_PRODUCT_PASSPORT_NEURAL_NETWORKS" / "95-00_GENERAL" /
        "95-00-01_Overview" / "95-00-01-010_Identity_Registers"
    )
    
    loops_base = register_base / "LOOPS"
    register_path = register_base / "ASSETS" / "95-00-01-010-A-001_BodyBrain_Identity_Register.csv"
    
    return {
        'repo_root': repo_root,
        'register_base': register_base,
        'loops_base': loops_base,
        'register_path': register_path
    }


def compute_next_step(am_status: str, dv_status: str, dpp_status: str,
                     om_status: str, oav_status: str) -> Tuple[str, str]:
    """
    Compute the next gate and action based on current circuit state.
    
    This is the canonical deterministic rule for the CCert/CVal circuit.
    
    Args:
        am_status: Status of At-Rest Model
        dv_status: Status of Design Validation
        dpp_status: Status of Digital Product Passport
        om_status: Status of Operational Mission
        oav_status: Status of On-Asset Validation
    
    Returns:
        Tuple of (next_gate, next_action)
    """
    if am_status == 'NOT_STARTED':
        return 'DV', "Write AM (At-Rest Model) first"
    
    elif dv_status not in ['PASSED', 'APPROVED']:
        return 'DV', "Complete DV and mark DV gate"
    
    elif dpp_status == 'NOT_ISSUED' and dv_status in ['PASSED', 'APPROVED']:
        return 'OAV', "Issue DPP (locked identity + claims)"
    
    elif om_status == 'NOT_DEFINED':
        return 'OAV', "Author OM (what DPP predicts operationally)"
    
    elif oav_status not in ['PASSED', 'APPROVED']:
        return 'OAV', "Define/Execute OAV (asset context truth validation)"
    
    else:
        return 'COMPLETE', "Append DT snapshot and propose AM′ (change-controlled update)"


def validate_bb_id(bb_id: str) -> bool:
    """
    Validate BB ID format.
    
    Args:
        bb_id: BB ID to validate
    
    Returns:
        True if valid, False otherwise
    """
    parts = bb_id.split('-')
    if len(parts) != 3:
        return False
    
    # First part should be 2 digits (ATA chapter)
    if not parts[0].isdigit() or len(parts[0]) != 2:
        return False
    
    # Second part should be "BB"
    if parts[1] != 'BB':
        return False
    
    # Third part should be 3 digits
    if not parts[2].isdigit() or len(parts[2]) != 3:
        return False
    
    return True


def format_csv_entry(bb_id: str, artifact_name: str, body_summary: str,
                    brain_summary: str, body_ata: str, brain_ata: str,
                    dal: str, brain_type: str, om_class: str,
                    notes: str = "") -> Dict[str, str]:
    """
    Create a CSV entry dictionary for a new artifact.
    
    Args:
        bb_id: BB ID
        artifact_name: Artifact name
        body_summary: Body summary
        brain_summary: Brain summary
        body_ata: Body ATA chapter
        brain_ata: Brain ATA chapter
        dal: Design Assurance Level
        brain_type: Brain type
        om_class: Operational Mission class
        notes: Optional notes
    
    Returns:
        Dictionary with all CSV columns
    """
    loop_path = f"LOOPS/{bb_id}"
    
    return {
        'bb_id': bb_id,
        'artifact_name': artifact_name,
        'body_summary': body_summary,
        'brain_summary': brain_summary,
        'body_ata': body_ata,
        'brain_ata': brain_ata,
        'dal': dal,
        'brain_type': brain_type,
        'dpp_id': 'TBD',
        'image_id': 'TBD',
        'sbom_ref': 'TBD',
        'bom_ref': 'TBD',
        'am_ref': f"{loop_path}/AM_{bb_id}.md",
        'dv_ref': 'TBD',
        'om_class': om_class,
        'oav_ref': 'TBD',
        'dt_ref': f"{loop_path}/DT_{bb_id}.md",
        'loop_packet_path': loop_path,
        'am_status': 'NOT_STARTED',
        'dv_status': 'NOT_STARTED',
        'dpp_status': 'NOT_ISSUED',
        'om_status': 'NOT_DEFINED',
        'oav_status': 'NOT_STARTED',
        'dt_status': '0',
        'next_gate': 'DV',
        'last_truth_snapshot_id': 'NONE',
        'notes': notes or f"Generated by Loop Packet Generator"
    }
