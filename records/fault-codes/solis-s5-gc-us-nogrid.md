---
id: fc:solis-s5-gc-us-nogrid
type: FaultCode
name: Solis S5-GC NO-GRID
aliases:
- NO-GRID
- nogrid
- Solis NO-GRID
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: NO-GRID
code_key: nogrid
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r2
    h: 3fc18463c15a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r2
    h: 3fc18463c15a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r2
    h: 3fc18463c15a
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r2
    h: 3fc18463c15a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Last step if the measurement circuit is suspected faulty.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r2
    h: 3fc18463c15a
  review: drafted
---
