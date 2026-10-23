---
id: symptom:battery-cell-imbalance
type: Symptom
name: Battery cell charge imbalance
aliases:
- battery imbalancing fault
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Sunny Island shows warning W948 (level 1) or error F932 (level 3), reported via SiCom, when battery
    cells have differing states of charge. SMA event 9315 reports the same condition as a battery imbalancing
    fault.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r15
    h: 9fc3a00f4839
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r1
    h: e7e1a00b10f1
  - src: src:sma-kb-event-9315
    loc: sec=h1
    h: ee7443143b20
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:battery-voltage-spread
  note: When batteries are in the same condition, voltage differences between positions in the arrangement
    or over time indicate a performance problem. Voltages must be corrected for voltage level, temperature,
    discharge rate and cell age.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h184
    h: 0ed4b3344ea0
  review: drafted
---
The Sunny Island battery inverter reports battery cells that hold different states of charge. It raises warning W948, or error F932 at a higher level, through its SiCom battery communication. SMA event 9315 calls this a battery imbalancing fault. It means the charge states of the individual cells differ too much. Cells in series drift apart in charge over time if they do not get regular equalization charges. This can reduce battery performance and lead to early failure of the storage system. Equalization charging brings the series cells back to a common state of charge. Check that it is set up with the cell voltage, absorption time and cycle time the battery manufacturer recommends. In the field, compare cell or battery voltages by position and track them over time. A spread between batteries that should be in the same condition points to a problem, but adjust the readings for temperature, discharge rate and age first. In flooded lead-acid batteries, differing acid concentrations are one condition that makes the Sunny Island recalibrate its state-of-charge value. If the imbalance fault persists, the installer should agree the next steps with the battery manufacturer.

<!-- review notes
- sentence 5: support check: partial - Position and time comparison and adjustments are stated, but temperature, discharge rate and age are listed alongside voltage level; the passage doesn't directly say to adjust 'first' as field practice, a minor omission.
- sentence 7: support check: partial - Passage says contact the installer who clarifies next steps with the manufacturer, but does not mention the fault persisting as a condition.
-->
