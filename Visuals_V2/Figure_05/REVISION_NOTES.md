# Figure 5 - Revision Notes
**Mandate:** Data appears incorrect -> re-audit, verify, reconstruct, do not reuse unvalidated
values. Provide original dataset, corrected dataset, source citations, explanation of discrepancy.

## 1. Original dataset (V1, from `figures/_dataset.md`)
| Year | Automotive (MAD bn) | Aerospace (MAD bn) |
|---|---|---|
| 2014 | 40 | 7.5 |
| 2016 | 54 | 9.8 |
| 2018 | 65 | 12.4 |
| 2020 | 72.7 | 12.9 |
| 2022 | 111.4 | **21.9** |
| 2024 | 157.0 | 26.45 |

## 2. Corrected dataset (V2, validated)
| Year | Automotive (MAD bn) | Aerospace (MAD bn) | Note |
|---|---|---|---|
| 2020 | 72.7 (V) | 12.9 (V) | COVID trough |
| 2022 | 111.3 (V) | 18.9 (est*) | aero estimate flagged |
| 2023 | 141.8 (V) | **21.8 (V)** | **the value V1 mislabeled as 2022** |
| 2024 | 157.0 (V) | 26.4 (V) | record |
*(V) validated against primary sources; (est*) reconstructed estimate. Full series incl.
reconstructed pre-2018 points in `dataset_fig05.csv`.*

## 3. Explanation of the discrepancy
- **Primary error - aerospace year shift.** V1's "MAD 21.9 bn @ 2022" is the **2023** Office des
  Changes value (MAD 21.8 bn). Reuters/Safran confirm 2023 = 21.8 and 2024 = 26.4. Because V1
  used even years only and skipped 2023, the mislabel was hidden. V2 inserts 2023 and assigns the
  value to its correct year.
- **Minor rounding (no material error):** automotive 2022 (111.4 -> 111.3), aerospace 2024
  (26.45 -> 26.4) - both within rounding tolerance.
- **Understated aerospace 2018:** V1's 12.4 is inconsistent with the validated 2019 ($1.9bn ~18)
  and 2020 ($1.3bn ~12.9) anchors; treated as uncertain and not charted.
- **Reconstructed pre-2018 points** (auto 40/54; aero 7.5/9.8) retained for the record but not
  charted, to keep validated and reconstructed data visually separate.

## 4. Visual changes
- Grouped bars (automotive green, aerospace gold) on a single MAD-bn axis for honest comparability.
- The one reconstructed estimate (2022 aerospace) is hatched and asterisked, with its status in
  the legend and footnote.
- An on-chart correction callout points at the 2023 aerospace bar and states the fix.
- Bold data labels on every bar; right-hand "what the numbers say" panel with USD equivalents and
  latest reads.

## QC checklist
- [x] Data accuracy - every charted point validated except one transparently flagged estimate
- [x] Source traceability - per-point citations (SOURCE_REGISTER.md)
- [x] Readability - data labels, single axis, no overlaps, 300 dpi
- [x] Executive presentation - record automotive number anchors the story
- [x] Academic publication - discrepancy documented; reproducible (`build_fig05.py`)
