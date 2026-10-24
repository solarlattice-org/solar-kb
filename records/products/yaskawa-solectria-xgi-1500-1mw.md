---
id: prod:yaskawa-solectria-xgi-1500-1mw
type: Product
name: Solectria XGI 1500-1MW
aliases:
- XGI 1500 1MW
- XGI 1500-1MW
- XGI 1500-1MW series
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  note: Utility-scale modular central inverter
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h18
    h: c4ed772f8539
  review: drafted
- claim_id: c2
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h172
    h: 8eb56217ad74
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=3.r4
    h: c13e93f0382a
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h175
    h: 7a4b0ffa2008
  review: drafted
  review_note: 'support check: partial - Passages show Yaskawa Solectria Solar offers combiners for the
    XGI and has contact info, but don''t explicitly state it manufactures the inverter.'
- claim_id: c3
  rel: certified_to
  target: std:ul-1741
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500-1mw
  note: Listed as UL 1741 2021 for all six models
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:ieee-1547
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h162
    h: 9c7ef4ef17bb
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ieee-1547-1-2020
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h162
    h: 9c7ef4ef17bb
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ieee-1547a-2020
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  note: Edition listed as 107.1-16
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r35
    h: b7e97bacc851
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:fcc-part-15b
  note: Subpart B, Class A
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r38
    h: cb397edb69d7
  review: drafted
- claim_id: c12
  rel: implements
  target: func:remote-firmware-update
  note: Firmware can be updated remotely through the Remote Access Portal or locally
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h142
    h: 5e5a0cc70aea
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r34
    h: bcb96866579d
  review: drafted
- claim_id: c13
  rel: implements
  target: func:constant-power-factor
  note: Adjustable power factor of ±0.80; other ranges apply to certain models
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
  review_note: 'support check: partial - Adjustable power factor ±0.80 is stated, but a constant power
    factor mode is not explicitly named.'
- claim_id: c14
  rel: implements
  target: func:constant-reactive-power
  note: Described as adjustable reactive power
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
  review_note: 'support check: partial - Adjustable reactive power is stated, but constant reactive power
    mode is not explicitly named.'
- claim_id: c15
  rel: implements
  target: func:limit-active-power
  note: Remote power curtailment
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c16
  rel: uses_protocol
  target: proto:ethernet
  note: Two interchangeable Ethernet ports; weather station and DAS add-ons connect over Ethernet
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h115
    h: 34dcdd81dd1d
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h23
    h: 731a890a2f87
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c17
  rel: uses_protocol
  target: proto:wifi
  note: Wi-Fi accessible user interface from a smart device
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h94
    h: 57a76033a3a1
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h23
    h: 731a890a2f87
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c18
  rel: compatible_with
  target: prod:yaskawa-solectria-cr1500-combiner
  note: CR1500-xxP-yyS-400 and CR1500-xxP-yyF-400S remote combiner series
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h172
    h: 8eb56217ad74
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c19
  rel: compatible_with
  target: arch:central-inverter-system
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h18
    h: c4ed772f8539
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
- claim_id: c20
  rel: compatible_with
  target: arch:functionally-grounded-pv-array
  note: DC configuration is DC negative grounded on all models
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=14.r11
    h: 36c582072b76
  review: drafted
  review_note: 'support check: partial - DC negative grounded is stated, but the passage doesn''t name
    a functionally grounded array architecture; this is implied.'
- claim_id: c21
  attr: rated_power
  value:
    nominal: 1
    unit: unit:MegaW
  conditions: Model XGI 1500-1MW-600, continuous real output power (1 MVA)
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=7
    h: 5bc1ed44e431
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=7.r2
    h: 2b0a5d726553
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r13
    h: 0d2125033199
  review: drafted
  review_note: possible conflict with c22 (same source; check the conditions); possible conflict with
    c23 (same source; check the conditions); possible conflict with c24 (same source; check the conditions);
    possible conflict with c25 (same source; check the conditions); possible conflict with c26 (same source;
    check the conditions)
- claim_id: c22
  attr: rated_power
  value:
    nominal: 0.99
    unit: unit:MegaW
  conditions: Model XGI 1500-0.99MW-600 (0.99 MVA)
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=7
    h: 5bc1ed44e431
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r13
    h: 0d2125033199
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c23 (same source; check the conditions); possible conflict with c24 (same source; check the conditions);
    possible conflict with c25 (same source; check the conditions); possible conflict with c26 (same source;
    check the conditions)
- claim_id: c23
  attr: rated_power
  value:
    nominal: 0.85
    unit: unit:MegaW
  conditions: Model XGI 1500-0.85MW-600 (0.85 MVA or 1 MVA versions)
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=7
    h: 5bc1ed44e431
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c24 (same source; check the conditions);
    possible conflict with c25 (same source; check the conditions); possible conflict with c26 (same source;
    check the conditions)
- claim_id: c24
  attr: rated_power
  value:
    nominal: 0.75
    unit: unit:MegaW
  conditions: Model XGI 1500-0.75MW-600 (0.75 MVA or 1 MVA versions)
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=7
    h: 5bc1ed44e431
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r13
    h: 0d2125033199
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c23 (same source; check the conditions);
    possible conflict with c25 (same source; check the conditions); possible conflict with c26 (same source;
    check the conditions)
- claim_id: c25
  attr: rated_power
  value:
    nominal: 0.5
    unit: unit:MegaW
  conditions: Model XGI 1500-0.50MW-600 (0.50 MVA or 1 MVA versions)
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=7
    h: 5bc1ed44e431
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r13
    h: 0d2125033199
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c23 (same source; check the conditions);
    possible conflict with c24 (same source; check the conditions); possible conflict with c26 (same source;
    check the conditions)
- claim_id: c26
  attr: rated_power
  value:
    nominal: 0.498
    unit: unit:MegaW
  conditions: Model XGI 1500-0.498MW-600 (0.498 MVA or 1 MVA versions)
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=7
    h: 5bc1ed44e431
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r13
    h: 0d2125033199
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c23 (same source; check the conditions);
    possible conflict with c24 (same source; check the conditions); possible conflict with c25 (same source;
    check the conditions)
- claim_id: c27
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC weighted average efficiency, all models
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r23
    h: d72cf3a65877
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
  review_note: possible conflict with c28 (same source; check the conditions)
- claim_id: c28
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h19
    h: 26c85640e61d
  review: drafted
  review_note: possible conflict with c27 (same source; check the conditions)
- claim_id: c29
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Nominal AC output voltage, three-phase, all models
  cite:
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: tbl=26.r11
    h: 9213964658bd
  review: drafted
---
The Solectria XGI 1500-1MW is a family of US-built utility-scale modular central inverters from Yaskawa Solectria Solar, offered in six models. Continuous real output ranges from 0.498 MW up to 1 MW depending on model, at a nominal 600 VAC three-phase output, and several models come in a 1 MVA version. The family uses 3-level power conversion with a CEC weighted efficiency of 98.5% and a maximum efficiency of 99.0%, housed in a UL Type 3R outdoor enclosure. The DC side is negative grounded, and the inverters are meant to pair with Solectria CR1500 remote PV combiners. Grid functions include adjustable reactive power, adjustable power factor, and remote power curtailment, and firmware can be updated either remotely or locally. Communication is over two Ethernet ports or a Wi-Fi user interface, and the inverters work with SolrenView monitoring without additional hardware. Listings include UL 1741 (2021) and UL 1741 SB, IEEE 1547-2018 with IEEE 1547.1-2020, UL 1998, CSA C22.2 No. 107.1, and FCC Part 15 Class A, with IEEE 1547 Category B normal and Category III abnormal performance.
