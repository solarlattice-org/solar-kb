---
id: symptom:grid-overfrequency
type: Symptom
name: Grid overfrequency
aliases:
- OV-G-F
- Over Grid Frequency
- Overfrequency
claims:
- claim_id: c1
  rel: observed_as
  target: meas:grid-frequency-reading-out-of-limit
  note: The inverter reports an overfrequency fault and disconnects from the grid while the frequency
    stays outside the permitted range.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=48.r1
    h: fb249c3b40c0
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h162
    h: bd3d762be238
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
The inverter raises a grid overfrequency fault when the grid frequency it measures goes above its upper limit. While the frequency is out of range, the inverter disconnects from the grid and stops exporting power. Usually the inverter reconnects by itself once the grid is back to normal. Some controllers use a separate overfrequency threshold that the grid must meet before reconnection is allowed. If the fault keeps coming back, first turn the DC switch off and measure the actual grid frequency at the inverter test points. If the grid really is high, contact the local utility. Next, check the grid standard and the overfrequency protection settings. Example defaults are 60.5 Hz on one SMA model, and 61.2 Hz and 62 Hz for the two Solis stages. Only raise the upper limit with the utility's permission. If the frequency you measure is normal but the inverter display still shows it as high, the inverter's measurement circuit may be faulty, and the inverter may need replacing. Some controllers expose the grid frequency reading over Modbus, so you can trend it in monitoring and compare it with the trip times.

<!-- review notes
- sentence 2: support check: partial - Disconnection from the grid is stated, but 'stops exporting power' is only implied and not explicitly said.
- sentence 4: support check: partial - Measuring frequency with DC switch off and contacting the utility are present, but the 'first' ordering and 'contact utility if grid is high' are only loosely supported; u16 says adjust limit with utility permission.
- sentence 5: support check: partial - Defaults 60.5, 61.2, 62 Hz and utility permission are present, but the SMA brand isn't named in the passage and 'check protection settings' is only implied.
- sentence 6: support check: partial - Passage says check LCD reading, may be a bad measurement circuit, and replace inverter, but the explicit normal-measured-vs-display-high conditional and replacement linkage are loosely stated.
- sentence 7: support check: partial - Modbus register for grid frequency is given, but trending in monitoring and comparison with trip times is not stated.
-->
