---
id: symptom:stc-power-drop
type: Symptom
name: Reduced STC output power
aliases:
- peak power loss
claims:
- claim_id: c1
  rel: observed_as
  target: meas:pmax-below-rated
  note: Flash or IV test of a stabilised module gives STC power below the nameplate minimum after allowing
    for tolerance and lab uncertainty.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h45
    h: 2e9980a0b004
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h67
    h: 91bca7f04152
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:iv-low-isc
  note: With delamination the Pmax loss comes mostly from lower Isc caused by extra reflection; LID also
    lowers Isc.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:low-voc
  note: LID/LeTID lowers Voc together with STC power.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:el-patchwork-pattern
  note: EL images becoming less uniform can sometimes point to ongoing light-induced degradation.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: drafted
- claim_id: c5
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Light induced degradation (light soaking), upper bound reported in one source
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: drafted
- claim_id: c6
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: Boron-oxygen LID in c-Si modules, occurring within the first days of sun exposure
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: disputed
  conflicts_with:
  - symptom:stc-power-drop#c9
  - symptom:stc-power-drop#c11
- claim_id: c7
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in PERC-type modules at temperatures above 50 °C, developing over years and adding
    to LID loss
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: disputed
  conflicts_with:
  - symptom:stc-power-drop#c9
  - symptom:stc-power-drop#c11
- claim_id: c8
  attr: typical_power_loss
  value:
    min: 1
    max: 4
    unit: unit:PERCENT
  conditions: LeTID in modules from manufacturers using in-line mitigation; varies by manufacturer
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: disputed
  conflicts_with:
  - symptom:stc-power-drop#c9
  - symptom:stc-power-drop#c11
- claim_id: c9
  attr: typical_power_loss
  value:
    nominal: 20
    unit: unit:PERCENT
  conditions: Field EFG-Si module with edge delamination and discoloration, first 3 years of deployment
    (reported as nearly 20% Pmax drop)
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: disputed
  conflicts_with:
  - symptom:stc-power-drop#c6
  - symptom:stc-power-drop#c7
  - symptom:stc-power-drop#c8
  review_note: possible conflict with c11 (same source; check the conditions)
- claim_id: c10
  attr: current_drop
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Same field EFG-Si module with delamination, Isc drop over the first 3 years (reported as
    about 5%)
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c11
  attr: typical_power_loss
  value:
    nominal: 11.5
    unit: unit:PERCENT
  conditions: PV system after 12 years of exposure, loss attributed mostly to delamination at the cell/encapsulant
    interface
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: disputed
  conflicts_with:
  - symptom:stc-power-drop#c6
  - symptom:stc-power-drop#c7
  - symptom:stc-power-drop#c8
  review_note: possible conflict with c9 (same source; check the conditions)
---
The module puts out less power at standard test conditions than its nameplate says. This is found by flash testing or IV tracing a stabilised module, and it may also show up in monitoring data. If the module was below tolerance when new, the cause is a non-conforming power rating rather than degradation. Lab measurement uncertainty and the manufacturer's tolerance must be taken into account before calling it non-conforming. Light induced degradation lowers STC power along with Isc and Voc early in the system's life, with no visible defect. In some cases a patchwork pattern in EL images points to it. Delamination lowers Pmax mainly by cutting short-circuit current, because the air gaps reflect more light. It can be seen visually, and pulse thermography or scanning acoustic microscopy can detect it. Corrosion or abrasion of the glass or its anti-reflective coating cuts light transmission. The loss is usually a few percent and levels off over time. Look for it visually, and check reflectance after cleaning. First, compare stabilised flash-test or IV results and early production trends against the nameplate and the losses expected for that module technology. Then have an accredited lab confirm the underperformance before filing a warranty claim.

<!-- review notes
- sentence 1: support check: partial - The passages give STC power below nameplate with detection by IV and MON, but flash testing is not stated for this defect (only stabilisation and IV) and the statement's nameplate comparison is slightly looser.
- sentence 2: support check: partial - Lab uncertainty and manufacturer tolerance are required, but the passages don't state that a new module below tolerance is a non-conforming rating rather than degradation, beyond calling it not a real failure causing no degradation.
- sentence 4: support check: partial - Reflection-driven Isc loss and detection by pulse thermography and SAM are stated, but visual detection of delamination is not stated in the passages.
-->
