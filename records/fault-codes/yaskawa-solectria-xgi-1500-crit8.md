---
id: fc:yaskawa-solectria-xgi-1500-crit8
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-8
aliases:
- CRIT-8
- crit8
- Yaskawa Solectria CRIT-8
- Ground Fault, Isolation Resistance Low
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-8
code_key: crit8
display_message: Ground Fault, Isolation Resistance Low
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
- claim_id: c5
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
  review_note: 'support check: partial - DC conductors are mentioned as the insulation resistance path,
    but DC cable is not clearly named as the affected component.'
- claim_id: c8
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
  review_note: 'support check: partial - A qualified person must locate and repair the ground fault, but
    the passage does not state a detection method called…'
- claim_id: c9
  rel: has_recovery
  target: ec:service-required
  note: A qualified person must locate and repair the ground fault.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r2
    h: db744e7edd62
  review: drafted
---
