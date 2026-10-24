---
id: method:rcd-function-test
type: DetectionMethod
name: RCD test button check
claims:
- claim_id: c1
  rel: produces
  target: meas:voltage-after-rcd-test
  note: After pressing the test button of residual-current device F7, voltage still measured at connection
    X3 means the RCD is not wired correctly.
  cite:
  - src: src:sma-doc-244194
    loc: tbl=21
    h: 32e6c8bbd0fd
  - src: src:sma-doc-244194
    loc: tbl=21.r1
    h: 473b0dc9debd
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: tbl=24
    h: 421f744ce3de
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: produces
  target: meas:contactors-not-deactivated
  note: After pressing the test button of residual-current device F2, the contactors (Q1, Q2 and Q3, or
    Q2 and Q3 depending on the device) should go into non-operative mode. If they do not, F2 is wired
    incorrectly.
  cite:
  - src: src:sma-doc-244194
    loc: tbl=21
    h: 32e6c8bbd0fd
  - src: src:sma-doc-244194
    loc: tbl=21.r2
    h: 025fff7b8e8e
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: tbl=24
    h: 421f744ce3de
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The RCD test button check uses the function test button built into a residual-current device to simulate a fault and confirm that the device trips. Some Sunny Central inverters send their control supply voltage out to external devices, and a residual current breaker protects those devices. That breaker has a function test button. On some devices, press the test button and then measure the downstream connection. If voltage is still present, the RCD is miswired and must be wired correctly. On other devices, press the test button and check that the contactors fed by the RCD drop out. If they stay energized, the RCD wiring must be corrected. Switch the residual-current device back on once the test is finished. The check helps find residual current device failure and RCD wiring errors. When commissioning, also confirm that any RCD on the AC circuit feeding an inverter is a type chosen according to IEC TS 62548. Some inverters need a type B RCD.

<!-- review notes
- sentence 1: support check: partial - Passage says the function test button simulates the failure, but doesn't explicitly say it confirms the device trips.
- sentence 6: support check: partial - Wiring errors are supported by the tasks, but RCD device failure detection is only implied by the failure simulation, not stated.
- sentence 1: review: partial - The passage says the function test button simulates the failure, but it does not say the check confirms that the device trips.
- sentence 4: review: partial - The tables say to press the test button, check that contactors Q1-Q3 go non-operative, and rewire F2 if they do not deactivate, but they never say the contactors are fed by the RCD.
-->
