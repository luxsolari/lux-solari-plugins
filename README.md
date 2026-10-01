# Lux Solari — Claude Code Plugins

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A personal plugin marketplace for Claude Code.

## Add this marketplace

```bash
claude plugin marketplace add luxsolari/lux-solari-plugins
```

Or from inside Claude Code:

```
/plugin marketplace add luxsolari/lux-solari-plugins
```

## Available plugins

### three-axes-framework

Always-active AI development philosophy that calibrates Claude's behavior across three axes — Mastery, Consequence, and Intent — to prevent comprehension debt.

```bash
claude plugin install three-axes-framework@lux-solari-plugins
```

See [three-axes-framework](https://github.com/luxsolari/three-axes-framework) for full documentation.

### sage-instructor

Adaptive programming instructor — structured courses with discovery-first teaching, AskUserQuestion interactions, progress tracking, and pluggable curricula. Depends on `three-axes-framework` (auto-installed alongside it).

```bash
claude plugin install sage-instructor@lux-solari-plugins
```

See [sage-instructor](https://github.com/luxsolari/sage-instructor) for full documentation.

### whiting

Bootstraps a repo's whole release discipline: init the repo, enforce
Conventional Commits, derive semver bumps from commit history, and publish
GitHub Releases straight from `CHANGELOG.md`. Includes an `inspect` skill
to audit and retrofit existing repos.

```bash
claude plugin install whiting@lux-solari-plugins
```

See [whiting](https://github.com/luxsolari/whiting) for full documentation.

### lux-swiss

Lux Swiss (formerly Duotone Swiss) — one of Lux Solari's house-mark design
systems. A strict two-color palette (ink + warm cream) plus a single
blood-red accent, Swiss-minimalist layout with visible borders and no
shadows, Space Mono / Space Grotesk typography, and hand-rolled SVG charts.
Applies a consistent aesthetic to any UI work by default and ships a
ready-to-paste Tailwind 4 theme.

```bash
claude plugin install lux-swiss@lux-solari-plugins
```

See [lux-swiss](https://github.com/luxsolari/lux-swiss) for full documentation.

### hannah

F1 strategy engineer for your LLM garage: analyzes a repo, reads your
hardware, and recommends the optimal local LLM models (Ollama, MLX, and
other local-inference setups).

```bash
claude plugin install hannah@lux-solari-plugins
```

See [hannah](https://github.com/luxsolari/hannah) for full documentation.

### tri-swiss

Tri-Swiss — a tri-tone (ink + cream + Swiss Red + Pastel Turquoise highlight)
Swiss-minimalist design system built around the Geist typeface family.
Sibling to `lux-swiss` (formerly Duotone Swiss); same governance, different
palette and type identity. Ships a ready-to-paste Tailwind 4 theme and a
component catalogue.

```bash
claude plugin install tri-swiss@lux-solari-plugins
```

See [tri-swiss](https://github.com/luxsolari/tri-swiss) for full documentation.

### bauer

Evidence-backed OWASP Web and LLM security audits for authorized codebase
reviews, with source tracing, deterministic reports, and optional Jev review.
Read-only by default; executing repository code requires permission and
isolation, and each Jev packet requires consent to disclose evidence externally.
Bauer is an agent workflow, not a standalone scanner or security certification.

```bash
claude plugin install bauer@lux-solari-plugins
```

Or from inside Claude Code:

```
/plugin install bauer@lux-solari-plugins
```

Bauer v0.1.1 is a documentation-only refresh with unchanged helper behavior.
The [canonical source](https://github.com/luxsolari/bauer/tree/9870701ce5fa73cecc71a9ed2e1935eeebb8e943)
records authenticated Claude Code session-local `bauer:bauer` execution and
reads of all four helpers. That bounded, read-only audit used cached guidance,
left its frozen source unchanged, and found no new demonstrated security
vulnerability; it did not exercise an activated marketplace plugin. The
publication-wording candidate was not reproduced, and secret-pattern screening
remains best effort, not a substitute for reviewing each disclosure packet.

The catalog already follows the canonical default branch, currently verified at
`8dd9d1d5175187255398562e0381a6118896d9cf`; no catalog source change is needed.
For optional Jev, use [current credential setup](https://github.com/luxsolari/bauer/blob/8dd9d1d5175187255398562e0381a6118896d9cf/README.md#configure-your-key):
persistent terminal environment setup or the recommended 1Password launcher,
with separate GUI launch-environment requirements and approval for each packet.
This post-tag README correction changes no helper behavior or release tag;
existing installs are not automatically verified or updated by this check.

See [Bauer](https://github.com/luxsolari/bauer) for usage, requirements, and full
audit limitations, and its [releases page](https://github.com/luxsolari/bauer/releases)
for publication status. This catalog keeps the canonical GitHub default-branch
source and resolves the version from upstream `plugin.json`; it does not pin
v0.1.1 or imply a tagged release, successful hosted CI, or current installation
verification.

## Maintaining this marketplace

Each plugin's `version` here is intentionally omitted — Claude Code resolves a
plugin's version from its own `plugin.json` first, so duplicating it here
would just be a second place for the number to go stale. Update the plugin's
own repo and its version bump is picked up automatically; this file only
needs to change when a plugin is added, removed, or its `source`/`homepage`
moves.

Test changes to this catalog locally before pushing:

```bash
claude plugin validate .                                    # validates the marketplace manifest
python3 -m unittest discover -s tests -v                     # checks Bauer source and metadata
```

Optional installation smoke test (changes your local Claude configuration):

```bash
claude plugin marketplace add ./lux-solari-plugins           # add the local copy
claude plugin install <name>@lux-solari-plugins              # install a plugin from it
```
