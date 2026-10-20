---
id: method:arc-fault-self-test
type: DetectionMethod
name: Arc fault self-test
aliases:
- AFCI Test
- Arc Fault Test
- AFCI self test
claims:
- claim_id: c1
  rel: produces
  target: meas:afci-self-test-fault
  note: On CPS SCA36KTL the LCD shows 'AFCI Fault' when the test finds a fault and 'TestFinish' when none
    is found. SMA STP-US inverters log self-test errors where the interference level is too high or too
    low, and Service must determine the cause.
  quote: '"TestFinish" will be displayed on the LCD if no fault is detected or "AFCI Fault" will be shown
    if a fault occurs'
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.8
    h: c7f6b92ccf45
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h290
    h: 7840645dc2cd
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h207
    h: 7840645dc2cd
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r1
    h: a3b3ba978302
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r1
    h: a3b3ba978302
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: produces
  target: meas:afci-self-test-pass
  note: CPS shows 'TestFinish'. Solectria PVI-TL shows 'AFCI Test Pass!', shuts down and then restarts
    into normal operation.
  cite:
  - src: src:chint-cps-36kw-usermanual-reduced
    loc: sec=5.4.8
    h: c7f6b92ccf45
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h118
    h: 76995e5e9a6e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The arc fault self-test is a built-in inverter function that checks whether the DC arc fault detection circuit (AFCI) is working. On CPS inverters, run it from the System Setting, OtherCmd menu. The inverter stops while it tests, then shows TestFinish if the circuit passes or AFCI Fault if it fails. On Solectria PVI-TL inverters, switch the AFCI Self Test option from disabled to enabled. If the circuit passes, the display shows a pass message and the inverter shuts down, then restarts into normal operation. For CPS ARC Protect and Arcboard Err alarms, first check that the logic connector to the arc board is secure, then run the test. If the alarm comes back, contact CPS Service to replace the arc board or the wiring box. This makes the test a way to confirm an arc detection board failure. The listed cause of Arcboard Err is poor contact or damage on the arc board. An ARC Protect stop can only be cleared by hand, using the ARCFaultClear command, so a passed self-test does not restart a tripped CPS inverter by itself. On SMA inverters, a self-test error that reports the interference level as too high or too low cannot be fixed in the field. Service must find the cause.

<!-- review notes
- sentence 5: support check: partial - Cause of Arcboard Err (poor contact or damage of Arcboard) is stated, but the passages do not say the test confirms an arc board failure.
- sentence 6: support check: partial - Passage says ARC Protect fault can only be cleared manually via ARCFaultClear, but does not explicitly say a passed self-test doesn't restart the inverter.
- sentence 7: support check: partial - Passages say the cause must be determined by Service, but not explicitly that it cannot be fixed in the field.
-->
