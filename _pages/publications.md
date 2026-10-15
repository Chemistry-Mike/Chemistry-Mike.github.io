---
layout: showcase
title: Publications
kicker: Peer-reviewed research
permalink: /publications/
nav_section: Publications
description: Research spanning molecular modeling, protein interactions, NMR prediction, pharmaceutical delivery, and quantitative analysis.
---
<p><a class="text-link" href="{{ site.author.googlescholar }}">View my Google Scholar profile ↗</a></p>
{% assign papers = site.publications | sort: 'date' | reverse %}
{% for paper in papers %}{% include publication-row.html paper=paper %}{% endfor %}
