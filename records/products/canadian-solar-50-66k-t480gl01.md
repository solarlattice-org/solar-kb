---
id: prod:canadian-solar-50-66k-t480gl01
type: Product
name: CSI-50/60/66K-T480GL01-UB
aliases:
- CSI-50K-T480GL01-UB
- CSI-60K-T480GL01-UB
- CSI-66K-T480GL01-UB
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  note: Manual published by CSI Solar Co., Ltd.
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=1.1
    h: 0c121e513fd9
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=h1
    h: 4606d502bf47
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=1.1
    h: 0c121e513fd9
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: arch:grid-tied-pv
  scope:
    applications:
    - on-grid
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=1.1
    h: 0c121e513fd9
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: sec=h1
    h: 4606d502bf47
  review: drafted
- claim_id: c4
  rel: implements
  target: func:dc-arc-fault-protection
  note: Integrated AFCI listed for all three models
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r34
    h: fed76822c9f2
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r34
    h: 748809acd862
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r34
    h: 65eea733c8d6
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=20.r17
    h: 1d1150897002
  review: drafted
  review_note: 'support check: partial - Interface RS485 is stated only for the 66K model; other models
    not shown in the passage.'
- claim_id: c6
  rel: uses_protocol
  target: proto:wifi
  note: Wi-Fi is optional
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=20.r17
    h: 1d1150897002
  review: drafted
  review_note: 'support check: partial - Optional WiFi is stated only for the 66K model row.'
- claim_id: c7
  attr: rated_power
  value:
    nominal: 50
    unit: unit:KiloW
  conditions: CSI-50K-T480GL01-UB at 480 V
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=6
    h: 1cd4d61bc461
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions)
- claim_id: c8
  attr: rated_power
  value:
    nominal: 60
    unit: unit:KiloW
  conditions: CSI-60K-T480GL01-UB at 480 V
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=6
    h: 1cd4d61bc461
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions)
- claim_id: c9
  attr: rated_power
  value:
    nominal: 66
    unit: unit:KiloW
  conditions: CSI-66K-T480GL01-UB at 480 V
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=6
    h: 1cd4d61bc461
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions)
- claim_id: c10
  attr: rated_output_current
  value:
    max: 60.2
    unit: unit:A
  conditions: Maximum output current, CSI-50K-T480GL01-UB
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r20
    h: 79723a524b0f
  review: drafted
- claim_id: c11
  attr: rated_output_current
  value:
    max: 79.4
    unit: unit:A
  conditions: Maximum output current, CSI-66K-T480GL01-UB
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r20
    h: 034713615d7a
  review: drafted
- claim_id: c12
  attr: max_input_voltage
  value:
    max: 1000
    unit: unit:V
  conditions: Maximum DC input voltage, all three models
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r3
    h: 2b45f112b911
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r3
    h: 808a7b2e0998
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r3
    h: 6e2fc72d7edd
  review: drafted
- claim_id: c13
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Nominal AC grid voltage
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=6
    h: 1cd4d61bc461
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r15
    h: b75771d74997
  review: drafted
- claim_id: c14
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Nominal grid frequency, all three models
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r17
    h: 9e44da0e167e
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r17
    h: 3661d3f32777
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r17
    h: fa6531d06449
  review: drafted
- claim_id: c15
  attr: frequency
  value:
    min: 59.5
    max: 60.5
    unit: unit:HZ
  conditions: Operating frequency range, all three models
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r18
    h: e977f1b4ec43
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r18
    h: 43bcae587028
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r18
    h: 829839be2bab
  review: drafted
- claim_id: c16
  attr: efficiency
  value:
    nominal: 98.8
    unit: unit:PERCENT
  conditions: Peak efficiency, all three models
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r30
    h: 59e0eaa2df4e
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r30
    h: 0a1f35a880a4
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r30
    h: e58401546918
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions)
- claim_id: c17
  attr: efficiency
  value:
    nominal: 98.4
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, all three models
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r31
    h: 89e8b1d74f71
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=17.r31
    h: 041af831aa85
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=15.r31
    h: c5fdfe42e7ad
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c18 (same source; check the conditions)
- claim_id: c18
  attr: efficiency
  value:
    min: 99.9
    unit: unit:PERCENT
  conditions: MPPT efficiency, CSI-66K-T480GL01-UB
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=19.r32
    h: 3c007cc76fdf
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions)
- claim_id: c19
  attr: operating_temperature
  value:
    min: -25
    max: 60
    unit: unit:DEG_C
  conditions: Ambient operating temperature range, all three models
  cite:
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=20.r7
    h: 11d4e8802600
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=18.r7
    h: daef79e24450
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=16.r7
    h: 74113c64845e
  review: drafted
---
The CSI-50/60/66K-T480GL01-UB is a family of Canadian Solar three-phase grid-tied string inverters that turn PV array DC power into AC for local loads and the grid. The family has three models, rated 50 kW, 60 kW and 66 kW, all on a 480 V grid. Every model takes up to 1000 V DC input and runs at a nominal 60 Hz, with an operating range of 59.5 to 60.5 Hz. Maximum output current is 60.2 A on the 50K model and 79.4 A on the 66K model. Peak efficiency is 98.8 percent and CEC weighted efficiency is 98.4 percent. The units have built-in DC arc-fault protection (AFCI) and are rated for ambient temperatures from -25 to 60 °C. They communicate over RS485, and WiFi is available as an option.

<!-- review notes
- sentence 1: support check: partial - Canadian Solar three-phase grid-tied inverters supported, but 'string' inverter type is not stated.
- sentence 3: support check: partial - 1000 V is shown for all models, but nominal frequency and range are shown only for the 66K model.
- sentence 7: support check: partial - RS485 and optional WiFi are shown only for the 66K model.
-->
