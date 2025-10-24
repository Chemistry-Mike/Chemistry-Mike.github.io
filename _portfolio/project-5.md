---
title: "Computational Innovation: Fragment-Based NMR Prediction for IDPs"
excerpt: "Developing and refining a multi-scale computational scheme (MD/ADMA/DFT) with novel partial optimization and clustering techniques to achieve highly accurate and efficient quantum mechanics-based NMR chemical shift predictions for Intrinsically Disordered Proteins.<br/><img src='/images/500x300.png'>"
collection: portfolio
---

## Project Goal: Accelerating Quantum Accuracy for Disordered Systems

This core methodological project focuses on extending and streamlining the **multi-scale computational scheme (MD/ADMA/DFT)** used for calculating **Nuclear Magnetic Resonance (NMR) chemical shifts (CSs)** in proteins that inherently lack a stable, well-defined 3D structure. The objective is to achieve **quantum mechanics (QM) level accuracy** while making the calculations **computationally tractable** for large, flexible systems like Intrinsically Disordered Proteins (IDPs).

---

### Core Methodological Refinements

1.  **Enhanced Accuracy via Partial Geometry Optimization:**
    * The original scheme couples classical **Molecular Dynamics (MD)** sampling with protein fragmentation using the **Adjustable Density Matrix Assembler (ADMA)** and **Density Functional Theory (DFT)** calculations.
    * We introduced a novel step: **partial re-optimization** of the raw MD geometries, specifically along **vibrational normal mode coordinates**.
    * While this did not universally improve agreement with the experiment, it **substantially decreased errors** associated with the ensemble averaging, thus enhancing the overall quality of the computational framework.

2.  **Efficiency through Machine Learning-Based Clustering:**
    * To address the high computational cost of demanding QM calculations, we implemented **machine-learning based cluster analysis**.
    * This technique effectively generates compact **Cluster Ensembles (CLUSTER ensembles)** that accurately represent the system's dynamic behavior, in contrast to generating numerous snapshots at regular intervals (**REGULAR ensembles**).
    * **Significant Cost Reduction:** A CLUSTER ensemble consisting of just **50 structures** yielded ensemble averages comparable to those obtained from a REGULAR ensemble containing **500 MD frames**. This achievement dramatically reduced the required computational time to obtain highly accurate CSs.

3.  **Optimal QM Parameters:**
    * The refined MD/ADMA/DFT framework utilized the **$6-311++G(d,p)$ basis set**, which was found to outperform alternative calculations (including $\text{IGLO}-\text{III}$ and both explicit and implicit solvation models) using the same density functional approximation ($\text{B3LYP}$).

This project page is under construction...
