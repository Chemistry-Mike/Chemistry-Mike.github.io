---
title: "Computational NMR Spectroscopy: Advancing Quantum Methods for Disordered Biomolecules"
excerpt: "Developing and refining advanced computational schemes (MD/ADMA/DFT/QM/MM) to achieve high-accuracy NMR chemical shift predictions for Intrinsically Disordered Proteins (IDPs) and to deconstruct the 31P NMR signal in modified nucleic acids.<br/><img src='/images/Front5-NMR.png'>"
collection: portfolio
---

<p>Jana Test: <img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Test"></p>
<p>Gary Test: <img src="{{ '/images/profile-gary-meints.png' | prepend: site.baseurl }}" alt="Gary Test"></p>

## Project Goal: Accelerating Quantum Accuracy for Dynamic Biomolecules

This combined methodological research focuses on developing, refining, and applying advanced **quantum mechanics (QM)**-based computational schemes to accurately predict and interpret **Nuclear Magnetic Resonance (NMR) chemical shifts (CSs)** in complex, dynamic systems, including **Intrinsically Disordered Proteins (IDPs)** and **Modified Nucleic Acids (DNA/RNA)**. The objective is to achieve **QM-level accuracy** while ensuring **computational tractability** and providing a detailed deconstruction of the $\text{CS}$ signal.

***

## Part 1: Fragment-Based NMR Prediction for IDPs

This section details the development and streamlining of a multi-scale computational framework to calculate highly accurate $\text{CSs}$ for IDPs, focusing on efficiency and quantum accuracy.

### Core Methodological Refinements (MD/ADMA/DFT)

1.  **Efficiency through Machine Learning-Based Clustering:**
    * To address the high computational cost of demanding QM calculations, we implemented **machine-learning based cluster analysis**.
    * This technique generated compact **Cluster Ensembles (CLUSTER ensembles)** that accurately represent the system's dynamic behavior with significantly fewer structures than traditional sampling (**REGULAR ensembles**).
    * **Impact:** A CLUSTER ensemble of just **50 structures** yielded ensemble averages comparable to those obtained from a REGULAR ensemble containing **500 MD frames**, dramatically reducing computational time.

2.  **Enhanced Accuracy via Partial Geometry Optimization:**
    * A novel step involving **partial re-optimization** of the MD geometries along **vibrational normal mode coordinates** was introduced.
    * This refinement **substantially decreased errors** associated with the ensemble averaging, enhancing the overall quality and stability of the computational framework.

3.  **Optimal QM Parameters:** The refined MD/ADMA/DFT framework utilized the **$6-311++G(d,p)$ basis set** in conjunction with the B3LYP functional, which was found to be the optimal choice for this application.

***

## Part 2: Deconstructing the $\text{}^{31}\text{P}$ NMR Signal in Modified Nucleic Acids

This section details the establishment and application of a **Quantum Mechanics/Molecular Mechanics (QM/MM)** pipeline to investigate the subtle effects of modifications in DNA/RNA on the **$\mathbf{^{31}P}$ NMR $\text{CS}$ signal**.

### Investigation Strategy: Signal Decomposition

The project's goal is to quantitatively separate the total experimental $\text{CS}$ into its distinct contributions:

1.  **Purely Electronic Effects ($\Delta\delta_{\text{Static}}$):** Changes arising solely from the chemical/electronic presence of a modification (e.g., an abasic site or a $\text{}^{19}\text{F}$ label), holding the geometry constant.
2.  **Geometric/Dynamic Effects ($\Delta\delta_{\text{Dynamic}}$):** Changes caused by bond rotations and conformational flexibility.

### Computational Pipeline

* **QM/MM Setup:** A representative nucleic acid fragment, terminated with appropriate caps and solvated with explicit ions, was established to model modified structures.
* **NMR Calculation:** Chemical shielding values were calculated using the **GIAO** method, followed by rigorous **benchmarking** of various functionals and basis sets.
* **Decomposition:** The difference between the total experimental shift ($\Delta\delta_{\text{Experimental}}$) and the purely calculated static electronic contribution ($\Delta\delta_{\text{Static}}$) provided a crucial quantitative estimation of the **dynamic and geometric influence** on the $\text{}^{31}\text{P}$ signal.

***

## Significance and Outlook

This combined body of work establishes **state-of-the-art computational methodologies** for two highly dynamic classes of biomolecules. It delivers both an **efficient, high-accuracy computational engine** for IDP $\text{CS}$ prediction and a **robust analytical tool** for interpreting the electronic and conformational factors governing the $\text{}^{31}\text{P}$ signal in modified nucleic acids, which is crucial for accurately interpreting experimental NMR data on these complex systems.

***

## Collaborators

<div style="overflow: auto;">
  <img src="images/profile-jana-pavlikova.jpg" alt="Jana Pavlikova" style="float: right; margin-left: 15px; width: 100px; height: auto; border-radius: 50%;">
  <p><b>Jana Pavlíková, Ph.D.</b>, played a crucial role in developing and validating the machine learning-based clustering methods for IDP simulations. Her expertise in data analysis and computational efficiency was instrumental in achieving the significant cost reductions for quantum chemical calculations.</p>
</div>

<div style="overflow: auto;">
  <img src="images/profile-gary-meints.png" alt="Gary Meints" style="float: right; margin-left: 15px; width: 100px; height: auto; border-radius: 50%;">
  <p><b>Prof. Gary Meints</b> provided essential guidance and resources for the quantum mechanics/molecular mechanics (QM/MM) pipeline for modified nucleic acids. His insights into experimental $\text{}^{31}\text{P}$ NMR data and the nuances of electronic structure theory were vital for establishing the decomposition strategy.</p>
</div>

<div style="overflow: auto;">
  <img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Pavlikova" style="float: right; margin-left: 15px; width: 100px; height: auto; border-radius: 50%;">
  <p><b>Jana Pavlíková, Ph.D.</b>, played a crucial role in developing and validating the machine learning-based clustering methods for IDP simulations (Part 1). Her expertise in data analysis and computational efficiency was instrumental in achieving the significant cost reductions for quantum chemical calculations.</p>
</div>

<div style="overflow: auto;">
  <img src="{{ '/images/profile-gary-meints.png' | prepend: site.baseurl }}" alt="Gary Meints" style="float: right; margin-left: 15px; width: 100px; height: auto; border-radius: 50%;">
  <p><b>Prof. Gary Meints</b> provided essential guidance and resources for the quantum mechanics/molecular mechanics (QM/MM) pipeline for modified nucleic acids (Part 2). His insights into experimental $\text{}^{31}\text{P}$ NMR data and the nuances of electronic structure theory were vital for establishing the decomposition strategy.</p>
</div>

![Test Image of Quantum Pharmacy Header](images/HeaderImage-QuantumPharmacy.png)

## Collaborators

![Test Image of Quantum Pharmacy Header]({{ '/images/HeaderImage-QuantumPharmacy.png' | prepend: site.baseurl }})

<div style="overflow: auto;">

## Collaboration Justification

### Dr. Jana Pavlíková (Charles University) 🇨🇿

Dr. Pavlíková is critical to **Part 1** of the project, focusing on **Intrinsically Disordered Proteins (IDPs)**, as she is a principal developer of this exact multi-scale computational methodology. Her expertise lies in coupling **Molecular Dynamics (MD)** with **fragmentation techniques** and **Density Functional Theory (DFT)** to accurately compute NMR chemical shifts for dynamic systems. Specifically, her work has validated the use of **machine learning-based clustering** and **partial re-optimization** to achieve quantum accuracy while significantly improving computational efficiency.

---

### Dr. Gary Meints (Michigan State University) 🇺🇸

Dr. Meints is essential for **Part 2**, which addresses **deconstructing the ${}^{31}\text{P}$ NMR signal in modified nucleic acids**, given his extensive background in the experimental analysis of this core subject. His research group is renowned for using **${}^{31}\text{P}$ Dynamic NMR** to characterize the subtle, sequence-dependent dynamics of the **DNA phosphate backbone** (specifically the BI/BII conformational equilibrium). This expertise provides the crucial **experimental data and physical chemistry benchmark** required to validate and interpret our proposed $\text{QM/MM}$ decomposition strategy.

***

## Collaborators

<div style="overflow: auto;">
  <img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Pavlikova" style="float: right; margin-left: 15px; width: 100px; height: auto; border-radius: 50%;">
  <p><b>Jana Pavlíková, Ph.D.</b>, played a crucial role in developing and validating the machine learning-based clustering methods for IDP simulations (Part 1). Her expertise in data analysis and computational efficiency was instrumental in achieving the significant cost reductions for quantum chemical calculations.</p>
</div>

<div style="overflow: auto;">
  <img src="{{ '/images/profile-gary-meints.png' | prepend: site.baseurl }}" alt="Gary Meints" style="float: right; margin-left: 15px; width: 100px; height: auto; border-radius: 50%;">
  <p><b>Prof. Gary Meints</b> provided essential guidance and resources for the quantum mechanics/molecular mechanics (QM/MM) pipeline for modified nucleic acids (Part 2). His insights into experimental $\text{}^{31}\text{P}$ NMR data and the nuances of electronic structure theory were vital for establishing the decomposition strategy.</p>
</div>

***

***

## Collaborators

### Jana Pavlíková, Ph.D.

<img src="{{ '/images/profile-jana-pavlikova.jpg' | prepend: site.baseurl }}" alt="Jana Pavlikova" style="width: 120px; height: auto; border-radius: 50%; display: block; margin: 0 auto 15px;">

<p>Jana Pavlíková, Ph.D., played a crucial role in developing and validating the machine learning-based clustering methods for IDP simulations (Part 1). Her expertise in data analysis and computational efficiency was instrumental in achieving the significant cost reductions for quantum chemical calculations.</p>

<hr/>

### Prof. Gary Meints

<img src="{{ '/images/profile-gary-meints.png' | prepend: site.baseurl }}" alt="Gary Meints" style="width: 120px; height: auto; border-radius: 50%; display: block; margin: 0 auto 15px;">

<p>Prof. Gary Meints provided essential guidance and resources for the quantum mechanics/molecular mechanics (QM/MM) pipeline for modified nucleic acids (Part 2). His insights into experimental $\text{}^{31}\text{P}$ NMR data and the nuances of electronic structure theory were vital for establishing the decomposition strategy.</p>
