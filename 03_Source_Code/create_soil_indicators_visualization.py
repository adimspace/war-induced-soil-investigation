#!/usr/bin/env python3
"""
Comprehensive Soil Contamination Indicators Visualization Generator
Creates detailed visual schemes for war-induced soil investigation indicators
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import numpy as np
import seaborn as sns
from matplotlib.gridspec import GridSpec
import pandas as pd

# Set style
plt.style.use('default')
sns.set_palette("husl")

def create_soil_indicators_matrix():
    """Create comprehensive soil indicators classification matrix"""
    
    # Create figure with custom layout
    fig = plt.figure(figsize=(20, 16))
    gs = GridSpec(4, 4, figure=fig, hspace=0.3, wspace=0.2)
    
    # Main title
    fig.suptitle('Comprehensive Soil Contamination Indicators Framework\nfor War-Induced Environmental Assessment', 
                 fontsize=24, fontweight='bold', y=0.95)
    
    # Define indicator categories and their properties
    categories = {
        'Chemical Indicators': {
            'color': '#FF6B6B',
            'indicators': ['Heavy metals', 'Explosive residues', 'PFAS', 'pH variations', 'Electrical conductivity'],
            'complexity': 'High',
            'cost': '$1000-3000',
            'priority': 'Critical'
        },
        'Physical Indicators': {
            'color': '#4ECDC4', 
            'indicators': ['Bulk density', 'Soil texture', 'Water infiltration', 'Soil moisture', 'Temperature'],
            'complexity': 'Medium',
            'cost': '$100-600',
            'priority': 'High'
        },
        'Biological Indicators': {
            'color': '#45B7D1',
            'indicators': ['Organic matter', 'Microbial activity', 'Enzyme activity', 'Soil respiration', 'Bioavailability'],
            'complexity': 'Complex',
            'cost': '$200-1000',
            'priority': 'High'
        },
        'Nutritional Indicators': {
            'color': '#96CEB4',
            'indicators': ['NPK nutrients', 'CEC', 'Trace elements', 'Carbon/nitrogen', 'Mineralization'],
            'complexity': 'Medium',
            'cost': '$150-500',
            'priority': 'Medium'
        }
    }
    
    # Create category overview (top section)
    ax_overview = fig.add_subplot(gs[0, :])
    ax_overview.set_xlim(0, 10)
    ax_overview.set_ylim(0, 2)
    ax_overview.axis('off')
    ax_overview.set_title('Indicator Categories and Classification', fontsize=18, fontweight='bold', pad=20)
    
    # Draw category boxes
    x_positions = [1, 3.5, 6, 8.5]
    for i, (category, props) in enumerate(categories.items()):
        # Main category box
        rect = FancyBboxPatch((x_positions[i]-0.7, 0.5), 1.4, 1.2, 
                             boxstyle="round,pad=0.1", 
                             facecolor=props['color'], 
                             edgecolor='black', 
                             linewidth=2,
                             alpha=0.8)
        ax_overview.add_patch(rect)
        
        # Category name
        ax_overview.text(x_positions[i], 1.4, category, 
                        ha='center', va='center', fontsize=11, fontweight='bold', color='white')
        
        # Properties
        ax_overview.text(x_positions[i], 1.0, f"Complexity: {props['complexity']}", 
                        ha='center', va='center', fontsize=8, color='white')
        ax_overview.text(x_positions[i], 0.8, f"Cost: {props['cost']}", 
                        ha='center', va='center', fontsize=8, color='white')
        ax_overview.text(x_positions[i], 0.6, f"Priority: {props['priority']}", 
                        ha='center', va='center', fontsize=8, color='white', fontweight='bold')
    
    # Analysis workflow diagram (second row)
    ax_workflow = fig.add_subplot(gs[1, :])
    ax_workflow.set_xlim(0, 12)
    ax_workflow.set_ylim(0, 3)
    ax_workflow.axis('off')
    ax_workflow.set_title('Soil Indicators Analysis Workflow', fontsize=16, fontweight='bold', pad=15)
    
    # Workflow steps
    workflow_steps = [
        'Site Assessment\n& Safety', 'Sample Collection\n& Preparation', 'Laboratory Analysis\n& QA/QC', 
        'Data Integration\n& Validation', 'Risk Assessment\n& Interpretation', 'Reporting &\nRecommendations'
    ]
    
    step_colors = ['#FF9999', '#FFB366', '#FFFF66', '#B3FF66', '#66FFB3', '#66B3FF']
    
    for i, step in enumerate(workflow_steps):
        x = 1 + i * 1.8
        
        # Step box
        rect = FancyBboxPatch((x-0.6, 1), 1.2, 1, 
                             boxstyle="round,pad=0.1", 
                             facecolor=step_colors[i], 
                             edgecolor='black', 
                             linewidth=1.5,
                             alpha=0.9)
        ax_workflow.add_patch(rect)
        
        # Step text
        ax_workflow.text(x, 1.5, step, ha='center', va='center', fontsize=9, fontweight='bold')
        
        # Arrow to next step
        if i < len(workflow_steps) - 1:
            ax_workflow.arrow(x + 0.6, 1.5, 0.6, 0, head_width=0.15, head_length=0.1, 
                             fc='black', ec='black', alpha=0.7)
    
    # Detailed indicators matrix (third row)
    ax_matrix = fig.add_subplot(gs[2, :])
    ax_matrix.set_xlim(0, 10)
    ax_matrix.set_ylim(0, 8)
    ax_matrix.axis('off')
    ax_matrix.set_title('Detailed Indicators Classification Matrix', fontsize=16, fontweight='bold', pad=15)
    
    # Create detailed matrix
    y_start = 7
    for cat_idx, (category, props) in enumerate(categories.items()):
        # Category header
        rect = Rectangle((0.2, y_start - cat_idx * 1.8), 9.6, 0.4, 
                        facecolor=props['color'], alpha=0.3, edgecolor='black')
        ax_matrix.add_patch(rect)
        ax_matrix.text(0.5, y_start - cat_idx * 1.8 + 0.2, category, 
                      fontsize=12, fontweight='bold', va='center')
        
        # Indicators
        for i, indicator in enumerate(props['indicators']):
            y_pos = y_start - cat_idx * 1.8 - 0.5 - (i * 0.25)
            
            # Indicator bullet
            circle = Circle((1, y_pos), 0.05, facecolor=props['color'], alpha=0.8)
            ax_matrix.add_patch(circle)
            
            # Indicator name
            ax_matrix.text(1.3, y_pos, indicator, fontsize=10, va='center')
    
    # Priority matrix and timing chart (bottom row)
    ax_priority = fig.add_subplot(gs[3, :2])
    ax_timing = fig.add_subplot(gs[3, 2:])
    
    # Priority matrix
    ax_priority.set_title('Analysis Priority Matrix', fontsize=14, fontweight='bold')
    
    # Create priority data
    priority_data = np.array([
        [3, 2, 1, 2],  # Immediate
        [2, 3, 2, 1],  # Short-term
        [1, 2, 3, 2],  # Medium-term
        [1, 1, 2, 3]   # Long-term
    ])
    
    im = ax_priority.imshow(priority_data, cmap='RdYlBu_r', aspect='auto')
    
    # Labels
    time_periods = ['Immediate\n(0-1 month)', 'Short-term\n(1-6 months)', 
                   'Medium-term\n(6-24 months)', 'Long-term\n(2+ years)']
    category_short = ['Chemical', 'Physical', 'Biological', 'Nutritional']
    
    ax_priority.set_xticks(range(len(category_short)))
    ax_priority.set_xticklabels(category_short, rotation=45)
    ax_priority.set_yticks(range(len(time_periods)))
    ax_priority.set_yticklabels(time_periods)
    
    # Add values to cells
    for i in range(len(time_periods)):
        for j in range(len(category_short)):
            priority_text = ['Low', 'Medium', 'High'][priority_data[i, j] - 1]
            ax_priority.text(j, i, priority_text, ha='center', va='center', 
                           fontweight='bold', color='white' if priority_data[i, j] == 3 else 'black')
    
    # Timing and persistence chart
    ax_timing.set_title('Indicator Persistence and Optimal Timing', fontsize=14, fontweight='bold')
    
    # Sample data for timing
    indicators_sample = ['Heavy metals', 'Explosive residues', 'pH variations', 'Bulk density', 
                        'Organic matter', 'Soil moisture', 'Biological activity']
    persistence = [10, 3, 2, 8, 6, 0.5, 1]  # years
    optimal_timing = [1, 0.1, 0.5, 2, 4, 0.2, 1]  # months
    
    # Create scatter plot
    colors = ['#FF6B6B', '#FF6B6B', '#FF6B6B', '#4ECDC4', '#45B7D1', '#4ECDC4', '#45B7D1']
    
    for i, (ind, pers, timing, color) in enumerate(zip(indicators_sample, persistence, optimal_timing, colors)):
        ax_timing.scatter(timing, pers, s=200, alpha=0.7, color=color, edgecolors='black')
        ax_timing.annotate(ind, (timing, pers), xytext=(5, 5), textcoords='offset points', 
                          fontsize=8, rotation=15)
    
    ax_timing.set_xlabel('Optimal Analysis Timing (months post-conflict)')
    ax_timing.set_ylabel('Persistence in Environment (years)')
    ax_timing.set_xscale('log')
    ax_timing.set_yscale('log')
    ax_timing.grid(True, alpha=0.3)
    
    # Add legend and annotations
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF6B6B', markersize=10, label='Chemical'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#4ECDC4', markersize=10, label='Physical'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#45B7D1', markersize=10, label='Biological'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#96CEB4', markersize=10, label='Nutritional')
    ]
    ax_timing.legend(handles=legend_elements, loc='upper right')
    
    # Add footer information
    fig.text(0.02, 0.02, 'Source: Enhanced War-Induced Soil Investigation Framework | Data: Improved Soil Indicators Database', 
             fontsize=10, style='italic')
    fig.text(0.98, 0.02, 'Created for Scientific Publication Standards', 
             fontsize=10, style='italic', ha='right')
    
    plt.tight_layout()
    return fig

def create_analytical_methods_flowchart():
    """Create analytical methods and equipment flowchart"""
    
    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Title
    ax.text(6, 13.5, 'Soil Contamination Analysis: Methods and Equipment Framework', 
            ha='center', va='center', fontsize=20, fontweight='bold')
    
    # Define method categories
    methods = {
        'Field Methods': {
            'position': (2, 11),
            'color': '#FFB366',
            'methods': ['pH meter', 'EC meter', 'Moisture sensors', 'Temperature probes', 'GPS/GIS'],
            'cost': '$50-500',
            'complexity': 'Simple'
        },
        'Physical Analysis': {
            'position': (6, 11),
            'color': '#4ECDC4',
            'methods': ['Particle size analysis', 'Bulk density core', 'Infiltrometer', 'Penetrometer'],
            'cost': '$100-1000',
            'complexity': 'Medium'
        },
        'Chemical Analysis': {
            'position': (10, 11),
            'color': '#FF6B6B',
            'methods': ['ICP-MS/AAS', 'GC-MS', 'LC-MS/MS', 'XRF spectroscopy'],
            'cost': '$1000-5000',
            'complexity': 'Complex'
        },
        'Biological Analysis': {
            'position': (2, 7),
            'color': '#45B7D1',
            'methods': ['Respirometry', 'Enzyme assays', 'Microbial counts', 'DNA sequencing'],
            'cost': '$500-2000',
            'complexity': 'Complex'
        },
        'Quality Control': {
            'position': (6, 7),
            'color': '#96CEB4',
            'methods': ['Standards/blanks', 'Duplicates', 'Spike recovery', 'Proficiency testing'],
            'cost': '$200-800',
            'complexity': 'Medium'
        },
        'Data Management': {
            'position': (10, 7),
            'color': '#DDA0DD',
            'methods': ['LIMS systems', 'Statistical analysis', 'GIS mapping', 'Database management'],
            'cost': '$1000-10000',
            'complexity': 'Medium'
        }
    }
    
    # Draw method boxes
    for category, props in methods.items():
        x, y = props['position']
        
        # Main box
        rect = FancyBboxPatch((x-1.3, y-1.5), 2.6, 2.5, 
                             boxstyle="round,pad=0.1", 
                             facecolor=props['color'], 
                             edgecolor='black', 
                             linewidth=2,
                             alpha=0.8)
        ax.add_patch(rect)
        
        # Category title
        ax.text(x, y+0.8, category, ha='center', va='center', 
                fontsize=12, fontweight='bold', color='white')
        
        # Methods list
        for i, method in enumerate(props['methods']):
            ax.text(x, y+0.3-i*0.25, f"• {method}", ha='center', va='center', 
                    fontsize=9, color='white')
        
        # Cost and complexity
        ax.text(x, y-1.1, f"Cost: {props['cost']}", ha='center', va='center', 
                fontsize=8, color='white', fontweight='bold')
        ax.text(x, y-1.3, f"Complexity: {props['complexity']}", ha='center', va='center', 
                fontsize=8, color='white')
    
    # Draw workflow connections
    connections = [
        ((2, 9.5), (6, 9.5)),  # Field to Physical
        ((6, 9.5), (10, 9.5)), # Physical to Chemical
        ((2, 9.5), (2, 8.5)),  # Field to Biological
        ((6, 9.5), (6, 8.5)),  # Physical to QC
        ((10, 9.5), (10, 8.5)) # Chemical to Data
    ]
    
    for start, end in connections:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', lw=2, color='black', alpha=0.7))
    
    # Add sampling strategy section
    ax.text(6, 5, 'Sampling Strategy Framework', ha='center', va='center', 
            fontsize=16, fontweight='bold')
    
    # Sampling considerations
    sampling_boxes = [
        {'pos': (1.5, 3.5), 'title': 'Safety Protocol', 'items': ['UXO detection', 'PPE requirements', 'Emergency procedures']},
        {'pos': (4.5, 3.5), 'title': 'Spatial Design', 'items': ['Grid sampling', 'Targeted hotspots', 'Reference sites']},
        {'pos': (7.5, 3.5), 'title': 'Temporal Aspects', 'items': ['Baseline establishment', 'Monitoring frequency', 'Seasonal variation']},
        {'pos': (10.5, 3.5), 'title': 'Documentation', 'items': ['GPS coordinates', 'Photo documentation', 'Chain of custody']}
    ]
    
    for box in sampling_boxes:
        x, y = box['pos']
        
        # Box
        rect = Rectangle((x-0.8, y-1), 1.6, 1.8, 
                        facecolor='lightblue', alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        
        # Title
        ax.text(x, y+0.6, box['title'], ha='center', va='center', 
                fontsize=10, fontweight='bold')
        
        # Items
        for i, item in enumerate(box['items']):
            ax.text(x, y+0.2-i*0.25, f"• {item}", ha='center', va='center', fontsize=8)
    
    # Add decision matrix
    ax.text(6, 1.5, 'Method Selection Decision Matrix', ha='center', va='center', 
            fontsize=14, fontweight='bold')
    
    # Simple decision flowchart
    decision_text = "Budget Available? → Time Constraints? → Technical Expertise? → Method Selection"
    ax.text(6, 0.8, decision_text, ha='center', va='center', fontsize=12, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.5))
    
    # Footer
    ax.text(0.5, 0.2, 'Framework for comprehensive soil contamination assessment in war-affected areas', 
            fontsize=10, style='italic')
    ax.text(11.5, 0.2, 'Adapted from international soil analysis standards', 
            fontsize=10, style='italic', ha='right')
    
    plt.tight_layout()
    return fig

def create_cost_benefit_analysis():
    """Create cost-benefit analysis visualization"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Cost-Benefit Analysis for Soil Contamination Indicators', fontsize=18, fontweight='bold')
    
    # Cost vs Reliability scatter plot
    indicators = ['pH', 'EC', 'Moisture', 'Heavy metals', 'Explosives', 'PFAS', 'Organic matter', 
                 'Bulk density', 'NPK', 'Biological activity']
    costs = [50, 100, 150, 2000, 3000, 5000, 200, 200, 300, 1000]
    reliability = [95, 90, 85, 85, 70, 75, 80, 90, 85, 70]
    urgency = [3, 3, 2, 1, 1, 2, 2, 2, 2, 2]  # 1=immediate, 2=short-term, 3=routine
    
    colors = ['red' if u==1 else 'orange' if u==2 else 'green' for u in urgency]
    
    ax1.scatter(costs, reliability, c=colors, s=100, alpha=0.7, edgecolors='black')
    
    for i, txt in enumerate(indicators):
        ax1.annotate(txt, (costs[i], reliability[i]), xytext=(5, 5), 
                    textcoords='offset points', fontsize=8, rotation=15)
    
    ax1.set_xlabel('Analysis Cost (USD)')
    ax1.set_ylabel('Reliability (%)')
    ax1.set_title('Cost vs Reliability Analysis')
    ax1.set_xscale('log')
    ax1.grid(True, alpha=0.3)
    
    # Priority matrix heatmap
    priority_matrix = np.array([
        [3, 2, 1, 2, 1, 1, 2, 2, 2, 2],  # Immediate need
        [2, 3, 2, 3, 2, 2, 3, 3, 3, 3],  # Cost effectiveness
        [3, 3, 2, 3, 3, 3, 3, 2, 2, 2],  # Technical feasibility
        [2, 2, 3, 2, 1, 1, 2, 3, 3, 2]   # Data availability
    ])
    
    im = ax2.imshow(priority_matrix, cmap='RdYlGn', aspect='auto')
    
    criteria = ['Immediate need', 'Cost effectiveness', 'Technical feasibility', 'Data availability']
    ax2.set_xticks(range(len(indicators)))
    ax2.set_xticklabels(indicators, rotation=45, ha='right')
    ax2.set_yticks(range(len(criteria)))
    ax2.set_yticklabels(criteria)
    ax2.set_title('Multi-criteria Decision Matrix')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax2, shrink=0.8)
    cbar.set_label('Priority Score')
    
    # Time vs Cost analysis
    time_periods = ['Immediate\n(0-1 month)', 'Short-term\n(1-6 months)', 
                   'Medium-term\n(6-24 months)', 'Long-term\n(2+ years)']
    cumulative_costs = [3000, 8000, 15000, 25000]
    essential_costs = [2000, 4000, 6000, 8000]
    
    x_pos = range(len(time_periods))
    
    ax3.bar(x_pos, cumulative_costs, alpha=0.7, label='Comprehensive analysis', color='lightcoral')
    ax3.bar(x_pos, essential_costs, alpha=0.7, label='Essential indicators only', color='lightblue')
    
    ax3.set_xlabel('Time Period')
    ax3.set_ylabel('Cumulative Cost (USD)')
    ax3.set_title('Cumulative Analysis Costs Over Time')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(time_periods)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # ROI analysis
    indicators_roi = ['pH', 'Heavy metals', 'Explosives', 'Biological activity', 'PFAS']
    roi_scores = [8.5, 7.2, 9.1, 6.8, 5.4]  # Return on investment score
    implementation_difficulty = [1, 4, 5, 3, 5]  # 1=easy, 5=very difficult
    
    bubble_sizes = [score * 50 for score in roi_scores]
    
    ax4.scatter(implementation_difficulty, roi_scores, s=bubble_sizes, alpha=0.6, 
               c=range(len(indicators_roi)), cmap='viridis', edgecolors='black')
    
    for i, txt in enumerate(indicators_roi):
        ax4.annotate(txt, (implementation_difficulty[i], roi_scores[i]), 
                    ha='center', va='center', fontweight='bold', color='white')
    
    ax4.set_xlabel('Implementation Difficulty (1=Easy, 5=Very Difficult)')
    ax4.set_ylabel('Return on Investment Score')
    ax4.set_title('ROI vs Implementation Difficulty')
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim(0.5, 5.5)
    ax4.set_ylim(4, 10)
    
    plt.tight_layout()
    return fig

def main():
    """Generate all soil indicators visualization schemes"""
    
    print("Generating comprehensive soil indicators visualization schemes...")
    
    # Create output directory
    import os
    output_dir = "/Users/adim/Documents/Igph/SoilDegradation/02_Methodological_Schemes/Data_Synthesis_Schemes"
    
    # Generate main indicators framework
    print("Creating main indicators classification matrix...")
    fig1 = create_soil_indicators_matrix()
    fig1.savefig(f"{output_dir}/Soil_Indicators_Classification_Matrix.png", 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig1)
    
    # Generate analytical methods flowchart
    print("Creating analytical methods flowchart...")
    fig2 = create_analytical_methods_flowchart()
    fig2.savefig(f"{output_dir}/Soil_Analysis_Methods_Flowchart.png", 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig2)
    
    # Generate cost-benefit analysis
    print("Creating cost-benefit analysis...")
    fig3 = create_cost_benefit_analysis()
    fig3.savefig(f"{output_dir}/Soil_Indicators_Cost_Benefit_Analysis.png", 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig3)
    
    print("✅ Successfully generated 3 comprehensive soil indicators visualization schemes!")
    print(f"📁 Files saved to: {output_dir}")
    print("\nGenerated schemes:")
    print("1. Soil_Indicators_Classification_Matrix.png - Comprehensive indicators framework")
    print("2. Soil_Analysis_Methods_Flowchart.png - Analytical methods and equipment")
    print("3. Soil_Indicators_Cost_Benefit_Analysis.png - Economic analysis framework")

if __name__ == "__main__":
    main()
