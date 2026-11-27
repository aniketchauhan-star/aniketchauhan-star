# Profile visuals: source

Every animated SVG in `assets/` is generated from these Python files, so you edit text here and rebuild instead of hand-editing the SVGs.

```bash
pip install fonttools brotli
python assets/source/build_all.py   # rewrites the SVGs in assets/
```

| File | What it draws |
| --- | --- |
| `hero.py` | The neon skyline banner: name, headline, hover cars, maglev, neon minar, lotus dome |
| `parts.py` | Typing strip, section headers, identity terminal, career map, skill matrix, project cards (`CARDS`), contact buttons, footer |
| `lib.py` | Shared helpers: palette, text measuring, embedded fonts, hover-car and train shapes |

- **Change your headline:** edit `role` in `hero.py`.
- **Card art:** each card's banner and pop-out sprites are WebP files in `art/` (real title screens and sprites from the games). They are embedded into the card SVG, because GitHub's image sandbox can't load external files.
- **Add a project card:** append an entry to `CARDS` in `parts.py`, then add a matching `<img>` to the main `README.md`.

The build checks every word against its font and stops with an error if a character is missing, so nothing ever renders in a fallback font.

**Fonts.** The fonts are renamed subsets of Orbitron, Share Tech Mono and Rajdhani, used under the SIL Open Font License 1.1. The licence texts are in `fonts/`.
