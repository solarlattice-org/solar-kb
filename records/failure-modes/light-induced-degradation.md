---
id: fm:light-induced-degradation
type: FailureMode
name: Light Induced Degradation (LID)
aliases:
- LID
category: Modules
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:light-exposure
  note: Power drops during the initial stabilization period when the module is first exposed to light.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.2.1
    h: c22ec9adead4
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h4
    h: c8bc75bb2d8d
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c2
  rel: caused_by
  target: stressor:boron-oxygen-defects
  note: Boron-oxygen complexes form in boron-doped cells, mostly Czochralski mono-Si with leftover oxygen.
    They trap charge carriers.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h5
    h: 048d7dac489d
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.2.1
    h: c22ec9adead4
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: affects
  target: comp:solar-cell
  note: Mostly affects p-type boron-doped mono and multi crystalline cells. n-type and Ga-doped cells
    are much less affected.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: presents_as
  target: symptom:stc-power-drop
  note: Seen early in system life. It does not come with any visual defect.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c5
  rel: presents_as
  target: symptom:isc-reduction
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:low-module-voc
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: presents_as
  target: symptom:fill-factor-reduction
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: presents_as
  target: symptom:el-nonuniform-pattern
  note: A patchwork pattern in EL images that grows more uneven can sometimes show that degradation is
    under way.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: Only for serious LID above 10%, seen mainly in early PERC cells made before LID was mitigated
    in manufacturing.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c10
  rel: leads_to
  target: fm:module-hotspot
  note: LID can cause mismatch between cells, which can trigger hot spots and speed up ageing.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:iv-curve-tracing
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=front
    h: ea45629cb646
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:el-imaging
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h6
    h: 0189f40b9ccf
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:flash-test
  note: Compare stabilized flash-test results with nameplate and with the degradation expected for the
    technology.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=front
    h: ea45629cb646
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h2
    h: 0877e796b00f
  review: drafted
- claim_id: c15
  rel: detected_by
  target: method:performance-monitoring
  note: Compare early-life production trends with nameplate and technology-specific expectations.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=front
    h: ea45629cb646
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h2
    h: 0877e796b00f
  review: drafted
- claim_id: c16
  rel: detected_by
  target: method:accredited-lab-test
  note: Use an accredited PV test laboratory to confirm the underperformance.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:low-lid-modules
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=front
    h: ea45629cb646
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h2
    h: 0877e796b00f
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:yield-model-initial-loss
  note: Underestimating initial degradation directly affects energy yield predictions.
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=front
    h: ea45629cb646
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h2
    h: 0877e796b00f
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:gallium-doped-cells
  note: Using Ga instead of B as the dopant removes B-O complex formation. Residual B impurities can still
    cause some LID.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.2.1
    h: c22ec9adead4
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:in-line-cell-stabilization
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passages say manufacturers adapted production to stabilise cells
    in-line, but this is described mainly for LeTID rather than clearly for LID.'
- claim_id: c21
  rel: mitigated_by
  target: mit:bom-verification
  note: Check the cell type.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c22
  rel: mitigated_by
  target: mit:power-warranty-verification
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c23
  rel: mitigated_by
  target: mit:warranty-claim
  note: Claim the missing power once underperformance is confirmed.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c24
  rel: mitigated_by
  target: mit:contractual-loss-limit
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c25
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: Classic LID in crystalline silicon modules, occurring only in the first days of sun exposure
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
  review_note: 'reviewer 2026-10-17: the compiler-flagged conflict is a different technology (amorphous
    vs crystalline silicon), not disagreement'
- claim_id: c26
  attr: typical_power_loss
  value:
    max: 30
    unit: unit:PERCENT
  conditions: Light soaking effect across all module technologies (upper bound)
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h3
    h: 950db263c013
  review: drafted
  review_note: 'support check: partial - The 30% upper bound is stated, but the claim that it applies
    across all module technologies is not.'
- claim_id: c27
  attr: typical_power_loss
  value:
    min: 10
    max: 30
    unit: unit:PERCENT
  conditions: Amorphous silicon modules (Staebler-Wronski effect) within the first months outdoors
  cite:
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h4
    h: c8bc75bb2d8d
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
- claim_id: c28
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID variant at elevated temperature, which can add to the LID loss
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h46
    h: 1ff4ba1a643e
  - src: src:pv-root-cause-light-induced-degradation
    loc: sec=h5
    h: 048d7dac489d
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
---
Light induced degradation is a loss of module power that happens when cells are first exposed to light. In crystalline silicon modules it is mostly caused by boron-oxygen defects. In crystalline modules it usually costs a few percent in the first days of sun, while amorphous silicon modules can lose much more over their first months. You will not see it on the module. It shows as lower output power, short-circuit current, open-circuit voltage and fill factor. Confirm it with IV tracing or flash testing, and compare stabilized results and early production against nameplate. EL and IR imaging can help. Severe cases can cause mismatch and hot spots that show up in an IR camera. If early losses look larger than expected, have an accredited lab confirm them and claim the missing power under the warranty. To prevent it, choose low-LID or gallium-doped cell technology, check the cell type in the bill of materials, and include initial stabilization losses in yield estimates.

<!-- review notes
- sentence 6: support check: partial - Confirming underperformance with an accredited lab and claiming missing power are stated, but the trigger 'larger than expected' and the 'under the warranty' framing are not explicit.
-->
