---
id: meas:snow-production-residual
type: Measurement
name: Snow-aligned production residual
aliases:
- Snow cover loss
- winter residuals
- SCADA production residuals
signals:
- point: model_103.W
  unit: unit:W
  pattern: abrupt drop after snowfall, gradual recovery during melt
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: usable irradiance reported while output stays low
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: module temperature used alongside residuals to follow melt
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: Yearly snow losses for standard framed modules at latitudes above 60°N in Sweden; 'most
    often' less than this
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passage says losses are ''most often less than 10%'' yearly;
    the statement frames this as ''up to 10%'' typical, which is roughly equivalent but an upper bound
    rather than typical.; possible conflict with c2 (same source; check the conditions); possible conflict
    with c3 (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)'
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 18
    unit: unit:PERCENT
  conditions: Annual production loss, snow-covered vs cleaned modules side by side, Sierra Mountains USA,
    0° tilt (Powers et al.)
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions)
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 15
    unit: unit:PERCENT
  conditions: Annual production loss, snow-covered vs cleaned modules, Sierra Mountains USA, 24° tilt
    (Powers et al.)
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions)
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 12
    unit: unit:PERCENT
  conditions: Annual production loss, snow-covered vs cleaned modules, Sierra Mountains USA, 39° tilt
    (Powers et al.)
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions)
- claim_id: c5
  attr: typical_power_loss
  value:
    min: 0.3
    max: 2.7
    unit: unit:PERCENT
  conditions: Annual snow-cover losses, grid-connected frameless modules at 28° tilt, Bavaria, southern
    Germany
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c7 (same source; check the conditions)
- claim_id: c6
  attr: typical_power_loss
  value:
    max: 100
    unit: unit:PERCENT
  conditions: Daily loss from snow cover, Konya, Turkey, January 2017, cleaned vs snow-covered modules
  note: Source says daily losses could be almost 100%
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage says daily losses could be almost 100% in Konya Jan 2017;
    ''typical'' up to 100% is slightly overstated but the note acknowledges it.'
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 23
    unit: unit:PERCENT
  conditions: Monthly loss from snow cover, Konya, Turkey, January 2017
  cite:
  - src: src:iea-pvps-t13-25-2022
    loc: sec=5.7.4
    h: 0de438523b95
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions); possible conflict with c3 (same source; check the conditions);
    possible conflict with c4 (same source; check the conditions); possible conflict with c5 (same source;
    check the conditions)
---
This signature is a shortfall between measured production and expected snow-free production that lines up in time with snowfall and snow on the modules. The plant can be available, and irradiance sensors can show usable resource, while snow-covered modules still produce little or no current. The loss often appears suddenly after snowfall, then fades gradually as the snow melts or slides off. Partial clearing can leave string and substring currents uneven, so the residual does not always scale with how much snow you can see. To confirm it, line up the SCADA residuals with timestamped snowfall, snow depth, temperature, wind and plane-of-array irradiance, plus camera, drone or field observations; a heated POA pyranometer helps provide the irradiance reference. Not every winter residual is snow: filter out cold-weather inverter behavior, clipping, curtailment, trackers frozen in stow, iced sensors and albedo effects before estimating the loss. If measured recovery after snow is slower than the energy model assumes, the model's snow-loss factor may need revising even when the equipment is working normally.
