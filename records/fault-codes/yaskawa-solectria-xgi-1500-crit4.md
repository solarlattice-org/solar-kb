---
id: fc:yaskawa-solectria-xgi-1500-crit4
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-4
aliases:
- CRIT-4
- crit4
- Yaskawa Solectria CRIT-4
- ARC Fault Detected
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-4
code_key: crit4
display_message: ARC Fault Detected
vendor_severity: Critical
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  review: drafted
  review_note: 'support check: partial - Inspection is a troubleshooting step, but the passage does not
    say the fault is detected by visual inspection; the inverter…'
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Operator clears the arc fault after repair and retests; technical support if it recurs.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r4
    h: b26ca2eacb3b
  review: drafted
---
