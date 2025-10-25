---
title: "Computational Study of 31P Chemical Shifts in Modified Nucleic Acids"
excerpt: "Developing and validating a quantum mechanics/molecular mechanics (QM/MM) pipeline to decompose the experimental $\text{}^{31}\text{P}$ NMR chemical shift (CS) signal into its underlying electronic (static) and geometric (dynamic) contributions for modified DNA/RNA. <br/><img src='/images/31P-Structures.png'>"
collection: portfolio
---

## Project Goal: Deconstructing the $\text{}^{31}\text{P}$ NMR Signal in Modified DNA

This research project establishes a robust **Quantum Mechanics (QM)** computational pipeline to investigate the subtle yet critical effects of modifications within nucleic acids (DNA/RNA) on the **$\text{}^{31}\text{P}$ Nuclear Magnetic Resonance (NMR) chemical shift (CS)** signal.

The goal is to quantify the distinct contributions of $\text{}^{31}\text{P}$ CS perturbation caused by:
1.  **Purely Electronic Effects:** Changes arising solely from the chemical/electronic presence of a modification (e.g., an abasic site or a $\text{}^{19}\text{F}$ label), holding the geometry constant.
2.  **Geometric/Dynamic Effects:** Changes caused by bond rotations and conformational flexibility.

---

### Core Investigation Strategy

This work aims to establish and quantify the significance of each contribution (electronic vs. dynamic) to the total experimental shift.

1.  **System Design:** The initial focus is on comparing the effects of a $\text{}^{19}\text{F}$ label versus an **abasic dideoxyribose** (loss of a nucleotide base) on the chemical shielding of the two adjacent phosphorus atoms[cite: 3233, 3312]. The computational model starts with a nucleic acid fragment, terminated with appropriate caps and solvated with explicit ions to neutralize charges.

2.  **Establishing the Computational Pipeline (QM/MM):**
    * **Starting Structure:** A representative model is established (e.g., from AlphaFold or built using standard B-DNA geometry).
    * **Geometry Optimization:** We perform simple optimizations using both low-level DFT or Molecular Mechanics (MM) to find a local energy minimum structure[cite: 3285, 3305]. Alternatively, an MD simulation can generate a pool of representative structures, especially if the DNA is single-stranded (ssDNA) and exhibits IDP-like flexibility.
    * **NMR Calculation:** Chemical shielding values are calculated using the **GIAO** method [cite: 3290, 3319], followed by extensive **benchmarking** of various functionals and basis sets[cite: 3295]. The final shieldings are converted to shifts by carefully selecting a reference (e.g., $\text{85\% Phosphoric Acid}$ or $\text{Triphenyl Phosphene}$).

3.  **Decomposing the Shift:**
    * The total experimental shift ($\Delta\delta_{\text{Experimental}}$) is compared to the purely calculated electronic static contribution ($\Delta\delta_{\text{Static}}$).
    * The difference ($\Delta\delta_{\text{Experimental}} - \Delta\delta_{\text{Static}}$) provides an estimation of the **dynamic and geometric influence** on the signal.

### Importance and Outlook

This work is crucial for accurately interpreting experimental NMR data on modified nucleic acids. It will help quantify the significance of conformational flexibility (or "geometric noise") in the $\text{}^{31}\text{P}$ signal, a factor often simplified in structural studies but recognized as critical based on previous experience with Intrinsically Disordered Proteins (IDPs).

