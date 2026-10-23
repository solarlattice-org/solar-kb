---
id: fc:solis-s6-eh1p-h-us-unbus0102
type: FaultCode
name: Solis S6-EH1P UN-BUS01/02
aliases:
- UN-BUS01/02
- unbus0102
- Solis UN-BUS01/02
- Under DC bus voltage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: UN-BUS01/02
code_key: unbus0102
display_message: Under DC bus voltage
page: 74
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=15.r1
    h: 90d9922920d3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-undervoltage
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r11
    h: f45a9c4d23db
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r1
    h: 90d9922920d3
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:choke
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r11
    h: f45a9c4d23db
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r1
    h: 90d9922920d3
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Inductor and driver connections inside the inverter.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r11
    h: f45a9c4d23db
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r1
    h: 90d9922920d3
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11.r1
    h: 90d9922920d3
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=11
    h: 76c7a1a42932
  review: drafted
---
