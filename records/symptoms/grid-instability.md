---
id: symptom:grid-instability
type: Symptom
name: Grid instability
aliases:
- Grid unstable
- GRID-INTF
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ac-line-thd-high
  note: The Solis GRID-INTF (grid unstable) alarm guidance says to test the AC line for THD with the DC
    switch off and again with it on, so distortion on the grid side is the signature to look for.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
  review_note: 'support check: partial - Passage supports testing AC line THD for GRID-INTF, but says
    nothing about the specific signals (phase voltage, current) being distorted or the measurement-type
    linkage beyond THD testing.'
- claim_id: c2
  rel: observed_as
  target: meas:grid-voltage-reading-out-of-limit
  note: For a repeated Sungrow Grid Abnormal fault, measure the actual grid and contact the utility if
    a grid parameter is outside the set range.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=39.r5
    h: 3c84a7b77032
  review: drafted
  review_note: 'support check: partial - Passage says to measure the grid and contact the utility if grid
    parameters exceed the set range, but doesn''t mention phase voltage or frequency specifically as outside
    limits.'
---
Grid instability shows up as an inverter alarm. On Solis units it is GRID-INTF, which means the inverter has seen an unstable grid or high internal fault current. First measure the AC voltage and test the AC line for harmonic distortion with the DC switch off. Then repeat the distortion test with the DC switch on. If the distortion is already there with the DC side off, the cause is probably on the grid side. If several inverters share the line, switch one off to see whether they are interacting. An impedance matching adjustment or matching box may help. If the grid looks clean, look for internal damage in the inverter or a wire that came loose during shipping. Sungrow inverters show a similar Grid Abnormal fault and start again once the grid is back to normal. If the fault keeps coming back, measure the grid. Call the local utility if a grid parameter is outside the set range, or Sungrow service if those causes are ruled out.

<!-- review notes
- sentence 3: support check: partial - Multiple inverters/turn one off and impedance matching are listed, but the inference that distortion with DC off implies a grid-side cause is not stated.
- sentence 4: support check: partial - Internal damage and loose wire in shipping are listed, but the conditional 'if grid looks clean' sequencing is not stated.
- sentence 5: support check: partial - Repeated-fault steps (measure grid, utility, Sungrow service) are stated, and the row begins with a fragment about the grid returning to normal, but automatic restart isn't clearly stated and 'similar' comparison is not in the passage.
-->
