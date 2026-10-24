---
id: fc:chint-sca-25ktl-208-isolationerr
type: FaultCode
name: CPS SCA25KTL-208 IsolationErr
aliases:
- IsolationErr
- isolationerr
- CPS IsolationErr
- Insulation resistance low
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: IsolationErr
code_key: isolationerr
display_message: Insulation resistance low
vendor_severity: Protection
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r8
    h: acaf4adf7562
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r2
    h: 81c46507b9b5
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r2
    h: 064a742016b1
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r7
    h: bcf81b9b362d
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r14
    h: 6097f6c3cfa2
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r3
    h: 91fe203f5279
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r8
    h: acaf4adf7562
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r2
    h: 81c46507b9b5
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r2
    h: 064a742016b1
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r7
    h: bcf81b9b362d
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r18
    h: 2086e621c3f7
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r19
    h: 2dd4d412445e
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r19
    h: 2dd4d412445e
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r2
    h: 81c46507b9b5
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r2
    h: 064a742016b1
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r7
    h: bcf81b9b362d
  review: drafted
  review_note: 'support check: partial - Passages say to trace the wiring of the faulted string for leakage,
    but a DC cable is not named explicitly.'
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r8
    h: acaf4adf7562
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r15
    h: 7449fd187fa6
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r16
    h: 1ac7d007f121
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r17
    h: 0049cd36947f
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r18
    h: 2086e621c3f7
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r2
    h: 81c46507b9b5
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r2
    h: 064a742016b1
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r7
    h: bcf81b9b362d
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r2
    h: 81c46507b9b5
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r2
    h: 064a742016b1
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r7
    h: bcf81b9b362d
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r19
    h: 2dd4d412445e
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r3
    h: 91fe203f5279
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Insulation resistance threshold parameter may be adjusted as a last step.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r2
    h: 81c46507b9b5
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r2
    h: 064a742016b1
  review: drafted
  review_note: 'support check: partial - The ISOResist parameter can be adjusted, but ''last step'' ordering
    and ''threshold'' are only implied by its position as item 6.'
- claim_id: c9
  rel: applies_to
  target: prod:chint-sca-25ktl-208
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r1
    h: ef57cb62b84d
  review: drafted
---
