---
id: prod:huawei-sun2000-25-30ktl-us
type: Product
name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
aliases:
- SUN2000-25KTL-US
- SUN2000-30KTL-US
- SUN2000-25-30KTL-US
- SUN2000-(25KTL, 30KTL)-US
category: Inverters
make: huawei
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:huawei
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=h1
    h: fb9f5545dc33
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    nominal: 25
    unit: unit:KiloW
  conditions: SUN2000-25KTL-US model, rated output power
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=5
    h: a045f558df53
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=5.r1
    h: d1545462f028
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c3
  attr: rated_power
  value:
    nominal: 30
    unit: unit:KiloW
  conditions: SUN2000-30KTL-US model, rated output power
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=5
    h: a045f558df53
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c4
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: Maximum efficiency, SUN2000-25KTL-US
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=44
    h: e728064b8a60
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=44.r1
    h: 297e3895e009
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: efficiency
  value:
    nominal: 98
    unit: unit:PERCENT
  conditions: CEC efficiency, SUN2000-25KTL-US
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=44
    h: e728064b8a60
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=44.r2
    h: 81a97fa15fda
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c6
  attr: max_input_voltage
  value:
    max: 1000
    unit: unit:V
  conditions: Both SUN2000-25KTL-US and SUN2000-30KTL-US
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=45.r2
    h: 34661d059c69
  review: drafted
- claim_id: c7
  attr: mppt_voltage_range
  value:
    min: 560
    max: 850
    unit: unit:V
  conditions: Full power MPPT voltage range, DC, both models
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=45.r6
    h: af9954e223ff
  review: drafted
- claim_id: c8
  attr: max_input_current
  value:
    max: 45
    unit: unit:A
  conditions: Total DC input, SUN2000-25KTL-US
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=45.r8
    h: 8e18e0ea691e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  attr: max_input_current
  value:
    max: 54
    unit: unit:A
  conditions: Total DC input, SUN2000-30KTL-US
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=45.r8
    h: 8e18e0ea691e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  attr: max_input_current
  value:
    max: 25
    unit: unit:A
  conditions: Per MPPT, both models
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=45.r8
    h: 8e18e0ea691e
  review: drafted
- claim_id: c11
  attr: rated_output_current
  value:
    max: 33
    unit: unit:A
  conditions: Maximum continuous AC output current, SUN2000-25KTL-US
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=47.r17
    h: 2b60eb5fb7dd
  review: drafted
- claim_id: c12
  attr: rated_output_current
  value:
    max: 40
    unit: unit:A
  conditions: Maximum continuous AC output current, SUN2000-30KTL-US
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=47.r17
    h: 2b60eb5fb7dd
  review: drafted
- claim_id: c13
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=49.r2
    h: 5d8ef5d0f121
  - src: src:huawei-huawei-sun2000-25-30ktl-us-quick-guide
    loc: tbl=5
    h: 9bbeb9209af5
  - src: src:huawei-huawei-sun2000-25-30ktl-us-quick-guide
    loc: tbl=5.r2
    h: 8a76557eb7ae
  review: drafted
- claim_id: c14
  rel: uses_protocol
  target: proto:power-line-communication
  conditions: Optional; only on variants with PLC. Only one communication mode (PLC or RS485) can be used
    at a time.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=49.r3
    h: bbc44bf178fb
  - src: src:huawei-huawei-sun2000-25-30ktl-us-quick-guide
    loc: tbl=5
    h: 9bbeb9209af5
  review: drafted
- claim_id: c15
  rel: lacks
  target: proto:power-line-communication
  conditions: Variant without PLC only
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-quick-guide
    loc: tbl=5.r2
    h: 8a76557eb7ae
  - src: src:huawei-huawei-sun2000-25-30ktl-us-quick-guide
    loc: tbl=5
    h: 9bbeb9209af5
  review: drafted
- claim_id: c16
  rel: implements
  target: func:dc-arc-fault-protection
  note: AFCI per UL 1699B, Type I
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=48.r10
    h: 00ee74fa8113
  review: drafted
- claim_id: c17
  rel: certified_to
  target: std:ul-1699b
  note: AFCI Type I
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=48.r10
    h: 00ee74fa8113
  review: drafted
  review_note: 'support check: partial - The passages say AFCI is to UL 1699B Type I. They do not say
    the inverter is certified.; review: partial - The spec row lists AFCI to UL 1699B Type I for both
    models, but it never says the inverters are certified to that standard.'
- claim_id: c18
  rel: implements
  target: func:insulation-monitoring
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=48.r8
    h: 36bde220c4bf
  review: drafted
- claim_id: c19
  rel: implements
  target: func:reverse-polarity-protection
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=48.r4
    h: 61af2ef64f13
  review: drafted
- claim_id: c20
  rel: implements
  target: func:string-monitoring
  note: PV string fault detection
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=48.r5
    h: b83ee0492edf
  review: drafted
- claim_id: c21
  rel: implements
  target: func:surge-protection
  note: Type II on both DC and AC sides
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=48.r7
    h: dce988aa9faa
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=48.r6
    h: f985891402e0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c22
  rel: compatible_with
  target: prod:amphenol-helios-h4
  note: DC connector fitted on the inverter
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=51.r4
    h: 6e1ed26141c1
  review: drafted
---
The Huawei SUN2000-25KTL-US and SUN2000-30KTL-US are transformerless three-phase string inverters. They are rated at 25 kW and 30 kW of output power. Both models accept up to 1,000 V DC at the input, and their full-power MPPT window runs from 560 to 850 V DC. Each MPPT takes at most 25 A. The maximum continuous AC output current is 33 A on the 25 kW model and 40 A on the 30 kW model. The 25 kW model lists a maximum efficiency of 98.6% and a CEC efficiency of 98.0%. Built-in protection includes a DC input switch, reverse polarity protection, insulation resistance detection, PV string fault detection and Type II surge protection on both the DC and AC sides. The inverter has an arc fault circuit interrupter (AFCI) to UL 1699B Type I. Its alarms include DC Arc Fault and AFCI Self-Check Failure. All units support RS485 communication, and PLC is an option on some variants. Only one of these modes can be used at a time, so do not connect the RS485 cable when PLC is used. The DC connectors are Amphenol Helios H4, and the enclosure is rated Type 4X.

<!-- review notes
- sentence 1: support check: partial - The passages give transformerless topology and the 25 kW and 30 kW ratings. They do not say three-phase or string inverter.
- sentence 1: review: partial - The transformerless topology and the 25 kW and 30 kW ratings are supported, but no passage says three-phase or string inverter.
-->
