---
id: symptom:abrupt-production-drop
type: Symptom
name: Abrupt production drop
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ac-power-step-drop
  note: After a snow event, output can fall sharply while the plant is still available and irradiance
    sensors still report usable resource, because covered modules cannot turn that light into current.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:snow-production-residual
  note: Production residuals in SCADA data line up in time with snowfall, snow depth, ambient temperature
    and irradiance records.
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
- claim_id: c3
  rel: observed_as
  target: meas:snow-cover-imagery
  note: Camera, drone or field observations confirm that snow covers the modules during the low-output
    period.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: drafted
  review_note: 'support check: partial - Camera/drone/field observations of module cover are mentioned
    as data to align, but not explicitly as confirming snow covers modules during low output.'
- claim_id: c4
  rel: observed_as
  target: meas:string-current-below-average
  note: While snow melts or slides off, partial clearing can leave uneven current across strings and substrings.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  review: drafted
---
An abrupt production drop is a sudden fall in plant output. After a snowfall, it can happen even though the plant is available and the irradiance sensors still show usable sunlight. In snow accumulation yield losses, snow on the module surface blocks the light, so covered modules produce no current. The drop comes suddenly after the snow, and recovery is usually gradual as the snow melts or slides off. During partial clearing, current can be uneven across strings and substrings, so the loss may not match how much snow you can see. Check timestamped weather data first: precipitation type, snowfall, snow depth, ambient temperature, wind and irradiance. Line these up with SCADA production residuals and with camera, drone or field observations of snow on the modules. Book snow cover loss separately from downtime. If snow is present but the system is not producing at all, treat it as downtime, not snow loss. If output recovers more slowly than the energy model's snow-loss assumptions predict, the snow-loss factor may need revising, even when the equipment is working normally. Monitoring should also confirm that the drop comes from a fault or a known cause, not from a cloudy day. Any drop below the expected performance ratio should lead to closer checks by maintenance staff.

<!-- review notes
- sentence 2: support check: partial - Abrupt drop and gradual melt/slide-off are stated, but 'produce no current' is overstated given partial coverage and 'usually' gradual recovery is not exactly stated.
- sentence 5: support check: partial - Passage says snow losses are distinguished from downtime when snow present and system not producing, but doesn't explicitly say to book it as downtime rather than snow loss.
- sentence 7: support check: partial - Passages say algorithms ascertain drop is from a fault not a cloudy day, and a drop in expected PR triggers closer monitoring by maintenance staff, but 'should confirm' as monitoring requirement is a slight stretch.
-->
