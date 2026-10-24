---
id: fc:solis-1p-4g-us-pvisopro0102
type: FaultCode
name: Solis 1P-4G-US PV ISO-PRO 01/02
aliases:
- PV ISO-PRO 01/02
- pvisopro0102
- Solis PV ISO-PRO 01/02
- Ground Protec on
category: Inverters
make: solis
make_name: Solis
model_family: 1p-4g-us
family_name: Solis-1P(3.6-10)K-4G-US
code: PV ISO-PRO 01/02
code_key: pvisopro0102
display_message: Ground Protec on
page: 62
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r4
    h: 94307fcd8bf8
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r13
    h: 661ca549c0f6
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r13
    h: 661ca549c0f6
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:insulation-resistance-test
  note: Repeat under the same weather as the alarm if first result is normal.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r4
    h: 94307fcd8bf8
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r13
    h: 661ca549c0f6
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r13
    h: 661ca549c0f6
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r4
    h: 94307fcd8bf8
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r13
    h: 661ca549c0f6
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r13
    h: 661ca549c0f6
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=15.r4
    h: 94307fcd8bf8
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r13
    h: 661ca549c0f6
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r13
    h: 661ca549c0f6
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  review: drafted
  review_note: 'support check: partial - Passages say physically check cables, which is roughly a DC cable
    check, but don''t say DC wiring specifically.'
- claim_id: c9
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  review: drafted
- claim_id: c11
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r3
    h: 7ee4aa6d1521
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15
    h: cb7b6f9ed265
  review: drafted
- claim_id: c12
  rel: applies_to
  target: prod:solis-1p-4g-us
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r6
    h: 01092224fc3d
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r6
    h: 01092224fc3d
  review: drafted
---
