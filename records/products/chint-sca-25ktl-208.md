---
id: prod:chint-sca-25ktl-208
type: Product
name: CPS SCA25KTL-DO/US-208
aliases:
- SCA 25 KTL DO US 208
- SCA25KTL-DO/US-208
category: Inverters
make: chint
product_level: family
model_number: SCA25KTL-DO/US-208
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=h8
    h: 2bbad8beea5e
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: sec=front
    h: f0c5fdda4d5f
  review: drafted
  review_note: 'support check: partial - Model name and ''CPS'' appear, but the passages do not state
    the full manufacturer name CHINT POWER SYSTEMS.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Transformerless topology
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=56.r1
    h: 0337ae91d360
  review: drafted
  review_note: 'support check: partial - Transformerless topology is stated, but the passages do not say
    the device is an inverter explicitly (implied by efficiency spec).'
- claim_id: c3
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: Maximum DC input voltage
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=55.r3
    h: 613b73cffb64
  review: drafted
- claim_id: c4
  attr: nominal_voltage
  value:
    nominal: 208
    unit: unit:V
  conditions: Rated AC output voltage
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=55.r15
    h: ef930493f62b
  review: drafted
- claim_id: c5
  attr: rated_output_current
  value:
    nominal: 69.5
    unit: unit:A
  conditions: Maximum AC output current at 208 VAC
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=55.r18
    h: 073df7751015
  review: drafted
- claim_id: c6
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated output frequency
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=55.r20
    h: 663609b77071
  review: drafted
- claim_id: c7
  attr: efficiency
  value:
    nominal: 97
    unit: unit:PERCENT
  conditions: Maximum efficiency, transformerless topology
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=56.r1
    h: 0337ae91d360
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ul-1741-sa
  note: Listed as UL1741-SA Ed. 2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57.r1
    h: 54666eb6b3ca
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:ul-1699b
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57.r1
    h: 54666eb6b3ca
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57.r1
    h: 54666eb6b3ca
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:ieee-1547
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57.r1
    h: 54666eb6b3ca
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:fcc-part-15
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57.r1
    h: 54666eb6b3ca
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c13
  rel: implements
  target: func:voltage-ride-through
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c14
  rel: implements
  target: func:frequency-ride-through
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c15
  rel: implements
  target: func:ramp-rate-control
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c16
  rel: implements
  target: func:constant-power-factor
  note: Listed as Specified-PF
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c17
  rel: implements
  target: func:volt-var
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c18
  rel: implements
  target: func:frequency-watt
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c19
  rel: implements
  target: func:volt-watt
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=57
    h: 542e2ebb3728
  review: drafted
- claim_id: c20
  rel: implements
  target: func:dc-arc-fault-protection
  note: Arc board with Arc Fault Test available from Settings menu
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=1.r13
    h: 1a9bace90d13
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r3
    h: 99d70367a788
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=52.r2
    h: bdd8e4eb27f4
  review: drafted
- claim_id: c21
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=2.r3
    h: ea831fdeff27
  review: drafted
---
The CPS SCA25KTL-DO/US-208 is a transformerless three-phase string inverter from CHINT Power Systems, built for 208 VAC grid connections. It takes up to 1000 VDC at the input, runs over a DC operating range of 200-950 VDC and starts at 330 V and 80 W. Its MPPTs can run independently or be combined in parallel. It delivers up to 69.5 A at 208 VAC and 60 Hz, with current THD below 3% and a maximum efficiency of 97%. Its listed smart-grid functions are voltage and frequency ride-through, ramp-rate control, specified power factor, Volt-VAr, Freq-Watt and Volt-Watt. You can select the IEEE 1547a2014, CA Rule 21, ISO-NE or HECO grid standard. It has DC arc-fault protection on an arc board. If you see Arcboard Err or ARC Protect, check that the logic connector to the arc board is secure and run the Arc Fault Test from the Settings menu. It communicates over RS485, and you load firmware upgrades through a USB port.

<!-- review notes
- sentence 1: support check: partial - Transformerless and 208VAC are supported, but 'three-phase', 'string inverter' and the full CHINT name are not stated.
- sentence 6: support check: partial - RS485 is supported; the USB port caption for firmware upgrades supports the USB firmware loading, but only as a figure caption.
-->
