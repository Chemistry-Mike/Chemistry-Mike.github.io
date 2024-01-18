---
title: "Improving IDP theoretical chemical shift accuracy and efficiency through a combined MD/ADMA/DFT and machine learning approach"
collection: publications
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: 'This paper is about the generation of NMR chemical shifts ab-inito from IDP trajectories using a multiscale approach.'
date: 2022-11-02
venue: 'Physical Chemistry and Chemical Physics'
paperurl: 'https://pubs.rsc.org/en/content/articlelanding/2022/cp/d2cp01638a'
citation:
---

This work presents an improved computational scheme for calculating NMR chemical shifts in intrinsically disordered proteins. The scheme couples molecular dynamics simulations with density functional theory calculations and incorporates partial geometry optimization and machine-learning based cluster analysis. Results show that the scheme can produce accurate CS calculations with reduced computational cost compared to conventional methods. 

[See Publication Here.](https://pubs.rsc.org/en/content/articlelanding/2022/cp/d2cp01638a)

**Abstract:** This work extends the multi-scale computational scheme for the quantum mechanics (QM) calculations of Nuclear Magnetic Resonance (NMR) chemical shifts (CSs) in proteins that lack a well-defined 3D structure. The scheme couples the sampling of an intrinsically disordered protein (IDP) by classical molecular dynamics (MD) with protein fragmentation using the adjustable density matrix assembler (ADMA) and density functional theory (DFT) calculations. In contrast to our early investigation on IDPs (Pavlíková Přecechtělová et al., J. Chem. Theory Comput., 2019, 15, 5642–5658) and the state-of-the art NMR calculations for structured proteins, a partial re-optimization was implemented on the raw MD geometries in vibrational normal mode coordinates to enhance the accuracy of the MD/ADMA/DFT computational scheme. In addition, machine-learning based cluster analysis was performed on the scheme to explore its potential in producing protein structure ensembles (CLUSTER ensembles) that yield accurate CSs at a reduced computational cost. The performance of the cluster-based calculations is validated against results obtained with conventional structural ensembles consisting of MD snapshots extracted from the MD trajectory at regular time intervals (REGULAR ensembles). CS calculations performed with the refined MD/ADMA/DFT framework employed the 6-311++G(d,p) basis set that outperformed IGLO-III calculations with the same density functional approximation (B3LYP) and both explicit and implicit solvation. The partial geometry optimization did not universally improve the agreement of computed CSs with the experiment but substantially decreased errors associated with the ensemble averaging. A CLUSTER ensemble with 50 structures yielded ensemble averages close to those obtained with a REGULAR ensemble consisting of 500 MD frames. The cluster based calculations thus required only a fraction of the computational time.

![Main](/images/Main.png)

