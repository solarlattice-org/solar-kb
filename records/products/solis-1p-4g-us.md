---
id: prod:solis-1p-4g-us
type: Product
name: Solis-1P(3.6-10)K-4G-US
aliases:
- Solis-1P3.6K-4G-US
- Solis-1P5K-4G-US
- Solis-1P6K-4G-US
- Solis-1P7.6K-4G-US
- Solis-1P10K-4G-US
- 4G Series Grid Inverter
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: sec=h1
    h: 4e1ce5097420
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: sec=h1
    h: bb2931c108ba
  review: drafted
  review_note: 'support check: partial - Manuals cover the model but the passages never name Solis as
    the maker explicitly beyond the title/model name.'
- claim_id: c2
  rel: implements
  target: func:dc-arc-fault-protection
  note: The manual has an ARC Fault section, and the inverter self-checks its AFCI module.
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=2.r7
    h: cd96a74c5033
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=15.r1
    h: b7cb293629dc
  review: drafted
  review_note: 'support check: partial - ARC Fault section and AFCI self-check fault imply AFCI, but protection
    is not explicitly stated.'
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  conditions: Standard on the 6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=21.r4
    h: 2ea95cfaeae7
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=17.r4
    h: 373f34fde685
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:cellular
  conditions: Optional on the 6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=21.r4
    h: 2ea95cfaeae7
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=17.r4
    h: 373f34fde685
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:wifi
  conditions: Optional on the 6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=21.r4
    h: 2ea95cfaeae7
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=17.r4
    h: 373f34fde685
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ul-1741-sb
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ul-1741-sa
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ieee-1547-2018
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:ul-1699b
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:ul-1998
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:fcc-part-15
  conditions: Class B; listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:cpuc-rule-21
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c13
  rel: certified_to
  target: std:hawaiian-electric-rule-14h
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c14
  rel: certified_to
  target: req:nfpa-70-2020-690-12
  conditions: Listed for the 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r34
    h: 1d747aa33885
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r34
    h: b3ad7cd7efc0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r34
    h: 11e760a952d0
  review: drafted
- claim_id: c15
  attr: rated_power
  value:
    nominal: 6
    unit: unit:KiloW
  conditions: Solis-1P6K-4G-US rated output power
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r9
    h: 4a55715d98d4
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions)
- claim_id: c16
  attr: rated_power
  value:
    nominal: 7.6
    unit: unit:KiloW
  conditions: Solis-1P7.6K-4G-US rated output power
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r9
    h: 4b9ce6e67bef
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions)
- claim_id: c17
  attr: rated_power
  value:
    nominal: 10
    unit: unit:KiloW
  conditions: Solis-1P10K-4G-US rated output power
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r9
    h: 7275a7482dc6
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions)
- claim_id: c18
  attr: max_input_voltage
  value:
    max: 600
    unit: unit:V
  conditions: Solis-1P6K, 7.6K and 10K-4G-US models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r1
    h: 1872a76773f6
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r1
    h: f42b376c9ded
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r1
    h: 027090ae8775
  review: drafted
- claim_id: c19
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Grid frequency, 6K, 7.6K and 10K models
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r14
    h: 51b2b1e56d65
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r14
    h: f86d50da1a5d
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r14
    h: 3b01391ab607
  review: drafted
- claim_id: c20
  attr: frequency
  value:
    min: 59.5
    max: 60.5
    unit: unit:HZ
  conditions: Grid frequency range, Solis-1P10K-4G-US
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r15
    h: a67a216425c5
  review: drafted
- claim_id: c21
  attr: efficiency
  value:
    nominal: 96.6
    unit: unit:PERCENT
  conditions: CEC efficiency, Solis-1P3.6K-4G-US
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=15.r22
    h: 8ba0ef81a0bf
  review: disputed
  review_note: possible conflict with c22 (same source; check the conditions)
  conflicts_with:
  - prod:solis-1p-4g-us#c23
- claim_id: c22
  attr: efficiency
  value:
    nominal: 97.1
    unit: unit:PERCENT
  conditions: CEC efficiency, Solis-1P5K-4G-US
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=17.r22
    h: b42615ebeed0
  review: disputed
  review_note: possible conflict with c21 (same source; check the conditions)
  conflicts_with:
  - prod:solis-1p-4g-us#c23
- claim_id: c23
  attr: efficiency
  value:
    nominal: 97.5
    unit: unit:PERCENT
  conditions: CEC efficiency, Solis-1P6K, 7.6K and 10K-4G-US
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=18.r22
    h: 9b7c9a100e56
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=20.r22
    h: e8e4e250c5d0
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=16.r22
    h: bb1f90059e6d
  review: disputed
  conflicts_with:
  - prod:solis-1p-4g-us#c21
  - prod:solis-1p-4g-us#c22
---
The Solis-1P 4G-US is a family of single-phase grid-tied inverters made by Solis, with models from 3.6K to 10K. The 6K, 7.6K and 10K models are rated at 6 kW, 7.6 kW and 10 kW of output, accept up to 600 V DC input and run on a 60 Hz grid. CEC efficiency is 96.6% on the 3.6K, 97.1% on the 5K and 97.5% on the 6K through 10K models. The 7.6K and 10K models use a transformerless topology and have an LCD display. RS-485 is the standard communication interface, and cellular or Wi-Fi are available as options. The inverter has DC arc-fault protection. An AFCI Check FAULT alarm means the AFCI module failed its self-check. To clear it, reset the inverter by switching the DC off and back on, and replace the inverter if the fault returns.

<!-- review notes
- sentence 1: support check: partial - Models 3.6K–10K and Solis name shown, but single-phase and grid-tied are only loosely implied (1P, grid inverter).
- sentence 4: support check: partial - Transformerless stated for both, but LCD display only given for the 10K, not 7.6K.
- sentence 6: support check: partial - AFCI self-check fault and reset/replace steps are stated, but DC arc-fault protection is only implied by the section title and 'if the fault returns' is an interpretation.
-->
