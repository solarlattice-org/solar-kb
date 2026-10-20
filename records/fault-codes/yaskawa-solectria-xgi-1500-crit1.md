---
id: fc:yaskawa-solectria-xgi-1500-crit1
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-1
aliases:
- CRIT-1
- crit1
- Yaskawa Solectria CRIT-1
- Software Parameter Load Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-1
code_key: crit1
display_message: Software Parameter Load Failure
vendor_severity: Critical
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r1
    h: ddfd206e8431
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r1
    h: ddfd206e8431
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:parameter-download-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r1
    h: ddfd206e8431
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r1
    h: ddfd206e8431
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r1
    h: ddfd206e8431
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Firmware update and power cycle first; technical support if it persists.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r1
    h: ddfd206e8431
  review: drafted
  review_note: 'support check: partial - Power cycle/firmware update then contact support is stated, but
    the passage does not say the code clears by manual reset.'
---
