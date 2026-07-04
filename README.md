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

### changelog-releases-assistant

Sets up GitHub Release automation driven by a repo's `CHANGELOG.md`: push a
version tag, get a Release whose body is pulled straight from the matching
changelog section — no manual release-notes writing.

```bash
claude plugin install changelog-releases-assistant@lux-solari-plugins
```

See [changelog-releases-assistant](https://github.com/luxsolari/changelog-releases-assistant) for full documentation.

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
