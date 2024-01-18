---
permalink: /
title: "Investigations into Disordered Proteins: Machine Learning"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

### Hello! **Ahoj!** Hallo! **Hej!** ¡Hola! **Bonjour!** Ciao! **Nǐ hǎo!** Marhaba! **Privet!**

Michael Bakker is a researcher working on his PhD in **Biophysics and Physical Chemistry** at **Charles University** with a particular focus in computational chemistry. The main focus of his investigation is **Intrinsically Disordered Proteins (IDPs)** and the application of machine learning algorithms on molecular dynamics trajectories.

My research involves exploring the **conformational phase space** and generating ideal **ensembles** to represent these proteins. The understanding of the phase space helps us to determine the accessible conformations of the proteins, and by generating ensembles, we can better predict properties of the system using more complex and computatonally expensive methods. I have presented my research findings at various conferences and published several papers on the topic. I am passionate about furthering my knowledge in this area and am **always looking for new opportunities to collaborate with other researchers.**

**Intrinsically Disordered Proteins (Brief Overview)**
======
**Intrinsically Disordered Proteins (IDPs)** are an important area of study and research for scientists due to their unique nature and the potential for a wide range of applications. IDPs are proteins that **lack a stable three-dimensional structure** and are instead formed by a large number of conformers in equilibrium. This makes them **difficult to study** using traditional methods such as crystallography or NMR. However, advances in computational methods have enabled researchers to study IDPs using **molecular dynamics simulations**. These simulations allow for the calculation of NMR chemical shifts and small-angle scattering (SAXS) data from these proteins, which can be used to derive their structure and investigate their properties or interactions. Below are two short example trajectories of an **ordered** (GB3) and **disordered** (MAP2C) protein.

Ordered Protein (GB3)      |       IDP (MAP2C)
:-------------------------:|:-------------------------:
![](/images/movie.gif)  |  ![](/images/movie2.gif)

**The current proteins of interest include:**

- **Statherin:** A salivary protein found in humans and other mammals that has a variety of functions, including protecting the teeth from acidic conditions. 
- **Human Tyrosine Hydroxylase 1:** An enzyme that is responsible for the production of dopamine, norepinephrine, and epinephrine, which are important neurotransmitters in the brain.
- **MAP2C:** A neuron-specific microtubule-associated protein that plays an important role in maintaining neuronal structure and function. 
- **Histatin 5:** An antifungal peptide found in saliva that can also act as an anti-inflammatory agent. 
- **Tau:** A microtubule-associated protein found in neurons that is implicated in Alzheimer’s disease. 
- **RNA Polymerase II CTD Heptad Repeats:** A repeating sequence in the RNA polymerase II molecule involved in transcriptional regulation.
- **p53 Protein Regions:** The "Guardian of the Genome" contains large sections of disordered regions both internal and terminal which provide functionality of the protein.

**Project 1: Locking the Domains - A Better Representation**
------
To be written.

**Project 2: Exploring the Conformational Landscape**
------
The molecular dynamics trajectories that are produced are generated like a movie file, using parameterized force-fields to understand the movement of the protein and surrounding solvent. This powerful tool produces massive quantities of conformations for IDPs and can be difficult to interpret, and even more difficult to compute quantum parameters. Fortunately, the field of machine learning has exploded in recent decades to encompass a vast toolkit for researchers to better delve into the chaos that are IDPs.

![Main](/images/Main.png)


**Project 3: Computing NMR Chemical Shifts**
------

Calculating the chemical shifts of IDPs can be of great interest to researchers due to its potential applications. Chemical shifts can provide valuable insights into the structure and dynamics of IDPs, which can be used to further our understanding of their behavior and interactions with other molecules. This can be used to develop new therapeutic treatments, drug delivery systems, and materials. Additionally, chemical shifts can be used to study the conformational phase space of IDPs, which can lead to a better understanding of their function and behavior.

Currently, the most common method for calculating NMR chemical shifts from IDPs is through molecular dynamics simulations. These simulations allow for the calculation of the conformations of the protein in order to generate an average chemical shift for each residue. This average can then be used to infer the structure of the IDP. There are several software packages available for this purpose, such as Sparta+, ShiftX, and AMBER, that excel in different areas but all have their limitations. For example, Sparta+ is capable of efficiently calculating chemical shifts but is limited in its accuracy, while ShiftX can provide more accurate results but is less efficient. It is important to understand the strengths and weaknesses of each software in order to select the best one for the task at hand.

Machine Learning Investigations
------
Machine learning algorithms are powerful tools for data analysis and can be used to gain insights into complex systems. These algorithms can be used to uncover patterns and trends in data, as well as to make predictions and decisions. Popular algorithms include dimensionality reduction methods, such as principal component analysis and singular value decomposition, and clustering algorithms, such as k-means clustering and hierarchical clustering. These algorithms can be used to analyze molecular dynamics trajectories, allowing researchers to explore the conformational phase space of IDPs and to generate ideal ensembles representing these proteins.

![ML](/images/DBSCAN.gif)


![CA](/images/KMEANS.gif)

Machine learning algorithms can be applied to the analysis of molecular dynamics trajectories of IDPs in order to gain insights into their structure, dynamics, and interactions with other molecules. Dimensionality reduction methods, such as principal component analysis and singular value decomposition, can be used to highlight the most important features of the trajectories, allowing researchers to uncover patterns and trends. Clustering algorithms, such as k-means clustering and hierarchical clustering, can be used to investigate the behavior and specific features of the trajectories. Finally, the workflow can be used to generate ideal ensembles that represent the conformational phase space of the IDP, which can be used in future higher-level computations.

![SCAN](/images/Scan.gif)

Ab-Initio Calculations for Chemical Shifts - A Multi-Scale Approach
------

This investigation extended the multi-scale computational scheme used to calculate Nuclear Magnetic Resonance (NMR) chemical shifts (CSs) in proteins that lack a well-defined 3D structure. The scheme employed classical molecular dynamics (MD) with protein fragmentation using the adjustable density matrix assembler (ADMA) and density functional theory (DFT) calculations. A partial re-optimization was then implemented on the raw MD geometries to enhance the accuracy of the scheme and machine-learning based cluster analysis was used to explore its potential in producing protein structure ensembles (CLUSTER ensembles) that yield accurate CSs at a reduced computational cost. The performance of the cluster-based calculations was validated against results obtained with conventional structural ensembles consisting of MD snapshots extracted from the MD trajectory at regular time intervals (REGULAR ensembles). The partial geometry optimization did not universally improve the agreement of computed CSs with the experiment, but it substantially decreased errors associated with the ensemble averaging. A CLUSTER ensemble with 50 structures yielded ensemble averages close to those obtained with a REGULAR ensemble consisting of 500 MD frames, thus requiring only a fraction of the computational time. 

This procedure allows us to calculate NMR chemical shifts using a multi-scale computational scheme that couples the sampling of intrinsically disordered proteins (IDPs) with protein fragmentation using the adjustable density matrix assembler (ADMA) and density functional theory (DFT) calculations. A partial re-optimization is then implemented on the raw MD geometries for enhanced accuracy and machine-learning based cluster analysis is used to explore the potential of producing protein structure ensembles that yield accurate CSs at a reduced computational cost. The results from this investigation show that this procedure is efficient and accurate, allowing us to obtain accurate CSs in a fraction of the computational time.

For more info
------
If you are interested in any of the projects above, feel free to contact me at any of the contact links on the sidebar.
