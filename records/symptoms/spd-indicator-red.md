---
id: symptom:spd-indicator-red
type: Symptom
name: SPD status indicator red
aliases:
- Red LED
claims:
- claim_id: c1
  rel: observed_as
  target: meas:spd-red-status-led
  note: A red LED on a phase or on neutral-ground means protection on that mode is lost or compromised;
    on units fitted with one, an audible alarm sounds as well.
  cite:
  - src: src:eaton-eaton-spd
    loc: sec=3.2
    h: 413badbb96aa
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  - src: src:eaton-eaton-spd
    loc: tbl=8.r3
    h: 6ac33fcf20dc
  - src: src:eaton-eaton-spd
    loc: tbl=8.r5
    h: 48baccb5ce64
  - src: src:eaton-eaton-spd
    loc: tbl=8.r4
    h: 28c46d3ae071
  - src: src:eaton-eaton-spd
    loc: tbl=7.r7
    h: '019039e56176'
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=56.r2
    h: '176220009679'
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c2
  rel: observed_as
  target: meas:spd-alarm-status-register
  note: Read-only boolean points report the red LED state for phases A, B, C and N-G over Modbus registers
    and BACnet binary objects (0 or OFF means the LED is off, 1 or ON means it is lit).
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=16.r6
    h: bce362a4a664
  - src: src:eaton-eaton-spd
    loc: tbl=16.r16
    h: b4cc2c0309d9
  - src: src:eaton-eaton-spd
    loc: tbl=22.r14
    h: dfb91c2fddc7
  - src: src:eaton-eaton-spd
    loc: tbl=22.r5
    h: 34e786bacb31
  - src: src:eaton-eaton-spd
    loc: tbl=22.r11
    h: a0b771e77d75
  - src: src:eaton-eaton-spd
    loc: tbl=22.r8
    h: 7df2b8a4d85b
  review: drafted
  review_note: 'support check: partial - Evidence shows RO BOOL registers/BV objects for N-G and phases
    (0 off, 1 on), but the Modbus registers for A and B and the BACnet details are only partly shown;
    the core is stated.'
- claim_id: c3
  rel: observed_as
  target: meas:inverter-spd-fault-code
  note: On CPS SCA inverters, Warn0100 (AC SPD) tells the operator to check the SPD indicator by eye.
    A red indicator means the SPD module should be replaced.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=56.r2
    h: '176220009679'
  review: drafted
---
The display panel on the surge protection device has a green and a red LED for each phase, and wye, split-phase and high-leg delta units have an extra pair for neutral-ground. Green means the mode is fully protected and red means protection has been lost. On units fitted with an audible alarm, the alarm sounds when an LED turns red. Use the silence button to stop it. If one phase or the neutral-ground LED is red, the likely cause is a significant surge event or an extended temporary overvoltage on that mode. If every phase LED is red, consider three causes: total loss of protection, an extended temporary overvoltage, or an SPD whose rated voltage is lower than the system voltage. In every case the fix is to replace the SPD. If the voltage rating is wrong, fit the correct-voltage model. If temporary overvoltage is suspected, find and correct its source first. If all LEDs are dark, the SPD is not showing a red status. Instead, check the supply voltage and the connections at the SPD. You can read the red LED state of each phase and of neutral-ground remotely through read-only Modbus registers and BACnet binary objects. When a CPS SCA inverter raises Warn0100, look at the SPD module first. Replace it if the indicator is red. If it is green, remove and reinsert it in its socket, and call service if the warning remains.

<!-- review notes
- sentence 2: support check: partial - Alarm sounds when an LED turns red is stated, but silencing varies: a silence button on features 1-3, and any of four pushbuttons on Power Xpert SPD.
- sentence 6: support check: partial - All LEDs off means SPD not connected to power and check voltage/connections, but 'not showing red status' is an inference.
-->
