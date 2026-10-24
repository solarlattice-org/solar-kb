---
id: concept:standard-test-conditions
type: Concept
name: Standard test conditions
aliases:
- STC
- standard testing conditions
- conditions de test standard
- Condizioni di test standard
- Condiciones de prueba estándar
- Standardtestbedingungen
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:air-mass
  note: STC specifies an AM 1.5 (Air Mass 1.5 G) spectral distribution.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1.3
    h: 64effa2385fb
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.6
    h: 22ab721b2405
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: tbl=8.r3
    h: 59aca9e89766
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:ptc-rating
  note: PTC is an alternative rating condition closer to field operation (higher cell temperature, wind
    speed specified).
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1.3
    h: 64effa2385fb
  - src: src:se-academy-home-hub-technical-essentials-na-technical-16-home-hub-oversizing
    loc: sec=h16
    h: 94ccca027dd5
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:nominal-operating-cell-temperature
  note: Listed alongside STC as another module rating condition.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-16-home-hub-oversizing
    loc: sec=h16
    h: 94ccca027dd5
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:iec-61215
  note: Crystalline silicon module qualification standard that includes performance testing at STC.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.6
    h: 22ab721b2405
  review: drafted
- claim_id: c5
  rel: related_to
  target: std:iec-61646
  note: Thin-film module qualification standard that includes performance testing at STC.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.6
    h: 22ab721b2405
  review: drafted
- claim_id: c6
  rel: related_to
  target: method:iv-curve-tracing
  note: Field I-V measurements are normalized to STC per ASTM E1036 translation methods.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=h52
    h: a35633edf001
  review: drafted
---
Standard test conditions (STC) are the universal reference rating condition used to state the electrical output of PV modules and arrays. STC means an irradiance of 1000 W/m2 with an AM 1.5 spectral distribution and a cell temperature of 25°C. Module qualification standards such as IEC 61215 for crystalline silicon and IEC 61646 for thin film include performance tests at STC. STC ratings say little about how a module performs in the field, where irradiance and temperature vary from site to site. Ratings closer to real operation also exist, such as PVUSA test conditions (PTC), which use a 45°C cell temperature and a 1 m/s wind speed, and nominal operating cell temperature (NOCT). In the field, I-V curve measurements are translated back to STC so they can be compared with the datasheet, following methods such as ASTM E1036. For best results, take those measurements under steady clear skies near solar noon, with irradiance above 800 W/m2 and little wind.

<!-- review notes
- sentence 6: support check: partial - ASTM E1036 normalizing field IV results to STC is stated, but comparison with the datasheet is not mentioned.
-->
