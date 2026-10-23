---
id: fc:generac-pwrcell-inverter-0x770d
type: FaultCode
name: Generac PWRcell Inverter 0X770D
aliases:
- 0X770D
- '0x770d'
- Generac 0X770D
category: Inverters
make: generac
make_name: Generac
model_family: pwrcell-inverter
family_name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
code: 0X770D
code_key: '0x770d'
page: 68
claims:
- claim_id: c1
  rel: defined_in
  target: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r14
    h: cb080830f74a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-phase-angle-abnormal
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r14
    h: cb080830f74a
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r14
    h: cb080830f74a
  review: drafted
  review_note: 'support check: partial - Corrective action says to check voltage measurement, but detection
    by grid voltage measurement isn''t explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=33.r14
    h: cb080830f74a
  review: drafted
---
