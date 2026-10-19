---
id: fm:snow-accumulation-losses
type: FailureMode
name: Snow Accumulation Yield Losses
category: Soiling
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:snow-load
  note: Loss arises when snow stays on the module surface after a snow event and blocks irradiance.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  review: drafted
  review_note: 'support check: partial - Passages say snow remaining on modules after a snow event blocks
    irradiance, but don''t name heavy snowfall as a stressor/cause explicitly.'
- claim_id: c2
  rel: caused_by
  target: stressor:low-sun-angle
  note: Low sun angles can extend how long snow stays on the array.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h5
    h: 7b6f8fb933e9
  review: drafted
  review_note: 'support check: partial - Low sun angle is said to affect how long snow remains, but not
    stated as a cause of the loss itself.'
- claim_id: c3
  rel: caused_by
  target: stressor:cold-module-temperature
  note: Cold modules can keep snow on the array longer; frame geometry, orientation and tracker position
    also matter.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h5
    h: 7b6f8fb933e9
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:module-glass
  note: Snow covering the module surface stops irradiance from reaching the cells.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:abrupt-production-drop
  note: Output can fall abruptly right after snowfall.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c6
  rel: presents_as
  target: symptom:gradual-production-recovery
  note: Output returns gradually as snow melts or slides off.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: presents_as
  target: symptom:low-output-despite-irradiance
  note: The plant is available and irradiance sensors show usable resource, but covered modules produce
    no current.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:uneven-string-current
  note: Partial clearing leaves clear and covered cells at different current levels, so loss is not proportional
    to visible snow area.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h5
    h: 7b6f8fb933e9
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:substring-loss
  note: Partial clearing can produce uneven current across substrings.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:weather-normalized-comparison
  note: Line up production residuals with snowfall, snow depth, precipitation type, ambient temperature,
    wind, plane-of-array irradiance and module temperature.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:camera-observation
  note: Camera images confirm whether modules are covered.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:drone-inspection
  note: Drone observations of module cover can be matched to SCADA residuals.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:visual-inspection
  note: Field observations of snow cover on the modules.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c14
  rel: detected_by
  target: method:snow-loss-model-comparison
  note: Compare measured recovery curves with regional snow-loss model output and the energy model assumptions.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c15
  rel: mitigated_by
  target: mit:loss-factor-separation
  note: Track winter residuals separately from generic soiling so snow losses are not hidden in monthly
    weather variance.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h5
    h: 7b6f8fb933e9
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer 2026-10-19: target mit:seasonal-residual-tracking merged into mit:loss-factor-separation'
- claim_id: c16
  rel: mitigated_by
  target: mit:tilt-optimization
  note: Consider tilt changes where they are economic.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:tracker-stow-strategy
  note: Evaluate tracker stow changes where they are economic.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c18
  rel: distinguished_from
  target: fm:grid-curtailment-losses
  by: method:weather-normalized-comparison
  note: Curtailment can overlap with snow events and should be filtered out using snowfall and cover data
    before recoverable snow loss is estimated.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h7
    h: a5ed6e5ad384
  review: drafted
  review_note: 'support check: partial - Curtailment overlapping with snow events and needing filtering
    is stated, but not the use of weather-normalized comparison or snowfall/cover data specifically.'
- claim_id: c19
  rel: distinguished_from
  target: fm:soiling-losses
  by: method:weather-normalized-comparison
  note: Snow losses are seasonal and tied to snowfall and recovery intervals; winter residuals should
    be tracked apart from generic soiling.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Tracking winter residuals separately from generic soiling is
    stated, but not weather-normalized comparison as a distinguishing method nor explicitly seasonal tied
    to recovery intervals in these passages.'
---
Snow accumulation losses happen when snow stays on the module surface after a snow event, so covered modules cannot turn the available irradiance into current. Production usually drops sharply after snowfall and comes back gradually as the snow melts or slides off, even while the plant is available and irradiance sensors show good resource. Patchy clearing causes mismatch between clear and covered cells, so current can be uneven across strings and substrings, and the loss may not match the visible covered area. Low sun angles, cold module temperatures, frame geometry, module orientation and tracker position all affect how long snow stays on the array. To confirm, line up timestamped snowfall, snow depth, temperature, wind and irradiance data with SCADA production residuals and with camera, drone or field observations of snow cover. Before blaming snow, filter out cold-weather inverter behavior, clipping, curtailment, frozen tracker stow, sensor icing and albedo effects. Compare measured recovery curves with the snow-loss assumptions in the energy model, and revise the snow-loss factor if the site clears more slowly than modeled. Track winter residuals separately from general soiling, and consider tracker stow, tilt, maintenance or design changes where they pay off.

<!-- review notes
- sentence 2: support check: partial - Passages say 'can be' abrupt and gradual, not 'usually', and 'may' be available.
-->
