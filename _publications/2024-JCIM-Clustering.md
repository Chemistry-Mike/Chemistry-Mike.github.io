---
title: "Streamlining NMR Chemical Shift Predictions for Intrinsically Disordered Proteins: Design of Ensembles with Dimensionality Reduction and Clustering"
collection: publications
permalink: /publication/2024-JCIM-Clustering
excerpt: ''
date: 2024-01-01
venue: 'Journal of Chemical Information and Modeling'
paperurl: 'https://pubs.acs.org/doi/10.1021/acs.jcim.4c00809'
citation: # 'Your Name, You. (2010). &quot;Paper Title Number 2.&quot; <i>Journal 1</i>. 1(2).'
---

[See Publication Here.](https://pubs.acs.org/doi/10.1021/acs.jcim.4c00809)

**Abstract:** By merging advanced dimensionality reduction (DR) and clustering algorithm (CA) techniques, our study advances the sampling procedure for predicting NMR chemical shifts (CS) in intrinsically disordered proteins (IDPs), making a significant leap forward in the field of protein analysis/modeling. We enhance NMR CS sampling by generating clustered ensembles that accurately reflect the different properties and phenomena encapsulated by the IDP trajectories. This investigation critically assessed different rapid CS predictors, both neural network (e.g., Sparta+ and ShiftX2) and database-driven (ProCS-15), and highlighted the need for more advanced quantum calculations and the subsequent need for more tractable-sized conformational ensembles. Although neural network CS predictors outperformed ProCS-15 for all atoms, all tools showed poor agreement with HN CSs, and the neural network CS predictors were unable to capture the influence of phosphorylated residues, highly relevant for IDPs. This study also addressed the limitations of using direct clustering with collective variables, such as the widespread implementation of the GROMOS algorithm. Clustered ensembles (CEs) produced by this algorithm showed poor performance with chemical shifts compared to sequential ensembles (SEs) of similar size. Instead, we implement a multiscale DR and CA approach and explore the challenges and limitations of applying these algorithms to obtain more robust and tractable CEs. The novel feature of this investigation is the use of solvent-accessible surface area (SASA) as one of the fingerprints for DR alongside previously investigated α carbon distance/angles or ϕ/ψ dihedral angles. The ensembles produced with SASA tSNE DR produced CEs better aligned with the experimental CS of between 0.17 and 0.36 r2 (0.18–0.26 ppm) depending on the system and replicate. Furthermore, this technique produced CEs with better agreement than traditional SEs in 85.7% of all ensemble sizes. This study investigates the quality of ensembles produced based on different input features, comparing latent spaces produced by linear vs nonlinear DR techniques and a novel integrated silhouette score scanning protocol for tSNE DR.

