---
id: fc:yaskawa-solectria-xgi-1500-crit10
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-10
aliases:
- CRIT-10
- crit10
- Yaskawa Solectria CRIT-10
- Ground Fault Detection Self Check Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-10
code_key: crit10
display_message: Ground Fault Detection Self Check Failure
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r4
    h: ca381f1f0949
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r4
    h: ca381f1f0949
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:ground-fault-detector-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r4
    h: ca381f1f0949
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r4
    h: ca381f1f0949
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r4
    h: ca381f1f0949
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; technical support if the error does not clear.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r4
    h: ca381f1f0949
  review: drafted
---
