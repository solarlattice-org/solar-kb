---
id: symptom:iv-curve-distortion
type: Symptom
name: Distorted IV curve shape
aliases:
- curve shape variations
claims:
- claim_id: c1
  rel: observed_as
  target: meas:iv-curve-step
  note: Steps or notches mean bypass diodes are conducting because part of the module or array cannot
    carry the string current. Causes include partial shading, partial soiling or snow, damaged cells,
    a shorted bypass diode, heavy cell mismatch, heterogeneous glass corrosion, and several interconnect
    failures that block current.
  cite:
  - src: src:iec-62446-1
    loc: sec=D.2
    h: e2d1cc6f1a29
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12
    h: f12a39856dc6
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:iv-rounded-knee
  note: A rounder knee can come from aging, or from higher series resistance at failed redundant cell
    interconnects. Check the slopes of both legs first, because changed slopes can make the knee look
    similar.
  cite:
  - src: src:iec-62446-1
    loc: sec=D.5
    h: 91494b8229fd
  - src: src:pv-root-cause-cell-interconnection-failure
    loc: sec=h8
    h: 9f1fbad653f1
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:iv-sloped-isc-region
  note: Shunt resistance has dropped because of shunt paths in the cells or interconnects, slight cell
    mismatch or uneven yellowing. Also listed for heterogeneous glass corrosion.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12
    h: f12a39856dc6
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:iv-shallow-voc-slope
  note: Series resistance has risen in the module, for example from interconnect resistance, corrosion
    in the junction box or interconnects, or slack joints.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:iv-low-isc
  note: Loss of transparency, glass corrosion or delamination acts like reduced irradiance. Homogeneous
    and heterogeneous cases change the curve shape differently.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12
    h: f12a39856dc6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c6
  rel: observed_as
  target: meas:low-voc
  note: Caused by failed cell interconnects, cell-to-cell shorts, bypass diode failure, LID or PID.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
- claim_id: c7
  rel: observed_as
  target: meas:fill-factor-reduction
  note: A sloped Isc region and a shallower slope near Voc both reduce fill factor and Pmax. Metallization
    corrosion shows a lower fill factor from higher series resistance.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h7
    h: 7c7e8aa5f488
  review: drafted
- claim_id: c8
  attr: typical_power_loss
  value:
    max: 3
    unit: unit:PERCENT
  conditions: Power loss from glass corrosion, given as a maximum
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
- claim_id: c9
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Power loss from corrosion of the antireflection coating, usually limited to the coating's
    initial gain
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
---
A normal IV curve is smooth and continuous: a nearly flat leg, a knee, and a steep leg down to open-circuit voltage. Distortion is any departure from that shape compared with the predicted curve. Before you look for a fault, make sure the difference is not caused by measurement error, instrument setup, or wrong module or string data entered in the tracer. For shape tests, use irradiance above 100 W/m2. On stable days, overlay the curves of identical strings, which should normally agree within about 5 %. Steps or notches mean bypass diodes are conducting. Likely causes are partial shading, soiling or snow, damaged cells, a shorted bypass diode, or several cell interconnection failures that block current. A rounded knee with higher series resistance points to failing redundant cell interconnects or to aging. A shallower slope near open-circuit voltage points to resistive joints or corrosion. A lower short-circuit current with an otherwise normal shape suggests uniform glass corrosion or loss of transparency. Patchy glass corrosion can also slope the curve near short-circuit current and add inflection points. Confirm the cause with infrared thermography, electroluminescence and visual inspection. These help separate interconnect failures from cracked cells or diode failures.

<!-- review notes
- sentence 5: support check: partial - Rounded knee with series resistance from redundant interconnect failure and aging is supported, but the shallower Voc slope is linked to interconnect resistance, corrosion and slack joints, not stated as 'resistive joints' exactly (close), and the rounded-knee/high-Rs link to aging is combined loosely.
- sentence 6: support check: partial - Heterogeneous glass corrosion sloping near Isc with inflection points is supported, but homogeneous cases are shown only in the table, and 'otherwise normal shape' for uniform corrosion or transparency loss is implied rather than stated.
-->
