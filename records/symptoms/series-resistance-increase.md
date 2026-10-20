---
id: symptom:series-resistance-increase
type: Symptom
name: Increased series resistance
aliases:
- Rs
- resistance in series
- serial resistance
- high resistance faults
claims:
- claim_id: c1
  rel: observed_as
  target: meas:iv-shallow-voc-slope
  note: Higher series resistance makes the IV curve less steep between Vmpp and Voc. Long cable runs can
    produce the same shape, so the model should account for them or the test should be repeated closer
    to the array.
  cite:
  - src: src:iec-62446-1
    loc: sec=D.6
    h: f87aef72de6f
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: observed_as
  target: meas:fill-factor-reduction
  note: Seen with metallization corrosion (together with lower Isc), with early-stage interconnect failure
    and with cell cracking.
  cite:
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Corrosion with lower Isc and interconnect failure with fill factor
    decrease are stated, but cell cracking is only described with a 2% absolute FF drop, and ''early-stage''
    interconnect failure is only loosely matched (stage 1).'
- claim_id: c3
  rel: observed_as
  target: meas:iv-rounded-knee
  note: Reported for interconnection failures where redundant interconnects still carry the current.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:low-vmp-voc-ratio
  note: In cracked-cell modules, a falling Vmp/Voc ratio points to series resistance. Light and dark IV
    curves, or light IV curves at two intensities, measure it best.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: observed_as
  target: meas:ir-hot-connection
  note: In the first phase of a connector failure, extra resistance produces heat that thermography can
    show, even when the electrical change is too small to detect.
  cite:
  - src: src:iec-62446-1
    loc: sec=D.6
    h: f87aef72de6f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h6
    h: e7691a95e9d7
  review: drafted
- claim_id: c6
  rel: observed_as
  target: meas:ir-hotspot
  note: Poor solder bonds in cell interconnects dissipate more power and heat up locally.
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 0.1
    unit: unit:PERCENT
  conditions: Per cut cell interconnection in cells with 4 busbars, from a series resistance increase
    of about 1%
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: disputed
  review_note: possible conflict with c8 (same source; check the conditions)
  conflicts_with:
  - symptom:series-resistance-increase#c9
- claim_id: c8
  attr: typical_power_loss
  value:
    nominal: 1
    unit: unit:PERCENT
  conditions: Per cut cell interconnection in cells with 3 busbars (less redundancy)
  cite:
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h5
    h: 5f9cbfc08864
  review: disputed
  review_note: possible conflict with c7 (same source; check the conditions)
  conflicts_with:
  - symptom:series-resistance-increase#c9
- claim_id: c9
  attr: typical_power_loss
  value:
    nominal: 2.6
    unit: unit:PERCENT
  conditions: Part of a 10% module power loss from induced cell cracking that is caused by a series resistance
    increase of 0.5 Ohm cm2
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.3
    h: b6c82133fe8c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
---
On an IV curve, increased series resistance makes the section between the maximum power point and Voc less steep. It also shows up as a lower fill factor and a more rounded knee. At array level, check first for damaged or undersized cables and for poor connections at module or array interconnects. A long cable run can produce the same curve shape, so repeat the trace closer to the array if you suspect this. Inside the module, the extra resistance can come from failing cell interconnects or junction box connections, from metallization corrosion, or from cell cracks. An infrared scan helps locate high-resistance faults. Defective connectors and poorly soldered interconnects show up as local heating, even before the electrical change can be measured. Corrosion is often visible to the eye and comes with a lower Isc. Interconnect failures and cracks are hard to see, so use EL imaging to find dark regions or crack lines. With cracked cells, most of the power loss comes from lost current rather than from series resistance.

<!-- review notes
- sentence 5: support check: partial - IR for high-resistance faults, connector early heating, and solder local heating are stated, but 'even before electrical change can be measured' for solder interconnects isn't stated (only for connectors, 'might be too small').
- sentence 6: support check: partial - Corrosion visibility with lower Isc and EL dark regions for interconnect failures are supported, but EL 'crack lines' for cracks are not stated explicitly (only that micro cracks are seen in EL images), and cracks being hard to see is only implied.
-->
