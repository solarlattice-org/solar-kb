---
id: fc:chint-sch-125ktl-aio-warn40
type: FaultCode
name: CPS SCH125KTL-AIO Warn0040
aliases:
- Warn0040
- warn40
- CPS Warn0040
- DC SPD fault
category: Inverters
make: chint
make_name: CPS
model_family: sch-125ktl-aio
family_name: CPS SCH125KTL-AIO/US-600
code: Warn0040
code_key: warn40
display_message: DC SPD fault
vendor_severity: Warning
page: 87
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch125ktl-aio-us-600-sep-2020
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r3
    h: 1b4d48802ac2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r3
    h: 1b4d48802ac2
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30
    h: 0677871be906
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r3
    h: 158d81f96f05
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r2
    h: f4aea49215fa
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r3
    h: 1b4d48802ac2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r3
    h: 3f967bac6d1d
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r7
    h: bef2ccc5ad7e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=56.r3
    h: 158d81f96f05
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r2
    h: f4aea49215fa
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r3
    h: 1b4d48802ac2
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=25.r3
    h: 3f967bac6d1d
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r7
    h: bef2ccc5ad7e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Several manuals call the alarm reserved and say it can be ignored in the field.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r2
    h: f4aea49215fa
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=33.r7
    h: bef2ccc5ad7e
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sch-125ktl-aio
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=30.r3
    h: 1b4d48802ac2
  review: drafted
---
