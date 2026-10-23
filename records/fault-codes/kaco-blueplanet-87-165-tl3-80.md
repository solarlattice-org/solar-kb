---
id: fc:kaco-blueplanet-87-165-tl3-80
type: FaultCode
name: KACO new energy blueplanet TL3 80
aliases:
- '80'
- KACO new energy 80
- Insulation meas. not pos-sible
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '80'
code_key: '80'
display_message: Insulation meas. not pos-sible
page: 106
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r1
    h: 16f544122cf6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-voltage-fluctuation
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r1
    h: 16f544122cf6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r1
    h: 16f544122cf6
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:power-stage-fault
  note: Only when the message appears continuously (defective semiconductor).
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r1
    h: 16f544122cf6
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r1
    h: 16f544122cf6
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the message persists continuously; also check PV module installation.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r1
    h: 16f544122cf6
  review: drafted
---
