---
id: fm:energy-meter-installation-error
type: FailureMode
name: Energy meter installation position error
aliases:
- PV connected on grid side of meter
- meter orientation incorrect
- phase assignment switched between charger and meter
- feed-in at night
- installed the wrong way round
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:installation-error
  note: The meter is mounted backwards, CTs or their secondary leads are reversed, or the PV feeder lands
    on the grid side of the meter.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  - src: src:sma-doc-240154
    loc: tbl=88.r1
    h: 23b7c5792a07
  - src: src:sma-doc-243910
    loc: sec=h54
    h: 3b5e487495bd
  review: drafted
  review_note: 'support check: partial - Passages support meter reversed, CTs/leads reversed, and PV on
    grid side as installation faults, but don''t name the generic ''installation error'' stressor explicitly
    beyond ''installed wrong way round''; mostly supported.'
- claim_id: c2
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  - src: src:sma-doc-240154
    loc: tbl=88.r1
    h: 23b7c5792a07
  - src: src:sma-doc-243910
    loc: sec=h54
    h: 3b5e487495bd
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:unrealistic-meter-values
  quote: The Energy Meter has been installed the wrong way round.
  cite:
  - src: src:sma-doc-240154
    loc: tbl=88.r1
    h: 23b7c5792a07
  - src: src:sma-doc-240154
    loc: tbl=88
    h: 883cfebb83c2
  - src: src:sma-doc-243910
    loc: sec=h54
    h: 3b5e487495bd
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:meter-wiring-reversed
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  - src: src:sma-doc-240154
    loc: tbl=88.r1
    h: 23b7c5792a07
  - src: src:sma-doc-243910
    loc: sec=h54
    h: 3b5e487495bd
  review: drafted
  review_note: 'support check: partial - Passages state meter/CT/lead orientation reversed causes wrong
    readings, but a ''meter wiring reversed'' symptom is only loosely stated (wrong way round).'
- claim_id: c5
  rel: presents_as
  target: symptom:night-grid-feed-in
  note: Possible causes include a reversed meter, reversed CTs or reversed CT secondary leads.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h9
    h: 5b2c9ff66213
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:production-mirrors-consumption
  note: 'Happens when PV is connected on the grid side of the meter: the meter only ever sees power drawn,
    so PV output gets counted as load.'
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:inverter-on-off-meter-check
  note: Switch the PV inverter on or off and watch the meter's live readings. If the size or direction
    of the power flow does not change, PV is not on the load side.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  review: drafted
- claim_id: c8
  rel: detected_by
  target: method:phase-current-measurement
  note: Compare the measured phase currents and polarities with the meter's web interface readings. A
    mismatch points to a faulty meter, CT, cable or voltage-tap installation.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  review: drafted
  review_note: 'support check: partial - u2 says mismatches between measured currents and web interface
    readings/polarities indicate incorrect installation (steps 1-4, 8), but ''faulty meter, CT, cable
    or voltage-tap'' omits CT ratio setting (step 8) and is slightly mapped.'
- claim_id: c9
  rel: detected_by
  target: method:visual-inspection
  note: Check the meter orientation (neutral on the grid side), the CT orientation and the CT location.
    Photos of CT placement help with verification.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h9
    h: 5b2c9ff66213
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:meter-wiring-check
  note: Reconnect and recommission the meter.
  cite:
  - src: src:sma-doc-240154
    loc: tbl=88.r1
    h: 23b7c5792a07
  - src: src:sma-doc-243910
    loc: sec=h54
    h: 3b5e487495bd
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:phase-sequence-correction
  note: After you correct the meter phase rotation, also check that the inverter grid-port phases line
    up with the meter phases.
  cite:
  - src: src:kb-solis-44002852865-smart-meter-phase-rotation-and-ct-polarity-verification
    loc: sec=h11
    h: 1eea811f0de1
  review: drafted
- claim_id: c12
  rel: distinguished_from
  target: fm:meter-ct-ratio-misconfiguration
  by: method:phase-current-measurement
  note: Both faults can cause export at night. If primary and secondary CT currents do not agree with
    the ratio, or the ratio set in the meter is wrong, the cause is the CT ratio. If the CTs or meter
    are reversed, the polarity is wrong.
  cite:
  - src: src:sma-kb-sunny-portal-energy-balance-graph-issues
    loc: sec=h1
    h: 671005070a40
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h9
    h: 5b2c9ff66213
  review: drafted
  review_note: 'support check: partial - u2 says current mismatches vs CT ratio indicate wrong CT ratio
    and orientation errors cause night feed-in, but it doesn''t explicitly use polarity to discriminate
    or state both faults cause export at night.'
---
This fault means the energy meter or its current transformers were installed wrong. The meter may be backwards, the CTs or their leads may be reversed, or the PV feeder may be connected on the grid side instead of the load side. The usual sign in monitoring is unrealistic meter values. Grid feed-in at night is another sign. If PV is on the grid side of the meter, the energy balance shows total generation equal to direct consumption, and PV output is counted as extra load. To confirm, check that the meter's neutral is on the grid side and that the CTs face the right way. Then measure each phase current and compare it with the meter's live readings and polarities. Switch the PV inverter on and off while watching the meter. If the power flow does not change, the PV is not on the load side. A power factor well away from unity suggests the voltage references and CTs are not matched phase to phase. To fix it, reconnect the meter correctly and recommission it. On three-phase hybrid systems, also make sure the inverter grid-port phases match the corrected meter phases.

<!-- review notes
- sentence 2: support check: partial - Unrealistic values and night grid feed-in are both given as symptoms, but 'usual sign' ranking is not stated.
- sentence 6: support check: partial - u35 says PF outside ±0.9 to ±1 means check voltage ref and CTs are matched phase-to-phase; 'suggests' is close, but it frames it as a check, not a diagnosis of swapped phases here.
-->
