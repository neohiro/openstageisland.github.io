import re, json, os, sys

errors = 0
def check(name, cond):
    global errors
    status = 'OK  ' if cond else 'FAIL'
    if not cond: errors += 1
    print(f'{status} {name}')

html = open('index.html', encoding='utf-8').read()

# Core invariants
check('doctype', re.search(r'<!DOCTYPE html>', html, re.I))
check('lang-attr', re.search(r'<html\s+lang="en"', html))
check('has-title', re.search(r'<title>[^<]+</title>', html))
check('has-meta-description', re.search(r'name="description"', html))
check('og-image-absolute', re.search(r'property="og:image"\s+content="https?://', html))
check('twitter-image-absolute', re.search(r'name="twitter:image"\s+content="https?://', html))
check('og-image-dimensions', re.search(r'og:image:width.*657', html, re.S))
check('theme-color-light', re.search(r'theme-color.*prefers-color-scheme:\s*light', html))
check('theme-color-dark', re.search(r'theme-color.*prefers-color-scheme:\s*dark', html))
check('color-scheme-both', re.search(r'color-scheme.*light\s+dark', html))
check('canonical', re.search(r'rel="canonical"', html))
check('no-dead-data-protocol', 'data-protocol=' not in html)
check('hero-img-actual-dims', re.search(r'width="657"\s+height="394"', html))
check('hero-fetchpriority', re.search(r'fetchpriority="high"', html))
check('sections-balanced', html.count('<section') == html.count('</section>'))
check('dl-balanced', html.count('<dl') == html.count('</dl>'))
check('dt-balanced', html.count('<dt>') == html.count('</dt>'))
check('dd-balanced', html.count('<dd>') == html.count('</dd>'))
check('aside-balanced', html.count('<aside') == html.count('</aside>'))

# Intro card
check('intro-card-is-section', re.search(r'<section[^>]+class="[^"]*intro-card[^"]*"', html))
check('intro-card-aria', 'aria-labelledby="intro-heading"' in html)
check('intro-card-aria-target', 'id="intro-heading"' in html)
check('intro-card-inside-main', re.search(r'<main[^>]*>\s*<section[^>]+class="[^"]*intro-card', html, re.S))
check('no-aside-intro', '<aside class="intro-card"' not in html)
check('join-cta-exists', 'https://join.secondlife.com/' in html)
check('join-cta-themed-class', 'class="cta-button cta-themed"' in html)
check('join-cta-rel-noopener', 'href="https://join.secondlife.com/"' in html and 'rel="noopener"' in html)
check('description-mentions-take-the-stage', 'take the stage' in html.lower())
check('description-no-booking-no-fee', 'no booking' in html.lower() and 'no fee' in html.lower())
check('cta-themed-icon-is-svg', re.search(r'<svg[^>]+class="cta-themed-icon"', html))
check('cta-themed-icon-aria-hidden', 'aria-hidden="true"' in html)
check('cta-themed-icon-focusable-false', 'focusable="false"' in html)
check('no-unicode-music-glyph', '&#9836;' not in html and '&#9834;' not in html and '&#9835;' not in html)
check('terminology-consistent-second-life', html.count('Second Life') >= 4 and 'Teleport in SL' not in html)
check('meta-description-under-160', 0 < len(re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html).group(1)) <= 160)

# NEW: og:description should be longer than meta (community line)
meta_desc = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html).group(1)
og_desc = re.search(r'property="og:description"\s+content="([^"]+)"', html).group(1)
check('og-desc-longer-than-meta', len(og_desc) > len(meta_desc))

# NEW: footer button row links exist
check('footer-privacy-link', 'href="https://neohiro.github.io/privacy/"' in html)
check('footer-tos-link', 'href="https://neohiro.github.io/tos/"' in html)

# CSS
css = open('assets/style.css', encoding='utf-8').read()
check('css-intro-card-styles', '.intro-card' in css)
check('css-intro-heading', '.intro-heading' in css)
check('css-intro-text', '.intro-text' in css)
check('css-cta-themed', '.cta-themed' in css)
check('css-cta-themed-icon', '.cta-themed-icon' in css)
check('css-stage-color-token', '--color-stage' in css)
check('css-braces-balanced', css.count('{') == css.count('}'))
check('css-cta-themed-base-no-decoration', re.search(r'\.cta-themed\s*\{[^}]*text-decoration:\s*none', css, re.S))
check('css-cta-themed-focus-contrast', '#b8860b' in css or 'outline:\s*3px\s+solid\s+[^#]' in css)
check('css-dark-intro-shadow', re.search(r'prefers-color-scheme:\s*dark[\s\S]{0,400}\.intro-card[\s\S]{0,200}box-shadow', css))
check('css-focus-token-comment', 'color-focus' in css and 'NOTE' in css)
check('css-no-emoji-font-fallback', '.cta-themed-icon' in css and 'flex-shrink' in css)

# NEW: glide animation styles
check('css-glide-track', '.glide-track' in css)
check('css-glide-rail', '.glide-rail' in css)
check('css-glide-card', '.glide-card' in css)
check('css-glide-animation', '@keyframes glide' in css)
check('css-reduced-motion-glide', 'prefers-reduced-motion: reduce' in css and 'animation: none' in css)
check('css-glide-mask', 'mask-image' in css or '-webkit-mask-image' in css)
check('css-glide-hover-pause', 'animation-play-state: paused' in css)

# NEW: footer button row
check('css-footer-button-row', '.footer-button-row' in css)

# JSON
data = json.load(open('data.json', encoding='utf-8'))
check('json-valid', True)
check('json-tagline', 'tagline' in data and '24/7' in data.get('tagline', ''))
check('json-join-url', data.get('join_url') == 'https://join.secondlife.com/')

# README
readme = open('README.md', encoding='utf-8').read()
check('readme-join-link', 'join.secondlife.com' in readme)
check('readme-tagline-aligned', 'free, 24/7' in readme)
check('readme-no-contradiction', 'belong to their respective owners' not in readme)
check('readme-mit-link', 'MIT License' in readme and 'LICENSE' in readme)

# Asset refs
local_refs = set()
for ref in re.findall(r'(?:href|src)="([^"#?][^"]*)"', html + readme):
    if ref.startswith(('http://', 'https://', '//', 'secondlife://', 'mailto:', 'data:')):
        continue
    base = ref.split('#', 1)[0].split('?', 1)[0]
    if base:
        local_refs.add(base)
broken = [r for r in local_refs if not os.path.exists(r)]
check('all-local-assets-exist', not broken)
if broken:
    print(f'  broken: {broken}')

# Workflow
y = open('.github/workflows/ci.yml', encoding='utf-8').read()
check('yaml-no-tabs', '\t' not in y)
check('yaml-permissions-block', 'permissions:' in y and 'id-token: write' in y)
check('yaml-uses-checkout-v5', 'actions/checkout@v5' in y)
check('yaml-uses-configure-pages-v5', 'actions/configure-pages@v5' in y)
check('yaml-uses-upload-pages-v4', 'actions/upload-pages-artifact@v4' in y)
check('yaml-uses-deploy-pages-v4', 'actions/deploy-pages@v4' in y)
check('yaml-has-environment', 'environment:' in y and 'github-pages' in y)
check('yaml-set-euo', 'set -euo pipefail' in y)
check('yaml-globstar', 'globstar' in y)
check('yaml-has-asset-ref-check', 'Validate internal links' in y)
check('yaml-no-silent-htmlhint', 'htmlhint' not in y)
check('yaml-html-title-check', '<title>' in y)
check('yaml-section-balance', '<section' in y and '</section>' in y)

print(f'\nTotal failures: {errors}')
sys.exit(1 if errors else 0)