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

Bauer v0.2.1 at canonical revision `08320e9155850cbd9b4be2f2051eb62bf4247f81` retains deterministic
Jev selection with disabled/MEDIUM defaults, explicit scheduling opt-in, complete
five-severity tables and a supplied-evidence completion/applicability gate. Five
CLI helpers plus the completion support module and 96 offline tests ship upstream.
The patch adds actual-chat preflight/closing warnings and generated JSON/Markdown
resource notes. Security audits can be token-intensive: repository tracing,
source queries, repeated evidence review and reporting can consume substantial
tokens. Usage depends on repository scope and host model; no exact estimate is
promised. Optional Jev charges are separate. If budget matters, agree on bounded
scope; unfinished mandatory checks remain partial under the continuation gate.
See [token guidance](https://github.com/luxsolari/bauer/blob/08320e9155850cbd9b4be2f2051eb62bf4247f81/README.md#token-usage).
Run report.py for both gate formats; completion.py has no standalone CLI. A separate boolean-only
helper-environment preflight proactively offers all eligible reviews when a key
is present; final packet approval remains separate from scheduling and key presence.
Actual Claude session-local plugin and Codex local-skill synthetic checks verified
queues, final count tables and present/absent preflight behavior without TypeSafe
requests. Corrected-helper eligible-offer exercises used dummy-only presence
and stopped for consent; no post-consent API transmission was tested. The gate
validates supplied records, not source truth. These are not fresh feed audits or
activated marketplace tests.
Current installation is not established by the catalog checks.

The catalog already follows `{"source":"github","repo":"luxsolari/bauer"}`;
source and metadata remain unchanged. It resolves version 0.2.1 from the canonical
manifest, not a duplicated catalog version or fixed tag. See [current setup](https://github.com/luxsolari/bauer/blob/08320e9155850cbd9b4be2f2051eb62bf4247f81/README.md#configure-your-key)
and [release status](https://github.com/luxsolari/bauer/releases). Earlier release
tags and historical limitations are preserved.

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
