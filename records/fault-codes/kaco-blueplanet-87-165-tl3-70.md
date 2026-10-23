---
id: fc:kaco-blueplanet-87-165-tl3-70
type: FaultCode
name: KACO new energy blueplanet TL3 70
aliases:
- '70'
- KACO new energy 70
- Fault in fan 1
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '70'
code_key: '70'
display_message: Fault in fan 1
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  note: Interior fan or its tacho signal
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
- claim_id: c6
  attr: output_limit
  value:
    nominal: 50
    unit: unit:PERCENT
  conditions: basis=rated_power; interior fan or tacho signal failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
  review_note: 'support check: partial - The row shows the device detects fan/tacho failure via the tacho
    signal, but no ''fan function check'' method is named.'
- claim_id: c8
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Fan plug check by qualified personnel
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r5
    h: 6111c1a12b1d
  review: drafted
---
