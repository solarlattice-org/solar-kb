---
id: method:battery-function-test
type: DetectionMethod
name: Battery charge/discharge function test
aliases:
- Battery charging test
- Discharge battery test
- Testing the function of the battery pack
- battery function test
- Battery Self Test
- function test
claims:
- claim_id: c1
  rel: produces
  target: meas:battery-function-test-failed-event
  note: The inverter logs a failed event for the charging test or the discharging test. The suggested
    follow-up is to check how the battery is installed and then run whichever test has not yet been done.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: produces
  target: meas:battery-function-test-passed-event
  note: Separate success events are logged for the charging test and the discharging test.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: produces
  target: meas:battery-test-start-conditions-unmet
  note: The test cannot start because the battery state of charge is too high or too low. For example,
    a battery at full charge can only be given the discharge test.
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
The battery function test checks that a connected battery accepts charge and delivers discharge on command. The inverter runs a separate charging test and a separate discharging test. On some hybrid inverters, you start the test in the battery configuration step of the installation wizard with the Charge battery and Discharge battery buttons. The test needs a suitable state of charge. A nearly full battery cannot be test-charged and a nearly empty battery cannot be test-discharged, so pick the test the battery can actually do. The inverter logs whether each test passed or failed. If a test fails, check how the battery is installed and run the test that has not yet been done. Even if a test is reported as unsuccessful, finish the installation wizard as usual. Some home hub systems have a battery self test under the maintenance diagnostics menu. It checks communications, charging and discharging, and saves past results for review. At large storage commissioning, a balancing test is run in both the charge and discharge directions after a manual discharge at rated power. Do not move on with the test plan unless these tests pass.

<!-- review notes
- sentence 1: support check: partial - Separate charging and discharging tests exist, but the passages never say the test checks that the battery accepts charge and delivers discharge on command; that purpose is inferred.
- sentence 6: support check: partial - The Home Hub self test under Maintenance > Diagnostics verifies communications, charge and discharge, and lets you view past results; 'saves past results' is implied, and 'some home hub systems' is a framing not in the passages.
- sentence 7: support check: partial - Passages state discharge to 0 by manual command at rated power, balancing test in both directions, and not moving forward unless all tests pass; they do not mention 'large storage commissioning' explicitly.
- sentence 7: review: partial - Powin secs 8.6/10.0 support a balancing test in both directions after a manual discharge to 0 at rated power, and say not to move the test plan forward unless all tests pass, but the 'large storage commissioning' scope is not…
-->
