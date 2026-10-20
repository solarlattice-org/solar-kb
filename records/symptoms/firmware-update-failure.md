---
id: symptom:firmware-update-failure
type: Symptom
name: Firmware update failure
claims:
- claim_id: c1
  rel: observed_as
  target: meas:update-condition-test-failed
  note: 'SMA event 7330: the update conditions check did not pass because the firmware package does not
    suit this inverter model.'
  quote: The testing of the update conditions was not successful. The firmware update package is not suitable
    for this inverter.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=9.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=20.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=9
    h: 782760f993f4
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=20
    h: 782760f993f4
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:firmware-integrity-check-abort
  note: On the Eaton SPD, a codepack integrity check stops the update when any image in a multi-image
    update is corrupt. The required action is to re-install the firmware.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=19.r13
    h: d8741a17a92d
  review: drafted
---
A failed firmware update shows up as an event message in the device's event log or on its user interface, not as a change in power output. On SMA string inverters, event 7330 (Condition test failed) means the update file did not pass the update-condition check because it is not the right package for that inverter. Events 7331 and 7332 show the update file being copied and then stored in the inverter's internal memory, so they tell you how far the update got before it stopped. On an Eaton surge protection device, the message that a codepack integrity check aborted the update means one of the images was corrupt, and the firmware should be installed again. After any update, open the user interface and look in the events for the success message (event 7320 on SMA units) to confirm the update finished. If the condition check fails, first make sure the update file you selected is the correct one for that product. Firmware problems can lead to a complete inverter failure, and software issues are normally fixed with a firmware update. If a restart does not help or the fault keeps coming back, a service team usually needs to find the cause.

<!-- review notes
- sentence 1: support check: partial - Passages show failures as event/error messages and that events are checked in the UI, but nothing says it does not appear as a power output change.
- sentence 3: support check: partial - 7331/7332 describe copying started and completed, but the passages don't say they indicate how far an update got before stopping.
- sentence 5: support check: partial - Event 7320 is the success event and the procedure says to check events in the UI, but this is only stated for the UI procedure, not 'any update' in general.
- sentence 6: support check: partial - The package being unsuitable and selecting the update file for the product are stated, but no passage explicitly instructs checking the file first after a failure.
-->
