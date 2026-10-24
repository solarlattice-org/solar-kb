---
id: tool:inclinometer
type: Tool
name: Inclinometer
aliases:
- digital level
- angle gauge
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  rel: part_of
  target: comp:single-axis-tracker
  note: The tracker inclinometer is a transducer built into the tracker control unit (TCU). It reports
    the tracker tilt angle that the controller uses as position feedback.
  cite:
  - src: src:test-cx-manuals-trina-ps-cm-commissioning-manual-vanguard
    loc: sec=5.2
    h: 9cbea1b23987
  - src: src:trn-training-industry-reports-and-guides-nrel-one-axis-trackers-improved-reliability-durability-perf
    loc: sec=h22
    h: 488244ea4280
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
An inclinometer measures tilt angle. On single-axis trackers it is a transducer built into the tracker control unit (TCU), and it gives the controller the tracker's inclination angle. Solid-state inclinometers replaced the older potentiometer feedback. They are more reliable, have finer resolution and measure the angle directly. Tracker commissioning includes the inclinometer angle adjustment, an offset setup that gives the controller an accurate reference angle. The controller stores this reference and uses it to work out tracker position. To set the offset, put a digital level on the flat of the panels and move the tracker by hand to a known angle, preferably horizontal. Enter the angle the level reads as the set point in the handy terminal or computer app, then check that the current position shown matches it. The TCU must be fixed firmly to the rotation axis so it turns with the tracker. Check orientation by moving the tracker east (the reading should go down) and then west (the reading should go up). If the readings move the wrong way, change the inclinometer orientation setting between north and south in the terminal or app. You have to log in before you can change it. A handheld inclinometer is also on the standard O&M toolkit list, next to a level and a compass. In shade measurements, the inclinometer's accuracy affects the result, so it should be factory calibrated.

<!-- review notes
- sentence 7: support check: partial - u7 lists the inclinometer, level and compass among tools, and u16 says shade-measurement accuracy depends on the inclinometer and all sensors should be factory calibrated. u7 does not say it is a handheld inclinometer or a standard O&M list, though.
- sentence 7: review: partial - The passages list the inclinometer with a level and a compass as O&M tools and say its accuracy affects shade measurements, with all sensors factory calibrated, but 'handheld' and 'standard toolkit list' are not stated.
-->
