# Figure 1 - Revision Notes
**Mandate:** Redo completely. Rebuild from source data. Prioritise clarity over complexity.

## 1. Old-version assessment (`figures/FIG-1.png`)
- **Text overlap.** Milestone labels collided where dates cluster (2004/06/08/09 and
  2016/17/18), making several entries unreadable.
- **Unclear message.** The chart presented a flat list of dated events; the reader could not
  see the report's central thesis - that the events fall into three *sequenced phases*
  (discipline -> construction -> certification).
- **Weak hierarchy / readability.** No visual encoding of phase, no directional cue, and
  labels competed with one another for attention.

## 2. New version (`FIG-01_sequencing_timeline_V2.png`)
- **One message, encoded in colour.** Three phase bands - Discipline (dark grey),
  Construction (dark green), Certification (muted gold) - make the sequencing thesis legible
  in under five seconds. Phase headers and date spans sit above each band.
- **Zero overlap, guaranteed.** Every label is placed in a dedicated lane (two levels above /
  two below the spine) with a thin leader line to its marker. An automated bounding-box check
  (`me_style.report_overlaps`, 12% safety margin) confirms **0 overlaps** across all 13 labels.
- **Clear axis & direction.** A single left-to-right time spine with an arrowhead communicates
  forward progression; markers are coloured by phase and ringed in white for separation.
- **Readable typography.** DejaVu Sans, 10.6 pt labels, bold year tags, generous spacing,
  white label cards outlined in the phase colour.

## 3. Explanation of changes
| Issue (V1) | Fix (V2) |
|---|---|
| Overlapping labels in date clusters | Hand-assigned 4-lane layout + leader lines; automated overlap gate |
| No phase narrative | Three coloured phase bands + headers encode discipline/construction/certification |
| No reading direction | Arrowed time spine, left-to-right |
| Flat hierarchy | Title states the message; colour carries the thesis; legend keys the phases |
| Mixed/decorative styling | Single house palette, no chartjunk, publication-quality 300 dpi |

## QC checklist
- [x] Data accuracy - factual milestones, fully sourced (see SOURCE_REGISTER.md)
- [x] Source traceability - every milestone cited
- [x] Readability - 0 measured label overlaps; 300 dpi
- [x] Executive presentation - 5-second message via colour-coded phases
- [x] Academic publication - sourced, neutral, reproducible (`build_fig01.py`)
