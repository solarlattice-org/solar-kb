---
id: prod:solis-rhi-1p-hv-us
type: Product
name: Solis RHI-1P(5-10)K-HVES-5G-US
aliases:
- RHI-1P5K-HVES-5G
- RHI-1P7.6K-HVES-5G
- RHI-1P10K-HVES-5G
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  attr: max_input_voltage
  value:
    nominal: 500
    unit: unit:V
  conditions: Maximum input voltage, all three models (5K, 7.6K, 10K)
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r3
    h: 95546fa8d8f8
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r3
    h: b4c816d8959d
  review: drafted
- claim_id: c2
  attr: mppt_voltage_range
  value:
    min: 90
    max: 450
    unit: unit:V
  conditions: MPPT voltage range, all three models
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r6
    h: 52fcb8aa197a
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r6
    h: 4af65dec7aab
  review: drafted
- claim_id: c3
  attr: rated_output_current
  value:
    nominal: 25
    unit: unit:A
  conditions: Rated output current, all three models
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r25
    h: 9fea763b011f
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r25
    h: e30a8b6ab03a
  review: drafted
- claim_id: c4
  attr: rated_power
  value:
    nominal: 6
    unit: unit:KiloW
  conditions: Rated output power row in the technical data table for the RHI-1P5K and RHI-1P7.6K models
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r19
    h: 6b7345320776
  review: drafted
- claim_id: c5
  attr: nominal_voltage
  value:
    nominal: 240
    unit: unit:V
  conditions: Rated AC output voltage line-to-line, all three models
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r22
    h: 442605bd912d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r22
    h: 7938b5cd87d8
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: nominal_voltage
  value:
    nominal: 120
    unit: unit:V
  conditions: Rated AC output voltage line-to-neutral, all three models
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r23
    h: c3b8d0f1482e
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r23
    h: 06aa03c800b5
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated frequency, all three models
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r24
    h: 80808071862b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r24
    h: c5d8985a0755
  review: drafted
- claim_id: c8
  attr: frequency
  value:
    min: 49.5
    max: 60.5
    unit: unit:HZ
  conditions: Frequency range as printed in the technical data, all three models
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r30
    h: 6e85c30bde31
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r30
    h: 95caffad29a6
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:can-bus
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r17
    h: bd4abbc04bda
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r17
    h: '622578269471'
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r17
    h: bd4abbc04bda
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r17
    h: '622578269471'
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=15.r17
    h: 88ad7f91754a
  review: drafted
- claim_id: c11
  rel: uses_protocol
  target: proto:wifi
  note: Listed as optional communication
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=15.r17
    h: 88ad7f91754a
  review: drafted
- claim_id: c12
  rel: uses_protocol
  target: proto:cellular
  note: GPRS listed as optional communication
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=15.r17
    h: 88ad7f91754a
  review: drafted
- claim_id: c13
  rel: implements
  target: func:backup-transfer
  note: Back-up switch time under 10 ms without ATR and under 300 ms with ATR connected (5K and 7.6K models)
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r21
    h: 4c447048f16d
  review: drafted
- claim_id: c14
  rel: implements
  target: func:dc-arc-fault-protection
  note: Has an AFCI module with self-check; AFCI Check FAULT alarm on self-check failure
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r2
    h: 86c0c0357b95
  review: drafted
  review_note: 'support check: partial - AFCI self-check fault alarm is stated, implying an AFCI module,
    but DC arc-fault protection itself is not explicitly stated.'
- claim_id: c15
  rel: compatible_with
  target: arch:split-phase-120-240v
  note: Rated output 240 V L-L and 120 V L-N
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r23
    h: c3b8d0f1482e
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=13.r22
    h: 442605bd912d
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r22
    h: 7938b5cd87d8
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=16.r23
    h: 06aa03c800b5
  review: drafted
---
The Solis RHI-1P(5-10)K-HVES-5G-US is a family of single-phase hybrid inverters for the US market, covering the RHI-1P5K, RHI-1P7.6K and RHI-1P10K models. Every model takes up to 500 V DC input, tracks MPP between 90 and 450 V, and starts up at 120 V. The AC output is rated at 240 V line-to-line and 120 V line-to-neutral, 60 Hz, with a rated output current of 25 A. The 5K and 7.6K models work with Li-ion batteries and list a rated output power of 6 kW. Switching to backup takes under 10 ms without an ATR and under 300 ms with an ATR connected. Communication is over CAN and RS485, and Wi-Fi or GPRS can be added as options. Fault messages listed for this family include AFCI Check FAULT (the AFCI module failed its self-check), DCinj-FAULT (high DC injection current) and DSP-B-FAULT (main and slave DSP cannot communicate). For each one, the first step is to restart the inverter or contact the installer.

<!-- review notes
- sentence 1: support check: partial - Single-phase and the three models are shown, but hybrid and US market are not stated in the passages.
-->
