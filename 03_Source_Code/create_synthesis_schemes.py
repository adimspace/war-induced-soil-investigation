#!/usr/bin/env python3
"""
Create data synthesis schemes for war-induced soil contamination investigations
These schemes show how to integrate data from all phases of the General_War_Induced_Soil_Investigation_Scheme
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrow, Polygon, Ellipse
import numpy as np
import seaborn as sns

# Set style for professional appearance
plt.style.use('default')
sns.set_palette("husl")

def create_data_synthesis_framework():
    """Create comprehensive data synthesis framework for war-induced soil investigations"""
    fig, ax = plt.subplots(1, 1, figsize=(24, 18))
    
    # Professional color palette
    colors = {
        'input_data': '#3498db',         # Blue - input data
        'processing': '#e74c3c',         # Red - processing
        'integration': '#f39c12',        # Orange - integration
        'analysis': '#27ae60',           # Green - analysis
        'synthesis': '#9b59b6',          # Purple - synthesis
        'outputs': '#1abc9c',            # Teal - outputs
        'validation': '#e67e22',         # Dark orange - validation
        'header': '#2c3e50'              # Dark blue-gray
    }
    
    # Clear axes and set limits
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 18)
    ax.axis('off')
    
    # Title
    title_box = FancyBboxPatch((0.5, 16.5), 23, 1.2, boxstyle="round,pad=0.1", 
                               facecolor=colors['header'], edgecolor='black', linewidth=2)
    ax.add_patch(title_box)
    ax.text(12, 17.1, 'Data Synthesis Framework for War-Induced Soil Contamination Investigations', 
            fontsize=18, fontweight='bold', ha='center', va='center', color='white')
    
    # Phase 1: Data Collection and Input (Top row)
    data_sources = [
        ('Geophysical Data', 1, 14, 3.5, 1.8, colors['input_data'], [
            '• Magnetic susceptibility maps',
            '• GPR subsurface profiles', 
            '• ERT resistivity models',
            '• Spatial coordinates (GPS)',
            '• Anomaly identification'
        ]),
        ('Geochemical Data', 5, 14, 3.5, 1.8, colors['input_data'], [
            '• Heavy metal concentrations',
            '• Major element composition',
            '• Trace element profiles',
            '• pH and conductivity',
            '• Quality control metrics'
        ]),
        ('Physical Data', 9, 14, 3.5, 1.8, colors['input_data'], [
            '• Particle size distribution',
            '• Bulk density measurements',
            '• Moisture content',
            '• Soil texture analysis',
            '• Structural parameters'
        ]),
        ('Microscopic Data', 13, 14, 3.5, 1.8, colors['input_data'], [
            '• SEM-EDS element maps',
            '• Particle morphology',
            '• Mineral identification',
            '• Surface textures',
            '• Compositional analysis'
        ]),
        ('Contextual Data', 17, 14, 3.5, 1.8, colors['input_data'], [
            '• Conflict history timeline',
            '• Munition type records',
            '• Weather conditions',
            '• Land use information',
            '• Sampling metadata'
        ])
    ]
    
    for title, x, y, width, height, color, content in data_sources:
        # Data source box
        source_box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                    facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(source_box)
        
        # Title
        ax.text(x + width/2, y + height - 0.2, title, fontsize=11, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # Content
        y_pos = y + height - 0.5
        for item in content:
            ax.text(x + 0.1, y_pos, item, fontsize=9, ha='left', va='center', color='white')
            y_pos -= 0.25
    
    # Phase 2: Data Processing and Standardization (Second row)
    processing_box = FancyBboxPatch((1, 11.5), 20, 2, boxstyle="round,pad=0.1", 
                                    facecolor=colors['processing'], edgecolor='black', linewidth=1)
    ax.add_patch(processing_box)
    ax.text(11, 13, 'DATA PROCESSING AND STANDARDIZATION', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    processing_steps = [
        'Quality Control:\n• Outlier detection\n• Missing data handling\n• Instrument drift correction',
        'Normalization:\n• Unit standardization\n• Background subtraction\n• Reference scaling',
        'Spatial Registration:\n• Coordinate alignment\n• Grid interpolation\n• Projection correction',
        'Temporal Alignment:\n• Time series organization\n• Sampling date correction\n• Sequence validation',
        'Data Validation:\n• Cross-method verification\n• Replicate analysis\n• Standard reference checks'
    ]
    
    for i, step in enumerate(processing_steps):
        x_pos = 2 + i * 4
        ax.text(x_pos, 12.2, step, fontsize=9, ha='left', va='center', color='white')
    
    # Phase 3: Multi-Parameter Integration (Third row)
    integration_box = FancyBboxPatch((1, 8.5), 20, 2.5, boxstyle="round,pad=0.1", 
                                     facecolor=colors['integration'], edgecolor='black', linewidth=1)
    ax.add_patch(integration_box)
    ax.text(11, 10.5, 'MULTI-PARAMETER INTEGRATION', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    # Integration methods
    integration_methods = [
        ('Statistical Integration', 2, 9.8, [
            '• Correlation analysis',
            '• Principal Component Analysis',
            '• Factor analysis',
            '• Cluster analysis',
            '• Multivariate statistics'
        ]),
        ('Spatial Integration', 6.5, 9.8, [
            '• GIS overlay analysis',
            '• Spatial correlation',
            '• Kriging interpolation',
            '• Buffer zone analysis',
            '• Distance modeling'
        ]),
        ('Geochemical Integration', 11, 9.8, [
            '• Element association analysis',
            '• Enrichment factor calculation',
            '• Source apportionment',
            '• Contamination indices',
            '• Pollution load assessment'
        ]),
        ('Physical Integration', 15.5, 9.8, [
            '• Texture-chemistry relationships',
            '• Particle size effects',
            '• Density correlations',
            '• Porosity influences',
            '• Transport mechanisms'
        ])
    ]
    
    for method_name, x, y, items in integration_methods:
        ax.text(x, y, method_name, fontsize=10, fontweight='bold', ha='left', va='center', color='white')
        for i, item in enumerate(items):
            ax.text(x, y - 0.3 - i*0.2, item, fontsize=8, ha='left', va='center', color='white')
    
    # Phase 4: Advanced Analysis and Modeling (Fourth row)
    analysis_box = FancyBboxPatch((1, 5.5), 20, 2.5, boxstyle="round,pad=0.1", 
                                  facecolor=colors['analysis'], edgecolor='black', linewidth=1)
    ax.add_patch(analysis_box)
    ax.text(11, 7.5, 'ADVANCED ANALYSIS AND MODELING', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    # Analysis categories
    analysis_categories = [
        ('Source Identification', 2, 6.8, [
            '• Fingerprinting analysis',
            '• Isotopic signatures',
            '• Mineral assemblages',
            '• Chemical ratios',
            '• Particle morphology'
        ]),
        ('Transport Modeling', 6.5, 6.8, [
            '• Dispersion patterns',
            '• Migration pathways',
            '• Deposition models',
            '• Weathering processes',
            '• Temporal evolution'
        ]),
        ('Risk Assessment', 11, 6.8, [
            '• Exposure modeling',
            '• Toxicity evaluation',
            '• Bioavailability assessment',
            '• Pathway analysis',
            '• Uncertainty quantification'
        ]),
        ('Predictive Modeling', 15.5, 6.8, [
            '• Machine learning models',
            '• Regression analysis',
            '• Time series forecasting',
            '• Scenario modeling',
            '• Validation protocols'
        ])
    ]
    
    for category_name, x, y, items in analysis_categories:
        ax.text(x, y, category_name, fontsize=10, fontweight='bold', ha='left', va='center', color='white')
        for i, item in enumerate(items):
            ax.text(x, y - 0.3 - i*0.2, item, fontsize=8, ha='left', va='center', color='white')
    
    # Phase 5: Synthesis and Interpretation (Fifth row)
    synthesis_box = FancyBboxPatch((1, 2.5), 20, 2.5, boxstyle="round,pad=0.1", 
                                   facecolor=colors['synthesis'], edgecolor='black', linewidth=1)
    ax.add_patch(synthesis_box)
    ax.text(11, 4.5, 'DATA SYNTHESIS AND INTERPRETATION', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    # Synthesis components
    synthesis_components = [
        ('Conceptual Model', 2, 3.8, [
            '• Process understanding',
            '• Contamination mechanisms',
            '• Environmental controls',
            '• Spatial relationships',
            '• Temporal dynamics'
        ]),
        ('Pattern Recognition', 6.5, 3.8, [
            '• Contamination zones',
            '• Impact gradients',
            '• Anomaly clusters',
            '• Background variations',
            '• Systematic trends'
        ]),
        ('Causal Relationships', 11, 3.8, [
            '• Source-impact linkages',
            '• Dose-response relationships',
            '• Environmental controls',
            '• Temporal correlations',
            '• Mechanistic insights'
        ]),
        ('Uncertainty Assessment', 15.5, 3.8, [
            '• Data quality evaluation',
            '• Model uncertainties',
            '• Spatial variability',
            '• Measurement precision',
            '• Confidence intervals'
        ])
    ]
    
    for component_name, x, y, items in synthesis_components:
        ax.text(x, y, component_name, fontsize=10, fontweight='bold', ha='left', va='center', color='white')
        for i, item in enumerate(items):
            ax.text(x, y - 0.3 - i*0.2, item, fontsize=8, ha='left', va='center', color='white')
    
    # Phase 6: Output Products and Validation (Bottom row)
    output_validation_box = FancyBboxPatch((1, 0.2), 20, 2, boxstyle="round,pad=0.1", 
                                           facecolor=colors['outputs'], edgecolor='black', linewidth=1)
    ax.add_patch(output_validation_box)
    ax.text(11, 1.7, 'OUTPUT PRODUCTS AND VALIDATION', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    outputs = [
        'Scientific Products:\n• Contamination maps\n• Risk assessment reports\n• Peer-reviewed publications',
        'Management Tools:\n• Decision support systems\n• Remediation plans\n• Monitoring protocols',
        'Policy Products:\n• Regulatory guidelines\n• Best practice manuals\n• Standard protocols',
        'Database Products:\n• Integrated datasets\n• Metadata catalogs\n• Reference materials',
        'Validation Results:\n• Cross-validation metrics\n• Uncertainty bounds\n• Quality indicators'
    ]
    
    for i, output in enumerate(outputs):
        x_pos = 2 + i * 4
        ax.text(x_pos, 1, output, fontsize=9, ha='left', va='center', color='white')
    
    # Add connecting arrows between phases
    # Data sources to processing
    for i in range(5):
        x_source = 2.75 + i * 4
        arrow1 = FancyArrow(x_source, 14, 0, -0.5, width=0.05, head_width=0.1, 
                           head_length=0.08, fc='darkblue', ec='darkblue', alpha=0.7)
        ax.add_patch(arrow1)
    
    # Processing to integration
    arrow2 = FancyArrow(11, 11.5, 0, -0.5, width=0.08, head_width=0.15, 
                        head_length=0.1, fc='darkred', ec='darkred', alpha=0.7)
    ax.add_patch(arrow2)
    
    # Integration to analysis
    arrow3 = FancyArrow(11, 8.5, 0, -0.5, width=0.08, head_width=0.15, 
                        head_length=0.1, fc='darkorange', ec='darkorange', alpha=0.7)
    ax.add_patch(arrow3)
    
    # Analysis to synthesis
    arrow4 = FancyArrow(11, 5.5, 0, -0.5, width=0.08, head_width=0.15, 
                        head_length=0.1, fc='darkgreen', ec='darkgreen', alpha=0.7)
    ax.add_patch(arrow4)
    
    # Synthesis to outputs
    arrow5 = FancyArrow(11, 2.5, 0, -0.3, width=0.08, head_width=0.15, 
                        head_length=0.1, fc='purple', ec='purple', alpha=0.7)
    ax.add_patch(arrow5)
    
    # Add feedback loops
    feedback_arrow1 = FancyArrow(21.5, 1.2, 2, 12, width=0.04, head_width=0.1, 
                                head_length=0.1, fc='gray', ec='gray', alpha=0.5, 
                                linestyle='--')
    ax.add_patch(feedback_arrow1)
    ax.text(22.5, 8, 'Feedback\nLoop', fontsize=10, ha='center', va='center', 
            rotation=80, style='italic', color='gray')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Data_Synthesis_Framework_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: Data_Synthesis_Framework_Scheme.png")

def create_integration_workflow_scheme():
    """Create detailed integration workflow for multi-source data"""
    fig, ax = plt.subplots(1, 1, figsize=(22, 16))
    
    colors = {
        'magnetic': '#e74c3c',           # Red
        'chemical': '#3498db',           # Blue
        'physical': '#f39c12',           # Orange
        'spatial': '#27ae60',            # Green
        'integration': '#9b59b6',        # Purple
        'validation': '#1abc9c',         # Teal
        'header': '#2c3e50'              # Dark blue-gray
    }
    
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Title
    title_box = FancyBboxPatch((0.5, 14.5), 21, 1.2, boxstyle="round,pad=0.1", 
                               facecolor=colors['header'], edgecolor='black', linewidth=2)
    ax.add_patch(title_box)
    ax.text(11, 15.1, 'Multi-Source Data Integration Workflow for War-Induced Soil Contamination', 
            fontsize=17, fontweight='bold', ha='center', va='center', color='white')
    
    # Data streams (left side)
    data_streams = [
        ('Magnetic Data Stream', 1, 11, 4, 2.5, colors['magnetic'], [
            'Raw Data:',
            '• Magnetic susceptibility (χ)',
            '• Frequency-dependent susceptibility',
            '• Magnetic anomaly maps',
            '',
            'Processed Data:',
            '• Background subtraction',
            '• Enhancement calculations',
            '• Spatial interpolation'
        ]),
        ('Chemical Data Stream', 1, 8, 4, 2.5, colors['chemical'], [
            'Raw Data:',
            '• Element concentrations',
            '• ICP-MS results',
            '• Quality control samples',
            '',
            'Processed Data:',
            '• Enrichment factors',
            '• Contamination indices',
            '• Statistical summaries'
        ]),
        ('Physical Data Stream', 1, 5, 4, 2.5, colors['physical'], [
            'Raw Data:',
            '• Particle size distribution',
            '• Bulk density values',
            '• Moisture content',
            '',
            'Processed Data:',
            '• Texture classifications',
            '• Physical property indices',
            '• Normalized values'
        ]),
        ('Spatial Data Stream', 1, 2, 4, 2.5, colors['spatial'], [
            'Raw Data:',
            '• GPS coordinates',
            '• Distance measurements',
            '• Site boundaries',
            '',
            'Processed Data:',
            '• Coordinate transformations',
            '• Spatial reference systems',
            '• Distance matrices'
        ])
    ]
    
    for title, x, y, width, height, color, content in data_streams:
        # Stream box
        stream_box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                    facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(stream_box)
        
        # Title
        ax.text(x + width/2, y + height - 0.2, title, fontsize=11, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # Content
        y_pos = y + height - 0.5
        for item in content:
            style = 'bold' if item.endswith(':') and item != '' else 'normal'
            if item == '':
                y_pos -= 0.1
            else:
                ax.text(x + 0.1, y_pos, item, fontsize=9, ha='left', va='center', 
                        color='white', fontweight=style)
                y_pos -= 0.22
    
    # Integration hub (center)
    integration_hub = Circle((11, 8), 2.5, facecolor=colors['integration'], 
                            edgecolor='black', linewidth=2)
    ax.add_patch(integration_hub)
    ax.text(11, 8.8, 'INTEGRATION', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    ax.text(11, 8.4, 'HUB', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='white')
    
    # Integration methods around the hub
    integration_methods = [
        ('Statistical\nCorrelation', 11, 11.5, 0.8),
        ('Spatial\nOverlay', 14, 8, 0.8),
        ('Principal\nComponent\nAnalysis', 11, 4.5, 0.8),
        ('Factor\nAnalysis', 8, 8, 0.8)
    ]
    
    for method, x, y, radius in integration_methods:
        method_circle = Circle((x, y), radius, facecolor='lightblue', 
                              edgecolor='darkblue', linewidth=1)
        ax.add_patch(method_circle)
        ax.text(x, y, method, fontsize=9, fontweight='bold', 
                ha='center', va='center', color='darkblue')
    
    # Arrows from data streams to integration hub
    stream_positions = [(3, 12.25), (3, 9.25), (3, 6.25), (3, 3.25)]
    for x_stream, y_stream in stream_positions:
        # Calculate arrow direction to hub center
        dx = 11 - x_stream - 2
        dy = 8 - y_stream
        length = np.sqrt(dx**2 + dy**2)
        dx_norm = dx / length * 3
        dy_norm = dy / length * 3
        
        arrow = FancyArrow(x_stream + 2, y_stream, dx_norm, dy_norm, 
                          width=0.06, head_width=0.12, head_length=0.1, 
                          fc='darkblue', ec='darkblue', alpha=0.7)
        ax.add_patch(arrow)
    
    # Output products (right side)
    output_box = FancyBboxPatch((16, 3), 5.5, 10, boxstyle="round,pad=0.1", 
                                facecolor=colors['validation'], edgecolor='black', linewidth=1)
    ax.add_patch(output_box)
    ax.text(18.75, 12.5, 'INTEGRATED PRODUCTS', fontsize=13, fontweight='bold', 
            ha='center', va='center', color='white')
    
    output_products = [
        'Contamination Maps:',
        '• Multi-parameter overlays',
        '• Risk level classifications',
        '• Hotspot identification',
        '• Gradient visualization',
        '',
        'Statistical Models:',
        '• Correlation matrices',
        '• Regression equations',
        '• Predictive models',
        '• Uncertainty estimates',
        '',
        'Assessment Reports:',
        '• Source identification',
        '• Impact evaluation',
        '• Risk characterization',
        '• Management recommendations',
        '',
        'Decision Support:',
        '• Remediation priorities',
        '• Monitoring strategies',
        '• Cost-benefit analyses',
        '• Implementation protocols'
    ]
    
    y_pos = 12.2
    for item in output_products:
        style = 'bold' if item.endswith(':') and item != '' else 'normal'
        if item == '':
            y_pos -= 0.15
        else:
            ax.text(16.2, y_pos, item, fontsize=9, ha='left', va='center', 
                    color='white', fontweight=style)
            y_pos -= 0.25
    
    # Arrow from hub to outputs
    arrow_output = FancyArrow(13.5, 8, 2.5, 0, width=0.08, head_width=0.15, 
                             head_length=0.15, fc=colors['integration'], 
                             ec=colors['integration'], alpha=0.8)
    ax.add_patch(arrow_output)
    
    # Quality control framework (bottom)
    qc_box = FancyBboxPatch((6, 0.5), 10, 1.5, boxstyle="round,pad=0.1", 
                            facecolor='lightgray', edgecolor='black', linewidth=1)
    ax.add_patch(qc_box)
    ax.text(11, 1.6, 'QUALITY CONTROL AND VALIDATION', fontsize=12, fontweight='bold', 
            ha='center', va='center')
    
    qc_items = [
        '• Cross-validation between independent datasets',
        '• Statistical significance testing of correlations',
        '• Uncertainty propagation through integration workflow',
        '• Expert review and validation of integrated products'
    ]
    
    for i, item in enumerate(qc_items):
        ax.text(6.2, 1.4 - i*0.2, item, fontsize=9, ha='left', va='center')
    
    # Integration workflow steps
    workflow_steps = [
        (7, 13, 'Step 1:\nData\nPreprocessing'),
        (9, 13, 'Step 2:\nNormalization\n& Scaling'),
        (11, 13, 'Step 3:\nSpatial\nAlignment'),
        (13, 13, 'Step 4:\nStatistical\nIntegration'),
        (15, 13, 'Step 5:\nValidation\n& QC')
    ]
    
    for x, y, step in workflow_steps:
        step_box = FancyBboxPatch((x-0.7, y-0.5), 1.4, 1, boxstyle="round,pad=0.05", 
                                  facecolor='lightyellow', edgecolor='black', linewidth=1)
        ax.add_patch(step_box)
        ax.text(x, y, step, fontsize=8, fontweight='bold', ha='center', va='center')
    
    # Arrows between workflow steps
    for i in range(len(workflow_steps)-1):
        x1 = workflow_steps[i][0] + 0.7
        x2 = workflow_steps[i+1][0] - 0.7
        y_arrow = workflow_steps[i][1]
        arrow = FancyArrow(x1, y_arrow, x2-x1, 0, width=0.03, head_width=0.08, 
                          head_length=0.05, fc='orange', ec='orange', alpha=0.7)
        ax.add_patch(arrow)
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Integration_Workflow_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: Integration_Workflow_Scheme.png")

def create_knowledge_synthesis_scheme():
    """Create knowledge synthesis and interpretation framework"""
    fig, ax = plt.subplots(1, 1, figsize=(20, 16))
    
    colors = {
        'observation': '#3498db',        # Blue
        'analysis': '#e74c3c',           # Red
        'interpretation': '#f39c12',     # Orange
        'knowledge': '#27ae60',          # Green
        'application': '#9b59b6',        # Purple
        'feedback': '#1abc9c',           # Teal
        'header': '#2c3e50'              # Dark blue-gray
    }
    
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Title
    title_box = FancyBboxPatch((0.5, 14.5), 19, 1.2, boxstyle="round,pad=0.1", 
                               facecolor=colors['header'], edgecolor='black', linewidth=2)
    ax.add_patch(title_box)
    ax.text(10, 15.1, 'Knowledge Synthesis and Scientific Interpretation Framework', 
            fontsize=16, fontweight='bold', ha='center', va='center', color='white')
    
    # Knowledge pyramid structure
    pyramid_levels = [
        # Level 1: Data/Observations (bottom - widest)
        ('Raw Observations', 2, 2, 16, 2, colors['observation'], [
            'Field Measurements:', 'Laboratory Analyses:', 'Spatial Data:', 'Temporal Records:',
            '• Magnetic anomalies', '• Element concentrations', '• GPS coordinates', '• Sampling dates',
            '• Soil samples', '• Mineral identification', '• Site boundaries', '• Weather conditions',
            '• Visual observations', '• Particle morphology', '• Land use maps', '• Conflict timeline'
        ]),
        
        # Level 2: Processed Information (middle-lower)
        ('Processed Information', 3, 5, 14, 2, colors['analysis'], [
            'Statistical Summaries:', 'Spatial Patterns:', 'Correlations:', 'Trends:',
            '• Descriptive statistics', '• Contamination maps', '• Parameter relationships', '• Temporal changes',
            '• Distribution patterns', '• Hotspot locations', '• Source signatures', '• Seasonal effects',
            '• Quality metrics', '• Distance relationships', '• Multivariate analysis', '• Long-term monitoring'
        ]),
        
        # Level 3: Interpreted Results (middle-upper)
        ('Interpreted Results', 4, 8, 12, 2, colors['interpretation'], [
            'Mechanistic Understanding:', 'Source Attribution:', 'Risk Assessment:', 'Process Models:',
            '• Contamination processes', '• Munition identification', '• Exposure pathways', '• Transport mechanisms',
            '• Environmental controls', '• Impact characterization', '• Health implications', '• Fate predictions',
            '• Spatial relationships', '• Historical reconstruction', '• Vulnerability mapping', '• Scenario analysis'
        ]),
        
        # Level 4: Scientific Knowledge (top - narrowest)
        ('Scientific Knowledge', 5, 11, 10, 2, colors['knowledge'], [
            'Conceptual Models:', 'General Principles:', 'Predictive Frameworks:', 'Best Practices:',
            '• Process understanding', '• Universal patterns', '• Forecasting models', '• Standard protocols',
            '• Causal relationships', '• Scaling relationships', '• Risk predictions', '• Quality guidelines',
            '• System dynamics', '• Comparative insights', '• Decision tools', '• Implementation strategies'
        ])
    ]
    
    for title, x, y, width, height, color, content in pyramid_levels:
        # Level box
        level_box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1", 
                                   facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(level_box)
        
        # Title
        ax.text(x + width/2, y + height - 0.2, title, fontsize=12, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # Content in columns
        col_width = width / 4
        for col in range(4):
            col_x = x + 0.2 + col * col_width
            # Header
            header_idx = col * 3
            if header_idx < len(content):
                ax.text(col_x, y + height - 0.5, content[header_idx], fontsize=9, 
                        fontweight='bold', ha='left', va='center', color='white')
                # Items
                for item_idx in range(1, 3):
                    content_idx = header_idx + item_idx
                    if content_idx < len(content):
                        ax.text(col_x, y + height - 0.5 - item_idx * 0.25, content[content_idx], 
                                fontsize=8, ha='left', va='center', color='white')
    
    # Application and feedback loop (right side)
    application_box = FancyBboxPatch((16, 8), 3.5, 5, boxstyle="round,pad=0.1", 
                                     facecolor=colors['application'], edgecolor='black', linewidth=1)
    ax.add_patch(application_box)
    ax.text(17.75, 12.5, 'APPLICATION', fontsize=12, fontweight='bold', 
            ha='center', va='center', color='white')
    
    applications = [
        'Policy Development:',
        '• Regulatory standards',
        '• Guidelines & protocols',
        '• Risk thresholds',
        '',
        'Management Actions:',
        '• Remediation planning',
        '• Monitoring programs',
        '• Emergency response',
        '',
        'Scientific Advancement:',
        '• Method improvement',
        '• Theory development',
        '• Technology innovation',
        '',
        'Capacity Building:',
        '• Training programs',
        '• Knowledge transfer',
        '• International cooperation'
    ]
    
    y_pos = 12.2
    for item in applications:
        style = 'bold' if item.endswith(':') and item != '' else 'normal'
        if item == '':
            y_pos -= 0.1
        else:
            ax.text(16.2, y_pos, item, fontsize=9, ha='left', va='center', 
                    color='white', fontweight=style)
            y_pos -= 0.2
    
    # Synthesis processes (left side)
    synthesis_box = FancyBboxPatch((0.5, 8), 3.5, 5, boxstyle="round,pad=0.1", 
                                   facecolor=colors['feedback'], edgecolor='black', linewidth=1)
    ax.add_patch(synthesis_box)
    ax.text(2.25, 12.5, 'SYNTHESIS PROCESSES', fontsize=11, fontweight='bold', 
            ha='center', va='center', color='white')
    
    synthesis_processes = [
        'Integration Methods:',
        '• Meta-analysis',
        '• Systematic review',
        '• Comparative analysis',
        '• Cross-validation',
        '',
        'Interpretation Tools:',
        '• Expert knowledge',
        '• Literature comparison',
        '• Theoretical frameworks',
        '• Peer review',
        '',
        'Validation Approaches:',
        '• Independent datasets',
        '• Alternative methods',
        '• Sensitivity analysis',
        '• Uncertainty assessment'
    ]
    
    y_pos = 12.2
    for item in synthesis_processes:
        style = 'bold' if item.endswith(':') and item != '' else 'normal'
        if item == '':
            y_pos -= 0.1
        else:
            ax.text(0.7, y_pos, item, fontsize=9, ha='left', va='center', 
                    color='white', fontweight=style)
            y_pos -= 0.2
    
    # Arrows showing knowledge flow upward
    for i in range(len(pyramid_levels)-1):
        current_level = pyramid_levels[i]
        next_level = pyramid_levels[i+1]
        
        # Center positions
        current_center_x = current_level[1] + current_level[3]/2
        current_top_y = current_level[2] + current_level[4]
        next_center_x = next_level[1] + next_level[3]/2
        next_bottom_y = next_level[2]
        
        arrow = FancyArrow(current_center_x, current_top_y, 
                          next_center_x - current_center_x, 
                          next_bottom_y - current_top_y, 
                          width=0.08, head_width=0.2, head_length=0.1, 
                          fc='darkgreen', ec='darkgreen', alpha=0.7)
        ax.add_patch(arrow)
    
    # Horizontal arrows to synthesis and application
    # From knowledge to application
    arrow_to_app = FancyArrow(15, 12, 1, 0, width=0.06, head_width=0.15, 
                             head_length=0.1, fc=colors['knowledge'], 
                             ec=colors['knowledge'], alpha=0.8)
    ax.add_patch(arrow_to_app)
    
    # From synthesis to observations (feedback)
    arrow_feedback = FancyArrow(2.25, 8, 0, -5.5, width=0.05, head_width=0.12, 
                               head_length=0.1, fc=colors['feedback'], 
                               ec=colors['feedback'], alpha=0.7)
    ax.add_patch(arrow_feedback)
    ax.text(1.5, 5.5, 'Feedback\nLoop', fontsize=9, ha='center', va='center', 
            rotation=90, style='italic', color=colors['feedback'])
    
    # Quality assurance framework (bottom)
    qa_box = FancyBboxPatch((0.5, 0.2), 19, 1.3, boxstyle="round,pad=0.1", 
                            facecolor='lightgray', edgecolor='black', linewidth=1)
    ax.add_patch(qa_box)
    ax.text(10, 1.2, 'KNOWLEDGE QUALITY ASSURANCE', fontsize=12, fontweight='bold', 
            ha='center', va='center')
    
    qa_elements = [
        'Reproducibility: Standardized methods and transparent documentation',
        'Validation: Multiple independent confirmation and peer review processes',
        'Uncertainty: Quantified confidence intervals and sensitivity analysis',
        'Applicability: Clear scope and limitations for knowledge application'
    ]
    
    for i, element in enumerate(qa_elements):
        ax.text(1, 1 - i*0.15, f"• {element}", fontsize=9, ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig('/Users/adim/Documents/Igph/SoilDegradation/Knowledge_Synthesis_Scheme.png', 
                dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Created: Knowledge_Synthesis_Scheme.png")

def main():
    """Generate comprehensive data synthesis schemes"""
    print("Generating Data Synthesis Schemes for War-Induced Soil Investigation...")
    create_data_synthesis_framework()
    create_integration_workflow_scheme()
    create_knowledge_synthesis_scheme()
    print("\nData synthesis schemes generation completed!")
    print("\nFiles created:")
    print("1. Data_Synthesis_Framework_Scheme.png - Complete data synthesis methodology")
    print("2. Integration_Workflow_Scheme.png - Multi-source data integration workflow")
    print("3. Knowledge_Synthesis_Scheme.png - Scientific knowledge synthesis framework")

if __name__ == "__main__":
    main()
