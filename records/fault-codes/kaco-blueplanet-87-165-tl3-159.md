---
id: fc:kaco-blueplanet-87-165-tl3-159
type: FaultCode
name: KACO new energy blueplanet TL3 159
aliases:
- '159'
- KACO new energy 159
- Waiting for fault acknow-ledgement
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '159'
code_key: '159'
display_message: Waiting for fault acknow-ledgement
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r8
    h: 6ed40dc647b7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r8
    h: 6ed40dc647b7
  review: drafted
  review_note: 'support check: partial - Row says DSP awaits configuration data and configuration must
    be completed, implying incomplete configuration, but it is not explicitly called…'
- claim_id: c3
  rel: mitigated_by
  target: mit:complete-device-configuration
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r8
    h: 6ed40dc647b7
  review: drafted
---
