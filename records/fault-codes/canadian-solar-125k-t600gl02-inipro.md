---
id: fc:canadian-solar-125k-t600gl02-inipro
type: FaultCode
name: Canadian Solar 125K-T600GL02 IN I-PRO
aliases:
- IN I-PRO
- inipro
- Canadian Solar IN I-PRO
- Initialization Protect ion
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 125k-t600gl02
family_name: CSI-125K-T600GL02-U
code: IN I-PRO
code_key: inipro
display_message: Initialization Protect ion
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r2
    h: 68bcd06b0203
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  note: Processor values disagree between master and slave controllers.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r2
    h: 4c094ee77fda
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r2
    h: 4c094ee77fda
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r2
    h: 4c094ee77fda
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replace inverter if it persists.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r2
    h: 4c094ee77fda
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r2
    h: 4c094ee77fda
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8
    h: b80e6cf9a87a
  review: drafted
  review_note: 'support check: partial - The table is titled ''Fault messages'' and lists IN I-PRO, but
    the row itself doesn''t state the device behavior; fault…'
- claim_id: c7
  rel: applies_to
  target: prod:canadian-solar-125k-t600gl02
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r2
    h: 68bcd06b0203
  review: drafted
---
