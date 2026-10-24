---
id: prod:generac-snaprs
type: Product
name: Generac SnapRS
aliases:
- SnapRS
- RS801
- RS801A
- RS802
category: MLPE
make: generac
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:rapid-shutdown-device
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h31
    h: 59459794ebbe
  review: drafted
- claim_id: c2
  rel: implements
  target: func:rapid-shutdown
  note: Module-level rapid shutdown inside the array; works together with PV Link.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h31
    h: 59459794ebbe
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h34
    h: 6272feef1a7c
  review: drafted
- claim_id: c3
  rel: requires
  target: prod:generac-pv-link
  note: Has to be paired with the S2502 PV Link to make a complete PVRSS under NEC 690.12.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h13
    h: 47cb3f937df4
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h34
    h: 6272feef1a7c
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h31
    h: 59459794ebbe
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:generac-pwrcell-inverter
  note: Listed as required PVRSE (one per PV module), along with PV Link, for PWRcell systems under the
    2017 and 2020 NEC.
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=9.r3
    h: 92c7a0443ae4
  review: drafted
  review_note: 'support check: partial - Passage lists SnapRS as required PWRcell PVRSE one per module
    under 2017/2020 NEC, but doesn''t name inverter model numbers.'
- claim_id: c5
  rel: certified_to
  target: std:ul-1741
  scope:
    products:
    - prod:generac-snaprs
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=4.r9
    h: e166f63e82cb
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=4.r9
    h: e166f63e82cb
  review: drafted
- claim_id: c7
  rel: certified_to
  target: req:nfpa-70-2017-690-12
  scope:
    standard: std:nfpa-70-2017
  conditions: when used with PV Link
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h31
    h: 59459794ebbe
  review: drafted
- claim_id: c8
  rel: certified_to
  target: req:nfpa-70-2020-690-12
  scope:
    standard: std:nfpa-70-2020
  conditions: when used with PV Link
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h31
    h: 59459794ebbe
  review: drafted
- claim_id: c9
  attr: max_input_current
  value:
    nominal: 13
    unit: unit:A
  conditions: RS801 model, maximum input current per device
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=4.r4
    h: da1ceda1917a
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions)
- claim_id: c10
  attr: max_input_current
  value:
    nominal: 14
    unit: unit:A
  conditions: RS801A model, maximum input current per device
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=4.r4
    h: da1ceda1917a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c11
    (same source; check the conditions)
- claim_id: c11
  attr: max_input_current
  value:
    nominal: 15
    unit: unit:A
  conditions: RS802 model, maximum input current per device
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=4.r4
    h: da1ceda1917a
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
- claim_id: c12
  attr: operating_temperature
  value:
    min: -40
    max: 70
    unit: unit:DEG_C
  conditions: operating temperature range for RS801, RS801A and RS802
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=4.r8
    h: 1597ac22aa4e
  review: drafted
- claim_id: c13
  attr: max_count
  value:
    nominal: 1
    unit: unit:NUM
  conditions: SnapRS devices per PV module
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h24
    h: c3a2a07a4097
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=9.r3
    h: 92c7a0443ae4
  review: drafted
---
Generac SnapRS is an inline module-level rapid shutdown device. It comes in the RS801, RS801A and RS802 models. SnapRS has to be paired with the Generac S2502 PV Link to form a complete rapid shutdown system. Together they meet NEC 690.12 in the 2017 and 2020 editions. After rapid shutdown starts, conductors inside the array boundary drop to 80 VDC or less. The datasheet lists a shutdown time of under 10 seconds. Maximum input current is 13 A for the RS801, 14 A for the RS801A and 15 A for the RS802. All three models run from -40 to 70 °C. All models are certified to UL 1741 and CSA 22.2 #107.1. You cannot run a functional test on SnapRS in the field, but simple multimeter checks can confirm its general health. PV Link reports a PVRSS count mismatch or a high-input failure if SnapRS units are missing, failed, wrongly installed or entered with the wrong count. Never change the SnapRS count just to force PV Link to run.

<!-- review notes
- sentence 1: review: partial - The passages state that SnapRS is an inline PV rapid shutdown device in models RS801, RS801A and RS802, but 'module-level' is not stated.
-->
