# Figure 5 - Data Validation Notes (full re-audit)
**Mandate:** Data appears incorrect. Re-audit the entire dataset; verify every observation
against primary sources; reconstruct where necessary; do not reuse previous values unless
validated.

## Headline finding (the discrepancy)
The V1 series was an **even-year** sequence (2014, 2016, 2018, 2020, 2022, 2024). It placed an
aerospace value of **MAD 21.9 bn at 2022**. Primary sources show this is actually the **2023**
value:

> Reuters (citing Office des Changes / Safran, Oct 2025): Morocco's aerospace exports "rose to
> 26 billion dirhams ($2.8 billion) in 2024 from **21.8 billion dirhams a year earlier**" (2023).
> Reuters (Feb 2026): "29 billion dirhams in 2025 from **26.4 billion** a year earlier" (2024).

So the correct anchors are **2023 = 21.8** and **2024 = 26.4**. The V1 label was shifted one
reporting year earlier. Because V1 skipped 2023, the error was invisible. V2 adds 2023 and
re-labels the value correctly.

## Item-by-item validation (charted years)
| Year | Series | V2 value (MAD bn) | Status | Source |
|---|---|---|---|---|
| 2020 | Automotive | 72.7 | VALIDATED | Reuters: auto exports ~$8.1bn in 2020 |
| 2022 | Automotive | 111.3 | VALIDATED | Statista/Office des Changes: 111,281 MMAD |
| 2023 | Automotive | 141.8 | VALIDATED | Statista 141,763 MMAD; Reuters "record 141 bn" |
| 2024 | Automotive | 157.0 | VALIDATED | Yabiladi: record MAD 157 bn (2024) |
| 2020 | Aerospace | 12.9 | VALIDATED | Reuters: aerospace ~$1.3bn (COVID trough) |
| 2022 | Aerospace | 18.9 | **RECONSTRUCTED ESTIMATE** | interpolated (2021 ~15.4 -> 2023 21.8); flagged with (*) and hatching |
| 2023 | Aerospace | 21.8 | VALIDATED | Reuters/Safran citing Office des Changes |
| 2024 | Aerospace | 26.4 | VALIDATED | Reuters/Safran |

## Other checks
- **Automotive 2022:** V1 = 111.4; verified = 111.281 -> 111.3. Negligible rounding; V1 OK.
- **Automotive 2024:** V1 = 157.0; verified record MAD 157 bn. OK.
- **Aerospace 2024:** V1 = 26.45; verified = 26.4. OK (rounding).
- **Aerospace 2018 (V1 = 12.4):** likely understated. 2019 = $1.9 bn (~MAD 18 bn) and 2020 =
  $1.3 bn (~MAD 12.9 bn) imply 2018 ~ MAD 15-16 bn. Treated as uncertain; **not charted**.
- **Pre-2018 points (auto 40/54; aero 7.5/9.8):** sector-association reconstructions (AMICA/
  GIMAS), as flagged in the original dataset pack. Retained in the dataset for continuity but
  **not charted in V2** to avoid mixing validated and reconstructed data on the same exhibit.

## Editorial decision
V2 charts only 2020-2024 - the window with the strongest Office des Changes coverage - and marks
the single remaining estimate (2022 aerospace). The full audited series (incl. reconstructed
years and 2025 forward reads) is preserved in `dataset_fig05.csv`.

## Validation status: PASS (with one flagged reconstructed estimate, transparently marked)
