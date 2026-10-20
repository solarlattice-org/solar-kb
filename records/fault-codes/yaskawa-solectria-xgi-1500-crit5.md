---
id: fc:yaskawa-solectria-xgi-1500-crit5
type: FaultCode
name: Yaskawa Solectria XGI-1500 CRIT-5
aliases:
- CRIT-5
- crit5
- Yaskawa Solectria CRIT-5
- AC Contactor Failure
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: xgi-1500
family_name: Yaskawa Solectria XGI 1500
code: CRIT-5
code_key: crit5
display_message: AC Contactor Failure
vendor_severity: Critical
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18
    h: bd286dd80521
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-contactor
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; technical support if the error does not clear.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=18.r5
    h: ee59ec31ba64
  review: drafted
  review_note: 'support check: partial - Power cycle then contact support is stated, but manual-reset
    clearing is only implied.'
---
