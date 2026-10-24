---
id: concept:active-power
type: Concept
name: Active power
aliases:
- real power
- kW
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:reactive-power
  note: Monitoring tables list active power in kW next to reactive power in kVAr; inverters offer separate
    active and reactive power control modes.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=61
    h: 8c2fd0c1a0b4
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: sec=13
    h: dbfd2876728c
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:limit-active-power
  note: Active power can be capped as a percentage of Pmax or of nameplate maximum real power.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=121.r1
    h: 8b279b943c55
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=121
    h: 8b9dc5293360
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: sec=13
    h: dbfd2876728c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=8.r3
    h: 2a514277a7d8
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:volt-watt
  note: 'P(V): exported active power set as a function of grid voltage.'
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: sec=13
    h: dbfd2876728c
  - src: src:sma-doc-265222
    loc: tbl=2.r3
    h: 91a8821bda1f
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:frequency-watt
  note: 'P(f): active power limited as a function of grid frequency; required for PV inverters in battery-backup
    systems.'
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: sec=13
    h: dbfd2876728c
  - src: src:sma-doc-265222
    loc: sec=h3
    h: 23423a925424
  - src: src:sma-doc-244194
    loc: sec=h51
    h: fea781993341
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c5
  rel: related_to
  target: func:active-power-setpoint
  cite:
  - src: src:sma-doc-275857
    loc: tbl=1.r22
    h: f57920f108ac
  - src: src:sma-doc-275857
    loc: tbl=34
    h: e87a57b6d054
  review: drafted
  review_note: 'support check: partial - The passages only have a table-of-contents entry ''Active Power
    Setpoint'' and external active power setting objects, so a relation is implied but little is stated.'
- claim_id: c6
  rel: related_to
  target: concept:nameplate-rating
  note: The nameplate active power rating is defined in watts at unity power factor.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=35.r1
    h: 12e3e7ebebe1
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:curtailment
  note: Active power curtailment sets a new active power value as a percentage of Pmax.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: sec=13
    h: dbfd2876728c
  review: drafted
---
Active power, also called real power, is the part of AC power that actually does work. It is measured in watts. Inverters, battery inverters and monitoring platforms usually show active power in kW, for example for the utility grid, a generator, an external source or the loads. The nameplate active power rating of a DER is the active power rating in watts at unity power factor. Inverters also have a nominal maximum value that caps the active power at their output. Inverters and battery systems can reduce active power on command, as a percentage of rated maximum power or of nameplate maximum real power. Grid support modes can also change active power with grid voltage (Volt-Watt, P(V)) or with grid frequency (Frequency-Watt, P(f)). In battery-backup systems, the PV inverters must be able to control their active power according to frequency. Active power is separate from reactive power, which monitoring tables list in kVAr, and inverters provide separate control modes for each.

<!-- review notes
- sentence 1: support check: partial - The passages say active power is in watts and mention real power, but not that it is the part of AC power that does work.
- sentence 1: review: partial - The passages back 'active power in watts' and use 'real power' for the same quantity, but none says active power is the part of AC power that does work.
-->
