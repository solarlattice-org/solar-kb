---
id: stressor:dust-accumulation
type: Stressor
name: Dust accumulation
aliases:
- dust soiling
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 20
    unit: unit:PERCENT
  conditions: Annual energy yield loss from soiling, varying with module location
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.6
    h: a3dffa29110f
  review: disputed
  conflicts_with:
  - stressor:dust-accumulation#c2
  - stressor:dust-accumulation#c4
  - stressor:dust-accumulation#c7
  - stressor:dust-accumulation#c8
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 4.4
    unit: unit:PERCENT
  conditions: Mean daily production loss from dust on modules, Malaga, Spain
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: disputed
  conflicts_with:
  - stressor:dust-accumulation#c1
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c3
  attr: typical_power_loss
  value:
    min: 20
    unit: unit:PERCENT
  conditions: Daily production loss during long dry periods of dust build-up, Malaga, Spain
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions)
- claim_id: c4
  attr: typical_power_loss
  value:
    min: 3
    max: 4
    unit: unit:PERCENT
  conditions: Power loss over a 5-week period, Belgium
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: disputed
  conflicts_with:
  - stressor:dust-accumulation#c1
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c5
  attr: typical_power_loss
  value:
    nominal: 5.86
    unit: unit:PERCENT
  conditions: Estimated annual soiling loss, Crete
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c6
  attr: typical_power_loss
  value:
    nominal: 6.9
    unit: unit:PERCENT
  conditions: Monthly power loss, plant on sandy soil, rural Southern Italy
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: typical_power_loss
  value:
    nominal: 1.1
    unit: unit:PERCENT
  conditions: Monthly power loss, plant on more compact soil, rural Southern Italy
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: disputed
  conflicts_with:
  - stressor:dust-accumulation#c1
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c4 (same source; check the conditions);
    possible conflict with c5 (same source; check the conditions); possible conflict with c6 (same source;
    check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: typical_power_loss
  value:
    nominal: 45.8
    unit: unit:PERCENT
  conditions: Soiling loss over three months with no cleaning, Kuwait
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h18
    h: 33a227523871
  review: disputed
  conflicts_with:
  - stressor:dust-accumulation#c1
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions);
    possible conflict with c6 (same source; check the conditions); possible conflict with c7 (same source;
    check the conditions)
---
Dust accumulation is the build-up of airborne mineral dust on PV equipment. On module glass, it reduces the amount of light reaching the cells, which lowers array current and energy yield. Losses on the modules show up as granular dust soiling losses. These build up during dry spells and mostly recover after rain or cleaning. Dew and humidity can cement dust onto the glass. Sandstorms or frequent cleaning can wear down the glass surface and its anti-reflective coating. Dust that collects on inverter air filters, air inlets and heat sinks blocks cooling. This can cause inverter overheating, temperature derating, shutdown and electronic failures. Exposure is worst in arid, windy and desert areas with little rain, on modules with low tilt, and near agricultural land. Exposure can be reduced by cleaning on a schedule matched to how fast dust builds up, cleaning right after dust storms, using anti-soiling coatings, and tilting modules more steeply. On inverters, clean the enclosure, air inlets and outlets, and filters regularly, and keep monitoring the temperature in inverter areas.

<!-- review notes
- sentence 2: support check: partial - Accumulation between rain or cleaning events and recovery after rain/cleaning are supported, but 'granular' and the notion of 'mostly recover after rain' is only loosely stated (reversible, mostly removed by cleaning).
- sentence 4: support check: partial - Dust blocking heat dissipation, temperature derating, overheating, switch-off and electronics damage are supported, but shutdown/electronic failures are tied to dust in generally and air inlets/heat sinks are not specifically named.
-->
