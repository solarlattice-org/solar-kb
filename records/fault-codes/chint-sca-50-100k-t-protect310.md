---
id: fc:chint-sca-50-100k-t-protect310
type: FaultCode
name: CPS SCA50-100K-T Protect0310
aliases:
- Protect0310
- protect310
- CPS Protect0310
- GFCI SENSOR Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0310
code_key: protect310
display_message: GFCI SENSOR Abn
vendor_severity: Protection
page: 136
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:ground-fault-detector-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: drafted
  review_note: 'support check: partial - Passage names a ground fault current sensor abnormal, which roughly
    implies detector failure, but not stated as failure mode explicitly.'
- claim_id: c4
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; contact service if the fault does not clear.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=54.r5
    h: 3a24d42b49b5
  review: drafted
---
