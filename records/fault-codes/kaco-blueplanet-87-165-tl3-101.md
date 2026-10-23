---
id: fc:kaco-blueplanet-87-165-tl3-101
type: FaultCode
name: KACO new energy blueplanet TL3 101
aliases:
- '101'
- KACO new energy 101
- Temperature plausibility er-ror
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '101'
code_key: '101'
display_message: Temperature plausibility er-ror
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r1
    h: da893bbe31a2
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:abnormal-temperature-reading
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r1
    h: da893bbe31a2
  review: drafted
  review_note: 'support check: partial - The passages describe a temperature plausibility error from comparing
    temperatures, which is close to an abnormal reading, but they do…'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r1
    h: da893bbe31a2
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r1
    h: da893bbe31a2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r1
    h: da893bbe31a2
  review: drafted
---
