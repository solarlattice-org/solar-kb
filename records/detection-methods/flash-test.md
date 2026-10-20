---
id: method:flash-test
type: DetectionMethod
name: Flash testing
claims:
- claim_id: c1
  rel: produces
  target: meas:pmax-below-rated
  note: Stabilized flash-test power is compared with the nameplate rating and with degradation expected
    for the module technology, to confirm LID.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=front
    h: ea45629cb646
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h2
    h: 0877e796b00f
  review: drafted
---
Flash testing measures a module's power output so it can be compared with its nameplate rating. To check for light induced degradation, compare stabilized flash-test results with the nameplate and with the degradation expected for that module technology. Use IV traces and early-life production trends alongside the flash test. If a plant loses power unexpectedly early in its life, confirm the loss with IV and flash testing. Module rated power is usually already reduced by the expected saturated LID loss. LID only counts as a failure when the measured saturated loss is larger than expected. To tell system degradation apart from module degradation, combine module test results with long-term normalized plant output, string or inverter trends and IV curve data. Module tests show average module degradation, but they cannot show by themselves the extra system loss that comes from mismatch when modules age at different rates.

<!-- review notes
- sentence 1: support check: partial - Passages mention comparing flash-test results with nameplate, but don't explicitly say flash testing measures module power output.
- sentence 6: support check: partial - Passages say combined data separates average module degradation from mismatch-driven system degradation, but don't explicitly state module tests alone cannot show the mismatch loss.
-->
