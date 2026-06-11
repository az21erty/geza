# Batch 1 - Delivery Summary (Figures 1, 5, 16C, 17, 18)

## 1. Revised visuals
| Figure | File |
|---|---|
| 1  | `Figure_01/FIG-01_sequencing_timeline_V2.png` |
| 5  | `Figure_05/FIG-05_auto_aerospace_exports_V2.png` |
| 16C| `Figure_16/FIG-16C_ocp_value_chain_ascent_V2.png` |
| 17 | `Figure_17/FIG-17_battery_investments_V2.png` |
| 18 | `Figure_18/FIG-18_battery_value_chain_position_V2.png` |

## 2. Revised datasets
`Figure_01/dataset_fig01.csv`, `Figure_05/dataset_fig05.csv` (original + corrected),
`Figure_16/dataset_fig16c.csv`, `Figure_17/dataset_fig17.csv`, `Figure_18/dataset_fig18.csv`.

## 3. Source register
One `SOURCE_REGISTER.md` per figure folder (citations + links).

## 4. Change log
- **FIG-1:** Rebuilt from source. Encoded the discipline -> construction -> certification thesis as
  three colour bands; eliminated label overlap via a 4-lane leader-line layout (automated check:
  **0 overlaps**); added reading direction and a one-line message title.
- **FIG-5:** **Data integrity fix.** The V1 series placed aerospace **MAD 21.9 bn at 2022**;
  primary sources (Reuters/Safran citing Office des Changes) show this is the **2023** value
  (MAD 21.8 bn); 2024 = 26.4 bn. Added 2023, re-labelled, validated automotive 2020-2024
  (72.7 / 111.3 / 141.8 / 157.0), flagged the single reconstructed estimate (2022 aerospace).
- **FIG-16C:** Reversed/clarified the value-added direction - ascending staircase + rising arrow +
  "RAW MATERIAL"/"MORE VALUE ADDED" anchors + arrowed axes. Anchored to OCP's 2024 revenue mix
  (69% fertilizers). Corrected stage order (acid precedes fertilizer).
- **FIG-17:** Replaced outdated numbers. **BTR ~USD 750 M** integrated cathode (50 kt) + anode
  (60 kt), ~**500,000 EVs/yr**, Tanger Tech (was ~USD 690 M, cathode only). **Shinzoom up to
  ~USD 500 M** (USD 460 M) anode. Cluster context (Gotion USD 1.3 bn).
- **FIG-18:** **Replaced** (recommendation: replace, not redesign). New exhibit shows value
  concentrates **midstream** while Morocco's strength is **upstream** - the "midstream value gap,"
  with each stage's concrete Moroccan assets.

## 5. Remaining issues / open items
- **FIG-5, 2022 aerospace (MAD ~18.9 bn):** a reconstructed estimate (interpolated between the
  validated 2021 ~15.4 and 2023 21.8); not an Office des Changes-confirmed figure. Flagged on-chart.
  *Action if needed:* confirm against the Office des Changes 2022 annual bulletin.
- **FIG-5, pre-2018 points:** sector-association reconstructions; audited into the dataset but not
  charted to avoid mixing confidence levels.
- **FIG-16C / FIG-18 curves:** schematic (relative) value ladders - per-tonne / per-stage margins
  are proprietary, so exact spacing is illustrative (clearly labelled). The ordering, direction and
  quantitative anchors are factual.
- **Originals not machine-readable here:** no OCR was available in the build environment, so V2
  reconstructs each exhibit from the manuscript's analytical content + the revision brief rather
  than tracing the V1 pixels. Content was matched to the report section in each case.

## QC status: all five figures pass the five-test gate (see each REVISION_NOTES.md).
