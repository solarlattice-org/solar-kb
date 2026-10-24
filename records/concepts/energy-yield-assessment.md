---
id: concept:energy-yield-assessment
type: Concept
name: Energy yield assessment
aliases:
- yield simulation
- PVsyst simulation
- energy estimate
- Energy yield prediction
- energy yield analysis
- yield estimation
category: Design
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:p50-p90
  note: Yield predictions are stated with confidence levels; investor-grade reports give at least P50
    and P90.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=6.3
    h: d3be6f14d355
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=h7
    h: a3826e06ada4
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:plane-of-array-irradiance
  note: Yield depends roughly linearly on plane-of-array irradiance, so resource-data uncertainty dominates
    prediction uncertainty.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=h7
    h: a3826e06ada4
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=6
    h: 4e28239ad51c
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: related_to
  target: concept:irradiance-transposition
  note: One simulation step converts horizontal irradiation to irradiation on the tilted collector plane
    for each time step.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=6
    h: 4e28239ad51c
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:typical-meteorological-year
  note: Simulations use a time series of typical irradiation and weather, for example an NSRDB TMY3 file.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=6
    h: 4e28239ad51c
  - src: src:enphase-enphase-iq8-pairing-with-imp-over-12a-modules
    loc: sec=h4
    h: 134a0a82052c
  review: drafted
- claim_id: c5
  rel: related_to
  target: tool:pvsyst
  note: Example yield simulations were run in PVsyst.
  cite:
  - src: src:enphase-enphase-iq8-pairing-with-imp-over-12a-modules
    loc: sec=h4
    h: 134a0a82052c
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:shading-loss
  note: A bankable assessment includes a full near and far shading review.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=4.5.1
    h: 43fbe7612a60
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=6
    h: 4e28239ad51c
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2
    h: 4dfe60445738
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: related_to
  target: fm:soiling-losses
  note: Site-specific soiling, snow and the cleaning regime are to be considered.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=4.5.1
    h: 43fbe7612a60
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=6
    h: 4e28239ad51c
  review: drafted
- claim_id: c8
  rel: related_to
  target: metric:performance-ratio
  note: PR prediction adds system design and BOS losses to the module energy rating.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.3
    h: 09d38d63a49f
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2
    h: 4dfe60445738
  review: drafted
- claim_id: c9
  rel: related_to
  target: metric:performance-loss-rate
  note: Module and system degradation affects long-term yield and adds uncertainty.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: tbl=1.r21
    h: ec35aaa4e3ce
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.3
    h: 09d38d63a49f
  review: drafted
- claim_id: c10
  rel: related_to
  target: metric:specific-yield
  note: A simple predicted annual yield is the location's specific annual yield multiplied by the system's
    nominal power.
  cite:
  - src: src:sma-doc-262660
    loc: sec=h272
    h: 13b16b43faa7
  - src: src:sma-doc-262631
    loc: sec=h250
    h: bd9694e20101
  - src: src:sma-doc-262660
    loc: sec=h264
    h: bd9694e20101
  review: drafted
- claim_id: c11
  rel: related_to
  target: metric:performance-index
  note: The Energy Performance Index compares observed specific yield with model-expected yield.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.3.6
    h: 083bce425b5b
  review: drafted
- claim_id: c12
  rel: related_to
  target: concept:om-contract
  note: The cleaning regime specified in the O&M contract feeds into the assessment.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=4.5.1
    h: 43fbe7612a60
  review: drafted
---
An energy yield assessment predicts how much electrical energy a PV plant will produce. It usually gives the average annual output over the plant's lifetime, which is typically taken as 25 to 30 years. It forms the basis for calculating project revenue, and lenders generally want a bankable assessment carried out or reviewed by an independent expert. The method uses hourly or sub-hourly time-step simulation. It takes typical weather data for the site, transposes the irradiance onto the module plane, models how the plant responds to irradiance and temperature, and then applies losses. The losses include near and far shading, soiling or snow, wiring, inverter, mismatch, degradation and downtime. Results are given with confidence levels such as P50 and P90. Because yield follows plane-of-array irradiance closely, uncertainty in the solar resource data dominates the overall uncertainty. Overall uncertainty is often quoted at around 5 percent, but in some cases it can be more than 10 percent. A quick estimate multiplies the specific annual yield for the location by the system's nominal power. After commissioning, the model's expected yield can be compared with the measured specific yield using the performance ratio or the Energy Performance Index.

<!-- review notes
- sentence 4: support check: partial - The passages mention shading, soiling or snow, wiring, inverter, module degradation and downtime, and mismatch in u18, but they do not present these as one list of losses for yield assessment.
- sentence 7: support check: partial - The passages support the quick estimate and the EPI comparison, but nothing says the PR can be used after commissioning to compare the model's expected yield with measured yield.
- sentence 7: review: partial - The SMA example supports the quick estimate and the EPI passage supports comparing measured specific yield with model-expected yield, but 'after commissioning' and using the performance ratio as the comparison metric are not stated.
-->
