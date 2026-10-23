---
id: fc:kaco-blueplanet-87-165-tl3-59
type: FaultCode
name: KACO new energy blueplanet TL3 59
aliases:
- '59'
- KACO new energy 59
- Self test error
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '59'
code_key: '59'
display_message: Self test error
page: 104
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r4
    h: fff389bf74da
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r4
    h: fff389bf74da
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r4
    h: fff389bf74da
  review: drafted
  review_note: 'support check: partial - Describes a self-test error but device behavior is not stated;
    fault class only loosely implied.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r4
    h: fff389bf74da
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  note: Authorised electrician must be notified
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r4
    h: fff389bf74da
  review: drafted
---
