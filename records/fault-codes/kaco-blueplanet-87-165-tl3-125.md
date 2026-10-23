---
id: fc:kaco-blueplanet-87-165-tl3-125
type: FaultCode
name: KACO new energy blueplanet TL3 125
aliases:
- '125'
- KACO new energy 125
- Relay control fault
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '125'
code_key: '125'
display_message: Relay control fault
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r2
    h: 9159d7080187
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r2
    h: 9159d7080187
  review: drafted
  review_note: 'support check: partial - The row is a relay control fault where the enable signal is read
    back and shutdown occurs on an incorrect…'
- claim_id: c3
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r2
    h: 9159d7080187
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r2
    h: 9159d7080187
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r2
    h: 9159d7080187
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r2
    h: 9159d7080187
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r2
    h: 9159d7080187
  review: drafted
---
