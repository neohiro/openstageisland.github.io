<!-- TEMPLATE-SHARED:HEADER -->
{# readme-header.html â€” used as the top of every repo README.md.

   Variables:
     org:    neohiro | fpm | osi | hplus
     title:  the repo name
     blurb:  one-line description

   Heartbeat also publishes /shared/repos/{owner}_{repo}/header.md which
   can be appended after this for project-specific badges/stats. #}

{%- assign org_label = include.org -%}
{%- case include.org -%}
{%- when 'neohiro' %}{% assign org_label = 'neohiro' %}{% when 'fpm' %}{% assign org_label = 'FrenzyPenguin Media' %}{% when 'osi' %}{% assign org_label = 'Open Stage Island' %}{% when 'hplus' %}{% assign org_label = 'transhumanists' %}{% endcase -%}

# {{ include.title }}

> {{ include.blurb }}

{% include badges.html org=include.org %}
{% include heartbeat-status.html %}
{% include sponsor-buttons.html %}
{% include contact-card.html %}

---

<!-- TEMPLATE-SHARED:FOOTER -->
{# readme-footer.html â€” used at the bottom of every repo README.md. #}

---
{% include legal-block.html %}
{% include social-links.html %}
{% include sponsor-buttons.html %}
{% include heartbeat-status.html %}

<sub>Synced from <code>template-shared/_includes/</code> â€” last publish: {{ site.time | date: '%Y-%m-%d %H:%M UTC' }}</sub>

{# readme-footer.html â€” used at the bottom of every repo README.md. #}

---
{% include legal-block.html %}
{% include social-links.html %}
{% include sponsor-buttons.html %}
{% include heartbeat-status.html %}

<sub>Synced from <code>template-shared/_includes/</code> â€” last publish: {{ site.time | date: '%Y-%m-%d %H:%M UTC' }}</sub>

