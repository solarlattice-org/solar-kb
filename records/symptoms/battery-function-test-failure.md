---
id: symptom:battery-function-test-failure
type: Symptom
name: Battery function test failed
aliases:
- Battery charging test failed
- Battery test electric discharge unsuccessful
- Start conditions for battery test not fulfilled
- Battery discharging test failed
- Event 9339
- Event 9336
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA events 9339 (charging test failed), 9340 (discharging test failed) and 9336 (start conditions
    for battery test not fulfilled) appear in the inverter event log.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  - src: src:sma-kb-event-9336-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: ef6af9755620
  - src: src:sma-kb-event-9339-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: 6a386298ab76
  - src: src:sma-kb-event-9339-with-sb3600se-10-or-sb5000se-10
    loc: sec=h1
    h: a9c62979ce12
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: observed_as
  target: meas:battery-soc-reading-low
  note: For event 9336 the battery state of charge is outside the range needed for the test. It may be
    too low, which blocks the discharge test, or too high, which blocks the charge test.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  - src: src:sma-kb-event-9336-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: ef6af9755620
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The inverter logs an event when the battery charge or discharge function test fails or cannot start: on SMA units, 9339 means the charging test failed, 9340 means the discharging test failed and 9336 means the start conditions were not met. Event 9336 is not a hardware fault. The battery is too full or too empty for the chosen test: at 100% charge only the discharge test can run, and near 0% only the charge test can run. On some models a failed charging test means the battery pack could not be charged, so check the battery pack function as described in the service manual. First check how the battery is installed, then run whichever test (charge or discharge) has not been run yet. If the message comes back, suspect an inverter-BMS communication fault. Check the battery communication cable and CAN bus wiring: the Enable and GND lines must be correct, the cable must be at least Cat5e twisted pair, no longer than 10 meters, and stripped 12 mm. When the battery is not detected over CAN, the cause can be faulty bus termination, wrong cabling, an unsuitable cable, poor inverter grounding, outdated software or an inverter defect. A separate CAN interface function test can rule out an inverter defect. Battery self tests check communication, charging and discharging, so a failure may come from any of the three.

<!-- review notes
- sentence 2: support check: partial - The SoC cause and the 100% and near-0% guidance are stated, but the passages never say that 9336 is not a hardware fault.
- sentence 5: support check: partial - The cable and wiring checks (Enable/GND, Cat5e, 10 m, twisted pair, 12 mm stripping) are stated, but the article never calls the cause an inverter-BMS communication fault.
- sentence 7: support check: partial - The passage says the test verifies communications, charge and discharge, but it doesn't say a failure may come from any of the three.
-->
