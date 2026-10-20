---
id: fc:yaskawa-solectria-xgi-1500-crit11
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-11
aliases:
- CRIT-11
- crit11
- Yaskawa Solectria CRIT-11
- Operational Self Check Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-11
code_key: crit11
display_message: Operational Self Check Failure
vendor_severity: Critical
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; description says service is needed, so contact support if it persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=19.r5
    h: 2ea826cbedaa
  review: drafted
---
