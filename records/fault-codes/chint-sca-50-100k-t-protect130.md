---
id: fc:chint-sca-50-100k-t-protect130
type: FaultCode
name: CPS SCA50-100K-T Protect0130
aliases:
- Protect0130
- protect130
- CPS Protect0130
- Inv Relay Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0130
code_key: protect130
display_message: Inv Relay Abn
vendor_severity: Protection
page: 132
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r4
    h: 324ac838c52d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r4
    h: 324ac838c52d
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r4
    h: 324ac838c52d
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r3
    h: 047f60916556
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r4
    h: 324ac838c52d
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r3
    h: 047f60916556
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Observe first; then restart via AC and DC switches; persistent case needs service or inverter
    replacement.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r4
    h: 324ac838c52d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r4
    h: 324ac838c52d
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r3
    h: 047f60916556
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a restart does not clear the fault.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r3
    h: 047f60916556
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the alarm persists after restart.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=50.r4
    h: 324ac838c52d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
