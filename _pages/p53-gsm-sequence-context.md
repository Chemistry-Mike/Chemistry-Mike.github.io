---
layout: showcase
title: "How sequence context changes AlphaFold3 predictions of p53"
kicker: p53 conference poster · Supplementary analysis
page_class: poster-study
nav_section: Research
permalink: /research/p53-gsm-sequence-context/
description: "A four-context AlphaFold3 pilot comparing the same p53 residues 1\u201328 against structural and NMR observables."
---
<p class="poster-back"><a href="{{ '/research/' | relative_url }}">← Back to research</a></p>
<p class="poster-study-status">Exploratory supplementary pilot · Benchmark manuscript resubmitted</p>
## Short answer

Including more p53 sequence context changed AlphaFold3 predictions for the same N-terminal residues, but did not uniformly improve or worsen agreement with experimental chemical shifts. Larger contexts produced a greater mean distance between residues 1 and 28; changes in chemical-shift agreement depended on the nucleus and metric.

## Why context matters

Generative structure models (GSMs) predict molecular conformations, and neighboring sequence or folded domains may influence their outputs. This pilot tests **AlphaFold3 only**, rather than all six GSMs in the benchmark.

We generated ensembles in four sequence contexts: the transactivation domains (TAD1/2); TAD1/2 plus the proline-rich domain (PRD); those regions plus the DNA-binding domain (DBD); and full-length p53. Every structural and chemical-shift comparison uses the **same stored residues 1–28**. The smallest context is TAD1/2, not an isolated TAD1 or isolated-1–28 baseline. The width of a stored array does not establish the biological length of its original prediction construct.

## Quantitative comparison

Nuclear magnetic resonance (NMR) chemical shifts probe local environments. Root-mean-square error (RMSE) measures absolute prediction error; chemical-shift errors below are in parts per million (ppm). The distance is the ensemble-mean Cα distance from residue 1 to residue 28, in nanometers (nm). Conformation counts are not counts of independent dynamical observations.

<div class="poster-table-scroll" role="region" aria-label="Shared residues 1–28 across four AlphaFold3 contexts" tabindex="0"><table data-poster-table="context-summary"><caption>Shared residues 1–28 across four AlphaFold3 contexts</caption><thead><tr><th scope="col">Prediction context</th><th scope="col">Conformations</th><th scope="col">Distance 1–28 (nm)</th><th scope="col">C′ RMSE (ppm)</th><th scope="col">Cα RMSE (ppm)</th><th scope="col">Cβ RMSE (ppm)</th><th scope="col">N RMSE (ppm)</th><th scope="col">HN RMSE (ppm)</th></tr></thead><tbody><tr><th scope="row">TAD1/2</th><td>4,950</td><td>3.60</td><td>1.304</td><td>0.728</td><td>0.710</td><td>1.116</td><td>0.423</td></tr><tr><th scope="row">TAD1/2 + PRD</th><td>4,995</td><td>4.08</td><td>1.249</td><td>0.734</td><td>0.686</td><td>1.157</td><td>0.435</td></tr><tr><th scope="row">TAD1/2 + PRD + DBD</th><td>4,620</td><td>5.79</td><td>1.132</td><td>0.721</td><td>0.612</td><td>1.044</td><td>0.462</td></tr><tr><th scope="row">Full-length p53</th><td>4,419</td><td>5.74</td><td>1.137</td><td>0.726</td><td>0.613</td><td>1.033</td><td>0.468</td></tr></tbody></table></div>

## Distance maps

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/context/ca_distances.png' | relative_url }}" aria-label="Open full-size figure: Four mean Cα distance maps for the shared p53 residues 1–28 in different AlphaFold3 sequence contexts."><img src="{{ '/images/research/p53-gsm/context/ca_distances.png' | relative_url }}" alt="Four mean Cα distance maps for the shared p53 residues 1–28 in different AlphaFold3 sequence contexts." width="7668" height="1786" loading="lazy"></a><figcaption>Ensemble-mean Cα–Cα distances in nm. Each map concerns the same 1–28 segment, not the dimensions of the whole construct. <a href="{{ '/images/research/p53-gsm/context/ca_distances.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Chemical-shift agreement

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/context/chemical_shifts.png' | relative_url }}" aria-label="Open full-size figure: Nucleus-specific squared Pearson correlations and RMSE for AlphaFold3 contexts against BMRB 17760."><img src="{{ '/images/research/p53-gsm/context/chemical_shifts.png' | relative_url }}" alt="Nucleus-specific squared Pearson correlations and RMSE for AlphaFold3 contexts against BMRB 17760." width="3323" height="574" loading="lazy"></a><figcaption>Ensemble-averaged absolute SPARTA predictions are compared with identical experimental assignments from BMRB 17760, separately for C′, Cα, Cβ, N, and the backbone amide proton HN. The plotted R² label denotes squared Pearson correlation (r²), not predictive R²; RMSE is in ppm. <a href="{{ '/images/research/p53-gsm/context/chemical_shifts.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Secondary-structure fractions

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/context/dssp.png' | relative_url }}" aria-label="Open full-size figure: Per-residue coil and helix fractions across the four AlphaFold3 contexts."><img src="{{ '/images/research/p53-gsm/context/dssp.png' | relative_url }}" alt="Per-residue coil and helix fractions across the four AlphaFold3 contexts." width="2810" height="1404" loading="lazy"></a><figcaption>Define Secondary Structure of Proteins (DSSP) assigns secondary structure using hydrogen-bond geometry. Coil and helix fractions are computed over all conformations; the omitted small strand populations are not renormalized away. <a href="{{ '/images/research/p53-gsm/context/dssp.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Positional variability

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/context/rmsf.png' | relative_url }}" aria-label="Open full-size figure: Per-residue Cα root-mean-square fluctuations for p53 residues 1–28, in nanometers."><img src="{{ '/images/research/p53-gsm/context/rmsf.png' | relative_url }}" alt="Per-residue Cα root-mean-square fluctuations for p53 residues 1–28, in nanometers." width="2430" height="969" loading="lazy"></a><figcaption>Root-mean-square fluctuation (RMSF), in nm, describes positional dispersion among generated conformers. It depends on preprocessing and alignment and is not a time-dependent dynamical measurement. <a href="{{ '/images/research/p53-gsm/context/rmsf.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Backbone dihedral distributions

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/context/ramachandran.png' | relative_url }}" aria-label="Open full-size figure: Normalized backbone phi and psi angle distributions for four contexts, pooled over residues 2–27."><img src="{{ '/images/research/p53-gsm/context/ramachandran.png' | relative_url }}" alt="Normalized backbone phi and psi angle distributions for four contexts, pooled over residues 2–27." width="3999" height="1102" loading="lazy"></a><figcaption>Paired backbone φ/ψ angles for residues 2–27 are normalized separately for each context using 5° × 5° bins on a shared color scale. <a href="{{ '/images/research/p53-gsm/context/ramachandran.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Interpretation

- Mean distance 1–28 increases from **3.60 nm** in TAD1/2 to **5.74–5.79 nm** in the larger contexts.
- Between TAD1/2 and full-length p53, C′ RMSE improves from **1.304 to 1.137 ppm**, whereas HN RMSE worsens from **0.423 to 0.468 ppm**. Cα RMSE changes little.
- C′ squared Pearson correlation falls from **0.692 to 0.572**, even as its RMSE improves. Association and absolute agreement are different tests. The metrics CSV also reports predictive R², which is a different quantity and may be negative.
- Mean DSSP helix fraction over residues 1–28 falls from approximately **42% to 30%** in the larger contexts. Reduced positional variability does not imply greater helicity.

## Methods and limitations

The experimental reference is [BMRB 17760](https://bmrb.io/data_library/summary/?bmrbId=17760): wild-type human p53 residues **1–93**, pH 7.4, 293 K, ionic strength 175 mM. We compare it with analyzed residues **1–28**, so this is **not construct-matched validation**. Both supplementary pilots use this entry; the primary benchmark uses BMRB 51984.

There are **124 common assignments per context**: 26 C′, 27 Cα, 27 Cβ, 22 N, and 22 HN. Experimental H maps to predicted HN; this reference has no Hα comparison. Absolute predicted shifts are averaged with equal conformer weights, without a fitted offset or random-coil subtraction.

RMSF depends on alignment. These descriptive summaries establish neither a causal mechanism, statistical significance, equilibrium populations, nor complete equilibrium sampling. They do not validate binding mechanisms or every observable, and the context trends cannot be generalized to other GSMs.

For a new disordered target, start with a small context pilot. Compare the same residue window and relevant experimental observables: a larger prediction context is not automatically better.

## Full overview figure

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/context/full_figure.png' | relative_url }}" aria-label="Open full-size figure: Composite overview of sequence-context effects on p53 residues 1–28."><img src="{{ '/images/research/p53-gsm/context/full_figure.png' | relative_url }}" alt="Composite overview of sequence-context effects on p53 residues 1–28." width="4000" height="3817" loading="lazy"></a><figcaption>AlphaFold3 contexts: TAD1/2, +PRD, +PRD+DBD, and full-length p53, with 4,950, 4,995, 4,620, and 4,419 conformations. Panels (a–d): Cα distance maps (nm); (e–h): squared Pearson correlation and RMSE (ppm); (i,j): DSSP coil and helix fractions; (k): Cα RMSF (nm); (l–o): normalized paired φ/ψ distributions. All comparisons concern the same analysis window, using BMRB 17760 for NMR. <a href="{{ '/images/research/p53-gsm/context/full_figure.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Downloads and related study

<ul class="poster-downloads"><li><a href="{{ '/files/research/p53-gsm/context/ca_distances.csv' | relative_url }}" download>ca_distances.csv</a></li><li><a href="{{ '/files/research/p53-gsm/context/chemical_shift_matches.csv' | relative_url }}" download>chemical_shift_matches.csv</a></li><li><a href="{{ '/files/research/p53-gsm/context/chemical_shift_metrics.csv' | relative_url }}" download>chemical_shift_metrics.csv</a></li><li><a href="{{ '/files/research/p53-gsm/context/dssp.csv' | relative_url }}" download>dssp.csv</a></li><li><a href="{{ '/files/research/p53-gsm/context/rmsf.csv' | relative_url }}" download>rmsf.csv</a></li></ul>


The [study dataset](https://doi.org/10.5281/zenodo.21309352) accompanies the p53 generative structure model benchmark. This does not imply that every additional website pilot asset or script is deposited there. Downloadable originals on this page are preserved unchanged; [asset checksums]({{ '/files/research/p53-gsm/asset-checksums.json' | relative_url }}) are available for verification.

**Related analysis:** [Explore the companion study]({{ '/research/p53-gsm-short-md-pipeline/' | relative_url }}).

**Study authors:** Michael Bakker, Oskar Svensson, and Marie Skepö.

**Contact:** [Michael Bakker](mailto:bakkerm@faf.cuni.cz). [Back to research]({{ '/research/' | relative_url }}).
