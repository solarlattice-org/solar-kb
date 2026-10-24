---
id: prod:canadian-solar-125ktl-gs-e
type: Product
name: CSI-125KTL-GS-E
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: sec=1.1
    h: 10ac41ff3a63
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Three-phase grid-tied PV inverter, transformerless topology
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: sec=1.1
    h: 10ac41ff3a63
  review: drafted
  review_note: 'support check: partial - Passage shows it''s a three-phase inverter converting DC to AC
    feeding the grid, but transformerless topology isn''t in this passage.'
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r33
    h: 54f7eea77dc2
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:ethernet
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r33
    h: 54f7eea77dc2
  review: drafted
- claim_id: c5
  rel: implements
  target: func:remote-firmware-update
  note: Datasheet lists OTA update as supported
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r34
    h: a5b64fbb8583
  review: drafted
- claim_id: c6
  rel: implements
  target: func:mppt
  note: Single MPPT
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r7
    h: 176ad44815a4
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r18
    h: 3c9c8677fb3d
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:cpuc-rule-21
  note: Listed including Rule 21 Phase II and III
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:ul-1699b
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c12
  rel: certified_to
  target: std:ieee-1547
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  rel: certified_to
  target: std:fcc-part-15
  note: Class A and B
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: drafted
- claim_id: c14
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r29
    h: 83e27d6aa879
  review: drafted
- claim_id: c15
  attr: max_input_voltage
  value:
    max: 1500
    unit: unit:V
  conditions: Maximum DC input voltage
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r1
    h: 9319b4374a90
  review: drafted
- claim_id: c16
  attr: max_input_current
  value:
    max: 150
    unit: unit:A
  conditions: Maximum DC input current, inverter has a single MPPT
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r5
    h: 7be2e2c95c23
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r7
    h: 176ad44815a4
  review: drafted
- claim_id: c17
  attr: rated_output_current
  value:
    nominal: 120
    unit: unit:A
  conditions: Rated AC output current
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r12
    h: 0ea241078b86
  review: drafted
- claim_id: c18
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Rated grid voltage, three-phase plus PE
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r11
    h: 44ddabd44010
  review: drafted
- claim_id: c19
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated grid frequency
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r15
    h: e1b1d3f4f34e
  review: drafted
- claim_id: c20
  attr: efficiency
  value:
    nominal: 99.1
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r16
    h: a9561566ff16
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions)
- claim_id: c21
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: EU (European weighted) efficiency
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r17
    h: 5ced0dbce29f
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions)
- claim_id: c22
  attr: operating_temperature
  value:
    min: -25
    max: 60
    unit: unit:DEG_C
  conditions: Operating ambient temperature range
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r23
    h: 006e7600084b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c23
  attr: max_count
  value:
    max: 20
    unit: unit:NUM
  conditions: Maximum number of input strings on the single MPPT
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: tbl=12.r7
    h: 176ad44815a4
  review: drafted
---
The CSI-125KTL-GS-E is a Canadian Solar three-phase grid-tied inverter. It converts DC power from a PV array into AC power for local loads and for export to the grid. It uses a transformerless design with fan cooling. The enclosure is rated NEMA 4X/IP65 and the display is an LCD. On the DC side it takes up to 1500 V and up to 150 A. It has one MPPT that accepts up to 20 strings through MC4 connectors. On the AC side it connects to a 600 V three-phase grid at 60 Hz and delivers a rated output current of 120 A. The datasheet gives a maximum efficiency of 99.1 percent, an EU efficiency of 98.6 percent and an operating ambient range of -25 to 60 degrees C. It communicates over RS485 or Ethernet and supports over-the-air firmware updates. It is listed to UL 1741, UL 1741 SA, Rule 21, UL 1998, UL 1699B, IEEE 1547, FCC Part 15 and CSA C22.2 107.1. If the OV-BUS alarm appears, the inverter has seen excessive voltage on its internal DC bus. Measure the DC and AC voltages and compare them with the LCD readings. Internal damage or a wire that came loose in shipping may mean the inverter must be replaced.

<!-- review notes
- sentence 1: support check: partial - Canadian Solar three-phase inverter converting DC to AC for loads and grid is stated, but 'grid-tied' is only supported via title/feed-grid wording; broadly supported though export wording is fine—minor.
- sentence 8: support check: partial - Passage supports high internal DC bus voltage, measuring DC/AC and comparing to LCD, internal damage/loose wire, replace inverter; 'may mean must be replaced' is loosely stated.
-->
