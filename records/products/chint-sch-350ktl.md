---
id: prod:chint-sch-350ktl
type: Product
name: CPS SCH350KTL-DO/US-800
aliases:
- SCH 350 KTL
- SCH 350 KTL DO US 800
- SCH350KTL-DO/US-800
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  attr: rated_power
  value:
    nominal: 350
    unit: unit:KiloW
  conditions: Maximum AC output power (selectable) at PF >0.99; apparent power 350 kVA
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c2
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c3
  attr: mppt_voltage_range
  value:
    min: 880
    max: 1300
    unit: unit:V
  conditions: MPPT voltage range at PF >0.99; operating DC input range is 500-1450 Vdc
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c4
  attr: max_input_current
  value:
    nominal: 40
    unit: unit:A
  conditions: Per MPPT, clipping point; 15 MPP trackers
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  attr: rated_output_current
  value:
    nominal: 253
    unit: unit:A
  conditions: Maximum AC output current at 800 Vac
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r19
    h: 470ad298aadb
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c6
  attr: nominal_voltage
  value:
    nominal: 800
    unit: unit:V
  conditions: Rated AC output voltage, 3-phase / PE grid connection
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r16
    h: d7249c93c182
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c7
  attr: nominal_voltage
  value:
    min: 680
    max: 880
    unit: unit:V
  conditions: AC output voltage operating range
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r17
    h: 05bdbf9b1f6b
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c8
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated output frequency
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r20
    h: 736c8da73a9b
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c9
  attr: frequency
  value:
    min: 57
    max: 63
    unit: unit:HZ
  conditions: Output frequency range
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r21
    h: 0b2ae731a547
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r28
    h: 249c7408f40d
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions)
- claim_id: c11
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r29
    h: 4f501d7e069a
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c12
  rel: implements
  target: func:mppt
  note: 15 MPP trackers, 2 non-fused DC inputs per MPPT
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37
    h: 22ea46d494cf
  review: drafted
- claim_id: c13
  rel: implements
  target: func:surge-protection
  note: Type II surge protection on both DC and AC sides
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r26
    h: 37ac7a1faa7c
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r12
    h: 081ed2495e46
  review: drafted
- claim_id: c14
  rel: implements
  target: func:constant-power-factor
  note: Power factor >0.99, adjustable to ±0.8
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=37.r22
    h: 3417b4611e14
  review: drafted
- claim_id: c15
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r21
    h: 3e2b79ec2d6a
  review: drafted
- claim_id: c16
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r21
    h: 3e2b79ec2d6a
  review: drafted
- claim_id: c17
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r21
    h: 3e2b79ec2d6a
  review: drafted
- claim_id: c18
  rel: certified_to
  target: std:fcc-part-15
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r21
    h: 3e2b79ec2d6a
  review: drafted
- claim_id: c19
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r21
    h: 3e2b79ec2d6a
  review: drafted
- claim_id: c20
  rel: uses_protocol
  target: proto:ieee-2030-5
  note: Listed among certifications and standards
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=38.r21
    h: 3e2b79ec2d6a
  review: drafted
---
The CPS SCH350KTL-DO/US-800 is a CHINT Power Systems three-phase string inverter for 1500 V PV arrays. It connects to an 800 Vac, 60 Hz grid. It delivers up to 350 kW (350 kVA) and up to 253 A of AC output current. It has 15 MPP trackers, each with two non-fused DC inputs, and each tracker clips at 40 A. The MPPT voltage window is 880 to 1300 Vdc. The inverter operates on DC input from 500 to 1450 Vdc and starts at 550 Vdc. Peak efficiency is 99.00% and CEC efficiency is 98.50%. Power factor is above 0.99 and can be adjusted to ±0.8. It has Type II surge protection on both the DC and AC sides, and load-rated DC switches. Firmware upgrades are done by contacting CPS Customer Service. Fault codes include CommErr (communication error), ExtFanErr (cooling fan failure), CfLowErr (flying capacitor voltage too low) and Fault0110 (bus imbalance). For CfLowErr, remove the branch with the lowest input voltage. For Fault0110, raise the DCI limit first, and replace the inverter if the fault does not clear.

<!-- review notes
- sentence 1: support check: partial - 1500 V, three-phase, 800 Vac, 60 Hz are supported, but manufacturer CHINT and 'string inverter' are not stated.
- sentence 1: review: partial - The table supports 3-phase, 1500 V, 800 Vac and 60 Hz, but it does not name CHINT Power Systems or say string inverter.
-->
