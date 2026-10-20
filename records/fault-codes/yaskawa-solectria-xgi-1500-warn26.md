---
id: fc:yaskawa-solectria-xgi-1500-warn26
type: FaultCode
name: Yaskawa Solectria XGI-1500 WARN-26
aliases:
- WARN-26
- warn26
- Yaskawa Solectria WARN-26
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: WARN-26
code_key: warn26
vendor_severity: Warning
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=20
    h: fc50119e7e7e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=9.1.2
    h: 03d6c2913989
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact support if the error persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=21.r9
    h: 8534a8b4965d
  review: drafted
  review_note: 'support check: partial - Power cycle then contact support is stated, and a power cycle
    is a manual action, but the row doesn''t explicitly…'
---
