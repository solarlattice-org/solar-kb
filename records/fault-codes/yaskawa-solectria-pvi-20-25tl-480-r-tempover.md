---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-tempover
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R TempOver
aliases:
- TempOver
- tempover
- Yaskawa Solectria TempOver
- Over-temperature protection
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: TempOver
code_key: tempover
display_message: Over-temperature protection
page: 80
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: Labelled as a protection event
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  review: drafted
  review_note: 'support check: partial - It is labelled over-temperature protection, but the passage doesn''t
    state it is a fault that stops the device; it may…'
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: Air inlet or fan may be blocked
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:proper-installation
  note: Check that the installation location and ambient temperature are within spec
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Can clear on its own within 30 minutes; contact after-sales service if it persists
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r1
    h: 8c02d6e0b326
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Final escalation step
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=36.r1
    h: 8c02d6e0b326
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=35.r7
    h: de38f915f9b1
  review: drafted
---
