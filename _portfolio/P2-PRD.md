---
title: "Research Project: Proline-Rich Regions in Disease"
excerpt: "Investigating the structural dynamics of proline-rich domains (PRDs) in key proteins like p53 and Tau using molecular dynamics simulations to understand disease mechanisms.<br/><img src='/images/Front2-PRD.png'>"
collection: portfolio
---

<div style="text-align: center;">
  <img src="/images/P2-PRD-Example.png" style="width: 100%">
</div>

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

## Project Collaborators

<div style="overflow: auto; margin-bottom: 20px;"> <img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Pavlíková, Ph.D." style="float: left; margin-right: 15px; width: 200px; height: auto; border-radius: 50%;"> <p>Dr. Pavlíková is a key collaborator vital for the Molecular Dynamics (MD) simulations and structural analysis of Intrinsically Disordered Proteins (IDPs) with Proline-Rich Regions (PRDs). Her work focuses on rigorously characterizing dynamic conformational ensembles and the effects of Post-Translational Modifications (PTMs) like hyperphosphorylation. She provides advanced methodological support for trajectory analysis, including the quantification of transient secondary structures (e.g., PPII helices) and the calculation of binding free energies to precisely delineate the impact of phosphorylation on protein-protein interactions (e.g., Tau-BIN1 SH3). Her insights ensure the computational models accurately reflect the biophysical reality of these disease-relevant systems.</p> </div>

<div style="overflow: auto; margin-bottom: 20px;"> <img src="{{ '/images/profile-marie-skepo.png' | prepend: site.baseurl }}" alt="Marie Skepö, Ph.D." style="float: left; margin-right: 15px; width: 200px; height: auto; border-radius: 50%;"> <p>Prof. Skepö, a Professor of Theoretical Chemistry at Lund University, is a leading authority on the computational biophysics of Intrinsically Disordered Proteins (IDPs). Her expertise is fundamental to this project, especially in accurate Molecular Dynamics (MD) simulations and the analysis of the p53 Proline-Rich Domain (PRD). Prof. Skepö's research establishes a quantitative link between computer simulations and experimental data (e.g., Small-Angle X-ray Scattering) to characterize complex conformational ensembles. Her group’s work specifically addresses the impact of Post-Translational Modifications (PTMs), like phosphorylation, on the stability and dynamics of disordered regions, ensuring the structural models used are rigorous and reliable.</p> </div>
