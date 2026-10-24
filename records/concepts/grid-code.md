---
id: concept:grid-code
type: Concept
name: Grid code
aliases:
- interconnection standard
- grid connection rules
- grid protection rules
- Grid Connection Rule
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:country-data-set
  note: 'Inverters set the grid code through a setting: SMA documents a procedure for changing the grid
    code and groups parameters under a country standard, and Delta shows Grid Code screens.'
  cite:
  - src: src:sma-doc-275857
    loc: tbl=17
    h: d3ec58a2d912
  - src: src:sma-doc-278879
    loc: tbl=2.r12
    h: 3de2e4e85514
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: fig=124
    h: 7155fb7070b6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passages show a Country standard parameter group, a ''Changing
    the Grid Code'' section and Grid Code screens, implying a setting, but don''t explicitly state grid
    code is a setting.'
- claim_id: c2
  rel: related_to
  target: std:ena-erec-g99
  note: UK G99 appears among the grid protection rules against which a vendor checks meter-based export
    limitation for compliance.
  cite:
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r8
    h: acb66fa86f6c
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r6
    h: 5ecce1c4c761
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r7
    h: 5ad1d3d1ac76
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r2
    h: 408e4c00d210
  review: drafted
  review_note: 'support check: partial - UK G99 - ENA 100 appears in the export limitation compliance
    table, but the passages don''t explicitly link it to the grid code concept.'
- claim_id: c3
  rel: related_to
  target: std:vde-ar-n-4105-2018
  note: Appears as a grid protection rule in a vendor's export limitation compliance table.
  cite:
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r8
    h: acb66fa86f6c
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r6
    h: 5ecce1c4c761
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r7
    h: 5ad1d3d1ac76
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r2
    h: 408e4c00d210
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:export-limitation
  note: Each meter is marked as compliant or not with each grid protection rule when used for export limitation.
  cite:
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r8
    h: acb66fa86f6c
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r6
    h: 5ecce1c4c761
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r7
    h: 5ad1d3d1ac76
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: tbl=4.r2
    h: 408e4c00d210
  review: drafted
- claim_id: c5
  rel: related_to
  target: std:ieee-1547
  note: NREL describes how the IEEE 1547 standards are used in the United States.
  cite:
  - src: src:ref-standards-ieee-ieee-1547-nrel-doc-63157
    loc: fig=3
    h: fc6c45664784
  review: drafted
  review_note: 'support check: partial - The passage is only a figure caption on IEEE 1547 use in the
    US; it doesn''t say NREL describes it, nor relate it to grid code.'
- claim_id: c6
  rel: related_to
  target: func:dynamic-voltage-support
  note: SMA inverters offer a dynamic grid support mode that can be set to off, limited or complete.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=75.r1
    h: 502ac7fea255
  - src: src:sma-doc-275857
    loc: tbl=91
    h: d814ad19561a
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:reactive-power
  note: In some countries, utility-scale PV plants must stay online when the grid is stressed and produce
    reactive energy to help stabilize it.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=1
    h: 6071f58ccb27
  review: drafted
---
Early residential PV systems simply followed a healthy grid and shut down when voltage or frequency went outside acceptable limits. In some countries, utility-scale PV plants may no longer shut down when the grid is stressed. They must support the grid instead, including by producing reactive energy. On the inverter, the grid code is chosen as a setting, sometimes called the grid connection rule or country standard. That setting fixes parameters such as the connection time after a restart. Some inverters also have a dynamic grid support mode that can be set to off, limited or complete. The inverter's self-diagnostics and alarms help keep it in compliance with grid standards.

<!-- review notes
- sentence 3: support check: partial - Grid Connection Rule title, Country standard group and connection time after restart appear, but the passages don't explicitly say the setting fixes that parameter or equate the names.
- sentence 5: support check: partial - Passage says self-diagnostic mechanisms ensure safety, availability and compliance with grid standards, but does not specifically say alarms keep the inverter compliant.
-->
