---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-pvvoltover
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R PVVoltOver
aliases:
- PVVoltOver
- pvvoltover
- Yaskawa Solectria PVVoltOver
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: PVVoltOver
code_key: pvvoltover
page: 82
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r5
    h: 71975546affc
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r5
    h: 71975546affc
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r5
    h: 71975546affc
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Compare meter reading with displayed value.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r5
    h: 71975546affc
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When display matches meter within tolerance.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r5
    h: 71975546affc
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When display deviates from meter reading beyond tolerance.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r5
    h: 71975546affc
  review: drafted
---
