---
id: fc:solis-s6-eh1p-h-us-ovigtr
type: FaultCode
name: Solis S6-EH1P OV-IgTr
aliases:
- OV-IgTr
- ovigtr
- Solis OV-IgTr
- AC side transient overcurrent
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh1p-h-us
family_name: Solis S6-EH1P(3.8-11.4)K-H-US
code: OV-IgTr
code_key: ovigtr
display_message: AC side transient overcurrent
page: 73
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
  cite:
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r6
    h: 70cc8eb6b664
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r6
    h: 2041dbc538a0
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r6
    h: 70cc8eb6b664
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r6
    h: 2041dbc538a0
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r6
    h: 2041dbc538a0
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r6
    h: 70cc8eb6b664
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r6
    h: 2041dbc538a0
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r6
    h: 2041dbc538a0
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r6
    h: 70cc8eb6b664
  review: drafted
  review_note: 'support check: partial - Fault class is only loosely implied by the rows (restart, return
    to factory).'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; factory repair or inverter replacement if it persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=16.r6
    h: 2041dbc538a0
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r6
    h: 70cc8eb6b664
  review: drafted
  review_note: 'support check: partial - Restart and repair/replace are stated, but manual reset clearing
    is not explicit.'
---
