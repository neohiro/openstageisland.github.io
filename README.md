# Open Stage Island

> A free, 24/7 open-air music stage in Second Life.

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
[![ Jekyll](https://img.shields.io/badge/Jekyll-4.4-blueviolet.svg)](https://jekyllrb.com/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-openstageisland.github.io-brightgreen)](https://openstageisland.github.io)

**Open Stage Island** is a free, 24/7 open-air music venue in Second Life's Derwent
region. Any electronic music artist can take the stage and play to a live audience —
no booking, no fee.

**Live site:** [openstageisland.github.io](https://openstageisland.github.io)

---

## Features

- **24/7 Open Air Stage** — Available to all electronic music artists, anytime.
- **DJ School** — Learn from experienced DJs and improve your skills.
- **Freebies** — Discover free items and interactive experiences.
- **Social Hub** — Make friends and connect with the community.
- **LGBTQI+ Friendly** — A safe and welcoming space for everyone.
- **Furry Friendly** — Anthro and furry avatars are warmly welcomed.

---

## How to visit

Teleport directly to the stage:

```
secondlife://Derwent/248/128/22
```

Or use the web map:

- [Second Life Maps](https://maps.secondlife.com/secondlife/Derwent/248/128/22)
- [Official Destination Page](https://secondlife.com/destination/open-stage-island)

**Region:** Derwent | **Coordinates:** 248 / 128 / 22 | **Maturity:** Moderate

---

## Repository structure

```
openstageisland.github.io/
├── _includes/      # Shared Jekyll includes
├── _layouts/       # Page layouts
├── assets/         # CSS, JS, images
├── heartbeats/     # Heart cadence signals
├── images/         # Hero and gallery images
├── data.json       # Structured venue data
├── index.md        # Homepage source
└── README.md       # This file
```

---

## Contributing

Want to contribute to the venue or report an issue?

1. Open an issue describing the suggestion or problem
2. For venue feedback, reach out in-world
3. For Second Life-specific bugs, include region name and coordinates

---

## Development

This site is built with [Jekyll](https://jekyllrb.com/). Dependencies are
managed via `Bundler` and declared in `Gemfile`. **No `Gemfile.lock` is
committed** — GitHub Actions installs gems fresh on each CI run using the
pessimistic constraints in `Gemfile`.

To preview locally:

```bash
gem install bundler
bundle install
bundle exec jekyll serve --livereload
```

CI builds the site with `bundle exec jekyll build` and deploys via the
`deploy-pages` action. A local build is **required before opening a PR** —
the CI validation step runs the full Jekyll build and will surface any Liquid
errors, missing includes, or plugin issues before merge.

---

## Sister sites

- [neohiro](https://neohiro.github.io) — Security hardening & privacy tools
- [FrenzyPenguin Media](https://frenzypenguin-media.github.io) — Video deep-dives on security
- [transhumanists](https://transhumanists.github.io) — Transhumanism & human enhancement

---

## License

CC BY-SA 4.0 — see [LICENSE](LICENSE).
