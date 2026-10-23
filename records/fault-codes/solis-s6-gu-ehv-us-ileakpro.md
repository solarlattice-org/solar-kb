---
id: fc:solis-s6-gu-ehv-us-ileakpro
type: FaultCode
name: Solis S6-GU ILeak-PRO
aliases:
- ILeak-PRO
- ileakpro
- Solis ILeak-PRO
- Leakage current protect ion
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: ILeak-PRO
code_key: ileakpro
display_message: Leakage current protect ion
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r1
    h: 1d19c0c43f5c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:insulation-loss
  note: Applies when the alarm occurs mainly in rain or high humidity.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r1
    h: 1d19c0c43f5c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r1
    h: 1d19c0c43f5c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r1
    h: 1d19c0c43f5c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  note: Strings reconnected one at a time to locate the fault.
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r1
    h: 1d19c0c43f5c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-parameter-change
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r1
    h: 1d19c0c43f5c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=15.r1
    h: 1d19c0c43f5c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=14.r1
    h: 1d19c0c43f5c
  review: drafted
  review_note: 'support check: partial - Protection alarm implies a fault but classification is not explicitly
    stated; plausible.'
---
