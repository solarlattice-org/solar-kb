---
id: prod:canadian-solar-75-100k-t480gl02
type: Product
name: CSI-75/80/90/100K-T480GL02-U
aliases:
- CSI-75K-T480GL02-U
- CSI-80K-T480GL02-U
- CSI-90K-T480GL02-U
- CSI-100K-T480GL02-U
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: sec=1.1
    h: 077e0ca26335
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Three-phase inverter converting PV DC power to AC for local loads and grid feed-in
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: sec=1.1
    h: 077e0ca26335
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: Standard communication connection on all four models
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r34
    h: 42b811f7646e
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r34
    h: 4b1c03e265ac
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r34
    h: 0e0493ed939c
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r34
    h: b46bf1121b82
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: uses_protocol
  target: proto:wifi
  note: Optional communication connection
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r34
    h: 42b811f7646e
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r34
    h: 4b1c03e265ac
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r34
    h: 0e0493ed939c
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r34
    h: b46bf1121b82
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:cellular
  note: Optional GPRS communication connection
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r34
    h: 42b811f7646e
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r34
    h: 4b1c03e265ac
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r34
    h: 0e0493ed939c
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r34
    h: b46bf1121b82
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:power-line-communication
  note: Optional PLC communication connection
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r34
    h: 42b811f7646e
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r34
    h: 4b1c03e265ac
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r34
    h: 0e0493ed939c
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r34
    h: b46bf1121b82
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:ethernet
  note: Optional communication connection
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r34
    h: 42b811f7646e
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r34
    h: 4b1c03e265ac
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r34
    h: 0e0493ed939c
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r34
    h: b46bf1121b82
  review: drafted
- claim_id: c8
  rel: implements
  target: func:mppt
  note: MPPT efficiency of 99.5% listed for the 100K model
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r19
    h: 65cd7bb9927c
  review: drafted
  review_note: 'support check: partial - Only a 99.5% MPPT efficiency for the 100K is given; this implies
    MPPT but the other models are not covered.'
- claim_id: c9
  rel: compatible_with
  target: prod:staubli-mc4
  note: Datasheet lists MC4 as the DC connection type
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r31
    h: eb72f6e9bef7
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r31
    h: 7fea29909f04
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r31
    h: 23169d0c2dfd
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r31
    h: b0bc6fce78e2
  review: drafted
  review_note: 'support check: partial - Datasheet lists MC4 connection, but the passages never name Staubli.'
- claim_id: c10
  attr: max_input_voltage
  value:
    max: 1000
    unit: unit:V
  conditions: Maximum DC input voltage, CSI-100K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r1
    h: 57f4ad580a7a
  review: drafted
- claim_id: c11
  attr: max_input_current
  value:
    nominal: 26
    unit: unit:A
  conditions: Per input, 8 inputs (listed as 8*26), CSI-75K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r6
    h: 42254dd23cbc
  review: drafted
- claim_id: c12
  attr: max_input_current
  value:
    nominal: 26
    unit: unit:A
  conditions: Per input, 9 inputs (listed as 9*26), CSI-80K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r6
    h: 5202fb3a9c78
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  attr: max_input_current
  value:
    nominal: 26
    unit: unit:A
  conditions: Per input, 10 inputs (listed as 10*26), CSI-90K-T480GL02-U and CSI-100K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r6
    h: 0c4d7ff7ed07
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r6
    h: 3c127d353bd9
  review: drafted
- claim_id: c14
  attr: rated_output_current
  value:
    nominal: 90.2
    unit: unit:A
  conditions: Rated output current, CSI-75K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r13
    h: b93507e9bd8f
  review: drafted
- claim_id: c15
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated grid voltage, three-phase plus PE (3/PE~480), CSI-100K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r12
    h: d032023f4d7e
  review: drafted
- claim_id: c16
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated grid frequency, CSI-100K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r16
    h: eb1c013b080d
  review: drafted
- claim_id: c17
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum efficiency, CSI-90K-T480GL02-U and CSI-100K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r17
    h: a5250f05d529
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=14.r17
    h: febf405dd0d1
  review: drafted
  review_note: possible conflict with c18 (same source; check the conditions); possible conflict with
    c19 (same source; check the conditions); possible conflict with c20 (same source; check the conditions)
- claim_id: c18
  attr: efficiency
  value:
    nominal: 98.7
    unit: unit:PERCENT
  conditions: Maximum efficiency, CSI-75K-T480GL02-U and CSI-80K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r17
    h: 64e29dee45fa
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r17
    h: bee2d7422533
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c19 (same source; check the conditions); possible conflict with c20 (same source; check the conditions)
- claim_id: c19
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: EU (European weighted) efficiency, CSI-100K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=15.r18
    h: 754268a04d85
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions); possible conflict with c20 (same source; check the conditions)
- claim_id: c20
  attr: efficiency
  value:
    nominal: 98.3
    unit: unit:PERCENT
  conditions: EU (European weighted) efficiency, CSI-75K-T480GL02-U and CSI-80K-T480GL02-U
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=13.r18
    h: 342938652fe1
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=12.r18
    h: 25e1cc297bdb
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions); possible conflict with c19 (same source; check the conditions)
---
The CSI-75/80/90/100K-T480GL02-U is a family of Canadian Solar three-phase string inverters that turn PV array DC power into AC power for local loads and for export to the grid. The 100K model takes up to 1000 V DC and connects to a 480 V three-phase grid with PE at 60 Hz. Each input is rated for 26 A. The 75K has eight inputs, the 80K has nine, and the 90K and 100K each have ten. The 75K and 80K models have a maximum efficiency of 98.7%, and the 90K and 100K models reach 99.0%. The 75K model is rated at 90.2 A AC output current. RS485 communication is standard. Wifi, GPRS, PLC and Ethernet are optional. The DC connectors are MC4. Each unit has a two-line LCD display, weighs 85 kg and is rated at 65 dB(A) or less of noise.

<!-- review notes
- sentence 1: support check: partial - Three-phase Canadian Solar inverters converting DC to AC are stated, but 'string' inverter type is not stated.
- sentence 7: support check: partial - MC4, 85 kg and ≤65 dB(A) are stated; the display is LCD,2x20Z, and 'two-line' is an inference from 2x20.
- sentence 1: review: partial - Section 1.1 supports Canadian Solar three-phase inverters that convert DC to AC for loads and the grid, but it never calls them 'string' inverters.
-->
