---
id: fc:sungrow-sg250hx-84
type: FaultCode
name: Sungrow SG250HX 84
aliases:
- '84'
- Sungrow 84
- Reverse Connec-tion Alarm of the Meter/CT
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg250hx
family_name: Sungrow SG250HX
code: '84'
code_key: '84'
display_message: Reverse Connec-tion Alarm of the Meter/CT
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sg250hx-us-uen-ver17-202203
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r4
    h: 6593c7f73af7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:meter-wiring-reversed
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r4
    h: 6593c7f73af7
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r4
    h: 6593c7f73af7
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:meter-wiring-check
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r4
    h: 6593c7f73af7
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Rated power setting of existing inverter, when existing system is enabled.
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r4
    h: 6593c7f73af7
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=42.r4
    h: 6593c7f73af7
  review: drafted
---
