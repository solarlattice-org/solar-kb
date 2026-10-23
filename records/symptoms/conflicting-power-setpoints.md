---
id: symptom:conflicting-power-setpoints
type: Symptom
name: Conflicting power setpoints
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On the Sunny Central CP XT this shows as error number 8702, meaning more than one digital active
    power setpoint is present. The listed inverter behavior is W in states S1 and S2, and the corrective
    measure is to contact the SMA Service Line.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r5
    h: a8a9b15963e6
  review: drafted
  review_note: 'support check: partial - Error 8702, the explanation, W in S1/S2 and contacting the SMA
    Service Line are stated, but the passage names no Sunny Central CP XT model and doesn''t say ''more
    than one'' precisely (it says ''several''); the fault-display observation framing is also not stated.'
---
On the Sunny Central CP XT, error 8702 means the inverter is receiving more than one digital active power setpoint at once. The listed behavior is W in both S1 and S2, and the manual says to contact the SMA Service Line. A conflict occurs when the lowest of all the maximum setpoints is below the highest of all the minimum setpoints, so no permitted range remains. When there is a conflict, the inverter takes the specifications in a fixed order. Manual input comes first, then the high-priority external inputs 2 and 1, then the P(V) and P(f) curves, and last the low-priority external inputs 2 and 1. Each setpoint input handles only one setpoint, and you can change the priority of the external inputs. Check which sources are writing to each input first. Active power setpoints sent over Modbus go to setpoint input 2, which lets them run in parallel with SMA system control. Check this path when two controllers may both be sending commands. Keep this separate from error 8701, which means the external active power setpoints are below 2 mA and invalid, so the inverter uses the last valid value or Pmax. Also keep it separate from 8703 and 8704, which flag invalid reactive power setpoints.

<!-- review notes
- sentence 1: support check: partial - Error 8702, W in S1 and S2 and the Service Line action are stated, but the passage doesn't name the Sunny Central CP XT, and 'several' setpoints is read as 'more than one'.
- sentence 2: support check: partial - The passage states a conflict when the minimum of the maximum setpoints is smaller than the maximum of the minimum setpoints; 'so no permitted range remains' is an inference, since the passage says the values 'result in a permitted range'.
- sentence 4: support check: partial - The one-setpoint-per-input and adjustable priority statements are present, but the advice to check which sources write to each input is not in the passage.
- sentence 5: support check: partial - Modbus active power setpoints go to setpoint input 2 and allow parallel operation with SMA system control, but the advice to check this path when two controllers send commands is not in the passage.
- sentence 6: support check: partial - 8701 is accurate (below 2 mA, invalid, last valid value or Pmax after a day change), but 8703 flags only an invalid power factor of the reactive setpoint, and 8704 flags invalid active and reactive setpoints, so lumping them as 'invalid reactive power setpoints' is imprecise.
-->
