---
title: 'Prolines Have Never Had So Much Style'
date: 2025-10-26
permalink: /posts/2025/10/FancyProlines/
tags:
  - Pymol
  - Polyproline Regions
  - Visualizations
---

For months, I'd been deep in the world of **Intrinsically Disordered Proteins (IDPs)**. These aren't the neat, rigid structures you see in textbooks; they're dynamic, flexible, and utterly central to life, handling critical tasks like cellular signaling and regulating protein-protein interactions.

Proline is one of the most structurally unique amino acids, and its rigid, five-membered pyrrolidine ring is a major player in protein folding, structure, and function. Yet, visualizing this ring clearly amidst the complex 3D structure of a protein can be surprisingly tricky.

<div style="text-align: center;">
  <img src="/images/Blog-1-CisVsTrans.png" style="width: 100%">
</div>

When you look at a protein structure, the proline ring (composed of the N, Cα, Cβ, Cγ, and Cδ atoms) is often just a regular part of the stick model. It can be hard to distinguish it from the backbone or side chains of other residues.

To truly study its conformation—like its famous puckering or its role in cis/trans isomerism—you need a visualization that highlights this critical ring in a dedicated, high-impact way.

First, load your PDB file into PyMol.

Next, run the script:

Use the command: proline_pentagons("peptide")

Remember to replace "peptide" with the name of the object you want to apply it to.

<div class="hover-swap-container">
  <img src="/images/FancyPolyProline-0.png" class="base-image" alt="PDB file loaded in PyMOL">
  <img src="/images/FancyPolyProline-1.png" class="hover-image" alt="PDB file with Proline script results">
</div>

The script also works for full structured proteins.

