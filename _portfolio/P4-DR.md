---
title: "Computational Innovation: Streamlining NMR Prediction via Clustering and Dimensionality Reduction"
excerpt: "Developing advanced computational protocols that integrate Dimensionality Reduction and Clustering to create highly representative conformational ensembles for accurate NMR chemical shift predictions in Intrinsically Disordered Proteins.<br/><img src='/images/Front4-DR.png'>"
collection: portfolio
---

## Project Goal: Designing Tractable Conformational Ensembles for IDPs

The principal objective of this research is to tackle the computational challenge inherent in characterizing **Intrinsically Disordered Proteins (IDPs)** via **NMR Chemical Shift (CS) predictions**. Accurately modeling these flexible systems at the quantum level requires large conformational ensembles, a process that rapidly becomes intractable.

We developed and validated a novel computational protocol that integrates **Dimensionality Reduction (DR)** and **Clustering Algorithms (CA)** to produce small, highly representative **Clustered Ensembles (CEs)**. This technique effectively bridges the gap between computationally demanding quantum calculations and the vast conformational space of IDPs.

---

<div style="text-align: center;">
  <img src="/images/P4-TOC.png" style="width: 100%">
</div>

---

### Key Methodological Innovations

1.  **Multiscale Dimensionality Reduction and Clustering:**
    * **The Problem:** Traditional clustering methods, like GROMOS (which uses RMSD), perform poorly on IDPs because they fail to account for the local interactions and high-dimensional nature of disordered systems.
    * **The Solution:** We implemented a multiscale approach that uses DR (specifically **tICA** and **tSNE**) *before* clustering to project the data into a lower-dimensional **latent space**, mitigating multicollinearity and computational complexity.
    * **Validated Performance:** Our CEs consistently demonstrated **superior performance** over traditional Sequential Ensembles (SEs) of similar size, outperforming them in approximately **85.7%** of all ensemble sizes evaluated.

2.  **Novel Fingerprint Selection:**
    * **New Feature:** We introduced **Solvent-Accessible Surface Area (SASA)** as a key structural fingerprint for DR, alongside traditional features like $\phi/\psi$ angles and $\alpha$-carbon distances.
    * **SASA Advantage:** Using **SASA-based tSNE** yielded CEs that were better aligned with experimental NMR CSs (improving the $r^2$ value by $0.17$ to $0.36$), as it offers a more comprehensive view of the protein's external interactions and transient structures.

3.  **Integrated Ensemble Selection:**
    * To overcome the complex parametrization of nonlinear DR techniques (like tSNE), we developed an integrated silhouette score scanning protocol (SS$_{INT}$). This metric rigorously selects the optimal combination of parameters (perplexity and cluster size) to ensure the resulting ensemble accurately represents both the local and global dynamics of the original trajectory.

---

### Evaluation and Impact on Advanced Prediction

This work also critically assessed rapid CS predictors for IDPs and directly addressed the challenge of **Post-Translational Modifications (PTMs)**:

* **Phosphorylation Deficiency:** We demonstrated that mainstream neural network-based tools like **Sparta+** and **ShiftX2** fail to accurately incorporate the influence of phosphorylation, as they were not trained on PTM data sets.
* **Need for Quantum Methods:** This deficiency highlights the necessity of implementing **higher-level quantum calculations (DFT)** to accurately capture PTM effects. Our clustering methodology makes these resource-intensive DFT calculations **tractable** by drastically reducing the size of the structural ensemble required for convergence.

---

## Project Collaborators

<div style="overflow: auto; margin-bottom: 20px;"> <img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Pavlíková, Ph.D." style="float: left; margin-right: 15px; width: 200px; height: auto; border-radius: 50%;"> <p>Dr. Jana Přecechtělová Pavlíková is the principal developer of our multi-scale computational framework, integrating Molecular Dynamics, Dimensionality Reduction, and Clustering to model dynamic systems. She applies tICA/tSNE and machine learning to generate compact Clustered Ensembles for accurate NMR Chemical Shift predictions in IDPs. Her work is crucial for ensuring rigorous ensemble selection and robustly coupling trajectory data with DFT for high-accuracy predictions.</p> </div>
