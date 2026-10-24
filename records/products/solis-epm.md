---
id: prod:solis-epm
type: Product
name: Solis Export Power Manager
aliases:
- EPM
- EPM3-5G-PRO
- EPM 5G-PLUS
- Solis-EPM3-5G-PRO
- Export Device
category: Monitoring and communications
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=h1
    h: e5cbc10f6189
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  review: drafted
- claim_id: c2
  rel: implements
  target: func:export-limitation
  note: Controls inverter output so grid export (backflow) does not exceed the set limit, based on meter
    and CT measurements.
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.8
    h: 95879712d1dd
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.7
    h: c2f13baa5004
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c3
  rel: implements
  target: func:communication-loss-fallback
  note: 'FailSafe setting: inverters stop or go to low generation if communications, CTs or EPM power
    fail.'
  cite:
  - src: src:kb-solis-44002027137-export-power-manager-setup-5g-plus
    loc: sec=h1
    h: 4eff29975b94
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: arch:grid-tied-pv
  scope:
    regions:
    - region:us
  conditions: All Solis grid-tied US models, single-phase and three-phase
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:solis-1p-4g-us
  conditions: Required for export control of systems with multiple inverters; a single single-phase inverter
    needs only the meter and CTs
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: sec=3.7
    h: 837fee14e4ce
  - src: src:solis-solis-export-power-control-application-note-v2-2-20250729
    loc: sec=h5
    h: 19d63137bc9c
  review: drafted
  review_note: 'support check: partial - Passages show the EPM is required for multiple inverters and
    the kit lists the Solis-1P(3.6-10)K-4G-US manual, but the explicit compatibility with that model is
    only implied and the single-inverter case is stated generally, not for this model.'
- claim_id: c6
  rel: incompatible_with
  target: arch:hybrid-inverter-system
  scope:
    regions:
    - region:us
  note: Hybrid inverters manage export themselves via CTs or meter plus CTs connected directly to the
    inverter.
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  review: drafted
- claim_id: c7
  rel: incompatible_with
  target: arch:ac-coupled-storage
  scope:
    regions:
    - region:us
  conditions: Not compatible with any energy storage inverter models
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:rs485
  note: Inverters daisy-chained via RS485; meter and logger connect to EPM over RS485.
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.8
    h: 95879712d1dd
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.7
    h: c2f13baa5004
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: sec=3.7
    h: 837fee14e4ce
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:modbus
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.8
    h: 95879712d1dd
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.7
    h: c2f13baa5004
  - src: src:kb-solis-44002027137-export-power-manager-setup-5g-plus
    loc: sec=h1
    h: 4eff29975b94
  review: drafted
- claim_id: c10
  rel: requires
  target: prod:acrel-agf-ae-d-200
  conditions: Single-phase systems with multiple inverters; supplied with two split-core CTs
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.8
    h: 95879712d1dd
  - src: src:solis-solis-export-power-control-application-note-v2-2-20250729
    loc: sec=h5
    h: 19d63137bc9c
  review: drafted
- claim_id: c11
  rel: requires
  target: prod:acrel-adl-3000
  conditions: Three-phase systems; supplied with three split-core CTs
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.7
    h: c2f13baa5004
  review: drafted
- claim_id: c12
  rel: has_hazard
  target: hazard:electric-shock
  note: Removing CTs under load opens the CT secondary, producing high voltage; do not perform the CT
    failure witness test under load.
  cite:
  - src: src:kb-solis-44002027137-export-power-manager-setup-5g-plus
    loc: sec=h1
    h: 4eff29975b94
  review: drafted
- claim_id: c13
  attr: max_count
  value:
    max: 10
    unit: unit:NUM
  conditions: Inverters per EPM when a Solis logger is used for monitoring; above this a third-party gateway
    is needed and FOMware is recommended
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.8
    h: 95879712d1dd
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=3.7
    h: c2f13baa5004
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: sec=3.7
    h: 837fee14e4ce
  review: drafted
- claim_id: c14
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Three-phase systems; EPM sold alone with three-phase meter and CTs
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions)
- claim_id: c15
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Three-phase systems; EPM sold alone with three-phase meter and CTs
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions)
- claim_id: c16
  attr: nominal_voltage
  value:
    nominal: 240
    unit: unit:V
  conditions: Single-phase systems; EPM sold as a kit with single-phase meter and CTs
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=1.1
    h: 92a1e237298d
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c15 (same source; check the conditions)
---
The Solis Export Power Manager (EPM) is a controller that watches how much power the site sends back to the grid and holds it below a limit you set. It works with all Solis grid-tied US inverters, single-phase and three-phase. It does not work with energy storage or hybrid inverters, because those control export themselves through their own CTs or meter. Three-phase 480 V and 600 V systems use an Acrel ADL 3000 meter with three split-core CTs. Single-phase 240 V systems with more than one inverter use an Acrel AGF-AE-D/200 meter with two CTs. The meter reports to the EPM over RS485 Modbus. The inverters are daisy-chained on RS485, and the Solis logger or a third-party gateway connects to the EPM. A Solis logger can handle at most 10 inverters. For larger systems, for third-party monitoring or for commercial 600 VAC sites, Solis recommends FOMware instead. A failsafe setting makes the inverters stop or drop to low output if communication, the CTs or the EPM's power supply fails. CT phase rotation and polarity must match the voltage connections: P1 faces the grid, and active power should read positive when exporting. Never remove the CTs under load. The open CT secondary can develop a dangerous high voltage.

<!-- review notes
- sentence 3: support check: partial - The ADL 3000 with three CTs is stated for three-phase systems and the AGF-AE-D/200 with two CTs for single-phase multi-inverter systems, but the pairing of the ADL 3000 specifically with 480/600 V is only implied.
- sentence 7: support check: partial - Phase rotation matching voltage, P1 on grid side and positive active power meaning export are stated, but polarity is not stated as having to match the voltage connections.
-->
