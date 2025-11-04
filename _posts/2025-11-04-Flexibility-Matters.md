---
title: 'Flexibility Matters: Challenges of Binding Disordered Regions'
date: 2025-11-04
permalink: /posts/2025/11/FlexibilityMatters/
tags:
  - Polyproline Regions
  - Visualizations
  - IDPs
  - Structural Biology
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simplified Figure and Text Layout</title>
    <!-- Load Tailwind CSS for utility classes -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Minimal custom styling for links */
        .article-link {
            color: #1d4ed8; /* Blue-700 */
            text-decoration: none;
        }
        .article-link:hover {
            color: #3b82f6; /* Blue-500 */
        }
    </style>
</head>
<body class="p-6">

    <!-- CORE LAYOUT COMPONENT: Stacks vertically on mobile, becomes horizontal on large screens (lg:flex-row) -->
    <div class="flex flex-col lg:flex-row gap-6 p-4 border border-gray-200 rounded-xl bg-white shadow-lg">

        <!-- Left Column: Image/Visual (takes up 1/3 width on large screens) -->
        <div class="lg:w-1/3 flex justify-center items-start">
            <div class="w-full">
                <!-- Image Placeholder to represent the Biophysical Journal Cover -->
                <img 
                    src="https://placehold.co/500x500/1e293b/f8fafc?text=Biophysical+Journal+Cover%0ATau+%26+BIN1+Dynamics" 
                    alt="Cover image of the November 4 issue of Biophysical Journal visualizing Tau and BIN1 interaction."
                    class="w-full rounded-xl shadow-lg border-4 border-indigo-200/50 object-cover"
                    onerror="this.onerror=null; this.src='https://placehold.co/500x500/1e293b/f8fafc?text=Error%3A+Placeholder+Failed';"
                >
                <div class="mt-4 text-center text-sm text-gray-600 italic">
                    Figure 1: Time-averaged visualization of the dynamic Tau-BIN1 interaction.
                </div>
            </div>
        </div>

        <!-- Right Column: Text Content (takes up 2/3 width on large screens) -->
        <div class="lg:w-2/3">
            <h1 class="text-2xl font-bold text-gray-900 mb-3 tracking-tight">
                Flexibility Matters: Challenges of Binding Disordered Regions
            </h1>
            
            <p class="mb-4 text-gray-700 leading-relaxed">
                We are excited to share a cover image of the <a href="https://www.cell.com/cms/asset/5b6bcd65-af83-4395-a40e-cdd750b6d6f9/cov200h.gif" target="_blank" class="article-link font-medium">November 4 issue of Biophysical Journal</a>, which captures the dynamic interaction between two proteins central to neurological health: Tau and BIN1. The figure represents a time-averaged visualization of thousands of molecular dynamics (MD) frames and is designed to show how phosphorylation reshapes Tau’s behavior in the BIN1 binding environment. Small purple spheres in the image mark phosphorylation sites, which visually demonstrate how the addition of negative charges shifts Tau’s proline-rich region (PRR) away from the canonical binding site.
            </p>

            <p class="mb-6 text-gray-700 leading-relaxed border-l-4 border-indigo-400 pl-4 bg-indigo-50 py-2">
                This visualization reflects our broader research focus: understanding how intrinsically disordered proteins and intrinsically disordered regions behave in protein-protein interactions. Tau’s PRR is highly flexible, and phosphorylation introduces localized negative charges that disrupt its affinity for BIN1’s SH3 domain. However, in both experiment (NMR) and simulations (MD), the complex still forms, and the binding pose is not altered.
            </p>
            
            <div class="pt-2 border-t border-gray-200">
                <p class="text-sm text-gray-600 mt-4">— Amina Gaffour, Michael Bakker, Krishnendu Bera, and Jana Pavlíková Přecechtělová</p>
            </div>
        </div>
        
    </div>

</body>
</html>



<div style="text-align: center;">
  <img src="/images/BiophysicalJournal.jpeg" style="width: 50%">
</div>

https://www.biophysics.org/blog/flexibility-matters-challenges-of-binding-disordered-regions

We are excited to share a cover image of the [November 4 issue of Biophysical Journal](https://www.cell.com/cms/asset/5b6bcd65-af83-4395-a40e-cdd750b6d6f9/cov200h.gif), which captures the dynamic interaction between two proteins central to neurological health: Tau and BIN1. The figure represents a time-averaged visualization of thousands of molecular dynamics (MD) frames and is designed to show how phosphorylation reshapes Tau’s behavior in the BIN1 binding environment. Small purple spheres in the image mark phosphorylation sites, which visually demonstrate how the addition of negative charges shifts Tau’s proline-rich region (PRR) away from the canonical binding site.

This visualization reflects our broader research focus: understanding how intrinsically disordered proteins and intrinsically disordered regions behave in protein-protein interactions. Tau’s PRR is highly flexible, and phosphorylation introduces localized negative charges that disrupt its affinity for BIN1’s SH3 domain. However, in both experiment (NMR) and simulations (MD), the complex still forms, and the binding pose is not altered. The effect of phosphorylation can be more precisely explained by the orientation of the unbound region of PRR, which shifts from the negatively charged residues in the RT-Src loop toward the positively charged residues near the distal or n-Src loops of the SH3 domain.

Real-world implications of this research are significant. In neurodegenerative diseases like Alzheimer’s, Tau phosphorylation disrupts normal protein binding, contributing to pathology. Our findings help explain how specific phosphate charges alter Tau’s structural preferences, which can inform drug development targeting Tau-BIN1 interactions. In addition, these insights support the identification of biomarkers for early diagnosis and guide computational modeling of intrinsically disordered proteins in biomedical research.

Even for those outside the field, this research offers a broader lesson: flexibility matters. Whether designing therapeutics, modeling biological systems, or interpreting protein behavior, understanding how dynamic regions respond to subtle chemical changes can unlock new strategies across different fields. You can find more information on our work at: http://chemistry-mike.github.io/ and https://portal.faf.cuni.cz/Groups/Mathematical-Pharmacy/

— Amina Gaffour, Michael Bakker, Krishnendu Bera, and Jana Pavlíková Přecechtělová