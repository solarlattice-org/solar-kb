---
id: fc:kaco-blueplanet-87-165-tl3-102
type: FaultCode
name: KACO new energy blueplanet TL3 102
aliases:
- '102'
- KACO new energy 102
- Plausibility fault efficiency
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '102'
code_key: '102'
display_message: Plausibility fault efficiency
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r2
    h: 409073c7a7da
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-dc-power-deviation
  note: Device efficiency outside permitted limits.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r2
    h: 409073c7a7da
  review: drafted
  review_note: 'support check: partial - Efficiency plausibility fault with efficiency required to stay
    within limits approximates an AC/DC power deviation, but the passages do not…'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r2
    h: 409073c7a7da
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r2
    h: 409073c7a7da
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r2
    h: 409073c7a7da
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r2
    h: 409073c7a7da
  review: drafted
---
