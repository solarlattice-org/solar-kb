---
id: symptom:battery-protection-mode
type: Symptom
name: Battery protection mode active
aliases:
- Battery-preservation mode
- LBM
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Sunny Island displays warnings W755, W756 and W757 for battery-preservation mode levels 1, 2 and
    3. Communication products report the mode under the battery error or battery fault message.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r12
    h: '500e83690236'
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r13
    h: 14f4b3806837
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=152.r14
    h: 0aa0678679c0
  - src: src:sma-doc-278742
    loc: sec=h920
    h: 61641486d709
  - src: src:sma-doc-259761
    loc: sec=h804
    h: 259c05c526c3
  review: drafted
---
Battery protection mode is a Sunny Island function that keeps the battery from being drained when its state of charge falls below set thresholds. It shows on the display as warnings W755, W756 or W757, one for each of the three levels, and communication products report it as a battery error or battery fault. At levels 1 and 2 the unit goes into energy-saving mode during a set time window. At level 2 it starts up every 2 hours outside that window to try to charge the battery. At level 3 the unit switches itself off to prevent deep discharge, and it must be switched on and started manually before the battery can charge again. The unit only enters this mode after no charging current has flowed into the battery for a minimum time, which can be set and defaults to 5 minutes. Also check the state of charge thresholds and the start and end times for each level under Battery > Protection mode, because these settings decide when the mode starts.

<!-- review notes
- sentence 6: support check: partial - The Battery > Protection mode path, SOC thresholds and start/end times are supported, but the claim to check them as a troubleshooting step is not stated, and level 3 has no times.
-->
