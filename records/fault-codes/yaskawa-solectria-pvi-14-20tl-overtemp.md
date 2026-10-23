---
id: fc:yaskawa-solectria-pvi-14-20tl-overtemp
type: FaultCode
name: Yaskawa Solectria PVI-14-20TL OverTemp
aliases:
- OverTemp
- overtemp
- Yaskawa Solectria OverTemp
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-14-20tl
family_name: Solectria PVI 14/20TL
code: OverTemp
code_key: overtemp
vendor_severity: Protection
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r1
    h: 02d4e0a04ae0
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r2
    h: c07b46116b41
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r3
    h: d056ffd39cfd
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r4
    h: c35000bf2bff
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r5
    h: c277db7a04f4
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r6
    h: 784c246d4cd5
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r1
    h: 02d4e0a04ae0
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r2
    h: c07b46116b41
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r3
    h: d056ffd39cfd
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r4
    h: c35000bf2bff
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r5
    h: c277db7a04f4
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r6
    h: 784c246d4cd5
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r1
    h: 02d4e0a04ae0
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r5
    h: aabec9e33b25
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r3
    h: d056ffd39cfd
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r2
    h: c07b46116b41
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r3
    h: d056ffd39cfd
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:installation-clearance
  note: Applies when poor cooling stems from improper installation.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r6
    h: aa0995381f56
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r4
    h: c35000bf2bff
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation if the alarm persists.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r6
    h: 784c246d4cd5
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Clears on its own once cooled after checks; service if it persists.
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=18.r4
    h: 0272c94b2138
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=12.r5
    h: c277db7a04f4
  review: drafted
---
