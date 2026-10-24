---
id: concept:ptc-rating
type: Concept
name: PVUSA test conditions rating
aliases:
- PTC
- PTC rating
- PVUSA Test Conditions
- Performance Test Conditions
- PVUSA PTC condition
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:standard-test-conditions
  note: PTC is an alternative rating condition to STC, meant to be closer to actual field operation; field
    I-V measurements may be translated to either.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=2.1.3
    h: 64effa2385fb
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h81
    h: 61249ec11972
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h25
    h: d427e780a501
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:iv-curve
  note: Field I-V measurements can be translated to the PTC condition to rate array or module power; I-V
    curves show the differences between rating conditions.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h81
    h: 61249ec11972
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: fig=87
    h: 9e7f3e21d8cf
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h25
    h: d427e780a501
  review: drafted
---
PTC, short for PVUSA Test Conditions and also called Performance Test Conditions, is a rating condition used to state PV module and array output under conditions closer to real field operation than Standard Test Conditions. STC assumes 1000 W/m2 at AM 1.5 and a 25°C cell temperature, which tends to overestimate field performance because arrays rarely see that irradiance and temperature together. Training guides describe PTC as 1000 W/m2 irradiance, 45°C cell temperature and 1 m/s wind speed. The PTC parameters come from the Nominal Terrestrial Environment that defines NOCT, which uses a lower irradiance of 800 W/m2. To rate array or module power in the field, an I-V measurement taken under whatever conditions apply can be translated to the PTC condition or to the ASTM standard reporting condition. Because PTC accounts for realistic operating temperature, a module's PTC rating is a better guide to expected field output than its STC nameplate.

<!-- review notes
- sentence 4: support check: partial - u5 says PTC parameters were based on NTE conditions that define NOCT and that NTE specifies a lower 800 W/m2, but the statement blurs this: NTE differs from PTC in having the lower irradiance, and PTC itself uses 1000 W/m2.
- sentence 6: support check: partial - The passages say STC overestimates field performance and PTC is closer to field operations, but they do not say PTC accounts for realistic operating temperature as the reason or call the PTC rating a better guide than the STC nameplate.
-->
