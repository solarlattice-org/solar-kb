---
id: fc:kaco-blueplanet-87-165-tl3-188
type: FaultCode
name: KACO new energy blueplanet TL3 188
aliases:
- '188'
- KACO new energy 188
- Semiconductor test not pos-sible
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '188'
code_key: '188'
display_message: Semiconductor test not pos-sible
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r8
    h: 22d06f5f5b98
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r8
    h: 22d06f5f5b98
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  note: Semiconductor actuation or filter voltage measurement faulty.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r8
    h: 22d06f5f5b98
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r8
    h: 22d06f5f5b98
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: AC and DC disconnection and reconnection.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r8
    h: 22d06f5f5b98
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r8
    h: 22d06f5f5b98
  review: drafted
  review_note: 'support check: partial - Faulty semiconductor test implies a fault, but the class isn''t
    stated explicitly.'
---
