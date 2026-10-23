---
id: fc:yaskawa-solectria-pvi-23-36tl-isolationerr
type: FaultCode
name: Yaskawa Solectria PVI-TL IsolationErr
aliases:
- IsolationErr
- isolationerr
- Yaskawa Solectria IsolationErr
- DC insulation impedance to ground
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-23-36tl
family_name: Solectria PVI 23/28/36TL
code: IsolationErr
code_key: isolationerr
display_message: DC insulation impedance to ground
vendor_severity: Protection
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-pvi-23-28tl
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r5
    h: 96e51e5f36fe
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r5
    h: 96e51e5f36fe
  review: drafted
- claim_id: c3
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
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r4
    h: 0a45e3bbf97d
  review: drafted
  review_note: 'support check: partial - The passage troubleshoots PV strings and wiring leakage, implying
    the PV array, but never states the alarm affects the PV array.'
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  note: String-by-string isolation to find leakage to earth.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r4
    h: 0a45e3bbf97d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r5
    h: 96e51e5f36fe
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  note: Installer must inspect installation for ground fault
  cite:
  - src: src:yaskawa-solectria-pvi-23-28tl
    loc: tbl=19.r5
    h: 96e51e5f36fe
  review: verified
  review_note: 'support check: partial - Row lists observing for auto-clear first, then service; installer
    inspection is stated but the clearing is not purely service-required.'
  verified_by: review-workflow
  verified_at: 2026-10-20
---
