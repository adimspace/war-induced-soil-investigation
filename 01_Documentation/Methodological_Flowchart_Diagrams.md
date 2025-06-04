# Methodological Scheme Flowchart

## Interactive HTML Visualization
The main visual representation is available in `Methodological_Scheme_Visualization.html`

## Simplified Flowchart (Mermaid Format)

```mermaid
graph TD
    A[Study Sites Selection] --> B[Site Characterization]
    B --> C[Umbric Albeluvisols Abruptic Soil]
    
    C --> D[PHASE I: FIELD INVESTIGATION]
    D --> E[Magnetometer Survey]
    D --> F[Soil Sampling Strategy]
    
    E --> G[Cesium Vapor Magnetometer<br/>±0.01 nT sensitivity<br/>1.0 × 0.1 m grid]
    F --> H[Systematic Collection<br/>Crater centers/rims<br/>Distance transects<br/>Background samples]
    
    G --> I[PHASE II: LABORATORY ANALYSIS]
    H --> I
    
    I --> J[Magnetic Properties Analysis]
    I --> K[Thermomagnetic Analysis]
    I --> L[Geochemical Analysis]
    
    J --> M[MFK1-FB Kappabridge<br/>χlf, χhf measurements<br/>χfd calculation]
    J --> N[SQUID Magnetometer<br/>Mrs, ARM analysis<br/>χARM/χ ratios]
    
    K --> O[KLY-5 Kappabridge<br/>-195°C to 700°C<br/>Curie temperature<br/>Magnetic mineralogy]
    
    L --> P[ElvaX Pro XRF<br/>As, Ba, Cu, Fe, Pb, Zn<br/>Matrix corrections<br/>Particle size <50μm]
    
    M --> Q[PHASE III: MICROSCOPIC ANALYSIS]
    N --> Q
    O --> Q
    P --> Q
    
    Q --> R[SEM/EDS Analysis]
    Q --> S[Magnetic Extract Study]
    
    R --> T[JSM-6700F & JCXA-733<br/>Particle morphology<br/>Chemical composition<br/>Size: 1.5-100 μm]
    
    S --> U[Iron-bearing particles<br/>Spherule characterization<br/>Post-blast residue ID]
    
    T --> V[DATA INTEGRATION]
    U --> V
    
    V --> W[Statistical Analysis]
    V --> X[Background Correction]
    V --> Y[Quality Control]
    V --> Z[Contamination Assessment]
    
    W --> AA[OUTCOMES]
    X --> AA
    Y --> AA
    Z --> AA
    
    AA --> BB[Technical Results<br/>• Magnetic enhancement<br/>• Heavy metal correlations<br/>• Particle characterization]
    
    AA --> CC[Environmental Applications<br/>• Rapid screening<br/>• Risk assessment<br/>• Rehabilitation planning]
    
    style A fill:#e74c3c,color:#fff
    style D fill:#e74c3c,color:#fff
    style I fill:#f39c12,color:#fff
    style Q fill:#2ecc71,color:#fff
    style V fill:#9b59b6,color:#fff
    style AA fill:#3498db,color:#fff
```

## Key Equipment Network

```mermaid
graph LR
    subgraph "Field Equipment"
        A1[Cesium Vapor Magnetometer<br/>Geologorazvedka PKM-1]
        A2[Sampling Tools<br/>Grid System]
    end
    
    subgraph "Magnetic Analysis Lab"
        B1[MFK1-FB Kappabridge<br/>Susceptibility]
        B2[KLY-5 Kappabridge<br/>Thermomagnetic]
        B3[SQUID Magnetometer<br/>Remanence]
        B4[MMPM10 Pulse Magnetizer<br/>Saturation]
    end
    
    subgraph "Chemical Analysis Lab"
        C1[ElvaX Pro XRF<br/>Heavy Metals]
        C2[RETSCH MM 300<br/>Sample Preparation]
    end
    
    subgraph "Microscopy Lab"
        D1[JSM-6700F SEM<br/>High Resolution]
        D2[JCXA-733 Microanalyzer<br/>EDS Analysis]
    end
    
    A1 --> B1
    A2 --> B1
    A2 --> C1
    B1 --> B2
    B2 --> B3
    B3 --> B4
    C2 --> C1
    B4 --> D1
    C1 --> D2
    
    style A1 fill:#e74c3c,color:#fff
    style A2 fill:#e74c3c,color:#fff
    style B1 fill:#f39c12,color:#fff
    style B2 fill:#f39c12,color:#fff
    style B3 fill:#f39c12,color:#fff
    style B4 fill:#f39c12,color:#fff
    style C1 fill:#2ecc71,color:#fff
    style C2 fill:#2ecc71,color:#fff
    style D1 fill:#9b59b6,color:#fff
    style D2 fill:#9b59b6,color:#fff
```

## Analysis Flow by Parameter Type

```mermaid
flowchart TB
    subgraph "Magnetic Parameters"
        M1[χ - Magnetic Susceptibility]
        M2[χfd - Frequency Dependence]
        M3[Mrs - Saturation Remanence]
        M4[ARM - Anhysteretic Remanence]
        M5[S300 - Hard/Soft Ratio]
        M6[Curie Temperature]
    end
    
    subgraph "Chemical Parameters"
        C1[As - Arsenic]
        C2[Ba - Barium]
        C3[Cu - Copper]
        C4[Fe - Iron]
        C5[Pb - Lead]
        C6[Zn - Zinc]
    end
    
    subgraph "Physical Parameters"
        P1[Particle Size]
        P2[Morphology]
        P3[Spatial Distribution]
        P4[Grain Size]
    end
    
    M1 --> CORR[Correlation Analysis]
    M2 --> CORR
    M3 --> CORR
    M4 --> CORR
    M5 --> CORR
    M6 --> CORR
    
    C1 --> CORR
    C2 --> CORR
    C3 --> CORR
    C4 --> CORR
    C5 --> CORR
    C6 --> CORR
    
    P1 --> CORR
    P2 --> CORR
    P3 --> CORR
    P4 --> CORR
    
    CORR --> RESULT[Integrated Assessment<br/>Contamination Mapping<br/>Source Identification]
    
    style CORR fill:#e67e22,color:#fff
    style RESULT fill:#8e44ad,color:#fff
```
