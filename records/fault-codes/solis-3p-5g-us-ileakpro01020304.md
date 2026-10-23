---
id: fc:solis-3p-5g-us-ileakpro01020304
type: FaultCode
name: Solis 3P-5G-US ILeak-PRO 01/02/03/04
aliases:
- ILeak-PRO 01/02/03/04
- ileakpro01020304
- Solis ILeak-PRO 01/02/03/04
- Leakage current protection
category: Inverters
make: solis
make_name: Solis
model_family: 3p-5g-us
family_name: Solis-3P(125-255)K-EHV-5G-US
code: ILeak-PRO 01/02/03/04
code_key: ileakpro01020304
display_message: Leakage current protection
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r5
    h: dcb57b87715b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r5
    h: dcb57b87715b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r11
    h: 04668f7557da
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r11
    h: 04668f7557da
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r5
    h: dcb57b87715b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r11
    h: 04668f7557da
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r11
    h: 04668f7557da
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r5
    h: dcb57b87715b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r11
    h: 04668f7557da
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r11
    h: 04668f7557da
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Internal inverter cable connections.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r5
    h: dcb57b87715b
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r11
    h: 04668f7557da
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=13.r11
    h: 04668f7557da
  review: drafted
---
