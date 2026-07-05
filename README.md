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

### lux-design-system

Duotone Swiss — Lux Solari's house design language. A strict two-color palette
(ink + warm cream) plus a single blood-red accent, Swiss-minimalist layout with
visible borders and no shadows, Space Mono / Space Grotesk typography, and
hand-rolled SVG charts. Applies a consistent aesthetic to any UI work by default
and ships a ready-to-paste Tailwind 4 theme.

```bash
claude plugin install lux-design-system@lux-solari-plugins
```

See [lux-design-system](https://github.com/luxsolari/lux-design-system) for full documentation.

## Maintaining this marketplace

Each plugin's `version` here is intentionally omitted — Claude Code resolves a
plugin's version from its own `plugin.json` first, so duplicating it here
would just be a second place for the number to go stale. Update the plugin's
own repo and its version bump is picked up automatically; this file only
needs to change when a plugin is added, removed, or its `source`/`homepage`
moves.

Test changes to this catalog locally before pushing:

```bash
claude plugin validate .                                    # checks marketplace.json syntax
claude plugin marketplace add ./lux-solari-plugins           # add the local copy
claude plugin install <name>@lux-solari-plugins              # install a plugin from it
```
