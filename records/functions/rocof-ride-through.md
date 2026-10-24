---
id: func:rocof-ride-through
type: Function
name: Rate-of-change-of-frequency ride-through
aliases:
- ROCOF ride-through
- PFRC
- ROCOF
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: subclass_of
  target: func:frequency-ride-through
  note: ROCOF ride-through applies within the continuous operation region and the low- and high-frequency
    ride-through regions.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=6.5.2.5
    h: 33cb7255e956
  review: drafted
  review_note: 'support check: partial - Passage states ROCOF ride-through applies within continuous operation
    and the low/high-frequency ride-through regions, but does not state that it is a kind of frequency
    ride-through (taxonomy relation is implied only by context).'
---
ROCOF ride-through means the DER stays connected and does not trip while grid frequency is changing quickly, as long as the rate of change stays within the limit for its performance category. The ride-through limits are 0.5 Hz/s for Category I, 2.0 Hz/s for Category II and 3.0 Hz/s for Category III. When compliance at the PCC is shown by the DER system itself, a type test is required. Evaluation and commissioning tests are not required in that case. Composite installations do need a DER evaluation and commissioning tests. One utility's default settings document accepts UL 1741 SB certification as enough proof of ROCOF ride-through for an individual inverter. That same document does not allow relays, controllers or any other site equipment outside the certified inverter to trip on ROCOF or to have ROCOF enabled.

<!-- review notes
- sentence 3: support check: partial - DER System row shows type tests R, evaluation and commissioning NR, and the Composite row shows evaluation and commissioning R, but the Composite type test is L (limited), which the statement does not mention; the meaning of R/NR is also not defined.
-->
