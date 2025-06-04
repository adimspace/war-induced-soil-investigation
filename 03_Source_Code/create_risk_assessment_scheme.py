#!/usr/bin/env python3
"""
Create a Risk Assessment and Decision Matrix Scheme for war-induced soil contamination
This complements the existing methodological schemes by providing decision-making frameworks
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrow, Polygon
import numpy as np
import seaborn as sns

# Set style for professional appearance
plt.style.use('default')
sns.set_palette("husl")

def create_risk_assessment_scheme():
    """Create comprehensive risk assessment and decision matrix scheme"""
    fig, ax = plt.subplots(1, 1, figsize=(24, 16))
    
    # Professional color palette
    colors = {
        'high_risk': '#c0392b',        # Dark red
        'medium_risk': '#f39c12',      # Orange
        'low_risk': '#27ae60',         # Green
        'assessment': '#2980b9',       # Blue
        'decision': '#8e44ad',         # Purple
        'monitoring': '#16a085',       # Teal
        'remediation': '#e74c3c',      # Red
        'header': '#34495e'            # Dark gray
    }
    
    # Clear axes and set limits
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Title
    title_box = FancyBboxPatch((0.5, 14.5), 23, 1.2, boxstyle="round,pad=0.1", 
                               facecolor=colors['header'], edgecolor='black', linewidth=2)
    ax.add_patch(title_box)
    ax.text(12, 15.1, 'Risk Assessment and Decision Matrix for War-Induced Soil Contamination', 
            fontsize=20, fontweight='bold', ha='center', va='center', color='white')
    
    # Phase 1: Data Input Assessment (Left side)
    input_box = FancyBboxPatch((0.5, 10.5), 7, 3.5, boxstyle="round,pad=0.1", 
                               facecolor=colors['assessment'], edgecolor='black', linewidth=1)
    ax.add_patch(input_box)
    ax.text(4, 13.5, 'DATA INPUT ASSESSMENT', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    # Input parameters
    input_params = [
        '• Magnetic susceptibility enhancement',
        '• Heavy metal concentrations (As, Ba, Cu, Fe, Pb, Zn)',
        '• Spatial distribution patterns',
        '• Background/reference values',
        '• Contamination depth profiles',
        '• Particle morphology data',
        '• Historical conflict activity level'
    ]
    
    for i, param in enumerate(input_params):
        ax.text(1, 13.2 - i*0.3, param, fontsize=10, ha='left', va='center', color='white')
    
    # Phase 2: Risk Matrix (Center)
    matrix_box = FancyBboxPatch((8.5, 5.5), 8, 8.5, boxstyle="round,pad=0.1", 
                                facecolor='white', edgecolor='black', linewidth=2)
    ax.add_patch(matrix_box)
    ax.text(12.5, 13.5, 'CONTAMINATION RISK MATRIX', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='black')
    
    # Create risk matrix grid
    contamination_levels = ['Low\n(<2x background)', 'Moderate\n(2-5x background)', 
                           'High\n(5-10x background)', 'Very High\n(>10x background)']
    exposure_levels = ['Low\nRisk', 'Medium\nRisk', 'High\nRisk', 'Critical\nRisk']
    
    # Matrix cells
    risk_colors = [
        [colors['low_risk'], colors['low_risk'], colors['medium_risk'], colors['medium_risk']],
        [colors['low_risk'], colors['medium_risk'], colors['medium_risk'], colors['high_risk']],
        [colors['medium_risk'], colors['medium_risk'], colors['high_risk'], colors['high_risk']],
        [colors['medium_risk'], colors['high_risk'], colors['high_risk'], colors['high_risk']]
    ]
    
    for i in range(4):
        for j in range(4):
            cell = Rectangle((9 + j*1.8, 9.5 + i*1.0), 1.7, 0.9, 
                           facecolor=risk_colors[i][j], edgecolor='black', linewidth=1)
            ax.add_patch(cell)
    
    # Matrix labels
    ax.text(8.2, 11.5, 'Exposure\nPotential', fontsize=11, fontweight='bold', 
            ha='center', va='center', rotation=90)
    ax.text(12.5, 9, 'Contamination Level', fontsize=11, fontweight='bold', 
            ha='center', va='center')
    
    # Axis labels
    for i, level in enumerate(contamination_levels):
        ax.text(9.85 + i*1.8, 8.5, level, fontsize=9, ha='center', va='center')
    
    for i, level in enumerate(exposure_levels):
        ax.text(8.7, 10 + i*1.0, level, fontsize=9, ha='center', va='center')
    
    # Phase 3: Decision Tree (Right side)
    decision_box = FancyBboxPatch((17.5, 10.5), 6, 3.5, boxstyle="round,pad=0.1", 
                                  facecolor=colors['decision'], edgecolor='black', linewidth=1)
    ax.add_patch(decision_box)
    ax.text(20.5, 13.5, 'DECISION FRAMEWORK', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    decisions = [
        'LOW RISK: Monitoring only',
        'MEDIUM RISK: Enhanced monitoring',
        '                + Risk communication',
        'HIGH RISK: Active remediation',
        '                + Access restrictions',
        'CRITICAL: Immediate intervention',
        '                + Emergency protocols'
    ]
    
    for i, decision in enumerate(decisions):
        ax.text(18, 13.2 - i*0.25, decision, fontsize=10, ha='left', va='center', color='white')
    
    # Phase 4: Monitoring Protocols (Lower left)
    monitor_box = FancyBboxPatch((0.5, 6), 7, 4, boxstyle="round,pad=0.1", 
                                 facecolor=colors['monitoring'], edgecolor='black', linewidth=1)
    ax.add_patch(monitor_box)
    ax.text(4, 9.5, 'MONITORING PROTOCOLS', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    monitor_items = [
        'Frequency Guidelines:',
        '• Low Risk: Annual monitoring',
        '• Medium Risk: Quarterly monitoring',
        '• High Risk: Monthly monitoring',
        '• Critical Risk: Continuous monitoring',
        '',
        'Key Indicators:',
        '• Metal bioavailability',
        '• Groundwater quality',
        '• Vegetation health',
        '• Human exposure pathways'
    ]
    
    for i, item in enumerate(monitor_items):
        style = 'bold' if item.endswith(':') else 'normal'
        ax.text(1, 9.2 - i*0.25, item, fontsize=10, ha='left', va='center', 
                color='white', fontweight=style)
    
    # Phase 5: Remediation Strategies (Lower right)
    remediation_box = FancyBboxPatch((17.5, 6), 6, 4, boxstyle="round,pad=0.1", 
                                     facecolor=colors['remediation'], edgecolor='black', linewidth=1)
    ax.add_patch(remediation_box)
    ax.text(20.5, 9.5, 'REMEDIATION STRATEGIES', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    remediation_items = [
        'Physical Methods:',
        '• Soil excavation/replacement',
        '• Magnetic separation',
        '• Particle size separation',
        '',
        'Chemical Methods:',
        '• Chemical stabilization',
        '• Electrokinetic treatment',
        '',
        'Biological Methods:',
        '• Phytoremediation',
        '• Biostimulation'
    ]
    
    for i, item in enumerate(remediation_items):
        style = 'bold' if item.endswith(':') else 'normal'
        ax.text(18, 9.2 - i*0.25, item, fontsize=10, ha='left', va='center', 
                color='white', fontweight=style)
    
    # Phase 6: Quality Assurance Framework (Bottom)
    qa_box = FancyBboxPatch((0.5, 0.5), 23, 2, boxstyle="round,pad=0.1", 
                            facecolor=colors['header'], edgecolor='black', linewidth=1)
    ax.add_patch(qa_box)
    ax.text(12, 2, 'QUALITY ASSURANCE & VALIDATION FRAMEWORK', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    qa_sections = [
        'Data Quality Checks:\n• Precision: <10% RSD\n• Accuracy: 80-120% recovery\n• Detection limits verification',
        'Statistical Validation:\n• Outlier identification\n• Spatial correlation analysis\n• Uncertainty quantification',
        'Expert Review:\n• Multi-disciplinary assessment\n• Peer validation\n• Stakeholder consultation',
        'Documentation:\n• Traceable procedures\n• Standardized reporting\n• Archival protocols'
    ]
    
    section_width = 5.5
    for i, section in enumerate(qa_sections):
        x_pos = 1 + i * section_width
        ax.text(x_pos, 1.2, section, fontsize=9, ha='left', va='center', color='white')
    
    # Add connecting arrows
    # Input to Matrix
    arrow1 = FancyArrow(7.5, 12.2, 1, 0, width=0.08, head_width=0.15, 
                        head_length=0.1, fc='darkblue', ec='darkblue', alpha=0.7)
    ax.add_patch(arrow1)
    
    # Matrix to Decision
    arrow2 = FancyArrow(16.5, 10, 1, 2, width=0.08, head_width=0.15, 
                        head_length=0.1, fc='darkblue', ec='darkblue', alpha=0.7)
    ax.add_patch(arrow2)
    
    # Decision to Actions
    arrow3 = FancyArrow(19, 10.5, -10.5, -2.5, width=0.06, head_width=0.12, 
                        head_length=0.1, fc='darkblue', ec='darkblue', alpha=0.7)
    ax.add_patch(arrow3)
    
    arrow4 = FancyArrow(21, 10.5, -1.5, -2.5, width=0.06, head_width=0.12, 
                        head_length=0.1, fc='darkblue', ec='darkblue', alpha=0.7)
    ax.add_patch(arrow4)
    
    # Add risk level legend
    legend_box = FancyBboxPatch((9, 6.5), 7, 2.5, boxstyle="round,pad=0.1", 
                                facecolor='lightgray', edgecolor='black', linewidth=1)
    ax.add_patch(legend_box)
    ax.text(12.5, 8.5, 'RISK LEVEL LEGEND', fontsize=12, fontweight='bold', 
            ha='center', va='center')
    
    legend_items = [
        ('Low Risk', colors['low_risk']),
        ('Medium Risk', colors['medium_risk']),
        ('High Risk', colors['high_risk'])
    ]
    
    for i, (label, color) in enumerate(legend_items):
        legend_rect = Rectangle((9.5 + i*2, 7.5), 0.3, 0.3, facecolor=color, 
                               edgecolor='black', linewidth=1)
        ax.add_patch(legend_rect)
        ax.text(10 + i*2, 7.65, label, fontsize=10, ha='left', va='center')
    
    # Add methodology note
    note_box = FancyBboxPatch((0.5, 3), 23, 2, boxstyle="round,pad=0.1", 
                              facecolor='lightyellow', edgecolor='black', linewidth=1)
    ax.add_patch(note_box)
    ax.text(12, 4.5, 'METHODOLOGICAL NOTES', fontsize=12, fontweight='bold', 
            ha='center', va='center')
    
    notes = [
        '• Risk assessment based on multiple contamination indicators (magnetic, chemical, spatial)',
        '• Contamination levels calculated relative to site-specific background values',
        '• Exposure potential considers land use, population density, and environmental sensitivity',
        '• Decision framework adaptable to local regulatory requirements and resource availability',
        '• Integration with existing soil contamination assessment standards (ISO 15799, ASTM E1739)'
    ]
    
    for i, note in enumerate(notes):
        ax.text(1, 4.2 - i*0.25, note, fontsize=10, ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Risk_Assessment_Decision_Matrix_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: Risk_Assessment_Decision_Matrix_Scheme.png")

def create_temporal_monitoring_scheme():
    """Create temporal monitoring and trend analysis scheme"""
    fig, ax = plt.subplots(1, 1, figsize=(20, 14))
    
    colors = {
        'timeline': '#3498db',
        'immediate': '#e74c3c',
        'short_term': '#f39c12',
        'long_term': '#27ae60',
        'indicator': '#9b59b6',
        'header': '#34495e'
    }
    
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Title
    title_box = FancyBboxPatch((0.5, 12.5), 19, 1.2, boxstyle="round,pad=0.1", 
                               facecolor=colors['header'], edgecolor='black', linewidth=2)
    ax.add_patch(title_box)
    ax.text(10, 13.1, 'Temporal Monitoring Framework for War-Induced Soil Contamination', 
            fontsize=18, fontweight='bold', ha='center', va='center', color='white')
    
    # Timeline axis
    timeline_y = 8
    timeline_arrow = FancyArrow(1, timeline_y, 17, 0, width=0.1, head_width=0.2, 
                                head_length=0.3, fc=colors['timeline'], ec=colors['timeline'])
    ax.add_patch(timeline_arrow)
    ax.text(19.5, timeline_y, 'Time', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Time phases
    phases = [
        ('Immediate\n(0-6 months)', 3, colors['immediate']),
        ('Short-term\n(6 months-2 years)', 8, colors['short_term']),
        ('Long-term\n(2-10 years)', 15, colors['long_term'])
    ]
    
    for phase_name, x_pos, color in phases:
        # Vertical line
        phase_line = plt.Line2D([x_pos, x_pos], [7.5, 8.5], color=color, linewidth=3)
        ax.add_line(phase_line)
        
        # Phase label
        phase_box = FancyBboxPatch((x_pos-1, 9), 2, 1, boxstyle="round,pad=0.1", 
                                   facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(phase_box)
        ax.text(x_pos, 9.5, phase_name, fontsize=10, fontweight='bold', 
                ha='center', va='center', color='white')
    
    # Monitoring activities for each phase
    immediate_activities = [
        'Initial Site Assessment',
        '• Rapid contamination screening',
        '• Safety hazard identification', 
        '• Emergency response protocols',
        '• Baseline data collection',
        '',
        'Monitoring Frequency: Weekly',
        'Key Parameters:',
        '• Surface contamination levels',
        '• Acute exposure risks',
        '• Weather-related dispersion'
    ]
    
    short_term_activities = [
        'Detailed Investigation',
        '• Comprehensive sampling',
        '• Source characterization',
        '• Exposure pathway analysis',
        '• Risk assessment refinement',
        '',
        'Monitoring Frequency: Monthly',
        'Key Parameters:',
        '• Contamination migration',
        '• Seasonal variations',
        '• Remediation effectiveness'
    ]
    
    long_term_activities = [
        'Long-term Monitoring',
        '• Trend analysis',
        '• Natural attenuation assessment',
        '• Ecosystem recovery monitoring',
        '• Human health surveillance',
        '',
        'Monitoring Frequency: Quarterly/Annual',
        'Key Parameters:',
        '• Long-term stability',
        '• Bioaccumulation trends',
        '• Remediation sustainability'
    ]
    
    activities_list = [immediate_activities, short_term_activities, long_term_activities]
    x_positions = [3, 8, 15]
    phase_colors = [colors['immediate'], colors['short_term'], colors['long_term']]
    
    for activities, x_pos, color in zip(activities_list, x_positions, phase_colors):
        activity_box = FancyBboxPatch((x_pos-1.5, 3), 3, 4, boxstyle="round,pad=0.1", 
                                      facecolor=color, edgecolor='black', linewidth=1, alpha=0.8)
        ax.add_patch(activity_box)
        
        for i, activity in enumerate(activities):
            style = 'bold' if not activity.startswith('•') and activity != '' else 'normal'
            ax.text(x_pos-1.4, 6.7 - i*0.3, activity, fontsize=9, ha='left', va='center', 
                    color='white', fontweight=style)
    
    # Monitoring indicators matrix
    indicator_box = FancyBboxPatch((1, 0.5), 18, 2, boxstyle="round,pad=0.1", 
                                   facecolor=colors['indicator'], edgecolor='black', linewidth=1)
    ax.add_patch(indicator_box)
    ax.text(10, 2, 'KEY MONITORING INDICATORS & THRESHOLD VALUES', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    indicators = [
        'Magnetic Susceptibility:\n• Background: <50×10⁻⁸ m³/kg\n• Elevated: >100×10⁻⁸ m³/kg',
        'Heavy Metals (mg/kg):\n• As: >20, Ba: >300\n• Cu: >100, Pb: >300, Zn: >300',
        'Spatial Extent:\n• Impact radius assessment\n• Migration distance tracking',
        'Environmental Impact:\n• Vegetation stress indicators\n• Soil biological activity'
    ]
    
    for i, indicator in enumerate(indicators):
        x_pos = 2 + i * 4.5
        ax.text(x_pos, 1.2, indicator, fontsize=9, ha='left', va='center', color='white')
    
    # Add arrows connecting phases
    for i in range(len(x_positions)-1):
        arrow = FancyArrow(x_positions[i]+1.5, 5, x_positions[i+1]-x_positions[i]-3, 0, 
                          width=0.05, head_width=0.1, head_length=0.2, 
                          fc='darkgray', ec='darkgray', alpha=0.6)
        ax.add_patch(arrow)
    
    # Decision points
    decision_y = 11
    for i, (phase_name, x_pos, color) in enumerate(phases[:-1]):
        decision_diamond = Polygon([(x_pos+2.5, decision_y), (x_pos+3, decision_y+0.3), 
                                   (x_pos+3.5, decision_y), (x_pos+3, decision_y-0.3)], 
                                  facecolor='yellow', edgecolor='black', linewidth=1)
        ax.add_patch(decision_diamond)
        ax.text(x_pos+3, decision_y, 'Decision\nPoint', fontsize=8, ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Temporal_Monitoring_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: Temporal_Monitoring_Scheme.png")

def main():
    """Generate risk assessment and temporal monitoring schemes"""
    print("Generating Risk Assessment and Decision Matrix Schemes...")
    create_risk_assessment_scheme()
    create_temporal_monitoring_scheme()
    print("\nRisk assessment schemes generation completed!")
    print("\nFiles created:")
    print("1. Risk_Assessment_Decision_Matrix_Scheme.png - Comprehensive risk assessment framework")
    print("2. Temporal_Monitoring_Scheme.png - Time-based monitoring protocols")

if __name__ == "__main__":
    main()
