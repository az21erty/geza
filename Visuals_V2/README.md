# THE MOROCCO EQUATION - Visual Package V2

Figure-by-figure revision of eight exhibits. The original figures in `/figures/` are **left
untouched**; every revised exhibit lives here under its own folder.

## Visual identity (all figures)
- Background: **white**
- Primary: **dark green** `#1B4332`
- Secondary: **dark grey** `#3D3D3D`
- Accent: **muted gold** `#B8860B`
- Type: clean sans-serif (DejaVu Sans), generous spacing, no chartjunk, 300 dpi.
- Shared style module: `_style/me_style.py` (palette, title block, source line, and an automated
  label-overlap checker used as a "no overlapping labels" gate).

## Contents (each folder)
- `build_figNN.py` - reproducible build script
- `FIG-..._V2.png` - the revised visual (300 dpi)
- `dataset_figNN.csv` - underlying dataset (original + corrected where relevant)
- `SOURCE_REGISTER.md` - source register / citations
- `REVISION_NOTES.md` - old-version assessment + new version + change explanation
- `DATA_VALIDATION.md` - per-observation validation

| Folder | Figure | Action taken |
|---|---|---|
| `Figure_01` | FIG-1 Sequencing timeline | Rebuilt from source; phase-coloured; 0 label overlaps |
| `Figure_05` | FIG-5 Automotive & aerospace exports | Full data re-audit; aerospace year-label corrected |
| `Figure_16` | FIG-16C OCP value-chain ascent | Reversed/clarified so "up = more value" is unambiguous |
| `Figure_17` | FIG-17 Battery investments | Replaced with verified BTR & Shinzoom data |
| `Figure_18` | FIG-18 (low value) | **Replaced** with battery value-chain gap exhibit |
| `Figure_21` | FIG-21 Risk matrix | Rebuilt with proper dispersion + methodology (Batch 2) |
| `Figure_23` | FIG-23 (unreadable) | Redesigned for readability (Batch 2) |
| `Figure_A`  | FIG-A Agric. vs non-agric. growth | Rebuilt on verified HCP data (Batch 2) |

## Reproduce
```
pip install matplotlib numpy
python3 Figure_01/build_fig01.py   # etc.
```

## QC gate
Every figure is checked against five tests: data accuracy, source traceability, readability,
executive presentation, academic publication. Text-heavy figures additionally pass an automated
bounding-box overlap check (`me_style.report_overlaps`).
