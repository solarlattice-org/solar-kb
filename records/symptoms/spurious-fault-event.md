---
id: symptom:spurious-fault-event
type: Symptom
name: Spurious fault event
aliases:
- Phantom event
- False alarm
- Event is non-relevant
- Relay error incorrectly displayed
- DC converter defective (no effect)
claims:
- claim_id: c1
  rel: observed_as
  target: meas:prediction-bound-exceedance
  note: In a statistical fault-detection test, measured voltage rose above the algorithm's upper bound
    just after a shading test ended. The algorithm logged a fault even though the module was no longer
    shaded, so the alarm was false.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=5.3.1.1
    h: 33ef5a556b09
  review: drafted
---
A spurious fault event is a fault or error message that appears even though no real hardware fault exists. The device may still block operation, as if the fault were real. One documented case is a firmware defect in an EV charger: an earlier firmware version reported a relay error and put the unit into operation inhibition while the relay hardware was fine. The manufacturer corrected this in a later firmware release. Before replacing parts, check the installed firmware version and update it, either automatically or by hand. Monitoring software can also raise false alarms. A statistical detector that compares measured power and voltage with predicted bounds flagged a fault when voltage briefly went above the upper bound right after a shading test had ended. Such detectors are tuned for a low false alarm rate, but some false alarms still occur. Check whether the flagged deviation lines up with a real, lasting change in output before sending a crew.

<!-- review notes
- sentence 3: support check: partial - The fix in FW 2.01.39.R and checking/updating (automatic or manual) are stated, but 'before replacing parts' is not stated.
- sentence 5: support check: partial - The passage supports low false alarm targets (<10%, lowest 7%) and some false alarms, but the advice to check for a real, lasting change before dispatching a crew is not stated.
-->
