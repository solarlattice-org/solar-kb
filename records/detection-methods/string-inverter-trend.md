---
id: method:string-inverter-trend
type: DetectionMethod
name: String and inverter trending
aliases:
- string level monitoring
- string-failure detection
claims:
- claim_id: c1
  rel: produces
  target: meas:motor-block-aligned-loss
  note: Normalized string or inverter output can show whether losses line up with grade breaks or tracker
    motor block boundaries rather than with equipment failure.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: produces
  target: meas:ac-power-step-drop
  note: When a string disconnects from a string inverter, AC power falls suddenly by an amount equal to
    that string's share of the power.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=3.1
    h: 9e7ebfc02859
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - u17 gives a sudden AC power decrease equal to the disconnected
    string''s power, but does not mention irradiance being unchanged.'
- claim_id: c3
  rel: produces
  target: meas:string-current-below-average
  note: With DC combiner monitoring, strings below 90% of the inverter's average string current are counted
    as abnormal when estimating string failure or mismatch loss.
  cite:
  - src: src:alsoenergy-kb-pv-model-losses
    loc: sec=front
    h: 10001d881d82
  review: drafted
  review_note: 'support check: partial - u40 uses 90% of average string current to define normally operating
    strings in string loss, but doesn''t say ''persistently'' or an abnormal count; it is also described
    for central inverters with combiners.'
---
String and inverter trending tracks string currents and inverter output over time and compares them against each other, against expected values, and against plant history. Monitoring at string level gives finer troubleshooting than inverter-level data, and current and voltage should be logged for every string at least every 15 minutes. Long-term normalized string or inverter trends help tell average module degradation apart from extra system degradation caused by mismatch when modules age at different rates. For terrain undulation yield losses, normalized row or inverter output compared across morning and afternoon windows shows whether losses cluster at grade breaks or motor block boundaries. Simple signatures, such as a sudden AC power drop matching one string's power, show a string disconnect. Comparisons work best when strings share the same orientation and shading, because uneven alignment or poor irradiance can trigger false alarms or make a normal signal look like a fault. Before touching DC cables when following up on the field, remember that PV strings produce lethal voltage in sunlight: wear proper PPE and confirm the cables are voltage-free with a meter first.

<!-- review notes
- sentence 1: support check: partial - Passages cover comparing trends, expected values and historical performance in pieces, but no single passage states trending string currents and inverter output against each other, expected values and plant history as a whole.
- sentence 4: support check: partial - Passages say comparing normalized row or inverter production across morning and afternoon windows and normalized output can show alignment with grade breaks/motor blocks, but the explicit morning/afternoon comparison showing clustering is only implied by combining them.
- sentence 6: support check: partial - u40 says string loss works best when strings share azimuth, tilt and shading, and u33 notes inhomogeneous alignment causes frequent events and poor irradiance causes erroneous messages, but the 'normal signal looks like a fault' idea is only loosely supported by u17's environmental-conditions example.
-->
