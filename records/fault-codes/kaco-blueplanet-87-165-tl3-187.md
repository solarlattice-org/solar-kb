---
id: fc:kaco-blueplanet-87-165-tl3-187
type: FaultCode
name: KACO new energy blueplanet TL3 187
aliases:
- '187'
- KACO new energy 187
- Fault in fan 4
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '187'
code_key: '187'
display_message: Fault in fan 4
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  note: Fan itself or its tacho signal may be at fault.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: detected_by
  target: method:fan-function-check
  note: Check whether the fan is blocked.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: drafted
  review_note: 'support check: partial - Action asks whether the fan is blocked, but a named detection
    method isn''t stated.'
- claim_id: c6
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Fan plug seating checked by qualified personnel.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:no-production-effect
  note: Power not reduced directly; any reduction comes only through temperature derating.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r7
    h: 1c87b6df8497
  review: drafted
  review_note: 'support check: partial - The device continues operating, but the row is labelled ''Fault
    in fan'' and warning is not stated.'
---
