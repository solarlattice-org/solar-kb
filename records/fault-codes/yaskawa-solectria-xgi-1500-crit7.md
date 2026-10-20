---
id: fc:yaskawa-solectria-xgi-1500-crit7
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-7
aliases:
- CRIT-7
- crit7
- Yaskawa Solectria CRIT-7
- Ground Fault, Excessive Leakage Current
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-7
code_key: crit7
display_message: Ground Fault, Excessive Leakage Current
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:leakage-current
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
  review_note: 'support check: partial - A qualified person must locate and repair the ground fault, but
    the passage does not state a detection method called…'
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  note: A qualified person must locate and repair the ground fault.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r1
    h: 8cc7b04502b0
  review: drafted
---
