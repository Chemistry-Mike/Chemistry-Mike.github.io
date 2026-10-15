---
layout: showcase
title: Publications
kicker: Peer-reviewed research
permalink: /publications/
nav_section: Publications
description: Research spanning molecular dynamics, NMR prediction, protein interactions, computational chemistry, educational models, pharmaceutical delivery, and applications of machine learning across disciplines.
---
{% include publication-metrics.html %}
<p class="publication-legend"><span class="first-author-star" aria-hidden="true">&#9733;</span> First-author publication</p>
{% assign papers = site.publications | sort: 'date' | reverse %}
{% for paper in papers %}{% include publication-row.html paper=paper %}{% endfor %}
