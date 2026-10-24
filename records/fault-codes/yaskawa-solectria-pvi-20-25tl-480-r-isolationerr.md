---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-isolationerr
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R IsolationErr
aliases:
- IsolationErr
- isolationerr
- Yaskawa Solectria IsolationErr
- Insulation resistance low
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: IsolationErr
code_key: isolationerr
display_message: Insulation resistance low
page: 81
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r4
    h: 0a45e3bbf97d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r5
    h: 96e51e5f36fe
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r4
    h: 0a45e3bbf97d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r4
    h: 0a45e3bbf97d
  review: drafted
  review_note: 'support check: partial - The passage troubleshoots PV strings and wiring leakage, implying
    the PV array, but never states the alarm affects the PV array.'
- claim_id: c4
  rel: detected_by
  target: method:fault-localization
  note: String-by-string isolation to find leakage to earth.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r4
    h: 0a45e3bbf97d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r5
    h: 96e51e5f36fe
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-pvi-20-25tl-480-r
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r4
    h: 0a45e3bbf97d
  review: drafted
---
