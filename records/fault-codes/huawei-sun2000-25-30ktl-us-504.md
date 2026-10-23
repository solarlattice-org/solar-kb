---
id: fc:huawei-sun2000-25-30ktl-us-504
type: FaultCode
name: Huawei SUN2000-25-30KTL-US 504
aliases:
- '504'
- Huawei 504
- Version Mismatch
category: Inverters
make: huawei
make_name: Huawei
model_family: sun2000-25-30ktl-us
family_name: Huawei SUN2000-25KTL-US / SUN2000-30KTL-US
code: '504'
code_key: '504'
display_message: Version Mismatch
vendor_severity: Minor
page: 102
claims:
- claim_id: c1
  rel: defined_in
  target: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r4
    h: 131d1beb27bc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r4
    h: 131d1beb27bc
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:software-version-mismatch
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r4
    h: 131d1beb27bc
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=59.r2
    h: 993b6fc1aaf9
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r4
    h: 131d1beb27bc
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=59.r2
    h: 993b6fc1aaf9
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r4
    h: 131d1beb27bc
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: sec=8.2
    h: db4d98f32335
  review: drafted
---
