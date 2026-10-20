---
id: fc:yaskawa-solectria-xgi-1500-warn3
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-3
aliases:
- WARN-3
- warn3
- Yaskawa Solectria WARN-3
- Islanding Detected
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-3
code_key: warn3
display_message: Islanding Detected
vendor_severity: Warning
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:islanding-detected
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Production resumes when the islanding event ends; support if AC present but no reconnection.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20.r3
    h: c2e7279a7a24
  review: drafted
---
