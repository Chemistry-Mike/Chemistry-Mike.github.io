---
permalink: /
title: "Investigations into Disordered Proteins"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hello! **Ahoj!** Hallo! **Hej!** ¡Hola! **Bonjour!** Ciao! **你好** مرحبا! **Привет!**
======

Michael Bakker is a researcher working on his PhD in **Biophysics and Physical Chemistry** at **Charles University** with a particular focus in computational chemistry. The main focus of his investigation is **Intrinsically Disordered Proteins (IDPs)** and the application of machine learning algorithms on molecular dynamics trajectories.

**About me:** My research involves exploring the **conformational phase space** and generating ideal **ensembles** to represent these proteins. The understanding of the phase space helps us to determine the accessible conformations of the proteins, and by **generating ensembles**, we can better predict properties of the system using more complex and computatonally expensive methods. I have presented my research findings at various conferences and published several papers on the topic. I am passionate about furthering my knowledge in this area and am **always looking for new opportunities to collaborate with other researchers.**

[Link](/_pages/about.md/#First)

# First

Intrinsically Disordered Proteins (Brief Overview)
======
**[Intrinsically Disordered Proteins (IDPs)](https://en.wikipedia.org/wiki/Intrinsically_disordered_proteins)** are an important area of study and research for scientists due to their unique nature and the potential for a wide range of applications. IDPs are proteins that **lack a stable three-dimensional structure** and are instead formed by a large number of conformers in equilibrium. This makes them **difficult to study** using traditional methods such as crystallography or NMR. However, advances in computational methods have enabled researchers to study IDPs using **molecular dynamics simulations**. These simulations allow for the calculation of **NMR chemical shifts and small-angle scattering (SAXS)** data from these proteins, which can be used to derive their structure and investigate their properties or interactions. Below are two short example trajectories of an **ordered** (GB3) and **disordered** (MAP2C) protein in **Table 1**.

**Table 1.** Graphical representation of a small snippet of a trajectory for an ordered and disordered protein.

Ordered Protein (GB3)      |       IDP (MAP2C)
:-------------------------:|:-------------------------:
![](/images/movie.gif)  |  ![](/images/movie2.gif)

**The current proteins of interest include:**

- **Statherin:** A salivary protein found in humans and other mammals that has a variety of functions, including protecting the teeth from acidic conditions. [STATH](https://en.wikipedia.org/wiki/STATH)
- **Human Tyrosine Hydroxylase 1:** An enzyme that is responsible for the production of dopamine, norepinephrine, and epinephrine, which are important neurotransmitters in the brain. [hTH1](https://en.wikipedia.org/wiki/Tyrosine_hydroxylase)
- **MAP2C:** A neuron-specific microtubule-associated protein that plays an important role in maintaining neuronal structure and function. [MAP2C](https://en.wikipedia.org/wiki/Microtubule-associated_protein) 
- **Histatin 5:** An antifungal peptide found in saliva that can also act as an anti-inflammatory agent. [HIST](https://en.wikipedia.org/wiki/Histatin)  
- **Tau:** A microtubule-associated protein found in neurons that is implicated in Alzheimer’s disease. [TAU](https://en.wikipedia.org/wiki/Tau_protein)  
- **RNA Polymerase II CTD Heptad Repeats:** A repeating sequence in the RNA polymerase II molecule involved in transcriptional regulation.[RNA CTD](https://en.wikipedia.org/wiki/RNA_polymerase_II_holoenzyme)  
- **p53 Protein Regions:** The "Guardian of the Genome" contains large sections of disordered regions both internal and terminal which provide functionality of the protein. [p53](https://en.wikipedia.org/wiki/P53)

**Molecular Dynamics Parameters (Overview)**
======

All molecular dynamics trajectories are generated using [GROMACS](https://onlinelibrary.wiley.com/doi/full/10.1002/jcc.20291) with starting structures generated with [Avogardo](https://jcheminf.biomedcentral.com/articles/10.1186/1758-2946-4-17) fully extended, and then allowed to relax within 100 ns after NVT and NPT equilibriation.

**[Force-Field.](https://manual.gromacs.org/2023.3/user-guide/force-fields.html)** The first step in performing molecular dynamics simulations is to select an appropriate force-field for the protein of interest. Forcefields are mathematical models that describe the interactions between atoms and molecules in a system. These forcefields are derived from experimental data and are able to reproduce many of the thermodynamic and structural properties of proteins. One popular forcefield used in molecular dynamics simulations is the Amber forcefield, which has been extensively parameterized for proteins and nucleic acids. Other popular forcefields include Charmm, OPLS, and GROMOS. The selection of the forcefield depends on the specific system and the type of interactions that need to be captured accurately. IDPs pose a particular challenge but several force fields such as [AMBERSD-ILDN](https://pubs.acs.org/doi/full/10.1021/ct501178z) and [CHARMM36m](https://www.sciencedirect.com/science/article/pii/S0006349520301685) have proven excellent for accounting for the particular challenges of IDPs.

**[Water Model.](https://manual.gromacs.org/archive/4.5/online/water.html)** Water models are important for the simulation of proteins, including intrinsically disordered proteins (IDPs). Intrinsically disordered proteins have a unique structure and behavior that requires specific water models to accurately represent their behavior in simulations. Traditionally, water models such as TIP3P, SPC, and SPC/E have been used in molecular simulations of proteins. These models have been successful in reproducing many properties of folded proteins, but they may not adequately capture the behavior of IDPs. This is because traditional water models are designed to accurately represent the behavior of bulk water, where the water molecules are highly structured and interact primarily through hydrogen bonding. However, the behavior of IDPs is different from that of folded proteins, and therefore, they require a different type of water model. Recently, new water models, such as the [TIP4P-D](https://pubs.acs.org/doi/10.1021/acs.jctc.6b00429) water model, have been specifically designed to better represent the properties of IDPs. These models have been shown to be more accurate in reproducing the behavior of IDPs in simulations, including their hydration properties, local dynamics, and conformational sampling. The TIP4P-D water model takes into account the polarizable nature of water molecules and has a slightly different geometry compared to traditional water models.

**Time Step.** After the simulation system is set up, the molecular dynamics simulation can be performed. This involves numerically integrating the equations of motion for each atom in the system, using forces calculated from the forcefield. The simulation time step, which is typically in the range of 1-2 fs, must be carefully chosen to ensure both accuracy and stability of the simulation.

**Distant Restraints.** Distance restraints are commonly used in molecular dynamics simulations to improve the accuracy of the results by imposing constraints on certain distances within the system. These restraints can be applied to maintain the relative positions of atoms, bonds, or other interactions in the system, and can be defined as either hard or soft constraints. Distance restraints in GROMACS can be applied in the MDP file using the [freezegrps](https://manual.gromacs.org/current/user-guide/mdp-options.html) parameter.

## **Project 1: Locking the Domains - A Better Representation**
------

![Main](/images/TOC.png)

**Figure 1.** Graphical representation of the procedure described in our [publication](https://pubs.acs.org/doi/full/10.1021/acs.jctc.3c00971) of locking the end terminals of an IDR and testing the various properties of the trajectory to find the best "fit" compared to experimental data.

One instance which is generally not considered is the **influence of neighboring regions**, particularly those which are **ordered** and have strict defined structures.

<div style="text-align:center"><img src="/images/PTL-Visualization.png" /></div>

The **pre-tetramerization loop (PTL)** of the tumor suppressor protein p53 is a crucial component in understanding the function of this vital protein. This loop is an intrinsically disordered region (IDR) that plays a significant role in the tetramerization process. The flexibility of this region is essential for the **conformational changes required for p53** to function properly. While traditional molecular dynamics (MD) simulations of the PTL provide a reasonable representation of its behavior, recent studies have shown the advantages of **restraining the end-to-end distance (EE<sub>dist</sub>)** of the loop. By simulating the trajectory of the PTL with a restrained EE<sub>dist</sub>, we gain a deeper understanding of its dynamics and its role in the tetramerization process. In this section, we will explore the effects of restraining the EEdist and how it can enhance our understanding of p53 and other intrinsically disordered regions. Our findings have important implications for studying the impact of mutations on p53's function and provide valuable insights into the conformational dynamics of intrinsically disordered proteins.

**Table 2.** Graphical representation of a small snippet of a trajectory for an unrestrained trajectory, compared to those in which distance restraints are applied.

UNLOCKED                   | EE<sub>dist</sub> = 7.0nm | EE<sub>dist</sub> = 5.0nm | EE<sub>dist</sub> = 3.0nm                    
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![](/images/nCp53.gif)     |  ![](/images/bCp53.gif)   |  ![](/images/lCp53.gif)   |  ![](/images/oCp53.gif)   


Overall, the investigation of the PTL region as an IDP revealed a **highly disordered and flexible structure**, as seen by its predicted disorder and Kratky plots. Unrestrained simulations showed a **wide variety of secondary structures**, primarily consisting of [PPII helices](https://en.wikipedia.org/wiki/Polyproline_helix) and random coils, with **multiple likely sites of intramolecular interactions**, primarily involving proline residues. When the PTL was simulated with terminal restraints, the conformational ensemble was greatly altered, with a shift in free energies and a preference for random coils and PPII helices at greater extended states. The intramolecular interactions also diverged, with a preference for **distant and internal interactions** in contracted states and more **local, terminal interactions** in expanded states. **The restrained trajectory at EE<sub>dist</sub> of 3.0 nm showed strong agreement with experimental data**, particularly with SAXS rigid body modeling and EM structures. This suggests that the restrained trajectory provides a more accurate representation of the PTL region's structure and conformational ensemble compared to the unrestrained simulations. Further investigation is needed to test for the influence of the zwitterionic or neutral state of the termini and its potential impact on intermolecular interactions of the IDR.

![Main](/images/Image.png)

**Project 2: Computing NMR Chemical Shifts**
------

Calculating the chemical shifts of IDPs can be of great interest to researchers due to its potential applications. Chemical shifts can provide valuable insights into the structure and dynamics of IDPs, which can be used to further our understanding of their behavior and interactions with other molecules. This can be used to develop new therapeutic treatments, drug delivery systems, and materials. Additionally, chemical shifts can be used to study the conformational phase space of IDPs, which can lead to a better understanding of their function and behavior.

Currently, the most common method for calculating NMR chemical shifts from IDPs is through molecular dynamics simulations. These simulations allow for the calculation of the conformations of the protein in order to generate an average chemical shift for each residue. This average can then be used to infer the structure of the IDP. There are several software packages available for this purpose, such as Sparta+, ShiftX, and AMBER, that excel in different areas but all have their limitations. For example, Sparta+ is capable of efficiently calculating chemical shifts but is limited in its accuracy, while ShiftX can provide more accurate results but is less efficient. It is important to understand the strengths and weaknesses of each software in order to select the best one for the task at hand.

**Project 3: Mapping the Conformational Landscape**
------
The molecular dynamics trajectories that are produced are generated like a movie file, using parameterized force-fields to understand the movement of the protein and surrounding solvent. This powerful tool produces massive quantities of conformations for IDPs and can be difficult to interpret, and even more difficult to compute quantum parameters. Fortunately, the field of machine learning has exploded in recent decades to encompass a vast toolkit for researchers to better delve into the chaos that are IDPs.

![Main](/images/Main.png)

Dimensionality reduction techniques can be effective in studying IDPs because they can help us better visualize and understand the complex and chaotic motion of these proteins. IDPs do not have well-defined structures and their conformational space is constantly changing, making it challenging to analyze their behaviors and relationships with traditional methods.

![Main](/images/DR-tSNE-Perp.gif)

Machine learning algorithms are powerful tools for data analysis and can be used to gain insights into complex systems. These algorithms can be used to uncover patterns and trends in data, as well as to make predictions and decisions. Popular algorithms include dimensionality reduction methods, such as principal component analysis and singular value decomposition, and clustering algorithms, such as k-means clustering and hierarchical clustering. These algorithms can be used to analyze molecular dynamics trajectories, allowing researchers to explore the conformational phase space of IDPs and to generate ideal ensembles representing these proteins.

Density Based Clustering   |  K-Means Clustering
:-------------------------:|:-------------------------:
![ML](/images/DBSCAN.gif)  |  ![CA](/images/KMEANS.gif)

Machine learning algorithms can be applied to the analysis of molecular dynamics trajectories of IDPs in order to gain insights into their structure, dynamics, and interactions with other molecules. Dimensionality reduction methods, such as principal component analysis and singular value decomposition, can be used to highlight the most important features of the trajectories, allowing researchers to uncover patterns and trends. Clustering algorithms, such as k-means clustering and hierarchical clustering, can be used to investigate the behavior and specific features of the trajectories. Finally, the workflow can be used to generate ideal ensembles that represent the conformational phase space of the IDP, which can be used in future higher-level computations.

![SCAN](/images/Scan.gif)

**Project 4: Ab-Initio Calculations for Chemical Shifts - A Multi-Scale Approach**
------

![SCAN](/images/Fragmentation.png)

This investigation extended the **multi-scale computational scheme** used to calculate **Nuclear Magnetic Resonance (NMR)** chemical shifts (CSs) in proteins that lack a well-defined 3D structure. The scheme employed **classical molecular dynamics (MD)** with **protein fragmentation** using the **adjustable density matrix assembler (ADMA)** and **density functional theory (DFT)** calculations. A **partial re-optimization** was then implemented on the raw MD geometries to enhance the accuracy of the scheme and **machine-learning based cluster analysis** was used to explore its potential in producing protein structure ensembles (**CLUSTER ensembles**) that yield accurate CSs at a reduced computational cost. The performance of the **cluster-based calculations** was validated against results obtained with **conventional structural ensembles** consisting of MD snapshots extracted from the MD trajectory at regular time intervals (**REGULAR ensembles**). The **partial geometry optimization** did not universally improve the agreement of computed CSs with the experiment, but it substantially decreased errors associated with the ensemble averaging. A CLUSTER ensemble with 50 structures yielded ensemble averages close to those obtained with a REGULAR ensemble consisting of 500 MD frames, thus requiring only a fraction of the computational time.

This procedure allows us to calculate **NMR chemical shifts** using a **multi-scale computational scheme** that couples the sampling of **intrinsically disordered proteins (IDPs)** with protein fragmentation using the **adjustable density matrix assembler (ADMA)** and **density functional theory (DFT) calculations**. A partial re-optimization is then implemented on the **raw MD geometries** for enhanced accuracy and **machine-learning based cluster analysis** is used to explore the potential of producing **protein structure ensembles** that yield accurate CSs at a reduced computational cost. The **[results](https://pubs.rsc.org/en/content/articlelanding/2022/cp/d2cp01638a)** from this investigation show that this procedure is **efficient and accurate**, allowing us to obtain accurate CSs in a **fraction of the computational time**.

For more info
------
If you are interested in any of the projects above, feel free to contact me at any of the contact links on the sidebar.
