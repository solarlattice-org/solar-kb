---
id: fc:solis-rhi-1p-hv-us-ovvbackup
type: FaultCode
name: Solis RHI-1P-HV OV-VBackup
aliases:
- OV-VBackup
- ovvbackup
- Solis OV-VBackup
- Backup overvoltage fault
category: Inverters
make: solis
make_name: Solis
model_family: rhi-1p-hv-us
family_name: Solis RHI-1P(5-10)K-HVES-5G-US
code: OV-VBackup
code_key: ovvbackup
display_message: Backup overvoltage fault
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r8
    h: bcf28adc0525
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:backup-ac-overvoltage
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:backup-power-outlet
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; factory repair if the fault persists
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  review: drafted
---
