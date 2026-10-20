---
id: fm:leakage-current
type: FailureMode
name: Leakage current
aliases:
- current leakage
- LC
claims:
- claim_id: c1
  rel: leads_to
  target: fm:potential-induced-degradation
  note: Leakage current between cells and grounded frame drives Na+ migration into cell stacking faults,
    shunting the cell (PID-s).
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.4
    h: c8ae742a163e
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h4
    h: 21df64fc133e
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: caused_by
  target: fm:bypass-diode-failure
  note: Heat from a failed diode can burn through the junction box or backsheet, after which leakage current
    may follow as a safety issue.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  - src: src:pv-root-cause-bypass-diode-failure
    loc: sec=h6
    h: bfcbbd1f5824
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: caused_by
  target: stressor:high-system-voltage
  note: Potential difference between cells and frame grows with modules in series; higher voltage gives
    more leakage.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.5
    h: c440122cb9d9
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h4
    h: 21df64fc133e
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=26.r2
    h: 1223ddfd18c3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: caused_by
  target: stressor:humid-climate
  note: High humidity raises conductivity of the leakage path.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.5
    h: c440122cb9d9
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: caused_by
  target: stressor:high-temperature
  note: Elevated module temperature increases leakage current.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.5
    h: c440122cb9d9
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:surface-soiling
  note: Positive charges from soiling can accelerate the process.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  review: drafted
  review_note: 'support check: partial - u9 says positive charges from soiling can accelerate the degradation
    process, not explicitly leakage current itself.'
- claim_id: c7
  rel: caused_by
  target: stressor:sodium-ion-migration
  note: Na+ accumulating in stacking faults creates a self-reinforcing path that further eases leakage
    toward the frame.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.4
    h: c8ae742a163e
  review: drafted
- claim_id: c8
  rel: affects
  target: comp:module-glass
  note: Main leakage path runs through the front glass; soda-lime glass supplies sodium ions.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.5
    h: c440122cb9d9
  review: drafted
  review_note: 'support check: partial - Passages say the main leakage path 1 forms Na+ in the glass and
    soda-lime glass accelerates PID, but not explicitly that the main path runs through the front glass.'
- claim_id: c9
  rel: affects
  target: comp:encapsulant
  note: Low-resistivity EVA facilitates leakage.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.4
    h: c8ae742a163e
  review: drafted
- claim_id: c10
  rel: affects
  target: comp:solar-cell
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h5
    h: 0ba88c724cf4
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.4
    h: c8ae742a163e
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.2.5
    h: c440122cb9d9
  review: drafted
- claim_id: c11
  rel: affects
  target: comp:junction-box
  note: A burnt-through junction box can open a leakage path.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c12
  rel: affects
  target: comp:backsheet
  note: A burnt-through backsheet can open a leakage path.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=38.r6
    h: c1a079fd37d5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=19.r5
    h: 7604ad2cfcc4
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:wet-leakage-test
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: fig=39
    h: 48fafd3c7c1e
  - src: src:iea-pvps-t13-09-2017
    loc: fig=82
    h: e86c421aecf2
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:pid-lab-test
  note: High voltage is applied between shorted leads and frame and the leakage current is metered, e.g.
    via a resistor to ground; leakage has not been clearly linked to power loss in c-Si.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.4
    h: c8ae742a163e
  - src: src:iea-pvps-t13-01-2014
    loc: fig=84
    h: eab40b0b3d44
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:system-grounding
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=front
    h: 4921d46d666f
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=26.r2
    h: 1223ddfd18c3
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:pid-offset-box
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=front
    h: 4921d46d666f
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  review: drafted
  review_note: 'support check: partial - Passages mention offset strategies but not a PV offset box specifically.'
- claim_id: c17
  rel: mitigated_by
  target: mit:pid-resistant-modules
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=front
    h: 4921d46d666f
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  review: drafted
---
Leakage current is unwanted current flowing between the cell circuit and the grounded frame or surroundings, driven by the voltage between cells and ground. It increases with higher system voltage, humidity and module temperature, and soiling or conductive surface layers can speed it up. Its main path runs through the front glass and encapsulant, carrying sodium ions into the cells, where they cause the shunting form of PID. Leakage current can also follow a bypass diode failure that burns through the junction box or backsheet, which makes it a safety issue. In the field the current is usually tiny, in the microamp range, so it is measured in lab or wet leakage tests by applying voltage between the shorted leads and the frame. Leakage current has not been clearly linked to the amount of power lost, so confirm PID damage with IV curves, EL and thermography as well. To reduce it, change the system grounding or use offset strategies, and choose PID-resistant modules.

<!-- review notes
- sentence 2: support check: partial - Voltage, humidity, temperature and soiling are supported, but 'conductive surface layers' speeding it up is not stated (glass conductivity is lowered by rain/pollutants).
- sentence 5: support check: partial - Microamp order of leakage and voltage applied via shorted leads are stated, but 'in the field' usually tiny and wet-leakage-test method details are not explicit.
-->
