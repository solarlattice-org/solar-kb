---
id: fc:chint-sca-50-100k-t-protect650
type: FaultCode
name: CPS SCA50-100K-T Protect0650
aliases:
- Protect0650
- protect650
- CPS Protect0650
- Steady State GFCI Prot
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0650
code_key: protect650
display_message: Steady State GFCI Prot
vendor_severity: Protection
page: 139
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r4
    h: 5705cb246e01
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r4
    h: 5705cb246e01
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r4
    h: 5705cb246e01
  review: drafted
  review_note: 'support check: partial - The row is about GFCI protection and leakage to earth ground,
    implying leakage current, though ''high leakage current'' is not…'
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r4
    h: 5705cb246e01
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r4
    h: 5705cb246e01
  review: drafted
  review_note: 'support check: partial - Passage says to trace wiring of the faulted string, which implies
    cables, but DC cables aren''t named explicitly.'
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  note: Add strings back one at a time to find the faulted string.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r4
    h: 5705cb246e01
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=57.r4
    h: 5705cb246e01
  review: drafted
---
