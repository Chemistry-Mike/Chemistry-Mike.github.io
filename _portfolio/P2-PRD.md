---
title: "Research Project: Proline-Rich Regions in Disease"
excerpt: "Investigating the structural dynamics of proline-rich domains (PRDs) in key proteins like p53 and Tau using molecular dynamics simulations to understand disease mechanisms.<br/><img src='/images/Front2-PRD.png'>"
collection: portfolio
---

## Project Goal: Decoding Dynamics of Proline-Rich Domains (PRDs)

This research project applies advanced **computational chemistry** and **biophysical modeling** to investigate the structural and functional dynamics of highly flexible **Proline-Rich Domains (PRDs)**, which are crucial components of Intrinsically Disordered Proteins (IDPs) involved in major diseases.

The primary focus is on two critical systems:

---

### 1. Tau Proline-Rich Region (PRR) in Alzheimer's Disease

This work characterized the Tau PRR fragment (Tau(210-240)) and its interaction with the **SH3 domain of BIN1**, a critical genetic risk factor for Alzheimer's disease (AD).

* **Hyperphosphorylation Effects:** We used extensive all-atom molecular dynamics (MD) and MMGBSA calculations to quantify the precise impact of **hyperphosphorylation** (at T212, T217, T231, and S235) on the Tau-BIN1 interaction.
* **Mechanism of Destabilization:** The addition of phosphate groups causes the Tau peptide to become more compact and disrupts transient secondary structures, which ultimately **destabilizes the complex**. The largest impact was a significant **diminution of salt-bridges** (e.g., R221-D537) and an electrostatic repulsion that shifts Tau's binding preference away from the RT-Src loop toward the more positively charged distal and n-Src loops of BIN1/SH3.
* **Therapeutic Insight:** These detailed structural insights propose a path forward for **targeted therapeutic strategies** focusing on modulating the key electrostatic interactions, rather than just the hydrophobic core interactions, to prevent the detrimental Tau-BIN1 pathology.

---

### 2. P53 Proline-Rich Domain (PRD)

The p53 PRD acts as a regulatory hub for the p53 tumor suppressor. The work focuses on accurately modeling its disordered nature and understanding how its high proline content dictates structure.

* **Structural Fingerprint:** We demonstrated that the p53 PRD exists as a highly flexible, predominantly disordered ensemble that is consistently enriched in **transient Polyproline II (PPII) helices**, interspersed with $\beta$-bends and turns.
* **Contextual Modeling:** By modeling the PRD as an **Intrinsically Disordered Region (IDR)**—by restraining the termini to mimic its connection to other globular domains—we showed that this *PPII-based secondary structure fingerprint* remains robust and largely unaffected by environmental constraints. This suggests the PRD acts as a **dynamic hinge**.
* **Mutational Impact:** Analysis of clinically relevant variants (P72R and P82L) provided a molecular basis for their functional consequences, showing how the loss of consecutive prolines (P72R) increases local flexibility, while disruption of a PXXP motif (P82L) eliminates an associated PPII helix.

---

(base) bakkerm@DESKTOP-0965AJO:~/09-Website/Chemistry-Mike.github.io/_portfolio$ cat P4-DR.md
---
title: "Computational Innovation: Streamlining NMR Prediction via Clustering and Dimensionality Reduction"
excerpt: "Developing advanced computational protocols that integrate Dimensionality Reduction and Clustering to create highly representative conformational ensembles for accurate NMR chemical shift predictions in Intrinsically Disordered Proteins.<br/><img src='/images/Front4-DR.png'>"
collection: portfolio
---

## Project Goal: Designing Tractable Conformational Ensembles for IDPs

The principal objective of this research is to tackle the computational challenge inherent in characterizing **Intrinsically Disordered Proteins (IDPs)** via **NMR Chemical Shift (CS) predictions**. Accurately modeling these flexible systems at the quantum level requires large conformational ensembles, a process that rapidly becomes intractable.

We developed and validated a novel computational protocol that integrates **Dimensionality Reduction (DR)** and **Clustering Algorithms (CA)** to produce small, highly representative **Clustered Ensembles (CEs)**. This technique effectively bridges the gap between computationally demanding quantum calculations and the vast conformational space of IDPs.

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

## Project Collaborators

<div style="overflow: auto; margin-bottom: 20px;"> <img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Pavlíková, Ph.D." style="float: left; margin-right: 15px; width: 200px; height: auto; border-radius: 50%;"> <p><b>Dr. Pavlíková</b> is a key collaborator whose expertise is vital for the **Molecular Dynamics (MD) simulations** and subsequent structural analysis of **Intrinsically Disordered Proteins (IDPs)**, particularly those exhibiting **Proline-Rich Regions (PRDs)**. Her work focuses on robustly characterizing the dynamic conformational ensembles of flexible proteins, including those affected by **Post-Translational Modifications (PTMs)** like **hyperphosphorylation**. She provides advanced methodological support for trajectory analysis, including the accurate quantification of **transient secondary structure elements (e.g., PPII helices)** and the calculation of binding free energies (like MMGBSA) to precisely delineate the **impact of phosphorylation** on protein-protein interactions (e.g., Tau-BIN1 SH3). Her insights ensure the computational models accurately reflect the biophysical reality of these disease-relevant disordered systems.</p> </div>

<div style="overflow: auto; margin-bottom: 20px;"> <img src="{{ '/images/profile-marie-skepo.png' | prepend: site.baseurl }}" alt="Marie Skepö, Ph.D." style="float: left; margin-right: 15px; width: 200px; height: auto; border-radius: 50%;"> <p><b>Prof. Skepö</b>, a Professor of Theoretical Chemistry at **Lund University**, is a leading authority on the **computational biophysics of Intrinsically Disordered Proteins (IDPs)**. Her expertise is fundamental to this project, particularly in the accurate **Molecular Dynamics (MD) simulations** and subsequent analysis of the **p53 Proline-Rich Domain (PRD)**. Prof. Skepö's research focuses on establishing a quantitative link between **computer simulations** and **experimental data** (e.g., Small-Angle X-ray Scattering) to characterize the complex conformational ensembles of IDPs. Her group’s work specifically addresses the impact of **Post-Translational Modifications (PTMs)**, like **phosphorylation**, on the stability and dynamics of disordered regions, ensuring the structural models used for both the p53 and Tau PRDs are biophysically rigorous and reliable.</p> </div>

