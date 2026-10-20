---
id: symptom:dark-surface-deposits
type: Symptom
name: Dark surface deposits
aliases:
- bio-soiling
- dark masses
- biological deposits
- sub-aerial biofilms
claims:
- claim_id: c1
  rel: observed_as
  target: meas:biofilm-surface-coverage
  note: Handheld digital microscopes image the glass directly. In a dataset of 50,000 images, average
    coverage was 3.2 +/- 4.9%, and observed coverage ranged from 0.2% to 34%. Bio-soiling was found in
    eight Koppen-Geiger climate zones.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h6
    h: 27c24638759c
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h5
    h: 4e874b23e982
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:no-recovery-after-rain
  note: Fungal deposits stay on the glass through rainfall, while ordinary dust may partly wash off.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h5
    h: 4e874b23e982
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:post-cleaning-production-step
  note: The key evidence is a production step-change after cleaning that repeats, especially where rain
    did not restore the expected output.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c4
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  review: drafted
---
Dark deposits on the module glass can come from sub-aerial biofilms, mainly black fungi. These organisms grow into dark masses and trap other particles. The deposits reduce how much light passes through the glass. The resulting soiling loss can change over time, and in humid subtropical regions it can stay at 5 to 11 percent of production. To tell fungal soiling apart from granular dust, look at how production responds to rain. Dust losses usually recover partly or fully after rain, while fungal deposits stay attached until targeted cleaning removes them. Check first whether irradiance-normalized production stays low after rain but steps up after a manual cleaning. Compare cleaning records against SCADA, irradiance and weather data to confirm this. Confirm the contaminant with a close visual inspection or a handheld microscope. The deposits can be patchy, so inspect several areas of the array rather than one representative module. Where deposits persist, clean as routine maintenance and update the production forecasts using the cleaning results.
