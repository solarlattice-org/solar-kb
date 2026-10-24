---
id: prod:enphase-m215-m250
type: Product
name: Enphase M215 / M250 Microinverters
aliases:
- Enphase M215
- Enphase M250
- M215-60
- M250-60
- M250-72
- M215-60-2LL-S22
- M215-60-2LL-S22-IG
- Enphase M250-60
- Enphase M250-72
- IQ 7-based M215
category: Inverters
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: sec=h1
    h: 901cd6e4281c
  - src: src:enphase-enphase-m215-m250-on-iq7-platform-installation-guide
    loc: sec=h1
    h: d04737869a36
  review: drafted
  review_note: 'support check: partial - Passages name Enphase M250/M215 microinverters and ''Enphase
    Energy'' customer support, but don''t explicitly state Enphase Energy makes them, though strongly
    implied.'
- claim_id: c2
  rel: instance_of
  target: comp:microinverter
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: sec=h1
    h: 901cd6e4281c
  - src: src:enphase-enphase-m215-m250-on-iq7-platform-installation-guide
    loc: sec=h1
    h: d04737869a36
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:power-line-communication
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=27.r9
    h: 15f9e69b3cd5
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=24.r8
    h: b4b4418a62eb
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=18.r8
    h: 15646e958dbe
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=21.r8
    h: c8ebf4ca0b6b
  review: drafted
- claim_id: c4
  rel: implements
  target: func:ground-fault-protection
  note: IQ 7-based M215/M250 expansion models; Class II double-insulated rating includes ground fault
    protection
  cite:
  - src: src:enphase-enphase-m215-m250-on-iq7-platform-installation-guide
    loc: sec=h1
    h: d04737869a36
  review: drafted
- claim_id: c5
  rel: requires
  target: prod:enphase-envoy
  note: An Envoy is needed to send the message that clears GFI Tripped or DC Resistance Low - Power Off
    conditions
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h103
    h: 04a54f598668
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h100
    h: c4f8a92bf35b
  review: drafted
- claim_id: c6
  attr: rated_power
  value:
    nominal: 240
    unit: unit:W
  conditions: Rated continuous AC output power, -40 C to +65 C, M250-60 and M250-72 (peak AC output 250
    W)
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c7
  attr: nominal_voltage
  value:
    min: 211
    max: 264
    nominal: 240
    unit: unit:V
  conditions: Nominal AC output voltage range, 240 VAC split phase, M250-60 and M250-72
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17.r6
    h: cac2971ecbef
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20.r6
    h: 984399d9e9b3
  review: drafted
- claim_id: c8
  attr: nominal_voltage
  value:
    min: 183
    max: 229
    nominal: 208
    unit: unit:V
  conditions: Nominal AC output voltage range, 208 VAC three phase, M250-60 and M250-72
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
- claim_id: c9
  attr: rated_output_current
  value:
    nominal: 1
    unit: unit:A
  conditions: Maximum AC output current at nominal voltage, 240 VAC split phase, M250
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 1.15
    unit: unit:A
  conditions: Maximum AC output current at nominal voltage, 208 VAC three phase, M250
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c11
  attr: frequency
  value:
    min: 57
    max: 61
    nominal: 60
    unit: unit:HZ
  conditions: Nominal AC output frequency range, M250
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
- claim_id: c12
  attr: frequency
  value:
    min: 57
    max: 62.5
    unit: unit:HZ
  conditions: Extended AC output frequency range, M250
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
- claim_id: c13
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: Peak inverter efficiency, M250-60 and M250-72
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions)
- claim_id: c14
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, M250-60 and M250-72
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions)
- claim_id: c15
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: Peak inverter efficiency, M215-60-2LL-S22-IG
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=23.r17
    h: a6ce518994d2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c17 (same source; check the conditions)
- claim_id: c16
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, M215-60-2LL-S22-IG
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=23.r18
    h: b63af208ecb6
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions)
- claim_id: c17
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, M215-60-2LL-S22
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=26.r18
    h: e678e349fba8
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
- claim_id: c18
  attr: operating_temperature
  value:
    min: -40
    max: 65
    unit: unit:DEG_C
  conditions: Ambient temperature range, M250-60 and M250-72
  cite:
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=20
    h: a845460cfc26
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=17
    h: e0a8e24f5b2a
  review: drafted
- claim_id: c19
  attr: max_count
  value:
    max: 16
    unit: unit:NUM
  conditions: M250 microinverters per AC branch circuit, 240 V single phase
  cite:
  - src: src:enphase-enphase-m215-m250-on-iq7-platform-installation-guide
    loc: tbl=3
    h: f1ef923a38c4
  review: drafted
- claim_id: c20
  attr: max_count
  value:
    max: 24
    unit: unit:NUM
  conditions: M250 microinverters per AC branch circuit, 208 V three phase
  cite:
  - src: src:enphase-enphase-m215-m250-on-iq7-platform-installation-guide
    loc: tbl=3
    h: f1ef923a38c4
  review: drafted
- claim_id: c21
  attr: max_count
  value:
    max: 17
    unit: unit:NUM
  conditions: M215 microinverters per AC branch circuit (20 A max), 240 V single phase
  cite:
  - src: src:enphase-enphase-m215-m250-on-iq7-platform-installation-guide
    loc: tbl=3
    h: f1ef923a38c4
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=23.r16
    h: dbc9762a1473
  review: drafted
- claim_id: c22
  attr: max_count
  value:
    max: 25
    unit: unit:NUM
  conditions: M215 microinverters per AC branch circuit (20 A max), 208 V three phase
  cite:
  - src: src:enphase-enphase-m215-m250-on-iq7-platform-installation-guide
    loc: tbl=3
    h: f1ef923a38c4
  - src: src:enphase-enphase-m250-installation-and-operation-manual-60hz
    loc: tbl=23.r16
    h: dbc9762a1473
  review: drafted
---
The Enphase M215 and M250 are module-level microinverters made by Enphase, built in M250-60, M250-72 and two M215-60 versions. The M250 is rated at 240 W continuous AC output, with 250 W peak, on either 240 V split-phase or 208 V three-phase service at 60 Hz. An AC branch circuit can hold up to 16 M250 units on 240 V or 24 on 208 V, and up to 17 M215 units on 240 V or 25 on 208 V. These units talk over power line communication, and their enclosures are rated NEMA 6. The IQ 7-based M215 and M250 expansion models are Class II double-insulated with ground fault protection, so they need no GEC, EGC or neutral conductor. A solid red status LED means a DC Resistance Low - Power Off fault on the M250 and M215-60-2LL-S22-IG, or a GFI Tripped fault on the M215-60-2LL-S22. These faults stay latched until an Envoy sends a clear message, and the clear will not hold while the cause, such as damaged insulation, wiring or moisture, is still present.

<!-- review notes
- sentence 1: support check: partial - Models M250-60, M250-72 and two M215-60 versions appear, but 'made by Enphase' and 'module-level' are only implied.
- sentence 2: support check: partial - 240 W continuous and 250 W peak, both voltages and 60 Hz nominal are given, but power is not stated per service type; reasonably implied.
- sentence 1: review: partial - The passages show Enphase M250-60, M250-72, M215-60-2LL-S22 and M215-60-2LL-S22-IG microinverters, but 'module-level' is not stated in them.
-->
