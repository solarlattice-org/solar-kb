---
id: prod:yaskawa-solectria-xgi-1500-dcg
type: Product
name: Solectria XGI 1500-DCG
aliases:
- XGI 1500 DCG
- XGI 1500-DCG
- XGI 1500 250 DCG
- XGI 1500-DCG models
- XGI 1500-250-DCG series
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h1
    h: 8e118d3d2649
  - src: src:yaskawa-xgi-1500-dcg-interconnection-guidelines
    loc: sec=h1
    h: 645c74748b80
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h164
    h: ead7ec075abd
  review: drafted
- claim_id: c2
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage, all four DCG models
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=23.r1
    h: fdd9fe2523fd
  review: drafted
- claim_id: c3
  attr: mppt_voltage_range
  value:
    min: 860
    max: 1250
    unit: unit:V
  conditions: Full-power input voltage range, XGI 1500-250/250-600-DCG and XGI 1500-225-600-DCG
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=23.r2
    h: 3d32069aa45b
  review: drafted
- claim_id: c4
  attr: mppt_voltage_range
  value:
    min: 750
    max: 1250
    unit: unit:V
  conditions: Full-power input voltage range, XGI 1500-200/200-480-DCG and XGI 1500-175-480-DCG
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: tbl=23.r2
    h: 3d32069aa45b
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: arch:functionally-grounded-pv-array
  note: Uses a functionally grounded DC negative, which prevents PID in susceptible modules
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h1
    h: 8e118d3d2649
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ul-1741
  note: UL 1741 Edition 3 (09/28/2021)
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h148
    h: 3cd140854ee5
  review: drafted
  review_note: 'support check: partial - The passage says the inverters comply with UL 1741 Edition 3,
    but it says nothing about certification, and it names only the 250 series.'
- claim_id: c7
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h148
    h: 3cd140854ee5
  review: drafted
  review_note: 'support check: partial - The passage says they comply with IEEE 1547-2018, not that they
    are certified, and it names only the 250 series.'
- claim_id: c8
  rel: certified_to
  target: std:ieee-1547-1-2020
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h148
    h: 3cd140854ee5
  review: drafted
  review_note: 'support check: partial - The passage says they comply with IEEE 1547.1-2020, not that
    they are certified, and it names only the 250 series.'
- claim_id: c9
  rel: uses_protocol
  target: proto:wifi
  note: Access from a smart device such as a laptop, tablet or smartphone
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h76
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=2.1.3
    h: 866841f76f1f
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:ethernet
  note: Two interchangeable Ethernet ports in the wire box; used for PC access, weather station and DAS
    add-ons
  cite:
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h76
    h: 3ce8feffcde0
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=2.1.3
    h: 866841f76f1f
  - src: src:yaskawa-xgi-1500-250-dcg-iom-docr-071081-dd
    loc: sec=h97
    h: a8ae78dd57b9
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:yaskawa-solectria-xgi-1500-powerrack
  conditions: XGI 1500-250/250-600-DCG model
  note: PowerRack models PRU-2 through PRU-8 hold two to eight XGI 1500-250/250-600-DCG inverters
  cite:
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=1.r3
    h: 1cb5deec38ca
  - src: src:yaskawa-xgi-1500-powerrack-design-guide-docr-071096-d
    loc: tbl=2.r3
    h: fbf95c7f6781
  review: drafted
---
The Solectria XGI 1500-DCG is a Yaskawa Solectria Solar family of inverters. It has four models: XGI 1500-250/250-600-DCG, 225-600-DCG, 200/200-480-DCG and 175-480-DCG. These inverters use a functionally grounded DC negative, which prevents potential induced degradation in PV modules that are prone to it. Yaskawa Solectria applications engineering must review every project's single-line diagram and transformer configuration. A separate transformer specification guide covers compatibility. Every model accepts a maximum DC input of 1500 V. The full-power input range is 860 to 1250 V on the 250 and 225 models and 750 to 1250 V on the 200 and 175 models. The inverters comply with UL 1741 Edition 3, IEEE 1547.1-2020 and IEEE 1547-2018. That covers Normal Operating Performance Category B and Abnormal Operating Performance Category III. You can reach the inverter over Wi-Fi from a smart device or over Ethernet from a PC. It has two interchangeable Ethernet ports in the wire box, and weather stations and data acquisition systems connect by Ethernet. The inverters work with SolrenView monitoring without extra hardware, and third-party monitoring platforms are also supported. The 250 kW DCG model is the inverter used in XGI 1500 PowerRack assemblies, which hold from two to eight units.

<!-- review notes
- sentence 1: support check: partial - The four models and the Yaskawa Solectria Solar link are supported, but 'family of inverters' is only implied (the passage calls the models a family).
- sentence 3: support check: partial - The required review is stated, and a transformer specification guide for compatibility exists, but only its title is given, so 'covers compatibility' is inferred.
-->
