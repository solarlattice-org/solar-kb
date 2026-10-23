---
id: fc:solis-s5-gc-us-arcfault
type: FaultCode
name: Solis S5-GC ARC-FAULT
aliases:
- ARC-FAULT
- arcfault
- Solis ARC-FAULT
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: ARC-FAULT
code_key: arcfault
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:arc-fault-detected
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r5
    h: 7fd24b969497
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=29.r4
    h: ce5381fca1c5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r19
    h: ce5381fca1c5
  review: drafted
  review_note: 'support check: partial - PV connection arcing and tight connections are mentioned, but
    DC connector is not named specifically.'
- claim_id: c5
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r5
    h: 7fd24b969497
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=29.r4
    h: ce5381fca1c5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r19
    h: ce5381fca1c5
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after the PV connection has been checked for arcing.
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r1
    h: fe536f2756ed
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: affects
  target: comp:junction-box
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  rel: detected_by
  target: method:junction-box-inspection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c11
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r4
    h: b4f347f61cee
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15
    h: cb7b6f9ed265
  review: verified
  review_note: 'support check: partial - Listed in the ''Fault messages'' table, but the row doesn''t
    state device behavior; classification only implied by table title.'
  verified_by: review-workflow
  verified_at: *id001
---
