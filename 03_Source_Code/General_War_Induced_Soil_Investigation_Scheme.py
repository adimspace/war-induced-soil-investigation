#!/usr/bin/env python3
"""
Create a comprehensive methodological scheme for war-induced soil disturbance and contamination investigation
This serves as a general pattern for scientific publications in soil contamination research
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrow, Polygon
import numpy as np
import seaborn as sns

# Set style for professional appearance
plt.style.use('default')
sns.set_palette("husl")

def create_general_war_soil_methodology():
    """Create comprehensive general methodological scheme for war-induced soil investigation"""
    fig, ax = plt.subplots(1, 1, figsize=(22, 18))
    
    # Professional color palette for different phases
    colors = {
        'pre_assessment': '#2c3e50',      # Dark blue-gray
        'field_work': '#e74c3c',         # Red
        'laboratory': '#f39c12',         # Orange
        'advanced_analysis': '#2ecc71',   # Green
        'data_processing': '#9b59b6',     # Purple
        'risk_assessment': '#3498db',     # Blue
        'remediation': '#1abc9c',         # Teal
        'monitoring': '#e67e22',          # Dark orange
        'quality': '#95a5a6'              # Gray
    }
    
    # Clear axes and set limits
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 18)
    ax.axis('off')
    
    # Main Title
    ax.text(7, 17.3, 'Comprehensive Methodological Scheme for Investigation of\nWar-Induced Soil Disturbance and Contamination', 
            fontsize=20, fontweight='bold', ha='center', va='center')
    ax.text(7, 16.7, 'A General Framework for Scientific Research and Environmental Assessment', 
            fontsize=14, style='italic', ha='center', va='center')
    
    # Phase 0: Pre-Assessment and Planning
    pre_box = FancyBboxPatch((0.5, 15), 13, 1.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=colors['pre_assessment'], 
                             edgecolor='black', 
                             alpha=0.9, linewidth=2)
    ax.add_patch(pre_box)
    ax.text(7, 15.8, 'PHASE 0: PRE-ASSESSMENT & STRATEGIC PLANNING', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(3.5, 15.4, '• Historical conflict mapping', fontsize=10, ha='center', color='white')
    ax.text(3.5, 15.1, '• Munition type identification', fontsize=10, ha='center', color='white')
    ax.text(7, 15.4, '• Baseline soil characterization', fontsize=10, ha='center', color='white')
    ax.text(7, 15.1, '• Safety protocols & access permits', fontsize=10, ha='center', color='white')
    ax.text(10.5, 15.4, '• Stakeholder engagement', fontsize=10, ha='center', color='white')
    ax.text(10.5, 15.1, '• Resource allocation planning', fontsize=10, ha='center', color='white')
    
    # Phase 1: Field Investigation
    field_box = FancyBboxPatch((0.5, 12.5), 4.2, 2.2, 
                               boxstyle="round,pad=0.1", 
                               facecolor=colors['field_work'], 
                               edgecolor='black', 
                               alpha=0.9, linewidth=2)
    ax.add_patch(field_box)
    ax.text(2.6, 14.3, 'PHASE I: FIELD INVESTIGATION', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(2.6, 13.9, 'Geophysical Survey:', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(2.6, 13.6, '• Magnetometry (metal detection)', fontsize=9, ha='center', color='white')
    ax.text(2.6, 13.3, '• Ground-penetrating radar', fontsize=9, ha='center', color='white')
    ax.text(2.6, 13.0, '• Electrical resistivity', fontsize=9, ha='center', color='white')
    ax.text(2.6, 12.7, 'Soil Sampling Strategy:', fontsize=10, fontweight='bold', ha='center', color='white')
    
    # Phase 2: Laboratory Analysis
    lab_box = FancyBboxPatch((4.9, 12.5), 4.2, 2.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=colors['laboratory'], 
                             edgecolor='black', 
                             alpha=0.9, linewidth=2)
    ax.add_patch(lab_box)
    ax.text(7, 14.3, 'PHASE II: LABORATORY ANALYSIS', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(7, 13.9, 'Chemical Analysis:', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(7, 13.6, '• Heavy metals (ICP-MS/XRF)', fontsize=9, ha='center', color='white')
    ax.text(7, 13.3, '• Explosive residues', fontsize=9, ha='center', color='white')
    ax.text(7, 13.0, '• Organic pollutants', fontsize=9, ha='center', color='white')
    ax.text(7, 12.7, 'Physical Properties:', fontsize=10, fontweight='bold', ha='center', color='white')
    
    # Phase 3: Advanced Analysis
    advanced_box = FancyBboxPatch((9.3, 12.5), 4.2, 2.2, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=colors['advanced_analysis'], 
                                  edgecolor='black', 
                                  alpha=0.9, linewidth=2)
    ax.add_patch(advanced_box)
    ax.text(11.4, 14.3, 'PHASE III: ADVANCED ANALYSIS', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(11.4, 13.9, 'Microscopic Analysis:', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(11.4, 13.6, '• SEM/EDS morphology', fontsize=9, ha='center', color='white')
    ax.text(11.4, 13.3, '• Particle size distribution', fontsize=9, ha='center', color='white')
    ax.text(11.4, 13.0, '• Mineral identification', fontsize=9, ha='center', color='white')
    ax.text(11.4, 12.7, 'Isotopic Analysis:', fontsize=10, fontweight='bold', ha='center', color='white')
    
    # Quality Control (Horizontal across phases)
    qc_box = FancyBboxPatch((0.5, 11.8), 13, 0.5, 
                            boxstyle="round,pad=0.05", 
                            facecolor=colors['quality'], 
                            edgecolor='black', 
                            alpha=0.8, linewidth=1)
    ax.add_patch(qc_box)
    ax.text(7, 12.05, 'QUALITY CONTROL: Reference Materials • Blank Samples • Duplicate Analysis • Inter-laboratory Validation', 
            fontsize=10, fontweight='bold', ha='center', color='white')
    
    # Phase 4: Data Processing & Integration
    data_box = FancyBboxPatch((1, 10), 5.5, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor=colors['data_processing'], 
                              edgecolor='black', 
                              alpha=0.9, linewidth=2)
    ax.add_patch(data_box)
    ax.text(3.75, 11.1, 'PHASE IV: DATA PROCESSING & INTEGRATION', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(3.75, 10.7, '• Geospatial analysis (GIS mapping)', fontsize=10, ha='center', color='white')
    ax.text(3.75, 10.4, '• Statistical correlation analysis', fontsize=10, ha='center', color='white')
    ax.text(3.75, 10.1, '• Contamination source apportionment', fontsize=10, ha='center', color='white')
    
    # Phase 5: Risk Assessment
    risk_box = FancyBboxPatch((7.5, 10), 5.5, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor=colors['risk_assessment'], 
                              edgecolor='black', 
                              alpha=0.9, linewidth=2)
    ax.add_patch(risk_box)
    ax.text(10.25, 11.1, 'PHASE V: RISK ASSESSMENT', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(10.25, 10.7, '• Human health risk evaluation', fontsize=10, ha='center', color='white')
    ax.text(10.25, 10.4, '• Ecological risk assessment', fontsize=10, ha='center', color='white')
    ax.text(10.25, 10.1, '• Exposure pathway modeling', fontsize=10, ha='center', color='white')
    
    # Phase 6: Remediation Planning
    remediation_box = FancyBboxPatch((1, 7.8), 5.5, 1.8, 
                                     boxstyle="round,pad=0.1", 
                                     facecolor=colors['remediation'], 
                                     edgecolor='black', 
                                     alpha=0.9, linewidth=2)
    ax.add_patch(remediation_box)
    ax.text(3.75, 9.2, 'PHASE VI: REMEDIATION PLANNING', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(3.75, 8.8, '• Technology selection & optimization', fontsize=10, ha='center', color='white')
    ax.text(3.75, 8.5, '• Cost-benefit analysis', fontsize=10, ha='center', color='white')
    ax.text(3.75, 8.2, '• Implementation timeline', fontsize=10, ha='center', color='white')
    ax.text(3.75, 7.9, '• Stakeholder consultation', fontsize=10, ha='center', color='white')
    
    # Phase 7: Long-term Monitoring
    monitoring_box = FancyBboxPatch((7.5, 7.8), 5.5, 1.8, 
                                    boxstyle="round,pad=0.1", 
                                    facecolor=colors['monitoring'], 
                                    edgecolor='black', 
                                    alpha=0.9, linewidth=2)
    ax.add_patch(monitoring_box)
    ax.text(10.25, 9.2, 'PHASE VII: LONG-TERM MONITORING', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(10.25, 8.8, '• Post-remediation effectiveness', fontsize=10, ha='center', color='white')
    ax.text(10.25, 8.5, '• Environmental fate & transport', fontsize=10, ha='center', color='white')
    ax.text(10.25, 8.2, '• Adaptive management strategies', fontsize=10, ha='center', color='white')
    ax.text(10.25, 7.9, '• Community health surveillance', fontsize=10, ha='center', color='white')
    
    # Arrows showing workflow
    # Horizontal arrows between phases 1-3
    arrow1 = FancyArrow(4.6, 13.6, 0.2, 0, width=0.03, head_width=0.1, 
                        head_length=0.08, fc='black', ec='black', alpha=0.8)
    ax.add_patch(arrow1)
    
    arrow2 = FancyArrow(9.0, 13.6, 0.2, 0, width=0.03, head_width=0.1, 
                        head_length=0.08, fc='black', ec='black', alpha=0.8)
    ax.add_patch(arrow2)
    
    # Vertical arrows to phases 4-5
    arrow3 = FancyArrow(3.75, 12.4, 0, -0.8, width=0.03, head_width=0.1, 
                        head_length=0.08, fc='black', ec='black', alpha=0.8)
    ax.add_patch(arrow3)
    
    arrow4 = FancyArrow(10.25, 12.4, 0, -0.8, width=0.03, head_width=0.1, 
                        head_length=0.08, fc='black', ec='black', alpha=0.8)
    ax.add_patch(arrow4)
    
    # Arrows to phases 6-7
    arrow5 = FancyArrow(3.75, 9.9, 0, -0.4, width=0.03, head_width=0.1, 
                        head_length=0.08, fc='black', ec='black', alpha=0.8)
    ax.add_patch(arrow5)
    
    arrow6 = FancyArrow(10.25, 9.9, 0, -0.4, width=0.03, head_width=0.1, 
                        head_length=0.08, fc='black', ec='black', alpha=0.8)
    ax.add_patch(arrow6)
    
    # Key Methodological Components
    components_box = FancyBboxPatch((0.5, 5.5), 13, 1.8, 
                                    boxstyle="round,pad=0.1", 
                                    facecolor='lightgray', 
                                    edgecolor='black', 
                                    alpha=0.9, linewidth=2)
    ax.add_patch(components_box)
    ax.text(7, 6.9, 'KEY METHODOLOGICAL COMPONENTS', fontsize=14, fontweight='bold', ha='center', color='black')
    
    # Create three columns for key components
    ax.text(2.8, 6.4, 'Analytical Techniques:', fontsize=11, fontweight='bold', ha='center', color='black')
    ax.text(2.8, 6.1, '• ICP-MS/OES, XRF, GC-MS', fontsize=9, ha='center', color='black')
    ax.text(2.8, 5.9, '• SEM-EDS, XRD, FTIR', fontsize=9, ha='center', color='black')
    ax.text(2.8, 5.7, '• Magnetic susceptibility', fontsize=9, ha='center', color='black')
    
    ax.text(7, 6.4, 'Contamination Indicators:', fontsize=11, fontweight='bold', ha='center', color='black')
    ax.text(7, 6.1, '• Heavy metals (Pb, Cu, Zn, Cr)', fontsize=9, ha='center', color='black')
    ax.text(7, 5.9, '• Explosive compounds (TNT, RDX)', fontsize=9, ha='center', color='black')
    ax.text(7, 5.7, '• Magnetic particles/spherules', fontsize=9, ha='center', color='black')
    
    ax.text(11.2, 6.4, 'Assessment Protocols:', fontsize=11, fontweight='bold', ha='center', color='black')
    ax.text(11.2, 6.1, '• International standards (ISO)', fontsize=9, ha='center', color='black')
    ax.text(11.2, 5.9, '• National guidelines', fontsize=9, ha='center', color='black')
    ax.text(11.2, 5.7, '• Risk-based approaches', fontsize=9, ha='center', color='black')
    
    # Research Applications and Innovation
    applications_box = FancyBboxPatch((0.5, 3.2), 13, 2, 
                                      boxstyle="round,pad=0.1", 
                                      facecolor='#34495e', 
                                      edgecolor='black', 
                                      alpha=0.9, linewidth=2)
    ax.add_patch(applications_box)
    ax.text(7, 4.8, 'RESEARCH APPLICATIONS & INNOVATION AREAS', fontsize=14, fontweight='bold', ha='center', color='white')
    
    ax.text(3.5, 4.3, 'Scientific Research:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(3.5, 4.0, '• Novel contamination tracers', fontsize=10, ha='center', color='white')
    ax.text(3.5, 3.7, '• Rapid screening methods', fontsize=10, ha='center', color='white')
    ax.text(3.5, 3.4, '• Predictive modeling', fontsize=10, ha='center', color='white')
    
    ax.text(7, 4.3, 'Policy & Management:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(7, 4.0, '• Environmental regulations', fontsize=10, ha='center', color='white')
    ax.text(7, 3.7, '• Post-conflict reconstruction', fontsize=10, ha='center', color='white')
    ax.text(7, 3.4, '• International cooperation', fontsize=10, ha='center', color='white')
    
    ax.text(10.5, 4.3, 'Technology Development:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(10.5, 4.0, '• Remote sensing integration', fontsize=10, ha='center', color='white')
    ax.text(10.5, 3.7, '• AI/ML data interpretation', fontsize=10, ha='center', color='white')
    ax.text(10.5, 3.4, '• Mobile laboratory systems', fontsize=10, ha='center', color='white')
    
    # Output Products
    outputs_box = FancyBboxPatch((0.5, 0.8), 13, 2.2, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor='#2980b9', 
                                 edgecolor='black', 
                                 alpha=0.9, linewidth=2)
    ax.add_patch(outputs_box)
    ax.text(7, 2.6, 'EXPECTED OUTPUTS & DELIVERABLES', fontsize=14, fontweight='bold', ha='center', color='white')
    
    ax.text(2.8, 2.1, 'Scientific Publications:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(2.8, 1.8, '• Peer-reviewed articles', fontsize=10, ha='center', color='white')
    ax.text(2.8, 1.5, '• Conference presentations', fontsize=10, ha='center', color='white')
    ax.text(2.8, 1.2, '• Method standardization', fontsize=10, ha='center', color='white')
    ax.text(2.8, 0.9, '• Database development', fontsize=10, ha='center', color='white')
    
    ax.text(7, 2.1, 'Technical Reports:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(7, 1.8, '• Contamination assessment', fontsize=10, ha='center', color='white')
    ax.text(7, 1.5, '• Risk evaluation studies', fontsize=10, ha='center', color='white')
    ax.text(7, 1.2, '• Remediation recommendations', fontsize=10, ha='center', color='white')
    ax.text(7, 0.9, '• Monitoring protocols', fontsize=10, ha='center', color='white')
    
    ax.text(11.2, 2.1, 'Policy Documents:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(11.2, 1.8, '• Guidelines & standards', fontsize=10, ha='center', color='white')
    ax.text(11.2, 1.5, '• Best practice manuals', fontsize=10, ha='center', color='white')
    ax.text(11.2, 1.2, '• Regulatory frameworks', fontsize=10, ha='center', color='white')
    ax.text(11.2, 0.9, '• Training materials', fontsize=10, ha='center', color='white')
    
    # Add connecting arrows for outputs
    arrow7 = FancyArrow(7, 7.7, 0, -4.5, width=0.04, head_width=0.15, 
                        head_length=0.12, fc='darkblue', ec='darkblue', alpha=0.7)
    ax.add_patch(arrow7)
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/General_War_Induced_Soil_Investigation_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: General_War_Induced_Soil_Investigation_Scheme.png")

def create_sampling_strategy_scheme():
    """Create detailed sampling strategy scheme"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    
    colors = {
        'impact': '#e74c3c',
        'transect': '#f39c12', 
        'background': '#2ecc71',
        'strategy': '#9b59b6'
    }
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(6, 9.5, 'Sampling Strategy for War-Induced Soil Contamination Studies', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Impact zone sampling
    impact_circle = Circle((3, 7), 1.2, facecolor=colors['impact'], alpha=0.6, edgecolor='black')
    ax.add_patch(impact_circle)
    ax.text(3, 7, 'IMPACT\nZONE', fontsize=11, fontweight='bold', ha='center', color='white')
    
    # Crater detail
    crater = Circle((3, 7), 0.3, facecolor='darkred', edgecolor='black')
    ax.add_patch(crater)
    
    # Sample points around crater
    crater_points = [(2.7, 7.3), (3.3, 7.3), (3.3, 6.7), (2.7, 6.7), (3, 7.5), (3, 6.5)]
    for i, (x, y) in enumerate(crater_points):
        point = Circle((x, y), 0.08, facecolor='yellow', edgecolor='black')
        ax.add_patch(point)
        ax.text(x+0.15, y+0.15, f'C{i+1}', fontsize=8, fontweight='bold')
    
    # Transect sampling
    for i, distance in enumerate([1.5, 2.0, 2.5]):
        circle = Circle((3, 7), distance, fill=False, edgecolor=colors['transect'], 
                       linestyle='--', linewidth=2, alpha=0.8)
        ax.add_patch(circle)
        
        # Transect points
        angles = [0, 45, 90, 135, 180, 225, 270, 315]
        for j, angle in enumerate(angles):
            rad = np.radians(angle)
            x = 3 + distance * np.cos(rad)
            y = 7 + distance * np.sin(rad)
            if 1 <= x <= 11 and 1 <= y <= 9:  # Keep within bounds
                point = Circle((x, y), 0.06, facecolor='orange', edgecolor='black')
                ax.add_patch(point)
                ax.text(x+0.1, y+0.1, f'T{i+1}', fontsize=7)
    
    # Background sampling
    bg_points = [(1, 8), (1, 6), (1, 4), (5, 8.5), (5, 5.5), (8, 8), (8, 6), (8, 4)]
    for i, (x, y) in enumerate(bg_points):
        point = Circle((x, y), 0.08, facecolor=colors['background'], edgecolor='black')
        ax.add_patch(point)
        ax.text(x+0.15, y+0.15, f'B{i+1}', fontsize=8, fontweight='bold')
    
    # Legend
    legend_items = [
        ('Crater samples (0-2m)', 'yellow', 'C'),
        ('Transect samples (2-40m)', 'orange', 'T'),
        ('Background samples (>40m)', colors['background'], 'B')
    ]
    
    for i, (label, color, symbol) in enumerate(legend_items):
        y_pos = 3 - i * 0.4
        legend_circle = Circle((9.5, y_pos), 0.1, facecolor=color, edgecolor='black')
        ax.add_patch(legend_circle)
        ax.text(9.8, y_pos, f'{symbol} - {label}', fontsize=10, va='center')
    
    # Sampling protocol
    protocol_box = FancyBboxPatch((6.5, 4), 5, 3.5, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=colors['strategy'], 
                                  edgecolor='black', 
                                  alpha=0.8, linewidth=2)
    ax.add_patch(protocol_box)
    ax.text(9, 7.1, 'SAMPLING PROTOCOL', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(9, 6.7, 'Sample Collection:', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(9, 6.4, '• Surface layer (0-10 cm)', fontsize=9, ha='center', color='white')
    ax.text(9, 6.1, '• Composite samples (~15g)', fontsize=9, ha='center', color='white')
    ax.text(9, 5.8, '• GPS coordinates recorded', fontsize=9, ha='center', color='white')
    ax.text(9, 5.5, 'Quality Assurance:', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(9, 5.2, '• Field blanks (10%)', fontsize=9, ha='center', color='white')
    ax.text(9, 4.9, '• Duplicate samples (20%)', fontsize=9, ha='center', color='white')
    ax.text(9, 4.6, '• Chain of custody', fontsize=9, ha='center', color='white')
    ax.text(9, 4.3, '• Preservation protocols', fontsize=9, ha='center', color='white')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Sampling_Strategy_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created: Sampling_Strategy_Scheme.png")

def create_analytical_workflow_scheme():
    """Create comprehensive analytical workflow scheme"""
    fig, ax = plt.subplots(1, 1, figsize=(18, 14))
    
    colors = {
        'sample_prep': '#e74c3c',
        'screening': '#f39c12',
        'quantitative': '#2ecc71',
        'advanced': '#9b59b6',
        'data': '#3498db'
    }
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(7, 11.5, 'Analytical Workflow for War-Induced Soil Contamination Assessment', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Sample preparation
    prep_box = FancyBboxPatch((0.5, 9), 3, 2, 
                              boxstyle="round,pad=0.1", 
                              facecolor=colors['sample_prep'], 
                              edgecolor='black', 
                              alpha=0.8, linewidth=2)
    ax.add_patch(prep_box)
    ax.text(2, 10.5, 'SAMPLE PREPARATION', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(2, 10.1, '• Drying (<40°C)', fontsize=9, ha='center', color='white')
    ax.text(2, 9.8, '• Sieving (<2mm)', fontsize=9, ha='center', color='white')
    ax.text(2, 9.5, '• Grinding (<50μm)', fontsize=9, ha='center', color='white')
    ax.text(2, 9.2, '• Homogenization', fontsize=9, ha='center', color='white')
    
    # Screening analysis
    screen_box = FancyBboxPatch((4, 9), 3, 2, 
                                boxstyle="round,pad=0.1", 
                                facecolor=colors['screening'], 
                                edgecolor='black', 
                                alpha=0.8, linewidth=2)
    ax.add_patch(screen_box)
    ax.text(5.5, 10.5, 'SCREENING ANALYSIS', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5.5, 10.1, '• Magnetic susceptibility', fontsize=9, ha='center', color='white')
    ax.text(5.5, 9.8, '• Portable XRF', fontsize=9, ha='center', color='white')
    ax.text(5.5, 9.5, '• pH & conductivity', fontsize=9, ha='center', color='white')
    ax.text(5.5, 9.2, '• Visual inspection', fontsize=9, ha='center', color='white')
    
    # Quantitative analysis
    quant_box = FancyBboxPatch((7.5, 9), 3, 2, 
                               boxstyle="round,pad=0.1", 
                               facecolor=colors['quantitative'], 
                               edgecolor='black', 
                               alpha=0.8, linewidth=2)
    ax.add_patch(quant_box)
    ax.text(9, 10.5, 'QUANTITATIVE ANALYSIS', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(9, 10.1, '• ICP-MS/OES metals', fontsize=9, ha='center', color='white')
    ax.text(9, 9.8, '• GC-MS organics', fontsize=9, ha='center', color='white')
    ax.text(9, 9.5, '• Ion chromatography', fontsize=9, ha='center', color='white')
    ax.text(9, 9.2, '• Total carbon/nitrogen', fontsize=9, ha='center', color='white')
    
    # Advanced analysis
    advanced_box = FancyBboxPatch((11, 9), 2.5, 2, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=colors['advanced'], 
                                  edgecolor='black', 
                                  alpha=0.8, linewidth=2)
    ax.add_patch(advanced_box)
    ax.text(12.25, 10.5, 'ADVANCED ANALYSIS', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(12.25, 10.1, '• SEM-EDS', fontsize=9, ha='center', color='white')
    ax.text(12.25, 9.8, '• XRD mineralogy', fontsize=9, ha='center', color='white')
    ax.text(12.25, 9.5, '• Isotope ratios', fontsize=9, ha='center', color='white')
    ax.text(12.25, 9.2, '• FTIR spectroscopy', fontsize=9, ha='center', color='white')
    
    # Data processing
    data_box = FancyBboxPatch((3, 6), 8, 2, 
                              boxstyle="round,pad=0.1", 
                              facecolor=colors['data'], 
                              edgecolor='black', 
                              alpha=0.8, linewidth=2)
    ax.add_patch(data_box)
    ax.text(7, 7.5, 'DATA PROCESSING & INTERPRETATION', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(5, 7.1, 'Statistical Analysis:', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(5, 6.8, '• Descriptive statistics', fontsize=9, ha='center', color='white')
    ax.text(5, 6.5, '• Correlation analysis', fontsize=9, ha='center', color='white')
    ax.text(5, 6.2, '• Multivariate statistics', fontsize=9, ha='center', color='white')
    
    ax.text(9, 7.1, 'Spatial Analysis:', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(9, 6.8, '• GIS mapping', fontsize=9, ha='center', color='white')
    ax.text(9, 6.5, '• Interpolation methods', fontsize=9, ha='center', color='white')
    ax.text(9, 6.2, '• Hotspot identification', fontsize=9, ha='center', color='white')
    
    # Quality metrics
    quality_box = FancyBboxPatch((1, 3.5), 12, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor='lightgray', 
                                 edgecolor='black', 
                                 alpha=0.8, linewidth=2)
    ax.add_patch(quality_box)
    ax.text(7, 4.6, 'QUALITY ASSURANCE METRICS', fontsize=12, fontweight='bold', ha='center', color='black')
    ax.text(3, 4.1, 'Accuracy: CRM recovery 85-115%', fontsize=10, ha='center', color='black')
    ax.text(7, 4.1, 'Precision: RSD <15% for duplicates', fontsize=10, ha='center', color='black')
    ax.text(11, 4.1, 'Detection limits: Method specific', fontsize=10, ha='center', color='black')
    ax.text(7, 3.8, 'Blank contamination: <5% of sample values', fontsize=10, ha='center', color='black')
    
    # Output products
    output_box = FancyBboxPatch((2, 1), 10, 2, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#34495e', 
                                edgecolor='black', 
                                alpha=0.8, linewidth=2)
    ax.add_patch(output_box)
    ax.text(7, 2.6, 'ANALYTICAL OUTPUTS', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(4, 2.1, '• Contamination concentration maps', fontsize=10, ha='center', color='white')
    ax.text(4, 1.8, '• Source fingerprinting results', fontsize=10, ha='center', color='white')
    ax.text(4, 1.5, '• Quality control reports', fontsize=10, ha='center', color='white')
    ax.text(4, 1.2, '• Method validation data', fontsize=10, ha='center', color='white')
    
    ax.text(10, 2.1, '• Risk assessment parameters', fontsize=10, ha='center', color='white')
    ax.text(10, 1.8, '• Remediation target values', fontsize=10, ha='center', color='white')
    ax.text(10, 1.5, '• Monitoring recommendations', fontsize=10, ha='center', color='white')
    ax.text(10, 1.2, '• Database for future studies', fontsize=10, ha='center', color='white')
    
    # Add arrows
    arrows = [
        (3.5, 10, 0.4, 0),  # prep to screening
        (7, 10, 0.4, 0),    # screening to quantitative
        (10.5, 10, 0.4, 0), # quantitative to advanced
        (7, 8.9, 0, -0.8),  # to data processing
        (7, 5.9, 0, -0.8)   # to outputs
    ]
    
    for x, y, dx, dy in arrows:
        arrow = FancyArrow(x, y, dx, dy, width=0.03, head_width=0.1, 
                          head_length=0.08, fc='black', ec='black', alpha=0.7)
        ax.add_patch(arrow)
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Analytical_Workflow_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created: Analytical_Workflow_Scheme.png")

def main():
    """Generate all general methodological schemes"""
    print("Generating comprehensive methodological schemes for war-induced soil investigation...")
    
    create_general_war_soil_methodology()
    create_sampling_strategy_scheme()
    create_analytical_workflow_scheme()
    
    print("\nAll general methodological schemes have been created successfully!")
    print("Files saved in: /Users/adim/Documents/Igph/SoilDegradation/")
    print("\nGenerated files:")
    print("1. General_War_Induced_Soil_Investigation_Scheme.png - Comprehensive methodology framework")
    print("2. Sampling_Strategy_Scheme.png - Detailed sampling protocols")
    print("3. Analytical_Workflow_Scheme.png - Complete analytical workflow")

if __name__ == "__main__":
    main()
