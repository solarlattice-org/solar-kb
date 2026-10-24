---
id: fc:chint-sca-50-100k-t-warn40
type: FaultCode
name: CPS SCA50-100K-T Warn0040
aliases:
- Warn0040
- warn40
- CPS Warn0040
- DC lightning protector Abn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Warn0040
code_key: warn40
display_message: DC lightning protector Abn
vendor_severity: Warning
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r2
    h: f4aea49215fa
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r2
    h: f4aea49215fa
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
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=47.r2
    h: f4aea49215fa
  review: drafted
---
