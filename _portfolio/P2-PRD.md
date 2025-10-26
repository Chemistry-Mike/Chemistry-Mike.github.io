---
title: "Research Project: Proline-Rich Regions in Disease"
excerpt: "Investigating the structural dynamics of proline-rich domains (PRDs) in key proteins like p53 and Tau using molecular dynamics simulations to understand disease mechanisms.<br/><img src='/images/P2-PRD-Example.png'>"
collection: portfolio
---

<div style="text-align: center;">
  <img src="/images/P2-PRD-Example.png" style="width: 100%">
</div>

## Section 1: Theoretical Insights into Proline-Rich Domains (PRDs)

Proline-Rich Domains (PRDs) are short stretches of amino acids enriched in proline residues, often found within Intrinsically Disordered Proteins (IDPs). Despite their lack of stable tertiary structure, PRDs play pivotal roles in cellular signaling, protein-protein interactions, and disease pathology.

### Polyproline II (PPII) Helices: The Signature Motif

- Structure: PPII helices are left-handed helices with three residues per turn and no internal hydrogen bonding. Their rigidity arises from the cyclic nature of proline, which restricts backbone flexibility.
- Stabilizing Features:
  - High proline content promotes PPII formation.
  - PXXP motifs (where X is any amino acid) are common stabilizers.
  - Flanking charged residues can enhance solubility and interaction specificity.
- Functional Contexts:
  - Frequently found in signaling proteins, cytoskeletal regulators, and transcription factors.
  - Serve as recognition motifs for SH3, WW, and EVH1 domains.
  - Act as dynamic scaffolds, enabling transient interactions without requiring folding.

### PRDs in Intrinsically Disordered Regions (IDRs)

- PRDs often reside within IDRs, contributing to conformational plasticity.
- Their modular nature allows them to act as hinges, linkers, or interaction hubs.
- Environmental factors (e.g., phosphorylation, crowding, binding partners) can modulate their structural ensemble without inducing full folding.

---

## Section 2: Case Studies of Functional PRDs

This section highlights two biologically and clinically significant PRDs—one from the Tau protein, implicated in Alzheimer's disease, and another from p53, the master tumor suppressor.

### Tau Proline-Rich Region (PRR) in Alzheimer's Disease

- Fragment Studied: Residues 210–240 of Tau.
- Interaction Partner: SH3 domain of BIN1, a genetic risk factor for AD.
- Key Findings:
  - Hyperphosphorylation at T212, T217, T231, and S235 compacts the Tau peptide and disrupts transient secondary structures.
  - Destabilization arises from diminished salt bridges (e.g., R221-D537) and electrostatic repulsion, shifting Tau's binding preference.
  - Therapeutic Implication: Targeting electrostatic interactions may offer a novel strategy to mitigate Tau-BIN1 pathology.

### p53 Proline-Rich Domain (PRD)

- Role: Regulatory hub within the p53 protein.
- Structural Characteristics:
  - Highly disordered with persistent PPII helices, beta-bends, and turns.
  - Robust secondary structure fingerprint even under constrained modeling conditions.
- Mutational Analysis:
  - P72R: Loss of consecutive prolines increases local flexibility.
  - P82L: Disruption of a PXXP motif eliminates a key PPII helix.
  - These mutations provide mechanistic insight into altered p53 function in cancer.

---

## Project Collaborators

<div style="overflow: auto; margin-bottom: 20px;"> <img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Pavlíková, Ph.D." style="float: left; margin-right: 15px; width: 200px; height: auto; border-radius: 50%;"> <p>Dr. Jana Prečechtělová Pavlíková is a key collaborator in Molecular Dynamics simulations and structural analysis of Intrinsically Disordered Proteins with Proline-Rich Domains. She specializes in characterizing conformational ensembles and assessing the impact of post-translational modifications like hyperphosphorylation. Her expertise in trajectory analysis and binding free energy calculations ensures that computational models accurately capture the biophysical behavior of disease-relevant protein interactions.</p> </div>

<div style="overflow: auto; margin-bottom: 20px;"> <img src="{{ '/images/profile-marie-skepo.png' | prepend: site.baseurl }}" alt="Marie Skepö, Ph.D." style="float: left; margin-right: 15px; width: 200px; height: auto; border-radius: 50%;"> <p>Prof. Skepö, Professor of Theoretical Chemistry at Lund University, is a leading expert in computational biophysics of Intrinsically Disordered Proteins. Her work is central to this project, particularly in Molecular Dynamics simulations of the p53 Proline-Rich Domain. By integrating simulations with experimental data like SAXS, her group rigorously characterizes conformational ensembles and evaluates how post-translational modifications, such as phosphorylation, affect the structure and dynamics of disordered regions.</p> </div>
