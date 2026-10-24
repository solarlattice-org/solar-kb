---
id: fm:ac-breaker-thermal-nuisance-trip
type: FailureMode
name: AC breaker thermal nuisance tripping
aliases:
- nuisance tripping
- circuit breaker overheating
- enclosure temperature rise
- premature tripping
claims:
- claim_id: c1
  rel: affects
  target: comp:ac-circuit-breaker
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  - src: src:sma-doc-275587
    loc: sec=h20
    h: 97055eeee3ca
  - src: src:sma-doc-275587
    loc: sec=h13
    h: 58448203629c
  - src: src:sma-doc-275587
    loc: sec=h14
    h: bab16ebc7a2a
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:ac-breaker-trip
  note: Breaker trips below its nominal current when it cannot shed heat.
  cite:
  - src: src:sma-doc-275587
    loc: sec=h20
    h: 97055eeee3ca
  - src: src:sma-doc-275587
    loc: sec=h13
    h: 58448203629c
  - src: src:sma-doc-275587
    loc: sec=h14
    h: bab16ebc7a2a
  - src: src:kb-solis-44002485766-1015-no-grid-ac-mcb-tripping
    loc: sec=h1
    h: 33303fa86332
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:high-temperature
  note: High temperature inside the breaker enclosure means less heat can leave the breaker. The enclosure
    temperature is not the same as the outside air temperature.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  - src: src:sma-doc-275587
    loc: sec=h14
    h: bab16ebc7a2a
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:solar-heat-gain
  note: How much the enclosure heats up depends on its color and which way it faces. Large east- and west-facing
    surfaces pick up the most heat in the evening.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:mutual-breaker-heating
  note: Breakers mounted close together, with inverters all feeding at full current, heat each other and
    trip early.
  cite:
  - src: src:sma-doc-275587
    loc: sec=h20
    h: 97055eeee3ca
  - src: src:sma-doc-275587
    loc: sec=h13
    h: 58448203629c
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:undersized-component
  note: A breaker that is rated too low or was not derated for temperature.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  - src: src:kb-solis-44002485766-1015-no-grid-ac-mcb-tripping
    loc: sec=h1
    h: 33303fa86332
  review: drafted
  review_note: 'support check: partial - Derating for temperature and MCB rating below recommended are
    mentioned, but the passages don''t directly say an undersized or non-derated breaker causes thermal
    nuisance tripping (u15 is a general MCB tripping checklist).'
- claim_id: c7
  rel: detected_by
  target: method:phase-current-measurement
  note: Check that the total current through the breaker stays within its rating.
  cite:
  - src: src:kb-solis-44001815757-ac-breaker-trips-steps-to-diagnose-and-resolve-issues
    loc: sec=2.2
    h: 8bfccd665513
  review: drafted
  review_note: 'support check: partial - Passage says to confirm total current doesn''t exceed rating,
    but doesn''t tie it to detecting thermal nuisance tripping or call it phase current measurement.'
- claim_id: c8
  rel: detected_by
  target: method:ambient-temperature-check
  note: Measure the temperature inside the AC enclosure, not the outside air temperature.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  review: drafted
  review_note: 'support check: partial - Passage distinguishes enclosure temperature from OSAT, but doesn''t
    explicitly say to measure it as a detection method.'
- claim_id: c9
  rel: mitigated_by
  target: mit:ac-protective-device-sizing
  note: Derate the breaker for enclosure temperature and use the breaker size the manufacturer specifies.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h3
    h: ed1216ee4475
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h120
    h: c0cdd47c085a
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: sec=h72
    h: d4a2962c0744
  - src: src:kb-solis-44002485766-1015-no-grid-ac-mcb-tripping
    loc: sec=h1
    h: 33303fa86332
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:breaker-spacing
  note: Leave more space between breakers so heat can dissipate, or apply the grouping correction factor
    when sizing.
  cite:
  - src: src:sma-doc-275587
    loc: sec=h20
    h: 97055eeee3ca
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:enclosure-cooling
  note: Use active or passive cooling and choose the enclosure's orientation to keep its temperature down.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h3
    h: ed1216ee4475
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:electronic-trip-breaker
  note: Electronic trip breakers often tolerate higher temperatures.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h3
    h: ed1216ee4475
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:full-rated-breaker
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h3
    h: ed1216ee4475
  review: drafted
- claim_id: c14
  attr: temperature_rise
  value:
    nominal: 28
    unit: unit:K
  conditions: Temperature inside the AC breaker enclosure above outside air temperature, recorded at one
    typical site in Florida in July
  note: At that site the inside of the enclosure reached 60 °C, which gave a worst-case breaker derate
    of 81%.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  review: drafted
---
The AC breaker trips below its nominal current because it is too hot to shed heat, even though there is no real overcurrent. Common causes are a hot enclosure from sun and conductor heat, and breakers mounted close together while several inverters feed at full current. The temperature inside the enclosure can be well above the outside air temperature, especially in enclosures with large east- or west-facing surfaces. To confirm, measure the load current through the breaker against its rating and check the temperature inside the enclosure. Also check that the breaker rating is not below what the inverter manufacturer recommends. To fix it, size the breaker with the temperature derate applied, or space the breakers further apart. Other options are cooling or reorienting the enclosure, or using electronic trip or 100% rated breakers.

<!-- review notes
- sentence 1: support check: partial - Tripping below nominal current from heat is stated, but 'even though there is no real overcurrent' is not explicit.
- sentence 4: support check: partial - Passages mention verifying current against rating and enclosure temperature vs OSAT, but don't explicitly prescribe checking enclosure temperature as a confirmation step.
-->
