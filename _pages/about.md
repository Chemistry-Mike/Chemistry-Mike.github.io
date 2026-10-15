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
    <div><p class="eyebrow">Research focus</p><h2 id="themes-title">Three unexplored paths.<br>One concentric goal.<br><strong>Explore the Unexplored.</strong></h2></div>
    <p>My research focuses on less-explored areas of pharmacology: diving into the dark proteome through intrinsically disordered proteins, seeking matches for orphan nuclear receptors, and devising new therapeutic strategies by mimicking protein interactions through peptidomimetics.</p>
  </div>
  <div class="theme-grid home-project-grid">
    {% for theme in site.data.research %}
    <a class="theme-card theme-card-illustrated" href="{{ '/research/' | relative_url }}#{{ theme.title | slugify }}">
      <div class="theme-illustration"><img src="{{ '/images/' | append: theme.image | relative_url }}" alt="" loading="lazy"></div>
      <div class="theme-copy"><h3>{{ theme.title }}</h3><p>{{ theme.description }}</p><span class="text-link">Explore the research →</span></div>
    </a>
    {% endfor %}
  </div>
</section>

<section class="contact-panel personal-closing" aria-labelledby="contact-title">
  <img class="contact-portrait" src="{{ '/images/ConferenceImage2.png' | relative_url }}" alt="Michael Bakker" width="320" height="320" loading="lazy">
  <div>
    <p class="eyebrow">Michael Bakker · B.Sc., M.Sc., Ph.D.</p>
    <h2 id="contact-title">Let’s connect.</h2>
    <p>I’m a postdoctoral researcher at Charles University in the Czech Republic, with ongoing collaborations with researchers in Germany, Sweden, and the United States. Interested in bioinformatics, pharmaceutical modeling, or protein dynamics? Get in touch to discuss ideas and potential collaborations.</p>
    <div class="actions"><a class="action" href="mailto:{{ site.author.email }}">Get in touch ↗</a><a class="action secondary" href="{{ '/cv/' | relative_url }}">About me & CV →</a></div>
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
