#!/usr/bin/env python3
"""
Create visual schemas for methodological approach to post-blast residue analysis
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrow
import numpy as np
import seaborn as sns

# Set style for professional appearance
plt.style.use('default')
sns.set_palette("husl")

def create_main_flowchart():
    """Create the enhanced main methodological flowchart with comprehensive details"""
    fig, ax = plt.subplots(1, 1, figsize=(20, 16))
    
    # Colors for different phases
    colors = {
        'phase1': '#e74c3c',  # Red
        'phase2': '#f39c12',  # Orange
        'phase3': '#2ecc71',  # Green
        'integration': '#9b59b6',  # Purple
        'outcomes': '#3498db',   # Blue
        'geospatial': '#1abc9c',  # Teal
        'qc': '#e67e22'  # Dark Orange
    }
    
    # Clear axes
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 15)
    ax.axis('off')
    
    # Title
    ax.text(6, 14.5, 'Enhanced Methodological Scheme: Magnetic and Chemical Analysis\nof Post-Blast Residue in Soil - Northern Ukraine Case Study', 
            fontsize=18, fontweight='bold', ha='center', va='center')
    
    # Study Site Characterization (Top row)
    site_box = FancyBboxPatch((0.5, 12.5), 11, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor=colors['geospatial'], 
                              edgecolor='black', 
                              alpha=0.8, linewidth=2)
    ax.add_patch(site_box)
    ax.text(6, 13.6, 'STUDY SITES & GEOSPATIAL FRAMEWORK', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(2.5, 13.1, 'BF-O: Ozera Battlefield', fontsize=10, ha='center', color='white')
    ax.text(2.5, 12.8, '(Artillery 120-155mm)', fontsize=9, ha='center', color='white')
    ax.text(6, 13.1, 'UXO-SP: Stari Petrivtsi', fontsize=10, ha='center', color='white')
    ax.text(6, 12.8, '(UXO Destruction Site)', fontsize=9, ha='center', color='white')
    ax.text(9.5, 13.1, 'MHS-D: Demydiv', fontsize=10, ha='center', color='white')
    ax.text(9.5, 12.8, '(Missile Hit Site)', fontsize=9, ha='center', color='white')
    
    # Phase 1: Field Investigation (Enhanced)
    phase1_box = FancyBboxPatch((0.5, 9), 3.5, 3, 
                                boxstyle="round,pad=0.1", 
                                facecolor=colors['phase1'], 
                                edgecolor='black', 
                                alpha=0.8, linewidth=2)
    ax.add_patch(phase1_box)
    ax.text(2.25, 11.6, 'PHASE I', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(2.25, 11.2, 'FIELD INVESTIGATION', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(2.25, 10.8, '• Magnetometer Survey:', fontsize=10, ha='center', color='white')
    ax.text(2.25, 10.5, 'Cesium Vapor PKM-1 (±0.01 nT)', fontsize=9, ha='center', color='white')
    ax.text(2.25, 10.2, 'Grid: 1.0 × 0.1 m resolution', fontsize=9, ha='center', color='white')
    ax.text(2.25, 9.8, '• Soil Sampling Strategy:', fontsize=10, ha='center', color='white')
    ax.text(2.25, 9.5, 'Crater centers/rims/transects', fontsize=9, ha='center', color='white')
    ax.text(2.25, 9.2, 'Background >40m from impacts', fontsize=9, ha='center', color='white')
    
    # Phase 2: Laboratory Analysis (Enhanced)
    phase2_box = FancyBboxPatch((4.25, 9), 3.5, 3, 
                                boxstyle="round,pad=0.1", 
                                facecolor=colors['phase2'], 
                                edgecolor='black', 
                                alpha=0.8, linewidth=2)
    ax.add_patch(phase2_box)
    ax.text(6, 11.6, 'PHASE II', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(6, 11.2, 'LABORATORY ANALYSIS', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(6, 10.8, '• Magnetic Properties:', fontsize=10, ha='center', color='white')
    ax.text(6, 10.5, 'MFK1-FB Kappabridge', fontsize=9, ha='center', color='white')
    ax.text(6, 10.2, 'χlf, χhf, χfd, ARM, Mrs', fontsize=9, ha='center', color='white')
    ax.text(6, 9.8, '• Thermomagnetic Analysis:', fontsize=10, ha='center', color='white')
    ax.text(6, 9.5, 'KLY-5 (-196°C to 700°C)', fontsize=9, ha='center', color='white')
    ax.text(6, 9.2, '• XRF: 10 elements analyzed', fontsize=9, ha='center', color='white')
    
    # Phase 3: Microscopic Analysis (Enhanced)
    phase3_box = FancyBboxPatch((8, 9), 3.5, 3, 
                                boxstyle="round,pad=0.1", 
                                facecolor=colors['phase3'], 
                                edgecolor='black', 
                                alpha=0.8, linewidth=2)
    ax.add_patch(phase3_box)
    ax.text(9.75, 11.6, 'PHASE III', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(9.75, 11.2, 'MICROSCOPIC ANALYSIS', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(9.75, 10.8, '• SEM/EDS Analysis:', fontsize=10, ha='center', color='white')
    ax.text(9.75, 10.5, 'JCXA-733 & JSM-6700F', fontsize=9, ha='center', color='white')
    ax.text(9.75, 10.2, '20 kV, 1-10 μm probe', fontsize=9, ha='center', color='white')
    ax.text(9.75, 9.8, '• Particle Morphology:', fontsize=10, ha='center', color='white')
    ax.text(9.75, 9.5, 'Spherules & fragments', fontsize=9, ha='center', color='white')
    ax.text(9.75, 9.2, '• Magnetic extracts', fontsize=9, ha='center', color='white')
    
    
    # Arrows between phases
    arrow1 = FancyArrow(4, 10.5, 0.15, 0, width=0.05, head_width=0.15, 
                        head_length=0.1, fc='black', ec='black')
    ax.add_patch(arrow1)
    
    arrow2 = FancyArrow(7.8, 10.5, 0.15, 0, width=0.05, head_width=0.15, 
                        head_length=0.1, fc='black', ec='black')
    ax.add_patch(arrow2)
    
    # Quality Control Section (New)
    qc_box = FancyBboxPatch((0.5, 7.2), 5, 1.2, 
                            boxstyle="round,pad=0.1", 
                            facecolor=colors['qc'], 
                            edgecolor='black', 
                            alpha=0.8, linewidth=2)
    ax.add_patch(qc_box)
    ax.text(3, 8, 'QUALITY CONTROL & VALIDATION', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(3, 7.6, '• Certified Reference Materials • Blank samples • Reproducibility tests', fontsize=10, ha='center', color='white')
    ax.text(3, 7.3, '• Background correction • SQUID magnetometer (1×10⁻⁷ A·m⁻¹)', fontsize=9, ha='center', color='white')
    
    # Geospatial Analysis Section (New)
    geo_box = FancyBboxPatch((6.5, 7.2), 5, 1.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=colors['geospatial'], 
                             edgecolor='black', 
                             alpha=0.8, linewidth=2)
    ax.add_patch(geo_box)
    ax.text(9, 8, 'GEOSPATIAL DATA PROCESSING', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(9, 7.6, '• GPS coordinates • Distance calculations • Spatial interpolation', fontsize=10, ha='center', color='white')
    ax.text(9, 7.3, '• Umbric Albeluvisols mapping • Contamination zones', fontsize=9, ha='center', color='white')
    
    # Integration Section (Enhanced)
    integration_box = FancyBboxPatch((2, 5), 8, 1.8, 
                                     boxstyle="round,pad=0.1", 
                                     facecolor=colors['integration'], 
                                     edgecolor='black', 
                                     alpha=0.8, linewidth=2)
    ax.add_patch(integration_box)
    ax.text(6, 6.4, 'DATA INTEGRATION & STATISTICAL ANALYSIS', fontsize=14, fontweight='bold', ha='center', color='white')
    ax.text(4, 5.9, 'Statistical Methods:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(4, 5.6, '• Descriptive statistics (Mean ± SD)', fontsize=10, ha='center', color='white')
    ax.text(4, 5.3, '• Distance-decay relationships', fontsize=10, ha='center', color='white')
    ax.text(8, 5.9, 'Correlation Analysis:', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(8, 5.6, '• Magnetic vs. chemical parameters', fontsize=10, ha='center', color='white')
    ax.text(8, 5.3, '• King\'s plot analysis', fontsize=10, ha='center', color='white')
    
    # Arrows to integration
    arrow3 = FancyArrow(6, 8.9, 0, -1.5, width=0.05, head_width=0.15, 
                        head_length=0.1, fc='black', ec='black')
    ax.add_patch(arrow3)
    
    # Outcomes Section (Enhanced)
    outcomes_box = FancyBboxPatch((1, 2), 10, 2.5, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=colors['outcomes'], 
                                  edgecolor='black', 
                                  alpha=0.8, linewidth=2)
    ax.add_patch(outcomes_box)
    ax.text(6, 4.1, 'OUTCOMES & ENVIRONMENTAL APPLICATIONS', fontsize=14, fontweight='bold', ha='center', color='white')
    
    ax.text(3, 3.6, 'Technical Results:', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(3, 3.2, '• Magnetic enhancement patterns', fontsize=10, ha='center', color='white')
    ax.text(3, 2.9, '• Heavy metal contamination maps', fontsize=10, ha='center', color='white')
    ax.text(3, 2.6, '• Curie temperature signatures', fontsize=10, ha='center', color='white')
    ax.text(3, 2.3, '• Spherule morphology database', fontsize=10, ha='center', color='white')
    
    ax.text(9, 3.6, 'Environmental Applications:', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(9, 3.2, '• Rapid soil contamination screening', fontsize=10, ha='center', color='white')
    ax.text(9, 2.9, '• Post-conflict rehabilitation planning', fontsize=10, ha='center', color='white')
    ax.text(9, 2.6, '• War impact assessment protocols', fontsize=10, ha='center', color='white')
    ax.text(9, 2.3, '• Magnetic proxy development', fontsize=10, ha='center', color='white')
    
    # Arrow to outcomes
    arrow4 = FancyArrow(6, 4.9, 0, -0.3, width=0.05, head_width=0.15, 
                        head_length=0.1, fc='black', ec='black')
    ax.add_patch(arrow4)
    
    # Key Parameters Box (New)
    key_params_box = FancyBboxPatch((0.5, 0.2), 11, 1.3, 
                                    boxstyle="round,pad=0.1", 
                                    facecolor='lightgray', 
                                    edgecolor='black', 
                                    alpha=0.8, linewidth=1)
    ax.add_patch(key_params_box)
    ax.text(6, 1.2, 'KEY PARAMETERS & INNOVATIONS', fontsize=12, fontweight='bold', ha='center', color='black')
    ax.text(3, 0.8, 'Magnetic Parameters: χ, χfd%, ARM, Mrs, S₃₀₀', fontsize=10, ha='center', color='black')
    ax.text(3, 0.5, 'Chemical Elements: Fe, Cr, Ni, Cu, Zn, Pb, As, Co, Ba, Cd', fontsize=10, ha='center', color='black')
    ax.text(9, 0.8, 'Innovation: First magnetic-chemical approach for post-blast', fontsize=10, ha='center', color='black')
    ax.text(9, 0.5, 'soil contamination assessment in Ukraine conflict zones', fontsize=10, ha='center', color='black')
    
    # Equipment boxes
    eq_boxes = [
        (0.5, 2, 'Magnetometer\nGeologorazvedka PKM-1'),
        (2.5, 2, 'Kappabridge\nMFK1-FB, KLY-5'),
        (4.5, 2, 'XRF Analyzer\nElvaX Pro'),
        (6.5, 2, 'SQUID\n2G Enterprises'),
        (8.5, 2, 'SEM/EDS\nJSM-6700F')
    ]
    
    for x, y, text in eq_boxes:
        eq_box = FancyBboxPatch((x, y), 1.8, 1, 
                                boxstyle="round,pad=0.05", 
                                facecolor='lightgray', 
                                edgecolor='black', 
                                alpha=0.7, linewidth=1)
        ax.add_patch(eq_box)
        ax.text(x+0.9, y+0.5, text, fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Site types
    site_text = 'Study Sites: BF-O (Battlefield) • UXO-SP (Ordnance Destruction) • MHS-D (Missile Impact)'
    ax.text(5, 0.5, site_text, fontsize=11, ha='center', style='italic', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Schema_Main_Flowchart.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created: Schema_Main_Flowchart.png")

def create_equipment_network():
    """Create equipment network diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Colors for equipment categories
    colors = {
        'field': '#e74c3c',
        'magnetic': '#f39c12',
        'chemical': '#2ecc71',
        'microscopy': '#9b59b6'
    }
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Equipment Network & Analysis Flow', 
            fontsize=18, fontweight='bold', ha='center')
    
    # Equipment positions and connections
    equipment = {
        'Magnetometer': (2, 8, colors['field'], 'Geologorazvedka PKM-1\n±0.01 nT sensitivity'),
        'Sampling': (2, 6.5, colors['field'], 'Grid System\nSystematic Collection'),
        'Kappabridge': (5, 7.5, colors['magnetic'], 'MFK1-FB\nSusceptibility'),
        'Thermomag': (5, 6, colors['magnetic'], 'KLY-5\nCurie Temperature'),
        'SQUID': (5, 4.5, colors['magnetic'], 'Remanence\nMeasurements'),
        'XRF': (8, 6.5, colors['chemical'], 'ElvaX Pro\nHeavy Metals'),
        'SEM': (8, 4.5, colors['microscopy'], 'JSM-6700F\nMorphology'),
        'EDS': (8, 3, colors['microscopy'], 'JCXA-733\nComposition')
    }
    
    # Draw equipment boxes
    for name, (x, y, color, desc) in equipment.items():
        box = FancyBboxPatch((x-0.7, y-0.4), 1.4, 0.8, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, 
                             edgecolor='black', 
                             alpha=0.8, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y+0.1, name, fontsize=11, fontweight='bold', ha='center', color='white')
        ax.text(x, y-0.2, desc, fontsize=8, ha='center', color='white')
    
    # Draw connections
    connections = [
        ('Magnetometer', 'Kappabridge'),
        ('Sampling', 'Kappabridge'),
        ('Sampling', 'XRF'),
        ('Kappabridge', 'Thermomag'),
        ('Thermomag', 'SQUID'),
        ('SQUID', 'SEM'),
        ('XRF', 'EDS')
    ]
    
    for start, end in connections:
        x1, y1 = equipment[start][:2]
        x2, y2 = equipment[end][:2]
        
        # Calculate arrow direction
        dx = x2 - x1
        dy = y2 - y1
        length = np.sqrt(dx**2 + dy**2)
        
        # Normalize and adjust for box size
        dx_norm = dx / length * 0.7
        dy_norm = dy / length * 0.4
        
        arrow = FancyArrow(x1 + dx_norm/2, y1 + dy_norm/2, 
                          dx - dx_norm, dy - dy_norm,
                          width=0.02, head_width=0.1, 
                          head_length=0.1, fc='gray', ec='gray', alpha=0.7)
        ax.add_patch(arrow)
    
    # Legend
    legend_items = [
        ('Field Equipment', colors['field']),
        ('Magnetic Analysis', colors['magnetic']),
        ('Chemical Analysis', colors['chemical']),
        ('Microscopy', colors['microscopy'])
    ]
    
    for i, (label, color) in enumerate(legend_items):
        y_pos = 2 - i * 0.3
        legend_box = Rectangle((0.5, y_pos-0.1), 0.3, 0.2, 
                              facecolor=color, edgecolor='black', alpha=0.8)
        ax.add_patch(legend_box)
        ax.text(1, y_pos, label, fontsize=10, va='center')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Schema_Equipment_Network.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created: Schema_Equipment_Network.png")

def create_parameter_analysis():
    """Create parameter analysis flowchart"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'Parameter Analysis & Integration Framework', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Parameter categories
    categories = {
        'Magnetic': {
            'pos': (2, 7.5),
            'color': '#e74c3c',
            'params': ['χ - Susceptibility', 'χfd - Frequency Dep.', 'Mrs - Saturation', 'ARM - Remanence']
        },
        'Chemical': {
            'pos': (5, 7.5),
            'color': '#2ecc71',
            'params': ['As - Arsenic', 'Ba - Barium', 'Cu - Copper', 'Fe - Iron', 'Pb - Lead', 'Zn - Zinc']
        },
        'Physical': {
            'pos': (8, 7.5),
            'color': '#9b59b6',
            'params': ['Particle Size', 'Morphology', 'Spatial Distribution']
        }
    }
    
    # Draw parameter boxes
    for cat_name, cat_data in categories.items():
        x, y = cat_data['pos']
        color = cat_data['color']
        params = cat_data['params']
        
        # Main category box
        cat_box = FancyBboxPatch((x-1, y-0.5), 2, len(params)*0.3+1, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor=color, 
                                 edgecolor='black', 
                                 alpha=0.8, linewidth=2)
        ax.add_patch(cat_box)
        
        # Category title
        ax.text(x, y+len(params)*0.15, cat_name + ' Parameters', 
                fontsize=12, fontweight='bold', ha='center', color='white')
        
        # Parameters
        for i, param in enumerate(params):
            ax.text(x, y+len(params)*0.15-0.3-i*0.25, f'• {param}', 
                    fontsize=9, ha='center', color='white')
    
    # Correlation analysis box
    corr_box = FancyBboxPatch((3.5, 4.5), 3, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor='#f39c12', 
                              edgecolor='black', 
                              alpha=0.8, linewidth=2)
    ax.add_patch(corr_box)
    ax.text(5, 5.5, 'CORRELATION ANALYSIS', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(5, 5.1, 'Statistical Integration', fontsize=10, ha='center', color='white')
    ax.text(5, 4.8, 'Spatial Relationships', fontsize=10, ha='center', color='white')
    
    # Results box
    result_box = FancyBboxPatch((2, 2), 6, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#3498db', 
                                edgecolor='black', 
                                alpha=0.8, linewidth=2)
    ax.add_patch(result_box)
    ax.text(5, 3.1, 'INTEGRATED ASSESSMENT', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(5, 2.7, 'Contamination Mapping • Source Identification', fontsize=10, ha='center', color='white')
    ax.text(5, 2.4, 'Risk Evaluation • Remediation Planning', fontsize=10, ha='center', color='white')
    
    # Arrows
    for cat_data in categories.values():
        x, y = cat_data['pos']
        arrow = FancyArrow(x, y-1.5, 0, -0.5, width=0.03, head_width=0.1, 
                          head_length=0.1, fc='black', ec='black', alpha=0.7)
        ax.add_patch(arrow)
    
    # Arrow to results
    arrow_result = FancyArrow(5, 4.4, 0, -0.7, width=0.05, head_width=0.15, 
                             head_length=0.1, fc='black', ec='black')
    ax.add_patch(arrow_result)
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Schema_Parameter_Analysis.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created: Schema_Parameter_Analysis.png")

def create_site_layout():
    """Create study sites layout diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'Study Sites and Sampling Strategy', 
            fontsize=16, fontweight='bold', ha='center')
    
    # Site descriptions
    sites = {
        'BF-O': {
            'pos': (2, 5.5),
            'color': '#e74c3c',
            'desc': 'Battlefield near Ozera\n• Artillery impact craters\n• 120-152mm munitions\n• Multiple impact points'
        },
        'UXO-SP': {
            'pos': (6, 5.5),
            'color': '#f39c12',
            'desc': 'UXO Destruction Site\nStari Petrivtsi\n• Controlled detonations\n• Open detonation pit'
        },
        'MHS-D': {
            'pos': (10, 5.5),
            'color': '#2ecc71',
            'desc': 'Missile Hit Site\nDemydiv\n• Cruise missile impact\n• Large crater formation'
        }
    }
    
    # Draw site boxes
    for site_name, site_data in sites.items():
        x, y = site_data['pos']
        color = site_data['color']
        desc = site_data['desc']
        
        site_box = FancyBboxPatch((x-1.5, y-1), 3, 2, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor=color, 
                                  edgecolor='black', 
                                  alpha=0.8, linewidth=2)
        ax.add_patch(site_box)
        
        ax.text(x, y+0.5, site_name, fontsize=14, fontweight='bold', ha='center', color='white')
        ax.text(x, y-0.2, desc, fontsize=9, ha='center', color='white', va='center')
    
    # Sampling strategy
    strategy_box = FancyBboxPatch((2, 2), 8, 1.5, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor='#34495e', 
                                  edgecolor='black', 
                                  alpha=0.8, linewidth=2)
    ax.add_patch(strategy_box)
    ax.text(6, 3.1, 'SAMPLING STRATEGY', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(6, 2.7, 'Crater Centers • Distance Transects • Background Locations (>40m)', 
            fontsize=10, ha='center', color='white')
    ax.text(6, 2.4, 'Grid-Based Collection • Surface Soil (0-10 cm) • ~15g per sample', 
            fontsize=10, ha='center', color='white')
    
    # Soil type info
    soil_text = 'Soil Type: Umbric Albeluvisols Abruptic\n(Weakly magnetic, low heavy metal baseline)'
    ax.text(6, 0.8, soil_text, fontsize=11, ha='center', style='italic',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Schema_Site_Layout.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Created: Schema_Site_Layout.png")

def main():
    """Generate all schema images"""
    print("Generating methodological schema images...")
    
    create_main_flowchart()
    create_equipment_network()
    create_parameter_analysis()
    create_site_layout()
    
    print("\nAll schema images have been created successfully!")
    print("Files saved in: /Users/adim/Documents/Igph/SoilDegradation/")
    print("\nGenerated files:")
    print("1. Schema_Main_Flowchart.png - Complete methodological overview")
    print("2. Schema_Equipment_Network.png - Equipment connections and workflow")
    print("3. Schema_Parameter_Analysis.png - Parameter integration framework") 
    print("4. Schema_Site_Layout.png - Study sites and sampling strategy")

if __name__ == "__main__":
    main()
