---
id: fc:solis-s6-eh3p-75-150k-us-afcicheck
type: FaultCode
name: Solis S6-EH3P75-150K AFCI-Check
aliases:
- AFCI-Check
- afcicheck
- Solis AFCI-Check
- AFCI self-test failure
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: AFCI-Check
code_key: afcicheck
display_message: AFCI self-test failure
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r18
    h: 9662b1a38062
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r4
    h: 2083a226e468
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=29.r3
    h: 9662b1a38062
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r18
    h: 9662b1a38062
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-detector-failure
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r6
    h: 391a0e888bc9
  review: drafted
  review_note: 'support check: partial - The cause is AFCI components self-protection failure, but no
    ''arc detection board'' is named.'
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r6
    h: 391a0e888bc9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r4
    h: 2083a226e468
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r6
    h: 391a0e888bc9
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=10.3.1
    h: 16fa984bf0d2
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; replace inverter if the fault persists.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r6
    h: 391a0e888bc9
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=20.r4
    h: 2083a226e468
  review: drafted
---
