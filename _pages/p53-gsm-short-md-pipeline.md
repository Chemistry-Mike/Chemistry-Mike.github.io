---
layout: showcase
title: "What short restrained processing changes in generative p53 ensembles"
kicker: p53 conference poster · Supplementary analysis
page_class: poster-study
nav_section: Research
permalink: /research/p53-gsm-short-md-pipeline/
description: "A six-model exploratory pilot of reconstruction, restrained minimization, and short molecular dynamics for p53 residues 1\u201328."
---
<p class="poster-back"><a href="{{ '/research/' | relative_url }}">← Back to research</a></p>
<p class="poster-study-status">Exploratory supplementary pilot · Benchmark manuscript resubmitted</p>
## Short answer

Reconstruction followed by restrained minimization and short molecular dynamics (MD) changed chemical-shift agreement substantially. Backbone amide-proton (HN) error decreased across all six generative structure models (GSMs), while heavy-atom responses were mixed. This processing-sensitivity pilot is **not a universally validated refinement method** or a substitute for independent experimental validation.

## The processing workflow

<ol class="poster-workflow">
<li>GSM coordinates</li><li>Backbone extraction</li><li>PULCHRA reconstruction</li><li>Hydrogen addition</li><li>Restrained minimization</li><li>100 ps restrained MD</li><li>Evaluation</li>
</ol>

The source script selects MDTraj `backbone` atoms. **No new coarse-grained (CG) simulation precedes this reconstruction**, and this is not a controlled Cα-only ablation. It is related to, but distinct from, the CALVADOS CG reconstruction pipeline: this six-GSM pilot starts from generated coordinates. The primary benchmark's GSM structures were not minimized or relaxed.

## Processing conditions

- OpenMM with `amber14-all.xml` (AMBER ff14SB protein parameters).
- **Vacuum**, no nonbonded cutoff, and hydrogen-bond constraints.
- Energy minimization: a maximum of **500 iterations**.
- Langevin-middle dynamics at **300 K**, friction **1 ps⁻¹**, timestep **2 fs**, **50,000 steps (100 ps)**.
- Cα restraints to each input conformation use `k × [(x−x₀)² + (y−y₀)² + (z−z₀)²]`, with **k = 1000 kJ mol⁻¹ nm⁻²**. Finite restraints limit motion; they do not mathematically fix backbone coordinates.

These conditions are not explicit-solvent or physiological sampling, full equilibration, or a guarantee against compaction artifacts.

## NMR agreement before and after processing

Nuclear magnetic resonance (NMR) predictions are compared using root-mean-square error (RMSE), in parts per million (ppm). Values below come directly from the exact heatmap TSV, using identical residue/atom assignments across methods and states. “Processed” corresponds to “Relaxed” in the supplied tables and figures.

<div class="poster-table-scroll" role="region" aria-label="HN and Cα errors: original versus full processing pipeline" tabindex="0"><table data-poster-table="pipeline-errors"><caption>HN and Cα errors: original versus full processing pipeline</caption><thead><tr><th scope="col">Model</th><th scope="col">HN original (ppm)</th><th scope="col">HN processed (ppm)</th><th scope="col">Cα original (ppm)</th><th scope="col">Cα processed (ppm)</th></tr></thead><tbody><tr><th scope="row">AlphaFold3</th><td>0.453</td><td>0.268</td><td>0.718</td><td>1.477</td></tr><tr><th scope="row">Boltz-2x</th><td>0.445</td><td>0.245</td><td>0.687</td><td>1.529</td></tr><tr><th scope="row">AlphaFlow</th><td>0.441</td><td>0.183</td><td>0.574</td><td>0.848</td></tr><tr><th scope="row">BioEmu</th><td>1.271</td><td>0.150</td><td>1.031</td><td>0.800</td></tr><tr><th scope="row">idpSAM</th><td>0.233</td><td>0.210</td><td>0.563</td><td>0.551</td></tr><tr><th scope="row">IDPFold</th><td>1.077</td><td>0.185</td><td>1.375</td><td>1.212</td></tr></tbody></table></div>

## Chemical-shift agreement

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/pipeline/nmr_heatmap_v11.png' | relative_url }}" aria-label="Open full-size figure: Before-and-after squared Pearson correlations and RMSE by nucleus for six generative models."><img src="{{ '/images/research/p53-gsm/pipeline/nmr_heatmap_v11.png' | relative_url }}" alt="Before-and-after squared Pearson correlations and RMSE by nucleus for six generative models." width="3600" height="3279" loading="lazy"></a><figcaption>Ensemble-averaged SPARTA+ predictions against BMRB 17760. R² labels mean squared Pearson correlation (r²), not predictive R². RMSE is in ppm. Heavy nuclei are Cβ, Cα, C′, and N; the proton comparison is HN. Each method and state uses the same 124 matched assignments. <a href="{{ '/images/research/p53-gsm/pipeline/nmr_heatmap_v11.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Positional dispersion

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/pipeline/rmsf_comparison_v8.png' | relative_url }}" aria-label="Open full-size figure: Cα root-mean-square fluctuation profiles before and after processing for all six models, in angstroms."><img src="{{ '/images/research/p53-gsm/pipeline/rmsf_comparison_v8.png' | relative_url }}" alt="Cα root-mean-square fluctuation profiles before and after processing for all six models, in angstroms." width="2200" height="3756" loading="lazy"></a><figcaption>Root-mean-square fluctuation (RMSF) describes per-residue Cα dispersion among aligned conformers, in Å. Original profiles are solid; processed profiles use dotted lines and circles. This is not motion along one continuous trajectory. <a href="{{ '/images/research/p53-gsm/pipeline/rmsf_comparison_v8.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Backbone geometry

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/pipeline/ramachandran_v8.png' | relative_url }}" aria-label="Open full-size figure: Normalized original and processed backbone phi and psi distributions for six models."><img src="{{ '/images/research/p53-gsm/pipeline/ramachandran_v8.png' | relative_url }}" alt="Normalized original and processed backbone phi and psi distributions for six models." width="7200" height="2760" loading="lazy"></a><figcaption>Normalized backbone φ/ψ distributions before and after the full processing pipeline. Pooled distributions cannot establish residue-specific stability or unchanged populations. <a href="{{ '/images/research/p53-gsm/pipeline/ramachandran_v8.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Structural sample counts

The following counts apply to the RMSF comparison in this pilot. They are not the primary benchmark’s replenished 1,000-structure counts. Original and processed ensembles can differ in membership; equal counts do not establish frame pairing.

<div class="poster-table-scroll" role="region" aria-label="Structural conformer counts used in the RMSF comparison" tabindex="0"><table data-poster-table="pipeline-counts"><caption>Structural conformer counts used in the RMSF comparison</caption><thead><tr><th scope="col">Model label</th><th scope="col">Original conformers</th><th scope="col">Processed conformers</th></tr></thead><tbody><tr><th scope="row">AF3</th><td>1002</td><td>1000</td></tr><tr><th scope="row">Boltz</th><td>1148</td><td>1148</td></tr><tr><th scope="row">AlphaFlow</th><td>1000</td><td>1000</td></tr><tr><th scope="row">BioEmu</th><td>960</td><td>959</td></tr><tr><th scope="row">idpSAM</th><td>1000</td><td>998</td></tr><tr><th scope="row">IDPFold</th><td>3000</td><td>2998</td></tr></tbody></table></div>

## What changed?

HN errors decreased for all six models, particularly BioEmu and IDPFold. Cα RMSE increased for AlphaFold3 and Boltz-2x, demonstrating why improved proton agreement does not establish uniform improvement.

Mean absolute residue-wise RMSF changes were approximately **0.035–0.121 Å** across methods; the largest single change was approximately **0.270 Å**. These are limited changes in positional dispersion, not proof that every structural feature was preserved. The Ramachandran plots retain the main populated regions without establishing unchanged populations.

## Interpretation and limitations

This comparison tests reconstruction, hydrogen addition, minimization, and restrained MD **together**. Improvements cannot be assigned solely to short MD or model architecture. Incomplete original atomic representations, particularly for IDPFold, allow reconstruction and protonation to contribute substantially.

The experimental reference, [BMRB 17760](https://bmrb.io/data_library/summary/?bmrbId=17760), measures wild-type p53 residues **1–93**, whereas the modeled/analyzed fragments contain **1–28**. This is not construct-matched validation. The reference conditions are pH 7.4, 293 K, and ionic strength 175 mM; the primary benchmark instead uses BMRB 51984.

Chemical shifts use equal conformer weights and no fitted referencing offset. The common assignment set totals **124**: 27 Cβ, 27 Cα, 26 C′, 22 N, and 22 HN. These are residue/atom assignments, **not conformer counts**. Missing Hα assignments are not imputed. Squared Pearson correlation measures association and differs from predictive R²; nuclei are not pooled into one score.

There are no uncertainty intervals or significance tests establishing universal improvement. Neither HN agreement nor a stable-looking RMSF profile demonstrates full ensemble accuracy, equilibrium populations, binding mechanisms, or complete equilibration. Original and processed structural samples are not assumed to be frame-paired.

Assess reconstruction, filtering, and relaxation together against relevant observables. An improvement for one nucleus motivates further validation; it is not a universal method ranking or a validated production pipeline.

## Full overview figure

<figure class="poster-figure"><a href="{{ '/images/research/p53-gsm/pipeline/final_figure_v4.png' | relative_url }}" aria-label="Open full-size figure: Composite overview of NMR agreement, RMSF, and dihedral distributions before and after restrained processing."><img src="{{ '/images/research/p53-gsm/pipeline/final_figure_v4.png' | relative_url }}" alt="Composite overview of NMR agreement, RMSF, and dihedral distributions before and after restrained processing." width="7200" height="6527" loading="lazy"></a><figcaption>Effects of reconstruction and restrained processing on generated p53 residues 1–28. Panels (a–h): squared Pearson correlation and uncalibrated RMSE (ppm) against BMRB 17760; (i–k): original solid and processed dotted/circle Cα RMSF profiles (Å); (l–q): normalized backbone φ/ψ distributions. AF3 means AlphaFold3. The full processing includes reconstruction, hydrogen addition, minimization, and short restrained vacuum MD. <a href="{{ '/images/research/p53-gsm/pipeline/final_figure_v4.png' | relative_url }}">Open full-size figure</a></figcaption></figure>

## Downloads and related study

<ul class="poster-downloads"><li><a href="{{ '/files/research/p53-gsm/pipeline/nmr_before_after_alignment.tsv' | relative_url }}" download>nmr_before_after_alignment.tsv</a></li><li><a href="{{ '/files/research/p53-gsm/pipeline/nmr_before_after_changes.tsv' | relative_url }}" download>nmr_before_after_changes.tsv</a></li><li><a href="{{ '/files/research/p53-gsm/pipeline/nmr_before_after_metadata.json' | relative_url }}" download>nmr_before_after_metadata.json</a></li><li><a href="{{ '/files/research/p53-gsm/pipeline/nmr_before_after_metrics.tsv' | relative_url }}" download>nmr_before_after_metrics.tsv</a></li><li><a href="{{ '/files/research/p53-gsm/pipeline/nmr_heatmap_data_v11.tsv' | relative_url }}" download>nmr_heatmap_data_v11.tsv</a></li><li><a href="{{ '/files/research/p53-gsm/pipeline/ramachandran_summary_v1.tsv' | relative_url }}" download>ramachandran_summary_v1.tsv</a></li><li><a href="{{ '/files/research/p53-gsm/pipeline/rmsf_alignment_v2.tsv' | relative_url }}" download>rmsf_alignment_v2.tsv</a></li><li><a href="{{ '/files/research/p53-gsm/pipeline/rmsf_plot_data_v2.tsv' | relative_url }}" download>rmsf_plot_data_v2.tsv</a></li></ul>


The [study dataset](https://doi.org/10.5281/zenodo.21309352) accompanies the p53 generative structure model benchmark. This does not imply that every additional website pilot asset or script is deposited there. Downloadable originals on this page are preserved unchanged; [asset checksums]({{ '/files/research/p53-gsm/asset-checksums.json' | relative_url }}) are available for verification.

**Related analysis:** [Explore the companion study]({{ '/research/p53-gsm-sequence-context/' | relative_url }}).

**Study authors:** Michael Bakker, Oskar Svensson, and Marie Skepö.

**Contact:** [Michael Bakker](mailto:bakkerm@faf.cuni.cz). [Back to research]({{ '/research/' | relative_url }}).
