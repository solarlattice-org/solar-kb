---
id: prod:canadian-solar-25-40k-t480gl01
type: Product
name: CSI-25/30/36/40K-T480GL01-UB
aliases:
- CSI-25K-T480GL01-UB
- CSI-30K-T480GL01-UB
- CSI-36K-T480GL01-UB
- CSI-40K-T480GL01-UB
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  note: The manual is published by CSI Solar Co., Ltd.
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=1.1
    h: c925f9649a6a
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Three-phase inverter that converts PV DC power to AC power for local loads and the grid
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=1.1
    h: c925f9649a6a
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: arch:grid-tied-pv
  scope:
    applications:
    - on-grid
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=h1
    h: 64c940e7f033
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=1.1
    h: c925f9649a6a
  review: drafted
  review_note: 'support check: partial - Feeding the grid is stated and the manual is titled grid-tied,
    but no storage exclusion is stated.'
- claim_id: c4
  rel: implements
  target: func:dc-arc-fault-protection
  note: Integrated AFCI listed for all four models
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r34
    h: 2f3149825b0f
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r34
    h: 94b574fc26ca
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r34
    h: 2b1fa73a0fd3
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r34
    h: 147b3c872101
  review: drafted
- claim_id: c5
  attr: rated_power
  value:
    nominal: 25
    unit: unit:KiloW
  conditions: CSI-25K-T480GL01-UB at 480 V
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=7
    h: c4d2afa6924e
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c6
  attr: rated_power
  value:
    nominal: 30
    unit: unit:KiloW
  conditions: CSI-30K-T480GL01-UB at 480 V
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=7
    h: c4d2afa6924e
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: rated_power
  value:
    nominal: 36
    unit: unit:KiloW
  conditions: CSI-36K-T480GL01-UB at 480 V
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=7
    h: c4d2afa6924e
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: rated_power
  value:
    nominal: 40
    unit: unit:KiloW
  conditions: CSI-40K-T480GL01-UB at 480 V
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=7
    h: c4d2afa6924e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c9
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Nominal AC grid voltage, all models
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=7
    h: c4d2afa6924e
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r15
    h: 6a6fe6492084
  review: drafted
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 30.1
    unit: unit:A
  conditions: Maximum AC output current, CSI-25K-T480GL01-UB
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r20
    h: 496ffa3a5f47
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions)
- claim_id: c11
  attr: rated_output_current
  value:
    nominal: 36.1
    unit: unit:A
  conditions: Maximum AC output current, CSI-30K-T480GL01-UB
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r20
    h: 79badb1eacaa
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c12
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: Maximum DC input voltage, CSI-36K-T480GL01-UB datasheet
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r3
    h: f9f0380d621c
  review: drafted
- claim_id: c13
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: Peak efficiency, 25K, 30K, 36K and 40K models
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r30
    h: 1dfab83ccd8e
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r30
    h: 1cded50f41fd
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r30
    h: 6e18e99ac491
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r30
    h: decb015816ff
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
- claim_id: c14
  attr: efficiency
  value:
    nominal: 98.3
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, 30K and 40K models
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r31
    h: 48590b3a9650
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r31
    h: 7cd0d43ada25
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions)
- claim_id: c15
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Nominal grid frequency, CSI-40K-T480GL01-UB
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r17
    h: 390859269b0e
  review: drafted
- claim_id: c16
  attr: frequency
  value:
    min: 59.5
    max: 60.5
    unit: unit:HZ
  conditions: Operating frequency range, CSI-40K-T480GL01-UB
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r18
    h: 40800b1e1912
  review: drafted
- claim_id: c17
  attr: operating_temperature
  value:
    min: -25
    max: 60
    unit: unit:DEG_C
  conditions: Ambient operating temperature range, 30K, 36K and 40K models
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=16.r7
    h: 7f29ce40f5f3
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=18.r7
    h: 62d4d1322928
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=20.r7
    h: d96cb5c5effe
  review: drafted
---
The CSI-25/30/36/40K-T480GL01-UB is a Canadian Solar family of four three-phase grid-tied string inverters that turn PV array DC power into AC power for local loads and the utility grid. The four models are rated at 25, 30, 36 and 40 kW, all on a 480 V grid connection. The 25K model has a maximum output current of 30.1 A and the 30K model has 36.1 A. The datasheet lists a maximum DC input voltage of 1000 V for the 36K model. Peak efficiency is listed at 98.6 percent. The CEC weighted efficiency is 98.3 percent for the 30K and 40K models. The 40K model is specified for a 60 Hz grid and operates between 59.5 and 60.5 Hz. Every model has integrated DC arc-fault circuit protection (AFCI).

<!-- review notes
- sentence 1: support check: partial - Four models, Canadian Solar, grid-tied manual and DC-to-AC function are stated, but 'string inverter' is not stated.
- sentence 1: review: partial - Canadian Solar, four models, three-phase, grid-tied and the DC-to-AC function for loads and grid are stated, but 'string' inverter is not.
-->
