---
id: fc:chint-sca-50-100k-t-protect1060
type: FaultCode
name: CPS SCA50-100K-T Protect1060
aliases:
- Protect1060
- protect1060
- CPS Protect1060
- BUS Current High
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect1060
code_key: protect1060
display_message: BUS Current High
vendor_severity: Protection
page: 143
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r5
    h: e4279da7e290
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r5
    h: e4279da7e290
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r5
    h: e4279da7e290
  review: drafted
  review_note: 'support check: partial - Bus Current High is not exactly inverter overcurrent; the mapping
    is loose though plausible.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear on its own within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r5
    h: e4279da7e290
  review: drafted
  review_note: 'support check: partial - Observing 5 minutes for auto-elimination implies auto-reset,
    with service if persisting.'
- claim_id: c5
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=61.r5
    h: e4279da7e290
  review: drafted
---
