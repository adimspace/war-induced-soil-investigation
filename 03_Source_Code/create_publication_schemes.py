#!/usr/bin/env python3
"""
Create a Multi-Scale Integration Scheme for war-induced soil contamination research
This shows how to integrate findings across different spatial and temporal scales
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrow, Polygon, Ellipse
import numpy as np
import seaborn as sns

# Set style for professional appearance
plt.style.use('default')
sns.set_palette("husl")

def create_multiscale_integration_scheme():
    """Create comprehensive multi-scale integration methodological scheme"""
    fig, ax = plt.subplots(1, 1, figsize=(22, 16))
    
    # Professional color palette
    colors = {
        'micro': '#e74c3c',           # Red - microscale
        'local': '#f39c12',           # Orange - local scale
        'regional': '#3498db',        # Blue - regional scale
        'global': '#27ae60',          # Green - global scale
        'integration': '#9b59b6',     # Purple - integration
        'methods': '#34495e',         # Dark gray - methods
        'temporal': '#e67e22',        # Dark orange - temporal
        'header': '#2c3e50'           # Very dark blue-gray
    }
    
    # Clear axes and set limits
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Title
    title_box = FancyBboxPatch((0.5, 14.5), 21, 1.2, boxstyle="round,pad=0.1", 
                               facecolor=colors['header'], edgecolor='black', linewidth=2)
    ax.add_patch(title_box)
    ax.text(11, 15.1, 'Multi-Scale Integration Framework for War-Induced Soil Contamination Research', 
            fontsize=18, fontweight='bold', ha='center', va='center', color='white')
    
    # Spatial scales (left side - vertical hierarchy)
    scales = [
        ('Microscale\n(μm-mm)', 2, 12, colors['micro'], [
            '• Individual particles', '• Mineral surfaces', '• Pore structure',
            '• Micro-aggregates', '• Crystal defects'
        ]),
        ('Local Scale\n(m-km)', 2, 9.5, colors['local'], [
            '• Crater sites', '• Sampling plots', '• Transect studies',
            '• Single battlefields', '• Site characterization'
        ]),
        ('Regional Scale\n(km-100km)', 2, 7, colors['regional'], [
            '• Multiple conflict zones', '• Watershed analysis', '• Administrative units',
            '• Ecosystem boundaries', '• Population centers'
        ]),
        ('Global Scale\n(>100km)', 2, 4.5, colors['global'], [
            '• International comparisons', '• Global databases', '• Climate effects',
            '• Transboundary impacts', '• Policy frameworks'
        ])
    ]
    
    for scale_name, x, y, color, characteristics in scales:
        # Scale box
        scale_box = FancyBboxPatch((x-1, y-1), 4, 2, boxstyle="round,pad=0.1", 
                                   facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(scale_box)
        ax.text(x+1, y, scale_name, fontsize=12, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # Characteristics
        char_box = FancyBboxPatch((x+4.5, y-1), 4, 2, boxstyle="round,pad=0.1", 
                                  facecolor=color, edgecolor='black', linewidth=1, alpha=0.7)
        ax.add_patch(char_box)
        for i, char in enumerate(characteristics):
            ax.text(x+4.7, y+0.6-i*0.25, char, fontsize=9, ha='left', va='center', color='white')
    
    # Methodological approaches (center)
    methods_box = FancyBboxPatch((10, 2), 6, 11, boxstyle="round,pad=0.1", 
                                 facecolor=colors['methods'], edgecolor='black', linewidth=2)
    ax.add_patch(methods_box)
    ax.text(13, 12.5, 'INTEGRATION METHODS', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    # Method sections
    method_sections = [
        ('Analytical Techniques:', [
            '• SEM-EDS (microscale)',
            '• XRD, FTIR (mineral scale)', 
            '• ICP-MS (elemental scale)',
            '• Magnetometry (field scale)',
            '• Remote sensing (regional scale)'
        ]),
        ('Statistical Methods:', [
            '• Hierarchical modeling',
            '• Multi-level analysis',
            '• Spatial autocorrelation',
            '• Scale-dependent variograms',
            '• Cross-scale correlation'
        ]),
        ('Data Integration:', [
            '• Multi-resolution datasets',
            '• Scale-appropriate sampling',
            '• Upscaling/downscaling',
            '• Uncertainty propagation',
            '• Model validation'
        ]),
        ('Validation Approaches:', [
            '• Cross-scale validation',
            '• Independent datasets',
            '• Expert knowledge',
            '• Historical records',
            '• Comparative studies'
        ])
    ]
    
    y_start = 11.8
    for section_title, items in method_sections:
        ax.text(10.3, y_start, section_title, fontsize=11, fontweight='bold', 
                ha='left', va='center', color='white')
        y_start -= 0.3
        for item in items:
            ax.text(10.5, y_start, item, fontsize=9, ha='left', va='center', color='white')
            y_start -= 0.22
        y_start -= 0.2
    
    # Temporal integration (right side)
    temporal_box = FancyBboxPatch((17, 8), 4.5, 5, boxstyle="round,pad=0.1", 
                                  facecolor=colors['temporal'], edgecolor='black', linewidth=1)
    ax.add_patch(temporal_box)
    ax.text(19.25, 12.5, 'TEMPORAL INTEGRATION', fontsize=12, fontweight='bold', 
            ha='center', va='center', color='white')
    
    temporal_items = [
        'Time Scales:',
        '• Immediate (hours-days)',
        '• Short-term (weeks-months)', 
        '• Medium-term (years)',
        '• Long-term (decades)',
        '',
        'Integration Aspects:',
        '• Process rates at different scales',
        '• Temporal data harmonization',
        '• Trend analysis across scales',
        '• Prediction model coupling',
        '• Legacy effect assessment'
    ]
    
    y_pos = 12.2
    for item in temporal_items:
        style = 'bold' if item.endswith(':') else 'normal'
        ax.text(17.2, y_pos, item, fontsize=9, ha='left', va='center', 
                color='white', fontweight=style)
        y_pos -= 0.25
    
    # Output products (right side bottom)
    output_box = FancyBboxPatch((17, 2), 4.5, 5.5, boxstyle="round,pad=0.1", 
                                facecolor=colors['integration'], edgecolor='black', linewidth=1)
    ax.add_patch(output_box)
    ax.text(19.25, 7, 'INTEGRATION OUTPUTS', fontsize=12, fontweight='bold', 
            ha='center', va='center', color='white')
    
    output_items = [
        'Scientific Products:',
        '• Scale-dependent models',
        '• Process understanding',
        '• Mechanistic insights',
        '• Predictive frameworks',
        '',
        'Applied Products:',
        '• Risk assessment tools',
        '• Management guidelines',
        '• Policy recommendations',
        '• Best practice protocols',
        '',
        'Database Products:',
        '• Multi-scale databases',
        '• Standardized protocols',
        '• Comparative datasets',
        '• Reference materials'
    ]
    
    y_pos = 6.7
    for item in output_items:
        style = 'bold' if item.endswith(':') else 'normal'
        ax.text(17.2, y_pos, item, fontsize=9, ha='left', va='center', 
                color='white', fontweight=style)
        y_pos -= 0.22
    
    # Add connecting arrows between scales
    for i in range(len(scales)-1):
        y1 = scales[i][2] - 1
        y2 = scales[i+1][2] + 1
        arrow = FancyArrow(2, y1, 0, y2-y1, width=0.05, head_width=0.15, 
                          head_length=0.1, fc='darkblue', ec='darkblue', alpha=0.6)
        ax.add_patch(arrow)
        # Bidirectional arrow
        arrow_up = FancyArrow(2.5, y2, 0, y1-y2, width=0.05, head_width=0.15, 
                             head_length=0.1, fc='darkblue', ec='darkblue', alpha=0.6)
        ax.add_patch(arrow_up)
    
    # Arrows from scales to methods
    for _, x, y, color, _ in scales:
        arrow = FancyArrow(x+8.5, y, 1, 0.5, width=0.04, head_width=0.1, 
                          head_length=0.08, fc=color, ec=color, alpha=0.7)
        ax.add_patch(arrow)
    
    # Arrows from methods to outputs
    arrow_to_temporal = FancyArrow(16, 11, 1, -0.5, width=0.05, head_width=0.12, 
                                  head_length=0.1, fc=colors['methods'], ec=colors['methods'], alpha=0.7)
    ax.add_patch(arrow_to_temporal)
    
    arrow_to_output = FancyArrow(16, 6, 1, -1, width=0.05, head_width=0.12, 
                                head_length=0.1, fc=colors['methods'], ec=colors['methods'], alpha=0.7)
    ax.add_patch(arrow_to_output)
    
    # Quality assurance framework (bottom)
    qa_box = FancyBboxPatch((0.5, 0.2), 21, 1.5, boxstyle="round,pad=0.1", 
                            facecolor='lightgray', edgecolor='black', linewidth=1)
    ax.add_patch(qa_box)
    ax.text(11, 1.3, 'QUALITY ASSURANCE FOR MULTI-SCALE INTEGRATION', fontsize=12, fontweight='bold', 
            ha='center', va='center')
    
    qa_items = [
        'Scale Consistency: Ensure data compatibility across scales through standardized units and reference frames',
        'Uncertainty Management: Propagate and quantify uncertainties from fine to coarse scales',
        'Validation Protocols: Cross-validate results using independent datasets and expert knowledge',
        'Documentation Standards: Maintain comprehensive metadata for scale-dependent processes and assumptions'
    ]
    
    for i, item in enumerate(qa_items):
        ax.text(1, 1.1 - i*0.15, f"• {item}", fontsize=9, ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Multiscale_Integration_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: Multiscale_Integration_Scheme.png")

def create_publication_framework_scheme():
    """Create a scheme specifically for scientific publication methodological sections"""
    fig, ax = plt.subplots(1, 1, figsize=(20, 14))
    
    colors = {
        'section1': '#3498db',        # Blue
        'section2': '#e74c3c',        # Red  
        'section3': '#f39c12',        # Orange
        'section4': '#27ae60',        # Green
        'section5': '#9b59b6',        # Purple
        'header': '#2c3e50',          # Dark blue-gray
        'quality': '#95a5a6'          # Gray
    }
    
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Title
    title_box = FancyBboxPatch((0.5, 12.5), 19, 1.2, boxstyle="round,pad=0.1", 
                               facecolor=colors['header'], edgecolor='black', linewidth=2)
    ax.add_patch(title_box)
    ax.text(10, 13.1, 'Scientific Publication Framework for War-Induced Soil Contamination Studies', 
            fontsize=16, fontweight='bold', ha='center', va='center', color='white')
    
    # Methodology sections for publications
    sections = [
        ('Study Area & Site Selection', 0.5, 8.5, 3.8, 3, colors['section1'], [
            'Geographic Context:',
            '• Coordinates and elevation',
            '• Geological setting',
            '• Climate and hydrology',
            '• Land use history',
            '',
            'Conflict History:',
            '• Timeline of activities',
            '• Munition types used',
            '• Impact assessment',
            '• Safety considerations'
        ]),
        
        ('Field Methods & Sampling', 4.5, 8.5, 3.8, 3, colors['section2'], [
            'Geophysical Survey:',
            '• Equipment specifications',
            '• Survey parameters',
            '• Grid design',
            '• Data acquisition',
            '',
            'Soil Sampling:',
            '• Sampling design',
            '• Collection protocols',
            '• Sample preservation',
            '• Chain of custody'
        ]),
        
        ('Laboratory Analysis', 8.5, 8.5, 3.8, 3, colors['section3'], [
            'Sample Preparation:',
            '• Drying and sieving',
            '• Homogenization',
            '• Subsampling',
            '• Storage conditions',
            '',
            'Analytical Methods:',
            '• Equipment details',
            '• Operating conditions',
            '• Calibration procedures',
            '• QA/QC protocols'
        ]),
        
        ('Data Analysis', 12.5, 8.5, 3.8, 3, colors['section4'], [
            'Statistical Analysis:',
            '• Descriptive statistics',
            '• Correlation analysis',
            '• Spatial analysis',
            '• Significance testing',
            '',
            'Software & Tools:',
            '• Statistical packages',
            '• GIS software',
            '• Specialized programs',
            '• Version information'
        ]),
        
        ('Quality Control', 16.5, 8.5, 3, 3, colors['section5'], [
            'Analytical QC:',
            '• Reference materials',
            '• Duplicate analyses',
            '• Blank samples',
            '• Recovery tests',
            '',
            'Data QC:',
            '• Outlier detection',
            '• Validation checks',
            '• Uncertainty analysis',
            '• Error propagation'
        ])
    ]
    
    for title, x, y, width, height, color, content in sections:
        # Section box
        section_box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                     facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(section_box)
        
        # Title
        ax.text(x + width/2, y + height - 0.2, title, fontsize=11, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # Content
        y_pos = y + height - 0.6
        for item in content:
            style = 'bold' if item.endswith(':') and item != '' else 'normal'
            if item == '':
                y_pos -= 0.1
            else:
                ax.text(x + 0.1, y_pos, item, fontsize=9, ha='left', va='center', 
                        color='white', fontweight=style)
                y_pos -= 0.2
    
    # Results presentation framework
    results_box = FancyBboxPatch((0.5, 4.5), 19, 3.5, boxstyle="round,pad=0.1", 
                                 facecolor='lightblue', edgecolor='black', linewidth=1)
    ax.add_patch(results_box)
    ax.text(10, 7.7, 'RESULTS PRESENTATION FRAMEWORK', fontsize=14, fontweight='bold', 
            ha='center', va='center')
    
    # Results subsections
    results_sections = [
        ('Descriptive Statistics\n& Data Overview', 2, 6.8, [
            '• Sample distribution maps',
            '• Summary statistics tables', 
            '• Data range and variability',
            '• Detection frequency'
        ]),
        ('Spatial Distribution\nAnalysis', 6.5, 6.8, [
            '• Contamination maps',
            '• Spatial correlation plots',
            '• Distance-decay relationships',
            '• Hotspot identification'
        ]),
        ('Source Identification\n& Characterization', 11, 6.8, [
            '• Principal component analysis',
            '• Factor analysis results',
            '• Source apportionment',
            '• Particle characterization'
        ]),
        ('Risk Assessment\n& Implications', 15.5, 6.8, [
            '• Contamination indices',
            '• Risk level mapping',
            '• Exposure assessment',
            '• Management recommendations'
        ])
    ]
    
    for title, x, y, items in results_sections:
        # Subsection title
        ax.text(x, y, title, fontsize=10, fontweight='bold', ha='center', va='center')
        
        # Items
        for i, item in enumerate(items):
            ax.text(x-1.5, y-0.5-i*0.2, item, fontsize=9, ha='left', va='center')
    
    # Discussion framework
    discussion_box = FancyBboxPatch((0.5, 1), 19, 3, boxstyle="round,pad=0.1", 
                                    facecolor='lightgreen', edgecolor='black', linewidth=1)
    ax.add_patch(discussion_box)
    ax.text(10, 3.7, 'DISCUSSION FRAMEWORK', fontsize=14, fontweight='bold', 
            ha='center', va='center')
    
    discussion_items = [
        'Contamination Patterns: Interpretation of spatial and temporal patterns in relation to conflict activities',
        'Source Attribution: Discussion of contamination sources and their relative contributions', 
        'Environmental Implications: Assessment of environmental impact and ecosystem effects',
        'Methodological Evaluation: Critical assessment of methods, limitations, and uncertainties',
        'Comparison with Literature: Comparison with similar studies and international standards',
        'Management Implications: Recommendations for remediation, monitoring, and risk management',
        'Future Research: Identification of knowledge gaps and research priorities'
    ]
    
    for i, item in enumerate(discussion_items):
        ax.text(1, 3.5 - i*0.3, f"• {item}", fontsize=9, ha='left', va='center')
    
    # Add connecting arrows
    for i in range(len(sections)-1):
        x1 = sections[i][1] + sections[i][3]
        x2 = sections[i+1][1]
        y_arrow = sections[i][2] + sections[i][4]/2
        arrow = FancyArrow(x1, y_arrow, x2-x1, 0, width=0.05, head_width=0.12, 
                          head_length=0.08, fc='darkblue', ec='darkblue', alpha=0.6)
        ax.add_patch(arrow)
    
    # Arrow from methods to results
    arrow_to_results = FancyArrow(10, 8.5, 0, -0.5, width=0.08, head_width=0.15, 
                                 head_length=0.1, fc='darkgreen', ec='darkgreen', alpha=0.7)
    ax.add_patch(arrow_to_results)
    
    # Arrow from results to discussion
    arrow_to_discussion = FancyArrow(10, 4.5, 0, -0.5, width=0.08, head_width=0.15, 
                                    head_length=0.1, fc='darkgreen', ec='darkgreen', alpha=0.7)
    ax.add_patch(arrow_to_discussion)
    
    # Publication standards note
    standards_box = FancyBboxPatch((0.5, 0.1), 19, 0.7, boxstyle="round,pad=0.05", 
                                   facecolor='lightyellow', edgecolor='black', linewidth=1)
    ax.add_patch(standards_box)
    ax.text(10, 0.45, 'Publication Standards: Follow journal-specific guidelines, ensure reproducibility through detailed methodology, '
                     'provide supplementary data, and maintain ethical standards for conflict zone research', 
            fontsize=9, ha='center', va='center', style='italic')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Publication_Framework_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: Publication_Framework_Scheme.png")

def main():
    """Generate multi-scale integration and publication framework schemes"""
    print("Generating Multi-Scale Integration and Publication Framework Schemes...")
    create_multiscale_integration_scheme()
    create_publication_framework_scheme()
    print("\nScheme generation completed!")
    print("\nFiles created:")
    print("1. Multiscale_Integration_Scheme.png - Multi-scale research integration framework")
    print("2. Publication_Framework_Scheme.png - Scientific publication methodology framework")

if __name__ == "__main__":
    main()
