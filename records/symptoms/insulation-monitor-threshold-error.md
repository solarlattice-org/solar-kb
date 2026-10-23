---
id: symptom:insulation-monitor-threshold-error
type: Symptom
name: Insulation monitor threshold error
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On the SMA Sunny Central CP XT this appears as error 6461 (threshold not adopted by the insulation
    monitoring device) or error 6448 (insulation monitoring delivers non-permitted values).
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r12
    h: c5274a5ad566
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r4
    h: 58b52105d499
  review: drafted
---
On SMA Sunny Central CP XT inverters, this shows up as error 6461. It means the insulation monitoring device has not accepted its configured threshold. The related error 6448 means the insulation monitoring is returning values that are not permitted. The inverter treats it as a warning. Start by checking the insulation monitoring device itself and the cabling to it. Do not confuse this with a real insulation fault. In that case the device reports error 3504, and you should check the PV array for ground faults. On some inverters the insulation thresholds are set by the user. There is a warning threshold that leaves feed-in running and an error threshold that stops feed-in, so check the configured values as well.

<!-- review notes
- sentence 5: support check: partial - Passages show user-set warning and error thresholds (warning continues feed-in, error interrupts), but they do not say to check configured values when diagnosing this fault, and the 'some inverters' scope is only loosely supported.
-->
