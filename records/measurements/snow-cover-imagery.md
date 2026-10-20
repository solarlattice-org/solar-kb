---
id: meas:snow-cover-imagery
type: Measurement
name: Snow cover in imagery
aliases:
- time-series POA digital images
- camera observations
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Annual snow losses for standard framed modules at latitudes above 60°N in Sweden
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Annual losses from snow coverage in most climates
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.1
    h: bc5cf195e596
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 18
    unit: unit:PERCENT
  conditions: Annual production loss, snow-covered vs cleaned modules at 0° tilt, Sierra Mountains, USA
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 15
    unit: unit:PERCENT
  conditions: Annual production loss, snow-covered vs cleaned modules at 24° tilt, Sierra Mountains, USA
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c5
  attr: typical_power_loss
  value:
    nominal: 12
    unit: unit:PERCENT
  conditions: Annual production loss, snow-covered vs cleaned modules at 39° tilt, Sierra Mountains, USA
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c4 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c6
  attr: typical_power_loss
  value:
    min: 0.3
    max: 2.7
    unit: unit:PERCENT
  conditions: Annual snow-cover losses, grid-connected frameless modules at 28° tilt, Bavaria, Germany
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 23
    unit: unit:PERCENT
  conditions: Monthly loss from snow cover in January 2017, Konya, Turkey, cleaned vs snow-covered string
  note: Daily losses in the same study were reported as almost total.
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c4 (same source; check the conditions); possible conflict with c5 (same source;
    check the conditions); possible conflict with c6 (same source; check the conditions)
---
This signature is snow seen covering modules in camera, drone or field images, shown either as full cover or as patches of covered and clear module area. Time-series images of the array plane, taken at five-minute intervals, can be split into snow and clear areas so the percentage of cover can be measured per module and per string. The image method does not yet measure snow depth, and snow often sheds unevenly across an array, so depth varies between modules. Match image timestamps with weather data and SCADA production residuals so you can tell when the array was covered, and how much of it, during snow and melt periods. The visible covered area does not always match the energy loss, because partial clearing causes uneven current across strings and substrings. Also check the lower edge of the array, since snow mounds shed under the rows can block the bottom of the modules. The failure mode behind this signature is Snow Accumulation Yield Losses, and surveillance cameras are recommended so that snow is detected quickly.

<!-- review notes
- sentence 1: support check: partial - Camera, drone or field observations of module cover and uneven shedding are mentioned, but nothing says the signature is defined as snow seen in images or describes full versus patchy appearance explicitly.
- sentence 2: support check: partial - Five-minute binarized images and module- and string-level snow cover quantification are stated, but in separate passages and the images are not specified as array-plane images.
- sentence 7: support check: partial - NITE's recommendation of surveillance cameras to detect snow quickly is stated, but the passages do not name the failure mode 'Snow Accumulation Yield Losses' (they only describe snow accumulation losses in the Soiling category).
-->
