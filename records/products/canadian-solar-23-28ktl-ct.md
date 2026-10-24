---
id: prod:canadian-solar-23-28ktl-ct
type: Product
name: CSI 23/28KTL-CT/US-480
aliases:
- CSI 23KTL-CT
- CSI 28KTL-CT
- 23KTL-CT/US-480
- 28KTL-CT/US-480
- CSI 23KTL-CT/US-480
- CSI 28KTL-CT/US-480
- 23KTL-CT
- 28KTL-CT
- CSI 23/28KTL-CT
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=front
    h: f3b9d2a73eef
  review: drafted
  review_note: 'support check: partial - Evidence is only the bare string ''CanadianSolar'', which suggests
    but does not state the manufacturer relation.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=34.r1
    h: a154a490818a
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:modbus
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=3.3.3
    h: ee92d25ee20a
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  note: 'RS485 cable: UTP CAT-5e or 3x #22-18 AWG communication cable, e.g. Belden 3106A.'
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: sec=3.3.3
    h: ee92d25ee20a
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=16.r1
    h: 35ca3a947813
  review: drafted
- claim_id: c5
  rel: implements
  target: func:mppt
  note: Two MPP trackers per model, with four DC inputs on each MPPT.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r4
    h: beb0303611da
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
- claim_id: c6
  rel: implements
  target: func:dc-arc-fault-protection
  note: Uses an Arcboard; arc faults are cleared with the ARCFaultClear command.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=31.r2
    h: 2a8f07023fcf
  review: drafted
  review_note: 'support check: partial - The Arcboard error and ARCFaultClear are in the passage, but
    it never states that the inverter provides DC arc-fault protection.'
- claim_id: c7
  rel: implements
  target: func:constant-power-factor
  note: Power factor above 0.99, adjustable to plus or minus 0.8.
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r10
    h: ad5edc9d8ce8
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
  review_note: 'support check: partial - The table gives a power factor of >0.99 and ±0.8 adjustable,
    but it does not name a constant power factor mode.'
- claim_id: c8
  attr: rated_power
  value:
    nominal: 23
    unit: unit:KiloW
  conditions: CSI 23KTL-CT/US-480, rated AC output power
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r8
    h: ccb247cee4ab
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: rated_power
  value:
    nominal: 28
    unit: unit:KiloW
  conditions: CSI 28KTL-CT/US-480, rated AC output power
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r8
    h: ccb247cee4ab
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c10
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: Both models, maximum DC input voltage
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
- claim_id: c11
  attr: mppt_voltage_range
  value:
    min: 480
    max: 800
    unit: unit:V
  conditions: CSI 23KTL-CT/US-480
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
- claim_id: c12
  attr: mppt_voltage_range
  value:
    min: 500
    max: 800
    unit: unit:V
  conditions: CSI 28KTL-CT/US-480
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
- claim_id: c13
  attr: max_input_current
  value:
    nominal: 25
    unit: unit:A
  conditions: CSI 23KTL-CT/US-480, per MPPT (Imp); total 50 A
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
- claim_id: c14
  attr: max_input_current
  value:
    nominal: 29
    unit: unit:A
  conditions: CSI 28KTL-CT/US-480, per MPPT (Imp); total 58 A
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions)
- claim_id: c15
  attr: rated_output_current
  value:
    nominal: 27.7
    unit: unit:A
  conditions: CSI 23KTL-CT/US-480, maximum AC output current
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r9
    h: 5a012a8ab053
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions)
- claim_id: c16
  attr: rated_output_current
  value:
    nominal: 33.7
    unit: unit:A
  conditions: CSI 28KTL-CT/US-480, maximum AC output current
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r9
    h: 5a012a8ab053
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions)
- claim_id: c17
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated AC output voltage, three-phase with N and PE; output voltage range 422-528 Vac
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r9
    h: 5a012a8ab053
  review: drafted
- claim_id: c18
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated output frequency
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r9
    h: 5a012a8ab053
  review: drafted
- claim_id: c19
  attr: frequency
  value:
    min: 59.3
    max: 60.5
    unit: unit:HZ
  conditions: Output frequency range
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r10
    h: ad5edc9d8ce8
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32
    h: 8bdf6fbb3f1f
  review: drafted
- claim_id: c20
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=33.r2
    h: 37d602a68a89
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions)
- claim_id: c21
  attr: efficiency
  value:
    nominal: 98
    unit: unit:PERCENT
  conditions: CEC weighted efficiency
  cite:
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=33.r2
    h: 37d602a68a89
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions)
---
The CSI 23/28KTL-CT/US-480 is a Canadian Solar transformerless three-phase string inverter family. It comes in a 23 kW model and a 28 kW model. Both models accept up to 1000 Vdc and have two MPP trackers with four DC inputs each. A load-rated DC switch handles DC disconnection. The MPPT range is 480-800 Vdc on the 23 kW model and 500-800 Vdc on the 28 kW model. Maximum input current per MPPT is 25 A and 29 A. The AC output is 480 Vac, 60 Hz, three-phase with neutral and PE. Maximum output current is 27.7 A on the 23 kW model and 33.7 A on the 28 kW model. Peak efficiency is 98.6 percent and CEC efficiency is 98.0 percent. Power factor can be adjusted, and output derates at high temperature. For communication the inverter uses Modbus over RS485. Firmware can be upgraded from a USB disk through the communication board's USB port. An Arcboard provides arc fault detection. An Arcboard Err fault points to poor contact or damage on that board. Clear it with ARCFaultClear after checking the board.

<!-- review notes
- sentence 5: support check: partial - The efficiencies and the adjustable power factor are stated, but the derating-curve caption only shows a high-temperature derating figure and does not state the derating behavior.
- sentence 7: support check: partial - The Arcboard Err causes and the ARCFaultClear step are stated, but the passage does not say the Arcboard provides arc fault detection.
-->
