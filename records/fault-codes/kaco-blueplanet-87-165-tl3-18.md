---
id: fc:kaco-blueplanet-87-165-tl3-18
type: FaultCode
name: KACO new energy blueplanet TL3 18
aliases:
- '18'
- KACO new energy 18
- Resid. current shutdown (AFI)
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '18'
code_key: '18'
display_message: Resid. current shutdown (AFI)
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r4
    h: e8cf06dd4b30
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r4
    h: e8cf06dd4b30
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r4
    h: e8cf06dd4b30
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r4
    h: e8cf06dd4b30
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ground-conductor-check
  note: Faulty earth cabling is the usual cause, often showing up during rain.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r4
    h: e8cf06dd4b30
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r4
    h: e8cf06dd4b30
  review: drafted
---
