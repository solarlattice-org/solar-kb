---
id: prod:sma-sunny-tripower-x
type: Product
name: Sunny Tripower X (international)
aliases:
- STP X
- STP 12-25-50
- STPX
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:ethernet
  note: Two Ethernet ports on each model.
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r41
    h: 399fbb2e2ea2
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:wifi
  note: Listed as local WLAN.
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r41
    h: 399fbb2e2ea2
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: RS485 client interface marked as optional in the data sheet.
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r41
    h: 399fbb2e2ea2
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:sma-modbus
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r41
    h: 399fbb2e2ea2
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:sunspec-modbus
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r41
    h: 399fbb2e2ea2
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:speedwire
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r41
    h: 399fbb2e2ea2
  - src: src:sma-doc-278405
    loc: tbl=40
    h: 7c2a90c9d147
  review: drafted
- claim_id: c7
  rel: implements
  target: func:system-manager
  scope:
    firmware_min: 02.06.04.R
  conditions: STP 12-50, STP 15-50, STP 20-50 and STP 25-50
  cite:
  - src: src:sma-doc-275857
    loc: tbl=3.r11
    h: 3f2a47524d95
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: prod:sma-sunny-tripower-smart-energy
  scope:
    firmware_min: 03.14.20.R
  conditions: Smart Energy runs as a subordinate device under a Sunny Tripower X 25 acting as System Manager
  cite:
  - src: src:sma-kb-is-the-sunny-tripower-x-as-a-system-manager-compatible-with-the-sunny-tripower-smar
    loc: sec=h1
    h: 639dfc70649d
  review: drafted
- claim_id: c9
  rel: compatible_with
  target: prod:sma-sunny-boy-smart-energy
  scope:
    firmware_min: 03.14.20.R
  conditions: SBSExx-50 runs as a subordinate device under a Sunny Tripower X 25 acting as System Manager
  cite:
  - src: src:sma-kb-is-the-sunny-tripower-x-as-a-system-manager-compatible-with-the-sunny-tripower-smar
    loc: sec=h1
    h: 639dfc70649d
  review: drafted
- claim_id: c10
  rel: implements
  target: func:dc-arc-fault-protection
  note: Arc-fault circuit interrupter (AFCI).
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r26
    h: 846a663c70db
  review: drafted
- claim_id: c11
  rel: implements
  target: func:iv-curve-scan
  note: Listed as I-V generator diagnostics.
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r26
    h: 846a663c70db
  review: drafted
  review_note: 'support check: partial - I-V generator diagnostics is listed, but equating it with I-V
    curve scan is an inference not stated in the passage.'
- claim_id: c12
  rel: implements
  target: func:ground-fault-protection
  note: Listed as ground fault monitoring.
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r23
    h: 17cfd1539a38
  review: drafted
- claim_id: c13
  rel: certified_to
  target: std:nrs-097-2-1
  note: NRS 097-2-1:2017
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r49
    h: 4eda273ae4a5
  review: drafted
- claim_id: c14
  rel: certified_to
  target: std:ena-erec-g99
  note: EREC G99/1-8:2021
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r49
    h: 4eda273ae4a5
  review: drafted
- claim_id: c15
  rel: certified_to
  target: std:synergrid-c10-11
  note: C10/C11:2019 & V1:2020
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r49
    h: 4eda273ae4a5
  review: drafted
- claim_id: c16
  rel: certified_to
  target: std:din-vde-v-0126-1-1
  note: VDE 0126-1-1:2013/A1:2012
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r49
    h: 4eda273ae4a5
  review: drafted
- claim_id: c17
  attr: rated_output_current
  value:
    nominal: 29
    unit: unit:A
  conditions: Sunny Tripower X 20, rated output current
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r16
    h: d7d22025d8d8
  review: drafted
  review_note: possible conflict with c19 (same source; check the conditions); possible conflict with
    c20 (same source; check the conditions)
- claim_id: c18
  attr: rated_output_current
  value:
    max: 36.6
    unit: unit:A
  conditions: Sunny Tripower X 20 and X 25, maximum output current
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r16
    h: d7d22025d8d8
  review: drafted
  review_note: 'support check: partial - Max output current of 36.6 A for X 20 and X 25 is stated, but
    it is a maximum current, not a rated current as the ''rated output current'' attribute and ''up to''
    wording suggest.'
- claim_id: c19
  attr: rated_output_current
  value:
    nominal: 36.2
    unit: unit:A
  conditions: Sunny Tripower X 25, rated output current
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r16
    h: d7d22025d8d8
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c20 (same source; check the conditions)
- claim_id: c20
  attr: rated_output_current
  value:
    nominal: 17.4
    unit: unit:A
  conditions: Sunny Tripower X 12, rated output current
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r16
    h: d7d22025d8d8
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c19 (same source; check the conditions)
- claim_id: c21
  attr: operating_temperature
  value:
    min: -25
    max: 60
    unit: unit:DEG_C
  conditions: Operating temperature range, all four models
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r31
    h: 665d2c514830
  review: drafted
- claim_id: c22
  attr: max_input_voltage
  value:
    max: 1000
    unit: unit:V
  conditions: Sunny Tripower X 15 and X 20
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r3
    h: a450206e07f1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c23
  attr: max_input_current
  value:
    max: 24
    unit: unit:A
  conditions: Maximum usable input current per MPP tracker, all four models
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r7
    h: 74fc044577d2
  review: drafted
- claim_id: c24
  attr: nominal_voltage
  value:
    nominal: 230
    unit: unit:V
  conditions: Rated grid voltage, line to neutral
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r15
    h: bbd06427f99a
  review: drafted
  review_note: possible conflict with c25 (same source; check the conditions)
- claim_id: c25
  attr: nominal_voltage
  value:
    nominal: 400
    unit: unit:V
  conditions: Nominal AC voltage line to line in the 230 V / 400 V grid option; 220/380 V and 240/415
    V also listed
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r12
    h: 412851b5ab20
  review: drafted
  review_note: possible conflict with c24 (same source; check the conditions)
- claim_id: c26
  attr: frequency
  value:
    nominal: 50
    unit: unit:HZ
  conditions: Rated grid frequency
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r15
    h: bbd06427f99a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c27
  attr: efficiency
  value:
    nominal: 98.2
    unit: unit:PERCENT
  conditions: Maximum efficiency, all four models
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r20
    h: f5796fa11b4f
  review: drafted
  review_note: possible conflict with c28 (same source; check the conditions)
- claim_id: c28
  attr: efficiency
  value:
    min: 97.6
    max: 98
    unit: unit:PERCENT
  conditions: European efficiency across the X 12 to X 25 models
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r20
    h: f5796fa11b4f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - European efficiency values 97.6–98.0% are listed, but the rows
    are ambiguous about which value applies to which model; range plausible though.; possible conflict
    with c27 (same source; check the conditions)'
- claim_id: c29
  attr: max_count
  value:
    nominal: 5
    unit: unit:NUM
  conditions: Number of managed devices (inverters, charging stations and energy meters) listed in the
    data sheet
  cite:
  - src: src:sma-doc-278883
    loc: tbl=1.r53
    h: cdad64917793
  review: drafted
  review_note: 'support check: partial - The value 5 is listed for a row labeled only ''(inverters, charging
    stations and energy meters)''; the heading for managed devices is truncated, though the context is
    implied.'
---
The Sunny Tripower X is a family of three-phase string inverters for the international market. It comes in four models: Sunny Tripower X 12, 15, 20 and 25, with type designations STP 12-50 to STP 25-50. Each model has a maximum efficiency of 98.2 percent and a rated grid connection of 230 V at 50 Hz. Each MPP tracker accepts up to 24 A of input current, and the units run from -25 to +60 degrees C. It communicates over two Ethernet ports, local WLAN and an optional RS485 interface. It supports SMA Modbus, SunSpec Modbus and Speedwire. The inverter can act as System Manager from firmware 02.06.04.R. With firmware 03.14.20.R or later, a Sunny Tripower X 25 can manage Sunny Tripower Smart Energy and Sunny Boy Smart Energy units as subordinate devices. Protection features include an arc-fault circuit interrupter, I-V generator diagnostics and ground fault monitoring. The enclosure is rated IP65. Listed approvals include EREC G99, NRS 097-2-1, C10/C11 and VDE 0126-1-1. Known issue: the fans can be loud. Firmware 02.06.04.R improved the fan control, and units built from June 21, 2023 have only one internal fan. From firmware 03.02.07.R, the web interface is reached over https instead of http.

<!-- review notes
- sentence 1: support check: partial - Type designations and four models are supported, but 'three-phase string inverters for the international market' is not clearly stated (only an output row '3 / 2').
- sentence 1: review: partial - The four models and the STP 12-50 to 25-50 designations are stated, but 'three-phase' rests only on an unexplained '3 / 2' output row, and 'string inverters' and 'international market' are not in the passages.
-->
