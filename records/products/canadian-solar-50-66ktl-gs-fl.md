---
id: prod:canadian-solar-50-66ktl-gs-fl
type: Product
name: CSI-50/60/66KTL-GS-FL
aliases:
- CSI-50KTL-GS-FL
- CSI-60KTL-GS-FL
- CSI-66KTL-GS-FL
- CSI-50KTL-GS
- CSI-60KTL-GS
- CSI-66KTL-GS
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=h4
    h: 457d53016613
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=1.1
    h: 4ca42001f1a4
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Three-phase grid-tied PV inverter that converts DC from the PV array to AC for local loads and
    the grid.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: sec=1.1
    h: 4ca42001f1a4
  review: drafted
- claim_id: c3
  attr: rated_power
  value:
    nominal: 50
    unit: unit:KiloW
  conditions: CSI-50KTL-GS-FL and CSI-50KTL-GS
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r5
    h: 39692e0bbd5c
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=4
    h: 9494d62ae21a
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions)
- claim_id: c4
  attr: rated_power
  value:
    nominal: 60
    unit: unit:KiloW
  conditions: CSI-60KTL-GS
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r5
    h: 2d5bbbfe8255
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=4
    h: 9494d62ae21a
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions)
- claim_id: c5
  attr: rated_power
  value:
    nominal: 66
    unit: unit:KiloW
  conditions: CSI-66KTL-GS
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r5
    h: 2d5bbbfe8255
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=4
    h: 9494d62ae21a
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions)
- claim_id: c6
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated AC grid voltage, all models
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r7
    h: 0cbe6c7ce074
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r7
    h: a78e7f9831bc
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=4
    h: 9494d62ae21a
  review: drafted
- claim_id: c7
  attr: rated_output_current
  value:
    nominal: 60.2
    unit: unit:A
  conditions: Rated grid output current, CSI-50KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r10
    h: e31fa652cfeb
  review: drafted
- claim_id: c8
  attr: efficiency
  value:
    min: 98.8
    unit: unit:PERCENT
  conditions: Maximum efficiency, CSI-50KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r15
    h: d2f08153561d
  review: drafted
- claim_id: c9
  attr: efficiency
  value:
    min: 98.8
    unit: unit:PERCENT
  conditions: Maximum efficiency, CSI-60KTL-GS and CSI-66KTL-GS
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r15
    h: ec814b828491
  review: drafted
- claim_id: c10
  attr: frequency
  value:
    min: 59.5
    max: 60.5
    unit: unit:HZ
  conditions: Operating range of utility frequency, CSI-50KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r25
    h: b6c26b60f172
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: e45b121aaf9c
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r26
    h: 8f0d98bb63fa
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:ieee-1547
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: e45b121aaf9c
  review: drafted
  review_note: 'support check: partial - IEEE1547 is listed as compliance for the 50 kW model; 60/66 passage
    shows garbled ''IEEE1S47'', and ''certified'' is stronger than ''compliance'' listing.'
- claim_id: c13
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: e45b121aaf9c
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r26
    h: 8f0d98bb63fa
  review: drafted
- claim_id: c14
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: e45b121aaf9c
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r26
    h: 8f0d98bb63fa
  review: drafted
- claim_id: c15
  rel: certified_to
  target: std:fcc-part-15
  note: Class B
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: e45b121aaf9c
  review: drafted
- claim_id: c16
  rel: uses_protocol
  target: proto:wifi
  note: Listed as an interface option
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r23
    h: 8fdc3a52def5
  review: drafted
  review_note: 'support check: partial - WIFI listed as interface only for the 60/66 models in the passage,
    not the -FL model.'
- claim_id: c17
  rel: uses_protocol
  target: proto:cellular
  note: GPRS listed as optional interface
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r23
    h: 8fdc3a52def5
  review: drafted
  review_note: 'support check: partial - GPRS optional interface is listed only for the 60/66 models,
    not the -FL model; GPRS as cellular is implied.'
- claim_id: c18
  rel: implements
  target: func:surge-protection
  note: Protection listed as DC class II, AC class III optional
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r16
    h: 013a0e96a248
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=12.r16
    h: 5e85fdf490d0
  review: drafted
---
The CSI-50/60/66KTL-GS-FL family is a line of Canadian Solar three-phase grid-tied PV inverters. They convert DC from the array into AC that can supply local loads and feed the grid. The manual covers four models: CSI-50KTL-GS-FL, CSI-50KTL-GS, CSI-60KTL-GS and CSI-66KTL-GS. They are rated at 50, 60 and 66 kW on a 480 V AC grid. The 50 kW models have a rated grid output current of 60.2 A, and the manual's maximum efficiency figure is above 98.8 percent. The units are transformerless, NEMA 4X enclosures. Surge protection is DC class II, with AC class III as an option. Over- and under-voltage and frequency trip times can be set in the grid protection settings. Listed compliance includes CSA C22.2 No. 107.1, UL 1741, IEEE 1547, UL 1998 and FCC Part 15 Class B.
