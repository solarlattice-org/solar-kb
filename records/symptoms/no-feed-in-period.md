---
id: symptom:no-feed-in-period
type: Symptom
name: Extended no feed-in period
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Galvo, Primo and Symo show status code 509 as a warning on the display when nothing has
    been fed in for 24 hours. Symo code 520 is the same warning for MPPT1 only.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: f098c673c83b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r2
    h: 0258f1217490
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r2
    h: 1e877d15227f
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r8
    h: 12b4c0960794
  review: drafted
  review_note: 'support check: partial - Passages show 509 and 520 as warnings on the display for no feed-in
    in 24 hours, but they don''t name Galvo, Primo or Symo models.'
---
The inverter has fed no power into the grid for at least the last 24 hours, and it shows a warning on its display. On Fronius Galvo, Primo and Symo inverters this warning is status code 509. On Symo units, code 520 shows the same condition for the MPPT1 input only, which points to that one input rather than the whole inverter. First, acknowledge the status code and check that all conditions for normal grid feed-in are met, for example that the modules are not covered with snow. If the code keeps coming back, look at the other status codes the inverter logs to find the real cause.

<!-- review notes
- sentence 2: support check: partial - Code 509 matches the description, but the passages don't name Galvo, Primo or Symo as the models.
- sentence 3: support check: partial - Code 520 is no feed-in in 24 hours from MPPT1 only, but the passage doesn't name Symo, and 'points to that one input' is only an inference.
-->
