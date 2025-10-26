---
title: 'Prolines Have Never Had So Much Style'
date: 2025-10-26
permalink: /posts/2025/10/FancyProlines/
tags:
  - Pymol
  - Polyproline Regions
  - Visualizations
  - IDPs
  - Structural Biology
---

For months, I'd been deep in the world of **Intrinsically Disordered Proteins (IDPs)**. These aren't the neat, rigid structures you see in textbooks; they're dynamic, flexible, and utterly central to life, handling critical tasks like cellular signaling and regulating protein-protein interactions.

Proline is one of the most structurally unique amino acids, and its rigid, five-membered pyrrolidine ring is a major player in protein folding, structure, and function. Yet, visualizing this ring clearly amidst the complex 3D structure of a protein can be surprisingly tricky.

## Why Prolines Demand Attention

The core structure of a proline—specifically the **pyrrollidine ring**—governs its behavior. A proline can exist in either a *cis* or *trans* isomeric state around the peptide bond, a switch that can completely change a protein's function. This image is to show the importance of understanding the structure of the proline.

<div style="text-align: center;">
  <img src="/images/Blog-1-CisVsTrans.png" style="width: 80%">
</div>

When you look at a protein structure, the proline ring (composed of the N, $\text{C}\alpha$, $\text{C}\beta$, $\text{C}\gamma$, and $\text{C}\delta$ atoms) is often just a regular part of the stick model. It can be hard to distinguish it from the backbone or side chains of other residues. To truly study its conformation—like its famous **puckering** or its role in *cis/trans* isomerism—you need a visualization that highlights this critical ring in a dedicated, high-impact way.

To solve this visualization problem, I wrote a Python script. This PyMOL extension uses **Custom Graphic Objects (CGOs)** to give every proline ring the spotlight it deserves.

## Hover over the image to see the transformation

<div class="hover-swap-container">
  <img src="/images/FancyPolyProline-0.png" class="base-image" alt="PDB file loaded in PyMOL">
  <img src="/images/FancyPolyProline-1.png" class="hover-image" alt="PDB file with Proline script results">
</div>

Here's a breakdown of what the script does:

### 1. High-Contrast Ring Highlighting

The heart of the script is the creation of CGOs that target the five ring atoms ($\text{N}$, $\text{C}\alpha$, $\text{C}\beta$, $\text{C}\gamma$, $\text{C}\delta$):

* **Yellow Filled Pentagon:** A **solid, yellow-filled CGO pentagon** is drawn across the face of the ring. This instantly defines the ring's plane and makes its structural conformation easy to spot.

* **Purple Tube Outline:** Thick **purple CGO cylinders** are drawn along the edges of the ring. This high-contrast outline ensures the feature pops against the protein structure.

### 2. Full Residue Styling

Beyond the ring itself, the script colors the entire proline residue **purple** and adjusts the display mode for clarity:
* It hides the default cartoon to minimize clutter.
* It automatically adds hydrogens and displays both hydrogen and non-hydrogen atoms as size-adjusted spheres, giving you full atomic detail.
* It creates an optional, semi-transparent **purple surface (`prings`)** over the ring atoms to show solvent accessibility.

To use the script, you must first load it into PyMOL. Once loaded, run the function with your object name:

Next, run the script:
```python
# Assuming you named your script fancyProlines.py
run fancyProlines.py

# Run the function on your structure
proline_pentagons("peptide")
```

Remember to replace "peptide" with the name of the object you want to apply it to.

When you look at a protein structure, the proline ring (composed of the N, Cα, Cβ, Cγ, and Cδ atoms) is often just a regular part of the stick model. It can be hard to distinguish it from the backbone or side chains of other residues.

To truly study its conformation—like its famous puckering or its role in cis/trans isomerism—you need a visualization that highlights this critical ring in a dedicated, high-impact way.

First, load your PDB file into PyMol.

Next, run the script:

Use the command: proline_pentagons("peptide")

Remember to replace "peptide" with the name of the object you want to apply it to.

The script also works for full structured proteins, instantly highlighting all prolines in a complex fold.

<div class="hover-swap-container">
  <img src="/images/FancyPolyProline-3.png" class="base-image" alt="PDB file loaded in PyMOL">
  <img src="/images/FancyPolyProline-2.png" class="hover-image" alt="PDB file with Proline script results">
</div>

The fancyProlines.py script is now an essential tool for my IDP research, and I hope it helps bring the same level of visual clarity to yours!
