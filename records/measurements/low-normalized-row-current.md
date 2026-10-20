---
id: meas:low-normalized-row-current
type: Measurement
name: Low normalized row current
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: lower POA-normalized string current than adjacent rows, varying between morning, noon and afternoon
    windows
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used to normalize string current
- point: model_307.WndSpd
  unit: unit:M-PER-SEC
  pattern: loss more visible during windy intervals
---
This signature is a tracker row whose normalized current comes in below the current of the rows next to it. The modules, inverters and irradiance sensors on that row can still look healthy. Tracker twist is the failure mode known to cause it. In a twisted row, one end or section sits at a different tilt from the rest of the row. The pattern often depends on time of day. It shows up most clearly at low sun angles, during backtracking transitions and in windy periods. Before comparing rows, normalize the output for irradiance and for inverter clipping. Then look at morning, solar-noon and afternoon data separately, because a twisted row can look fine at one tracker position and underperform at another. Comparing string output normalized to plane-of-array irradiance against the commanded and measured row angles helps confirm the cause. In the field, measure string currents with a clip-on ammeter while the inverter is tracking normally. Under stable irradiance, identical strings should usually read within 5 % of the average string current. If irradiance is unstable, you can delay the test, use a reference string, correct the readings with an irradiance meter, or run an IV curve test. Several factors other than twist can also make the measured current lower than expected.

<!-- review notes
- sentence 4: support check: partial - Passage says to identify underperforming rows after normalizing for irradiance and clipping and to compare morning, noon and afternoon windows, but it doesn't say to normalize before comparing rows. 'Solar-noon' and the reason are present.
-->
