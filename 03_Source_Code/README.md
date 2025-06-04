# Source Code
## Python Scripts for Methodological Scheme Generation

This folder contains all Python scripts used to generate the methodological framework schemes. These scripts can be used to modify existing schemes or create new ones.

## 🐍 **Python Scripts**

### **Original Case Study Generator**
- **`generate_schema_images.py`**
  - Generates case-specific schemes for Ukrainian research
  - Functions: `create_main_flowchart()`, `create_equipment_network()`, `create_parameter_analysis()`, `create_site_layout()`
  - Enhanced with detailed case study information

### **General Framework Generator**
- **`General_War_Induced_Soil_Investigation_Scheme.py`**
  - Creates universal application frameworks
  - Functions: `create_general_framework()`, `create_sampling_strategy()`, `create_analytical_workflow()`
  - 7-phase comprehensive methodology

### **Risk Assessment Generator**
- **`create_risk_assessment_scheme.py`**
  - Generates risk and monitoring frameworks
  - Functions: `create_risk_assessment_matrix()`, `create_temporal_monitoring_scheme()`
  - Decision support and time-based protocols

### **Publication Framework Generator**
- **`create_publication_schemes.py`**
  - Creates publication and integration schemes
  - Functions: `create_multiscale_integration()`, `create_publication_framework()`
  - Multi-scale approaches and scientific communication

### **Data Synthesis Generator**
- **`create_synthesis_schemes.py`**
  - Generates data synthesis and knowledge integration schemes
  - Functions: `create_data_synthesis_framework()`, `create_integration_workflow()`, `create_knowledge_synthesis()`
  - Meta-analysis and systematic review protocols

## 🛠️ **Requirements**

### **Python Environment**
```bash
# Activate the existing environment
source ../pdf_env/bin/activate

# Or create new environment
python -m venv venv
source venv/bin/activate
```

### **Required Packages**
```python
matplotlib>=3.10.3
numpy>=2.2.6
pandas>=2.2.3
pillow>=11.2.1
```

## 🎨 **Customization Guide**

### **Modifying Existing Schemes**
1. **Colors:** Update color palettes in each script's color definitions
2. **Content:** Modify text, boxes, and connections within functions
3. **Layout:** Adjust figure sizes and positioning parameters
4. **Styling:** Change fonts, line weights, and visual elements

### **Creating New Schemes**
1. **Template:** Use existing scripts as templates
2. **Structure:** Follow the established function organization pattern
3. **Quality:** Maintain 300 DPI and professional styling standards
4. **Consistency:** Use similar color schemes and typography

### **Running Scripts**
```bash
cd /Users/adim/Documents/Igph/SoilDegradation/03_Source_Code

# Run individual scripts
python generate_schema_images.py
python General_War_Induced_Soil_Investigation_Scheme.py
python create_risk_assessment_scheme.py
python create_publication_schemes.py
python create_synthesis_schemes.py
```

## 🔧 **Script Functions Overview**

### **Image Generation Functions**
- **Figure Setup:** Creates matplotlib figures with appropriate sizing
- **Color Management:** Defines professional color palettes
- **Content Creation:** Adds text, boxes, arrows, and connections
- **Quality Control:** Ensures 300 DPI output and proper formatting
- **File Management:** Saves PNG files with optimized compression

### **Reusable Components**
- **Box Creation:** Standardized box styles and positioning
- **Arrow Drawing:** Consistent connection styles
- **Text Formatting:** Professional typography and sizing
- **Color Schemes:** Harmonized palettes across all schemes

## 📐 **Technical Standards**

### **Image Quality**
- **Resolution:** 300 DPI for publication quality
- **Format:** PNG for maximum compatibility
- **Size:** Optimized for scientific publication requirements
- **Colors:** Professional scientific palette

### **Code Quality**
- **Documentation:** Comprehensive comments and docstrings
- **Modularity:** Reusable functions and components
- **Consistency:** Standardized coding patterns
- **Maintainability:** Clear structure for easy modification

## 🚀 **Extension Possibilities**

### **New Framework Areas**
- **Environmental Monitoring:** Extended protocols for different environments
- **Technology Integration:** AI/ML and remote sensing integration
- **International Standards:** Regional adaptation frameworks
- **Specialized Applications:** Industry-specific methodologies

### **Interactive Features**
- **Web Interfaces:** HTML/JavaScript interactive schemes
- **Dynamic Generation:** Parameter-driven scheme creation
- **Database Integration:** Automated scheme updates from data
- **User Customization:** Interface for non-programmers

---

*These scripts provide complete control over the methodological scheme generation process, enabling customization and extension for specific research needs.*
