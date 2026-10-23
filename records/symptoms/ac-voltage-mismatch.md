---
id: symptom:ac-voltage-mismatch
type: Symptom
name: AC voltage measurement mismatch
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Sunny Central CP XT inverters, warning 6451 means the inverter's measured AC voltage is below
    the grid voltage, and warning 6452 means the measured grid voltage is below the inverter voltage.
    Both are warnings (W) in operating states S1 and S2. The corrective measure is to contact the SMA
    Service Line.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r6
    h: a3a63ad66354
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r5
    h: a3dbd339652a
  review: drafted
  review_note: 'support check: partial - Codes 6451/6452 meanings, W in S1/S2 and contacting SMA Service
    Line are stated, but ''Sunny Central CP XT'' model is not in passages, and the ''warning active while
    disagreeing with grid-side measurement'' framing is interpretive.'
- claim_id: c2
  rel: observed_as
  target: meas:inverter-grid-voltage-deviation
  note: The VAC test compares the AC voltage the inverter displays with the grid voltage measured as close
    to the inverter as possible. The accepted window is up to 5 V above or 1 V below the measured voltage.
    This is a pass/fail threshold, not a typical deviation.
  cite:
  - src: src:sma-doc-bfs-stptlee-rm-xx-10
    loc: sec=9
    h: b17b29301127
  - src: src:sma-doc-ast-stptl10-rm-xx-10
    loc: sec=10
    h: 9a4d1e9c23f2
  - src: src:sma-doc-stptl-20-con-rm-xx-10
    loc: sec=9
    h: b17b29301127
  - src: src:sma-doc-bfs-stptlee-rm-xx-10
    loc: sec=h269
    h: 1c16bb3e7702
  - src: src:sma-doc-bfs-stptlee-rm-xx-10
    loc: sec=h201
    h: ac3c456e0ced
  review: drafted
---
This symptom is a disagreement between the AC voltage the inverter measures on its own side and the voltage measured on the utility grid side. On Sunny Central CP XT central inverters it shows as warning 6451, where the inverter-side voltage reads lower than the grid, or warning 6452, where the grid-side voltage reads lower than the inverter. Both codes are warnings, and the manufacturer's only listed corrective action is to contact the SMA Service Line. To confirm a reading error, compare the voltage shown on the inverter display or communication product with a meter reading taken as close to the inverter as possible. In the SMA VAC test, the inverter reading may be up to 5 V higher or 1 V lower than the measured grid voltage. Outside that window, contact service. Do this check after any part of the inverter's voltage measurement area has been replaced, because those parts affect measurement accuracy. On some inverters, faults in the voltage sensing hardware are reported as their own codes, such as a voltage sense failure or a voltage sensing firmware mismatch. Check the fault log for these.

<!-- review notes
- sentence 2: support check: partial - The 6451/6452 descriptions match, but the passages don't name Sunny Central CP XT.
- sentence 7: support check: partial - The table lists Voltage Sense Failure and Voltage Sensing Firmware Mismatch as hardware failure codes, but the advice to check the fault log is not stated.
- sentence 7: review: partial - The table lists Voltage Sense Failure and Voltage Sensing Firmware Mismatch as hardware failure codes, but the advice to check the fault log is not in the passage.
-->
