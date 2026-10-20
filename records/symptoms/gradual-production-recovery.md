---
id: symptom:gradual-production-recovery
type: Symptom
name: Gradual production recovery
claims:
- claim_id: c1
  rel: observed_as
  target: meas:snow-production-residual
  note: Production falls abruptly after snowfall, then climbs back gradually as snow melts or slides off.
    Line the residuals up against timestamped snowfall, snow depth, temperature, wind and irradiance data.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: drafted
  review_note: 'support check: partial - Passages support abrupt drop then gradual recovery and aligning
    residuals with weather data, but not the specific signal patterns (rising over days, POAI usable while
    AC below expected as stated), though the latter is loosely implied.'
- claim_id: c2
  rel: observed_as
  target: meas:snow-cover-imagery
  note: Camera, drone or field observations of module snow cover, checked against the production residuals
    during the recovery period.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - Passages mention camera/drone/field observations of module cover
    aligned with residuals, but not specifically checking during the recovery period.'
- claim_id: c3
  rel: observed_as
  target: meas:string-current-below-average
  note: While snow partly clears, current becomes uneven across strings and substrings, so the loss does
    not always scale with the visible snow-covered area.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: drafted
  review_note: 'support check: partial - Uneven current across strings during partial clearing is stated,
    but nothing about string currents staying below average or the specific channel.'
---
After a snow event, production falls sharply and then comes back slowly as the snow melts or slides off the modules. The plant can be available and the irradiance sensors can show good resource while covered modules still make little current. Snow that clears only partly makes string and substring currents uneven, so the loss may not match how much snow you can see. Begin with timestamped weather data such as snowfall, snow depth, temperature, wind and irradiance, and line it up with the SCADA production residuals and any camera, drone or field views of snow cover. Compare the measured recovery curve with the energy model's snow-loss assumptions; if a site clears more slowly than modeled, it may need a revised snow-loss factor even when the equipment is fine. Do not put every winter residual down to snow: first filter out cold-weather inverter behavior, clipping, curtailment, trackers frozen in stow, iced sensors and albedo effects. Track winter residuals separately from ordinary soiling losses.

<!-- review notes
- sentence 7: support check: partial - Mitigation says track winter residuals separately from generic soiling; the statement says 'ordinary soiling', which is equivalent, but it's framed as a mitigation not a general rule.
-->
