---
id: fm:potential-induced-degradation
type: FailureMode
name: Potential Induced Degradation (PID)
aliases:
- PID
category: Modules
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:high-system-voltage
  note: Stress grows with the number of modules in series; p-type cells degrade in negative-polarity strings,
    n-type in positive-polarity strings.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h4
    h: 21df64fc133e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=front
    h: 4921d46d666f
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c2
  rel: caused_by
  target: fm:leakage-current
  note: PID-s is driven by leakage current through the front glass and encapsulant.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=front
    h: 4921d46d666f
  - src: src:pv-root-cause-potential-induced-degradation
    loc: tbl=1.r2
    h: 9a1182df900c
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:sodium-ion-migration
  note: Na+ ions moving mainly from the glass into the cell create shunts.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:moisture-exposure
  note: Humidity, rain wetting and condensation speed up degradation; the electrochemical form is corrosion
    from moisture ingress.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: tbl=1.r3
    h: 777f6ba7af3e
  review: drafted
  review_note: 'support check: partial - Humidity, rain wetting and condensation accelerate PID and electrochemical
    corrosion from moisture infiltration is listed, but moisture as a cause of PID itself is only acceleration.'
- claim_id: c5
  rel: caused_by
  target: stressor:high-temperature
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
  review_note: 'support check: partial - Temperature is said to accelerate PID, but not that high operating
    temperature is a cause.'
- claim_id: c6
  rel: caused_by
  target: stressor:surface-soiling
  note: Dust carrying positive charges increases PID risk.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h9
    h: 1a8ef7f958ed
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:solar-cell
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: tbl=1.r1
    h: f5b8d9f781ff
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c8
  rel: affects
  target: comp:module-glass
  note: Leakage path and sodium source.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:gradual-performance-decline
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:warm-cells-near-frame
  note: IR pattern of warmer cells near the bottom frame or a patchwork pattern, strongest in modules
    near one string pole.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c11
  rel: presents_as
  target: symptom:hotspot-ir-image
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h7
    h: 4ba0228f747c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
  review_note: 'support check: partial - Hot spots are mentioned and IR thermography reveals hotspots,
    but the primary IR pattern is warmer cells; hotspots are secondary/late.'
- claim_id: c12
  rel: presents_as
  target: symptom:fill-factor-reduction
  note: Typical of PID-s, along with lower shunt resistance; more visible under low light.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c13
  rel: presents_as
  target: symptom:low-module-voc
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c14
  rel: presents_as
  target: symptom:isc-reduction
  note: Mainly PID-p; for PID-s Isc only drops in a very advanced stage.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c15
  rel: presents_as
  target: symptom:dark-cells-el
  note: PID-s cells near the frame show reduced luminescence, especially at low current bias.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c16
  rel: detected_by
  target: method:el-imaging
  note: EL at about one tenth of rated current can find PID early, before power loss is noticed.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h7
    h: 4ba0228f747c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c17
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h7
    h: 4ba0228f747c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c18
  rel: detected_by
  target: method:iv-curve-tracing
  note: Used to confirm and quantify loss together with IR or EL.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h7
    h: 4ba0228f747c
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c19
  rel: detected_by
  target: method:voc-measurement
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h7
    h: 4ba0228f747c
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  review: drafted
- claim_id: c20
  rel: detected_by
  target: method:pid-lab-test
  note: IEC 62804 chamber test; a module fails above 5% power degradation.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h7
    h: 4ba0228f747c
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c21
  rel: leads_to
  target: fm:encapsulant-discoloration
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: drafted
- claim_id: c22
  rel: leads_to
  target: fm:delamination
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: tbl=3.r17
    h: 75fbc77dd47e
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
- claim_id: c23
  rel: leads_to
  target: fm:severe-metallization-corrosion
  note: Corrosion appears as a secondary failure in advanced stages; not reversible.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: tbl=1.r3
    h: 777f6ba7af3e
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:regular-cleaning
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h9
    h: 1a8ef7f958ed
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c25
  rel: mitigated_by
  target: mit:system-grounding
  note: For example setting the frame to a negative potential.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h9
    h: 1a8ef7f958ed
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  review: drafted
- claim_id: c26
  rel: mitigated_by
  target: mit:pid-offset-box
  note: Applies reverse voltage overnight.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h9
    h: 1a8ef7f958ed
  review: drafted
- claim_id: c27
  rel: mitigated_by
  target: mit:pid-resistant-modules
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  review: drafted
- claim_id: c28
  rel: mitigated_by
  target: mit:alternative-encapsulant
  note: Such as TPO.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h9
    h: 1a8ef7f958ed
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c29
  rel: mitigated_by
  target: mit:low-sodium-glass
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h9
    h: 1a8ef7f958ed
  review: drafted
- claim_id: c30
  rel: mitigated_by
  target: mit:arc-layer-optimization
  note: Higher Si/N ratio or an added SiO2 layer under the ARC.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h9
    h: 1a8ef7f958ed
  review: drafted
- claim_id: c31
  rel: mitigated_by
  target: mit:polarity-reversal-regeneration
  note: PID-p can be fully regenerated; PID-s only if caught in time.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h2
    h: ff7ac62c1dc0
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c32
  attr: typical_power_loss
  value:
    nominal: 41
    unit: unit:PERCENT
  conditions: Average performance loss reported for a 10.7 MW plant in Spain (Libby et al.)
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h4
    h: 21df64fc133e
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
- claim_id: c33
  attr: typical_power_loss
  value:
    min: 20
    max: 80
    unit: unit:PERCENT
  conditions: Reduction of PV string performance after commissioning, per Libby et al.
  cite:
  - src: src:pv-root-cause-potential-induced-degradation
    loc: sec=h3
    h: 0587f1d564ae
  review: drafted
  review_note: 'support check: partial - Source says ''up to 20-80%'', an upper bound range, not a typical
    value.'
- claim_id: c34
  attr: typical_power_loss
  value:
    min: 20
    unit: unit:PERCENT
  conditions: Yield losses observed within 1 year in past field cases
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h63
    h: 8878a24975cb
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-16
  review_note: 'support check: partial - Source says losses of 20 percent and more within 1 year; 20%
    is a lower bound, not typical.'
---
PID is module degradation driven by high voltage between the cells and the grounded frame. The voltage grows with the number of modules in a string and drives leakage currents. Heat, humidity, wet surfaces and soiling speed it up. Cells near the frame and modules at one end of the string are hit hardest. You usually cannot see it by eye. What you see is a power loss that keeps growing, and string losses can reach 20 to 80 percent. Infrared imaging in sunlight often shows warmer cells along the bottom frame or a patchwork pattern. EL imaging at low current shows dark cells near the frame and catches PID early. Confirm it and measure the loss with IV curve tracing or Voc checks. Look for a lower fill factor and lower Voc, and for lower Isc in the polarization type. To prevent it, keep modules clean, use grounding or offset boxes that apply reverse voltage at night, and choose PID-resistant modules. If you catch it early, reversing the bias polarity can regenerate affected modules. Corrosion damage at later stages cannot be reversed.

<!-- review notes
- sentence 1: support check: partial - Voltage between cells and frame growing with series modules and leakage currents is stated, but 'grounded frame' is not explicit.
- sentence 3: support check: partial - Not visible by eye and growing power loss stated, and up to 20-80% string loss, but 'can reach' matches only as an upper bound.
-->
