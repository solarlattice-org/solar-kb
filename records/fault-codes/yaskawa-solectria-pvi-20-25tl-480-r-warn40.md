---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-warn40
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R Warn0040
aliases:
- Warn0040
- warn40
- Yaskawa Solectria Warn0040
- DC SPD fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: Warn0040
code_key: warn40
display_message: DC SPD fault
vendor_severity: Warning
page: 79
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r2
    h: 33a4ad355b14
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r2
    h: 33a4ad355b14
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  note: Alarm is reserved; field occurrences may be ignored
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r2
    h: 33a4ad355b14
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=34.r2
    h: 33a4ad355b14
  review: drafted
---
