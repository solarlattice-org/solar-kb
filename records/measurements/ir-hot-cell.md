---
id: meas:ir-hot-cell
type: Measurement
name: Hot cell in IR image
aliases:
- Heated cells
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    max: 25
    unit: unit:DEG_C
  conditions: IBC half-cell module with built-in Zener bypass behaviour, indoor hot-spot test at 55°C
    module temperature per IEC 61215-2:2021; rise of hot cell over module temperature
  note: Reported as significantly lower than PERC and SHJ modules under the same test.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
- claim_id: c2
  attr: temperature_rise
  value:
    min: 10
    max: 20
    unit: unit:DEG_C
  conditions: Heated cells in field IR inspection classed as unproblematic at the current stage, to be
    observed in regular thermographic inspections
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h58
    h: df4b70555c37
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c3
  attr: temperature_rise
  value:
    min: 15
    unit: unit:DEG_C
  conditions: Severe cell defects seen in UAV-based IR mapping of a plant with more than ten thousand
    modules; such defects correlated strongly with reduced string current
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: temperature_rise
  value:
    nominal: 3
    unit: unit:DEG_C
  conditions: Cells located close to the junction box versus the rest of the cell matrix, 2 kWp c-Si installation
    after 12 years of field exposure
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.1.3
    h: 73bb98342b5b
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions)
---
A hot cell shows up in the IR image as one whole cell that is evenly warmer than its neighbours. This is different from a hot spot, where the heat is concentrated in one small area. It usually comes from cell cracking or shading, which causes a current mismatch and drives the weaker cell into reverse bias, so the cell dissipates power as heat. Take the image during clear, stable weather with high irradiance and the inverter running. Make sure the module has reached steady state, and compare short-circuit, open-circuit and maximum power point load conditions where you can. Cells affected by PID by shunting look warmer in sunlight near maximum power point. They look cooler when current is injected in the dark. Look for warm cells near the bottom frame on modules close to the negative pole of the string. Cell cracks and cell interconnection failures can also show up as heated cells or hot spots in IR images. Hot cells can lead to further damage such as discoloration, delamination, interconnection failures, cell cracks and loss of electrical insulation. Keep moderately heated cells under close watch in regular thermographic inspections, because the temperature difference may grow over time.

<!-- review notes
- sentence 1: support check: partial - Passage says a hot cell gives a homogeneous temperature rise throughout the cell area versus the localised heating of a hot spot, but 'evenly warmer than its neighbours' in the IR image is a slight extrapolation.
- sentence 2: support check: partial - Cell cracking or shading causing current mismatch and reverse bias with the cell dissipating heat is stated, but 'usually' is not stated.
- sentence 5: support check: partial - Interconnection failure appearing as a hot spot in IR is stated, and figure captions suggest IR detection of cracks, but no passage text states that cracks appear as heated cells or hot spots.
-->
