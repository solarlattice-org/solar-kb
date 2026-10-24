---
id: fc:chint-sca-50-100k-t-protect330
type: FaultCode
name: CPS SCA50-100K-T Protect0330
aliases:
- Protect0330
- protect330
- CPS Protect0330
- Internal hardware exception
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0330
code_key: protect330
display_message: Internal hardware exception
vendor_severity: Protection
page: 137
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r1
    h: c046c4bde076
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r1
    h: c046c4bde076
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r1
    h: c046c4bde076
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; then restart; persistent case needs service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r1
    h: c046c4bde076
  review: drafted
  review_note: 'support check: partial - Observe for auto-elimination, then restart, then service; auto-reset
    is suggested but not firmly stated as the clearing mode.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r1
    h: c046c4bde076
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r1
    h: c046c4bde076
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=55.r1
    h: c046c4bde076
  review: drafted
---
