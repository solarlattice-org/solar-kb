---
id: fm:string-fuse-failure
type: FailureMode
name: String fuse failure
aliases:
- String Err.
- Damaged fuse
claims:
- claim_id: c1
  rel: affects
  target: comp:string-fuse
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h269
    h: 2f21dd0defb6
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: caused_by
  target: stressor:undersized-component
  note: Fuses sized incorrectly for the single-string current can be damaged; fuses protect against return
    currents from a faulty string.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h111
    h: ea078ce30773
  review: drafted
  review_note: 'support check: partial - The passages say incorrectly sized fuses can damage the fuse
    and that fuses protect against return currents. They don''t say a string fuse failure is caused by
    an undersized component. They also don''t say the sizing is for single-string current in a way that
    links to this cause.; review: partial - The passage says fuses sized wrongly for single-string currents
    can damage the fuse, and that fuses guard against return currents, but it never says the fuse is too
    small, so the ''undersized'' cause goes beyond the text.'
- claim_id: c3
  rel: caused_by
  target: stressor:installation-error
  note: Strings paralleled outside the inverter can push input current above the fuse rating.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  review: drafted
  review_note: 'support check: partial - The passages say to check whether input current exceeds the fuse
    rating if parallel strings were made outside the inverter. They don''t call this an installation error
    or state outright that it causes fuse failure.; review: partial - The W017 rows tell you to check
    that string current does not exceed the fuse rating when strings were paralleled outside the inverter,
    which implies the cause, but they never state it as a cause or call it an installation…'
- claim_id: c4
  rel: presents_as
  target: symptom:string-current-error
  note: Reported as warning W017 String Err. on models with monitored string fuses.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: presents_as
  target: symptom:abrupt-production-drop
  note: Output falls suddenly by roughly the power of one string.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.5
    h: e99cf005beed
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: presents_as
  target: symptom:hotspot-ir-image
  note: Heated or overheated string fuses in combiner boxes show as thermal abnormalities.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=5
    h: fc0f2dc6c73f
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=29
    h: 39c8e0698b73
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: detected_by
  target: method:fuse-check
  note: Check fuse state on the fuse boards with a multimeter.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=5
    h: fc0f2dc6c73f
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=29
    h: 39c8e0698b73
  review: drafted
  review_note: 'support check: partial - IR imaging detects heated string fuses in combiner boxes, but
    the passages do not say it detects a fuse failure (open or blown fuse).; review: partial - The IEA
    passages say IR imaging detects heated or overheated string fuses in combiner boxes, but they never
    say it detects a failed (open or blown) fuse.'
- claim_id: c9
  rel: detected_by
  target: method:performance-monitoring
  note: A sudden power drop about equal to one string's output points to a string fault such as a blown
    fuse.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.5
    h: e99cf005beed
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  rel: mitigated_by
  target: mit:fuse-replacement
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h269
    h: 2f21dd0defb6
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.8.5.2
    h: 6a584bf20b9a
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c11
  rel: mitigated_by
  target: mit:safety-isolation
  note: Open AC and DC disconnects, disconnect strings, wait for stored energy to discharge and confirm
    zero current with a clamp meter before changing fuses.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h269
    h: 2f21dd0defb6
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=4.8.5.2
    h: 6a584bf20b9a
  review: drafted
  review_note: 'review: partial - Every step in the note (open the AC/DC disconnects, disconnect the strings,
    wait for stored energy to discharge, confirm zero current with a clamp meter) is in the passages,
    but only as safety prerequisites for replacing a fuse, not as…'
- claim_id: c12
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: If no fuse is open but the alarm persists, check the configured presence or absence of input strings.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=44.r4
    h: 84bd9c214225
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  review: drafted
  review_note: 'review: partial - The rows do say to check the configured presence or absence of input
    strings if no fuse is damaged and the alarm persists, but that step deals with a false alarm when
    no fuse has failed, not with string fuse…'
---
A string fuse failure is an open or damaged fuse that protects a single PV string. The string then stops contributing power. Fuses that are wrongly sized for the string current can be damaged. So can fuses that carry more current than their rating, for example when strings are paralleled outside the inverter. In monitoring data it can appear as a sudden output drop roughly equal to one string's power. On inverters with monitored fuses it raises a string current error warning. Thermal imaging can also find heated or overheated string fuses in combiner boxes. To confirm, check each fuse on the fuse boards with a multimeter. If no fuse is open but the alarm stays on, review the inverter's string configuration settings. Before replacing a fuse, open the AC and DC disconnects and disconnect the strings. Wait for stored energy to discharge, and check with a clamp meter that no current is flowing. Replace the open fuse, then check that the string input current does not exceed the fuse rating.

<!-- review notes
- sentence 1: support check: partial - The passages say a string stops producing when its DC fuse is blown, and that W017 covers damaged string fuses. They do not define the failure as an open or damaged fuse protecting a single string.
-->
