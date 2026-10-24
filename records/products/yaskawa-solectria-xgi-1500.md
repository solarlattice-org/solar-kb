---
id: prod:yaskawa-solectria-xgi-1500
type: Product
name: Solectria XGI 1500
aliases:
- XGI 1500
- XGI 1500c
- SGI 1500
- Solectria XGI
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-yss-xgi-interconnection-guidelines-2025-10-23
    loc: sec=h2
    h: f3d316df09cd
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h172
    h: 8eb56217ad74
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Passages show Yaskawa Solectria Solar offers/documents XGI 1500
    inverters, but never explicitly state it makes them (title only implies).'
- claim_id: c2
  rel: uses_protocol
  target: proto:wifi
  note: Communication platform reachable over WiFi from a smart device.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=h66
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h94
    h: 57a76033a3a1
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h75
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h76
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h75
    h: 3ce8feffcde0
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:ethernet
  note: Accessible over Ethernet from a PC; the 1MW series has two interchangeable Ethernet ports.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=h66
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h94
    h: 57a76033a3a1
  - src: src:yaskawa-xgi-1500-175-250-iom-docr-071074-dd
    loc: sec=h75
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h76
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-125-166-iom-docr-071015-ff
    loc: sec=h75
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h115
    h: 34dcdd81dd1d
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus
  note: A Smart Grid Feature and Modbus Manual covers XGI 1500 models from 125/125 to 250/250.
  cite:
  - src: src:yaskawa-xgi-1500-modbus-map-docr-071063-rev-h
    loc: sec=h1
    h: 5ee1b3755496
  review: drafted
  review_note: 'support check: partial - A Modbus manual exists for those models, but the passage only
    lists models and doesn''t explicitly say the inverter uses Modbus protocol.'
- claim_id: c5
  rel: implements
  target: func:remote-firmware-update
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  note: Manual firmware updates are supported through the Remote Access Portal.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h142
    h: 5e5a0cc70aea
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ul-1741
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  note: Listed as UL 1741 2021 for all XGI 1500-1MW models.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ieee-1547
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ul-1998
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  note: Listed as CSA C22.2 No. 107.1-16; testing agency TÜV Rheinland.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
  review_note: 'support check: partial - CSA C22.2 No. 107.1-16 is listed, but TÜV Rheinland as testing
    agency is not in the cited passage (u2).; review: partial - CSA C22.2 No. 107.1-16 is listed for every
    XGI 1500 model, but the note''s claim that TÜV Rheinland is the testing agency does not appear in
    the cited row.'
- claim_id: c10
  rel: compatible_with
  target: arch:functionally-grounded-pv-array
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-dcg
  note: DCG models use a functionally grounded DC negative, which prevents PID in susceptible modules;
    Applications Engineering must review each project's single-line diagram and transformer configuration.
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h1
    h: 8e118d3d2649
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:yaskawa-solectria-cr1500-combiner
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  note: CR1500-xxP-yyS-400 and CR1500-xxP-yyF-400S remote combiners are designed for the XGI 1500-1MW
    series.
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h172
    h: 8eb56217ad74
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: prod:yaskawa-solectria-xgi-1500-powerrack
  note: PowerRacks combine two to eight XGI 1500 inverters.
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h4
    h: 71b645bd4111
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h5
    h: 22cc42e5db8c
  review: drafted
- claim_id: c13
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Absolute maximum DC input voltage per XGI 1500-250 inverter in PowerRack configurations
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=1.r6
    h: 3b00693b379a
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=2.r7
    h: f7b81b344bd0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c14
  attr: mppt_voltage_range
  value:
    min: 860
    max: 1250
    unit: unit:V
  conditions: Full-power MPPT voltage range per XGI 1500-250 inverter in PowerRack configurations
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=1.r7
    h: 970996ff042a
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=2.r7
    h: f7b81b344bd0
  review: drafted
- claim_id: c15
  attr: mppt_voltage_range
  value:
    min: 860
    max: 1450
    unit: unit:V
  conditions: MPPT operating voltage range per XGI 1500-250 inverter in PowerRack PRU-5 to PRU-8 configurations
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=2.r8
    h: 0624bc3690a7
  review: drafted
- claim_id: c16
  attr: max_input_current
  value:
    nominal: 296.7
    unit: unit:A
  conditions: Maximum operating PV current per XGI 1500-250 inverter in PowerRack configurations
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=1.r10
    h: e095e52003f9
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions)
- claim_id: c17
  attr: max_input_current
  value:
    nominal: 800
    unit: unit:A
  conditions: Maximum rated PV short-circuit current (sum of Isc x 1.25) per XGI 1500-250 inverter in
    PowerRack configurations
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=1.r13
    h: 32c985694af6
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=2.r14
    h: 74e6ce19d1f9
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions)
- claim_id: c18
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Nominal three-phase AC output voltage, range -12% to +10%, XGI 1500-250 PowerRack configurations
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=2.r15
    h: fe3126543ff7
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=1.r14
    h: 6ae20f27c7c0
  review: drafted
- claim_id: c19
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Nominal operating AC frequency, XGI 1500-250 PowerRack configurations
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=2.r19
    h: 1b3aedf4cd59
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c20
  attr: rated_power
  value:
    nominal: 225
    unit: unit:KiloW
  conditions: XGI 1500-225 model at 600 Vac
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h5
    h: 22cc42e5db8c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c21
  attr: rated_power
  value:
    nominal: 200
    unit: unit:KiloW
  conditions: XGI 1500-200 model at 480 Vac
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h5
    h: 22cc42e5db8c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c22
  attr: rated_power
  value:
    nominal: 175
    unit: unit:KiloW
  conditions: XGI 1500-175 model at 480 Vac
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h5
    h: 22cc42e5db8c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c21 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c23
  attr: rated_power
  value:
    nominal: 125
    unit: unit:KiloW
  conditions: XGI 1500-125 model at 600 Vac
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: sec=h5
    h: 22cc42e5db8c
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c21 (same source; check the conditions); possible conflict with c22 (same source; check the conditions)
---
The Solectria XGI 1500 is a family of 1500 V three-phase inverters made by Yaskawa Solectria Solar. It includes the 125 to 250 kW models, the DCG variants and the XGI 1500-1MW utility-scale modular central series. In PowerRack configurations, each XGI 1500-250 inverter accepts up to 1500 Vdc. It tracks at full power from 860 to 1250 Vdc and feeds 600 Vac three-phase at 60 Hz. A PowerRack combines two to eight XGI 1500 inverters, for totals between 0.5 MW and 2 MW. It can also use the 600 Vac or 480 Vac models. You can reach the inverters over WiFi from a smart device or over Ethernet from a PC. They work with SolrenView monitoring without extra hardware, and a Modbus manual covers the smart grid features. The DCG models functionally ground the DC negative, which prevents PID in modules that are susceptible to it. Yaskawa's Applications Engineering team must review each project's single-line diagram and transformer configuration. The 1MW models are listed to UL 1741, IEEE 1547, UL 1998 and CSA C22.2 No. 107.1, with TÜV Rheinland as the testing agency. They support manual firmware updates through the Remote Access Portal. The CR1500 remote combiners are designed to pair with the XGI 1500-1MW series.

<!-- review notes
- sentence 1: support check: partial - Models, DCG variants and 1MW utility-scale modular central series are shown, but 1500 V three-phase and manufacturer explicitly aren't fully stated for the family.
- sentence 1: review: partial - The passages support the maker, the 125-250 kW models, the DCG variants and the 1MW utility-scale modular central series, but never state that the family is 1500 V three-phase.
-->
