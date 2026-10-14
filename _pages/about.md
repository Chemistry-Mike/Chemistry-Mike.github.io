---
layout: showcase
home: true
title: Michael Bakker — Bioinformatics & Pharmaceuticals
permalink: /
excerpt: Exploring protein dynamics, molecular recognition, and human disease through bioinformatics and pharmaceutical modeling.
redirect_from:
  - /about/
  - /about.html
---
<section class="hero" aria-labelledby="home-title">
  <div class="hero-copy">
    <p class="eyebrow hero-identity">Michael Bakker · Bioinformatics & Pharmaceuticals</p>
    <h1 id="home-title">Understanding proteins<br><em>in motion.</em></h1>
    <p class="lede">I combine molecular simulations, quantum chemistry, and machine learning to investigate how protein dynamics shape biological function and disease.</p>
    <p class="hero-affiliation">Postdoctoral researcher · Charles University, Czech Republic</p>
    <div class="actions">
      <a class="action" href="{{ '/research/' | relative_url }}">Explore Research →</a>
      <a class="action secondary" href="{{ '/publications/' | relative_url }}">View Publications</a>
    </div>
  </div>
  <figure class="hero-art">
    <img src="{{ '/images/NewMainImage.png' | relative_url }}" alt="Protein ribbon visualization with highlighted helices and a bound molecule" width="1181" height="1261" fetchpriority="high">
    <figcaption>Exploring the unexplored regions of pharmacology.</figcaption>
  </figure>
</section>

<div class="discipline-strip" aria-label="Research interests">
  <span>Pharmaceutical Modeling</span><span>Disordered Proteins</span><span>Machine Learning</span><span>Peptidomimetics</span>
</div>

<section class="home-section" aria-labelledby="themes-title">
  <div class="section-heading">
    <div><p class="eyebrow">Research focus</p><h2 id="themes-title">Three main projects.<br>One pharmaceutical focus.</h2></div>
    <p>My current researches focuses on the areas of pharmacology which are either unattainable or unresolved in current research by focusing on the dark proteome, peptidomimetics and orphan nuclear receptors.</p>
  </div>
  <div class="theme-grid">
    {% for theme in site.data.research %}
    <a class="theme-card theme-card-illustrated" href="{{ '/research/' | relative_url }}#{{ theme.title | slugify }}">
      <div class="theme-illustration"><img src="{{ '/images/' | append: theme.image | relative_url }}" alt="" loading="lazy"></div>
      <div class="theme-copy"><h3>{{ theme.title }}</h3><p>{{ theme.description }}</p><span class="text-link">Explore the research →</span></div>
    </a>
    {% endfor %}
  </div>
</section>

<section class="featured-story home-section" aria-labelledby="p53-title">
  <figure class="story-figure">
    <img src="{{ '/images/P53-C.png' | relative_url }}" alt="Molecular illustration of the p53 pre-tetramerization loop" loading="lazy">
    <figcaption>The pre-tetramerization loop: a flexible region of p53.</figcaption>
  </figure>
  <div class="story-copy">
    <p class="eyebrow">Featured research · p53</p>
    <h2 id="p53-title">What can a flexible<br>protein region tell us?</h2>
    <p>My p53 research asks how the context around a disordered region changes the structures it can adopt, and how phosphorylation influences its dynamics.</p>
    <p>Using molecular dynamics simulations, we investigate how neighboring domains constrain the pre-tetramerization loop. Comparing these simulated ensembles with experimental NMR chemical shifts helps assess how well the models capture its behavior.</p>
    <a class="action secondary" href="{{ '/portfolio/P7-P53/' | relative_url }}">Explore the p53 project →</a>
    <div class="story-papers" aria-label="Related p53 publications">
      <span class="eyebrow">Related papers</span>
      <a href="{{ '/publication/2024-JCTC-Expansion' | relative_url }}">Domain context & conformational dynamics →</a>
      <a href="{{ '/publication/2024-JCTC-PTM' | relative_url }}">Phosphorylation of the regulatory domain →</a>
    </div>
  </div>
</section>

<section class="home-section" aria-labelledby="papers-title">
  <div class="section-heading">
    <div><p class="eyebrow">Selected work</p><h2 id="papers-title">From simulations<br>to published insights.</h2></div>
    <a class="text-link" href="{{ '/publications/' | relative_url }}">All publications →</a>
  </div>
  {% assign selected = '2025-Biophys-Tau,2024-JCIM-Clustering,2022-PCCP-ADMA' | split: ',' %}
  {% for id in selected %}{% for paper in site.publications %}{% if paper.path contains id %}{% include publication-row.html paper=paper %}{% endif %}{% endfor %}{% endfor %}
</section>

<section class="home-section" aria-labelledby="writing-title">
  <div class="section-heading">
    <div><p class="eyebrow">Notes from the workflow</p><h2 id="writing-title">Writing & tools.</h2></div>
    <a class="text-link" href="{{ '/writing/' | relative_url }}">Browse writing and tools →</a>
  </div>
  <div class="theme-grid">
    {% for post in site.posts limit:2 %}
    <article class="note-card"><p class="eyebrow">{{ post.date | date: '%B %Y' }}</p><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><a class="text-link" href="{{ post.url | relative_url }}">Read article →</a></article>
    {% endfor %}
    <article class="note-card tool-spotlight"><p class="eyebrow">PyMOL · Visualization tools</p><h3>Give your prolines<br>some style.</h3><p>Explore the visualization guide and download the accompanying PyMOL script.</p><div class="tool-spotlight-links"><a class="text-link" href="{{ '/posts/2025/10/FancyProlines/' | relative_url }}">Read the guide →</a><a class="text-link" href="{{ '/PyMolScripts/fancyProlines.py' | relative_url }}" download>Download script ↓</a></div></article>
  </div>
</section>

<section class="contact-panel personal-closing" aria-labelledby="contact-title">
  <img class="contact-portrait" src="{{ '/images/ConferenceImage2.png' | relative_url }}" alt="Michael Bakker" width="160" height="160" loading="lazy">
  <div>
    <p class="eyebrow">Michael Bakker · Ph.D.</p>
    <h2 id="contact-title">Let’s connect.</h2>
    <p>I’m a postdoctoral researcher at Charles University in the Czech Republic. Interested in protein dynamics or computational chemistry? Get in touch to discuss ideas and potential collaborations.</p>
    <div class="actions"><a class="action" href="mailto:{{ site.author.email }}">Get in touch ↗</a><a class="action secondary" href="{{ '/cv/' | relative_url }}">About me & CV →</a></div>
  </div>
</section>
