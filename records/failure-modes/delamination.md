---
id: fm:delamination
type: FailureMode
name: Delamination
aliases:
- Front delamination
- Backsheet delamination
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:low-quality-material
  note: Raw material quality is named as a main origin; transport and installation are said not to cause
    delamination.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:manufacturing-defect
  note: Includes the manufacturing process, contamination such as poorly cleaned glass, and too-short
    lamination times.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:moisture-exposure
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:high-temperature
  note: Debond growth speeds up sharply with higher temperature and humidity.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:uv-exposure
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:mechanical-stress
  note: Residual thermal stresses at the interface and external mechanical loads on the module.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:module-glass
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c8
  rel: affects
  target: comp:solar-cell
  note: The cell/EVA interface may be more prone to delamination than the EVA/glass interface.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:encapsulant
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c10
  rel: affects
  target: comp:backsheet
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c11
  rel: affects
  target: comp:cell-interconnect-ribbon
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c12
  rel: affects
  target: comp:junction-box
  note: Delamination near the junction box can loosen it.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=17.r3
    h: b816426a98a2
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:visible-delamination
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:backsheet-bubbles
  note: Backsheet delamination may look wavy, with bumps, bubbles, ripples or peeled layers.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c15
  rel: presents_as
  target: symptom:isc-reduction
  note: Extra reflection at the new air interfaces lowers current.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  review: drafted
- claim_id: c16
  rel: presents_as
  target: symptom:stc-power-drop
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c17
  rel: presents_as
  target: symptom:substring-loss
  note: Severe current mismatch can activate bypass diodes.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c18
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=11.r2
    h: 3d6e72f20727
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  review: drafted
- claim_id: c19
  rel: detected_by
  target: method:insulation-resistance-test
  note: Hints at severe delamination only; not suitable for early detection.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=11.r2
    h: 3d6e72f20727
  review: drafted
- claim_id: c20
  rel: detected_by
  target: method:ir-thermography
  note: Pulse and lock-in thermography can find delamination that is not visible.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c21
  rel: detected_by
  target: method:scanning-acoustic-microscopy
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c22
  rel: detected_by
  target: method:ultrasonic-scanning
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  review: drafted
- claim_id: c23
  rel: detected_by
  target: method:x-ray-tomography
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  review: drafted
- claim_id: c24
  rel: leads_to
  target: fm:severe-metallization-corrosion
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:pv-root-cause-severe-metallization-corrosion
    loc: sec=h6
    h: ab4b4f0e5fd4
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
  review_note: 'support check: partial - Delamination leads to corrosion of metallic components, but ''severe''
    metallization corrosion is not specifically stated.'
- claim_id: c25
  rel: leads_to
  target: fm:insulation-loss
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.1.1
    h: bc3b4163c337
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c26
  rel: leads_to
  target: fm:leakage-current
  note: Most likely when delamination forms a continuous path from the circuit to the module edge.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  review: drafted
- claim_id: c27
  rel: leads_to
  target: fm:junction-box-failure
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=17.r3
    h: b816426a98a2
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=36.r3
    h: b816426a98a2
  review: drafted
- claim_id: c28
  rel: leads_to
  target: fm:arc-fault
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h60
    h: 6cc7189f11a4
  review: drafted
- claim_id: c29
  rel: mitigated_by
  target: mit:module-replacement
  note: Replace modules that lose electrical safety or insulation resistance, or that have an active bypass
    diode.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  review: drafted
- claim_id: c30
  rel: mitigated_by
  target: mit:close-monitoring
  note: Watch modules with minor delamination using regular visual inspections and ground fault detection.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  review: drafted
- claim_id: c31
  rel: mitigated_by
  target: mit:certified-products
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=1.2
    h: 00007ee51ba7
  review: drafted
- claim_id: c32
  attr: typical_power_loss
  value:
    nominal: 20
    unit: unit:PERCENT
  conditions: Field-deployed EFG-Si module, first 3 years of deployment, with delamination, moisture ingress
    and contact corrosion (reported as nearly 20%)
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
  review_note: 'support check: partial - Nearly 20% Pmax drop in first 3 years of an EFG-Si module is
    stated, but it''s a single case and ''typical'' is not stated.; possible conflict with c34 (same source;
    check the conditions)'
- claim_id: c33
  attr: current_drop
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Isc drop of the same EFG-Si module over its first 3 years of deployment (reported as about
    5%)
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
- claim_id: c34
  attr: typical_power_loss
  value:
    nominal: 11.5
    unit: unit:PERCENT
  conditions: PV system after 12 years of exposure, with loss attributed mainly to cell/encapsulant delamination
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.2
    h: 5147bca98d09
  review: drafted
  review_note: possible conflict with c32 (same source; check the conditions)
---
Delamination is a loss of adhesion between the layers of a module, such as glass, encapsulant, cells and backsheet. Its main causes are poor raw materials, manufacturing problems and exposure to heat, UV and moisture in service. Transport and installation do not cause it. The air gaps reflect more light, which lowers module current and power. A large mismatch can switch on bypass diodes. Delamination also lets moisture in more quickly, which can lead to corrosion of metal contacts. Delamination near the edge or the junction box is a safety risk, because it can cause insulation faults, leakage currents or a loose junction box. It is usually easy to see during a visual inspection from the front. Thermography can find delamination that is not visible, and insulation testing only flags severe cases. Replace modules that have lost insulation resistance or electrical safety, or that have an active bypass diode. Monitor the rest with regular visual inspections and ground fault detection.
