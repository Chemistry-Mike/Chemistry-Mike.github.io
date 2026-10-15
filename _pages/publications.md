---
layout: showcase
title: Publications
kicker: Peer-reviewed research
permalink: /publications/
nav_section: Publications
description: Research spanning molecular dynamics, NMR prediction, protein interactions, computational chemistry, educational models, pharmaceutical delivery, and applications of machine learning across disciplines.
---
<p><a class="text-link" href="{{ site.author.googlescholar }}">View my Google Scholar profile ↗</a></p>
{% assign papers = site.publications | sort: 'date' | reverse %}
{% for paper in papers %}{% include publication-row.html paper=paper %}{% endfor %}
