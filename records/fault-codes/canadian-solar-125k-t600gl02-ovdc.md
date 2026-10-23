---
id: fc:canadian-solar-125k-t600gl02-ovdc
type: FaultCode
name: Canadian Solar 125K-T600GL02 OV-DC
aliases:
- OV-DC
- ovdc
- Canadian Solar OV-DC
- DC voltage is too high
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 125k-t600gl02
family_name: CSI-125K-T600GL02-U
code: OV-DC
code_key: ovdc
display_message: DC voltage is too high
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=10.r3
    h: 4a5cc9d0fbbf
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r3
    h: a8e629da74cd
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r3
    h: 4a5cc9d0fbbf
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r3
    h: 4a5cc9d0fbbf
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r3
    h: a8e629da74cd
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r3
    h: 4a5cc9d0fbbf
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r3
    h: 4a5cc9d0fbbf
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when measured string voltage is high due to too many modules.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r3
    h: a8e629da74cd
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r3
    h: 4a5cc9d0fbbf
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r3
    h: 4a5cc9d0fbbf
  review: drafted
  review_note: 'support check: partial - Passages say too many panels in string causes high DCV but do
    not explicitly state a string configuration correction action.'
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r3
    h: a8e629da74cd
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r3
    h: 4a5cc9d0fbbf
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r3
    h: 4a5cc9d0fbbf
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Escalation when display reading suggests faulty measurement circuit.
  cite:
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r3
    h: a8e629da74cd
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=11.r3
    h: 4a5cc9d0fbbf
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=13.r3
    h: 4a5cc9d0fbbf
  review: drafted
---
