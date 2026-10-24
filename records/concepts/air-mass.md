---
id: concept:air-mass
type: Concept
name: Air mass
aliases:
- AM1.5
- AM 1.5
- AM
- Absolute air mass
- AMa
- Air Mass 1.5 G
category: Irradiance
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:standard-test-conditions
  note: AM 1.5 sets the spectral distribution used for STC module rating.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h83
    h: 595094656aa5
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=8
    h: 251e1e2ddbf1
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:nominal-operating-cell-temperature
  note: NOCT conditions also specify an Air Mass 1.5 G spectrum.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=8
    h: 251e1e2ddbf1
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:direct-normal-irradiance
  note: Air mass is the relative path length that direct solar radiation travels through the atmosphere.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h83
    h: 595094656aa5
  review: drafted
  review_note: 'support check: partial - Air mass is defined as the path length of direct solar radiation,
    but the passages never link it to direct normal irradiance as a concept.'
- claim_id: c4
  rel: explains
  target: fm:spectral-effect-losses
  note: Changes in air mass shift the solar spectrum, which changes module short-circuit current.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h16
    h: 196ba4bcf438
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=3.2.2
    h: cc128f301ebe
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:short-circuit-current
  note: Performance models use an empirical air-mass function to correct Isc for spectral effects.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h16
    h: 196ba4bcf438
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=3.2.2
    h: cc128f301ebe
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:thin-film-pv
  note: Amorphous silicon modules show a stronger spectral response, so air mass is added as a model parameter.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=3.2.2
    h: cc128f301ebe
  review: drafted
  review_note: 'support check: partial - Air mass is added as a model parameter for a-Si because of its
    spectral response, but the passages do not compare a-Si to other technologies as having a ''stronger''
    response, and they do not say ''thin-film'' generally.'
- claim_id: c7
  rel: related_to
  target: stressor:air-mass-variation
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=h89
    h: c6cbc7d03242
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h16
    h: 196ba4bcf438
  review: drafted
- claim_id: c8
  attr: typical_power_loss
  value:
    max: 3
    unit: unit:PERCENT
  conditions: Cumulative effect of solar spectral (air mass) variation on annual energy production, as
    reported in the Sandia array performance model
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h16
    h: 196ba4bcf438
  review: drafted
  review_note: 'support check: partial - The passages say the cumulative spectral effect on annual energy
    is less than 3%, which supports an upper bound, but not a ''typical loss up to 3 percent''. Also the
    effect is not described as a loss.'
---
Air mass is the relative length of the path that direct sunlight takes through the atmosphere. It changes with sun position and with site altitude, which is why it is corrected using the ratio of local pressure to sea-level pressure. It is calculated as one divided by the cosine of the solar zenith angle. AM 0 means sunlight outside the atmosphere, and AM 1 means the sun is directly overhead at sea level. AM 1.5 matches a sun altitude of about 42 degrees. It is the reference spectrum used to test and rate PV cells and modules under Standard test conditions and NOCT conditions. Air mass changes both the amount of sunlight reaching the ground and its spectral content, so a module's short-circuit current moves as air mass changes through the day. For crystalline silicon, normalized Isc is typically several percent higher at high air mass than at solar noon. Over a year the spectral effect on energy production is usually small: more than 90% of the available solar energy arrives at air mass values below 3. Amorphous silicon thin-film modules respond more strongly, so models for them may add air mass as an extra parameter. When analysing monitoring data, setting a minimum sun elevation angle keeps air mass differences small, which keeps spectral mismatch low when you compare performance.

<!-- review notes
- sentence 2: support check: partial - 1/cos(zenith), AM 0 as outside the atmosphere, and AM 1 with the sun overhead are stated, but AM 1 is stated 'in the tropics' or at sea level for AMa, not generally for both together; mostly supported.
-->
