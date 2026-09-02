# Contributing to FableBridge

Thanks for helping improve FableBridge.

## Principles

Contributions should preserve four properties:

1. **Honest claims** — never imply an instruction file transfers model intelligence or proprietary capabilities.
2. **Portable behavior** — prefer rules that make sense across coding-agent harnesses.
3. **Small surface area** — V0.x should stay easy to read, install, audit, and remove.
4. **Verifiability** — generated adapters must remain deterministic and tests must describe observable behavior.

## Development

Requires Python 3.9+ and no third-party packages.

```bash
python scripts/render.py --check
python -m unittest discover -s tests -v
```

If you intentionally change `FABLE51.md`, regenerate adapters:

```bash
python scripts/render.py
```

Then run the checks again.

## Adding an adapter

An adapter should:

- use the host agent's documented repository-instruction location;
- preserve the canonical behavior profile without adding model-equivalence claims;
- have deterministic rendering support in `scripts/render.py`;
- have an installer mapping in `scripts/install.py` when installation can be done safely;
- never silently overwrite an existing user file.

## Sources

If a contribution attributes a behavior specifically to Fable 5.1, add a public primary source to `docs/behavior-sources.md`. General engineering guidance should be labeled as FableBridge-added rather than attributed to Anthropic.
