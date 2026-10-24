---
id: fc:chint-sca-25ktl-480-protect110
type: FaultCode
name: CPS SCA25KTL-480 Protect0110
aliases:
- Protect0110
- protect110
- CPS Protect0110
- BUS over voltage (firmware)
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-480
family_name: CPS SCA25KTL-DO-R/US-480
code: Protect0110
code_key: protect110
display_message: BUS over voltage (firmware)
vendor_severity: Protection
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-25kw-user-manual-rev-2-1
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r3
    h: b26eea3b7da6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r3
    h: b26eea3b7da6
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r4
    h: 137cab5686ff
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r3
    h: b26eea3b7da6
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r5
    h: 06066af60e87
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r5
    h: 2a8300288ac9
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r4
    h: 137cab5686ff
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r3
    h: b26eea3b7da6
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r5
    h: 06066af60e87
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r5
    h: 2a8300288ac9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r4
    h: 137cab5686ff
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r3
    h: b26eea3b7da6
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r5
    h: 06066af60e87
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r5
    h: 2a8300288ac9
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r5
    h: 2a8300288ac9
  review: drafted
  review_note: 'support check: partial - The passages give no explicit stop or trip behaviour for Protect0110,
    only a protection-type fault with restart steps.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle clears normal case; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=35.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r4
    h: 137cab5686ff
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r3
    h: b26eea3b7da6
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r5
    h: 06066af60e87
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=26.r5
    h: 6c7c616f8b09
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=34.r5
    h: 2a8300288ac9
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-25ktl-480
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r3
    h: b26eea3b7da6
  review: drafted
---
