---
id: fc:chint-sch-100-125ktl-gfcierr
type: FaultCode
name: CPS SCH100-125KTL GFCIErr
aliases:
- GFCIErr
- gfcierr
- CPS GFCIErr
- leakage current high
category: Inverters
make: chint
make_name: CPS
model_family: sch-100-125ktl
family_name: CPS SCH100/125KTL-DO/US-600
code: GFCIErr
code_key: gfcierr
display_message: leakage current high
vendor_severity: Protection
page: 76
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the table header
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36
    h: 17d36efd4fe1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r2
    h: 7a7bde079930
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r3
    h: b7d515f0584f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r3
    h: d12e0f8ca061
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r8
    h: 22c9d8acfe1c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r20
    h: 96b93ee16db5
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r4
    h: 2747c5d1bd14
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r2
    h: 7a7bde079930
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r3
    h: b7d515f0584f
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r3
    h: d12e0f8ca061
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r8
    h: 22c9d8acfe1c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r24
    h: 6a5eccf0d8b6
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r1
    h: f228faa0c6d0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r3
    h: d12e0f8ca061
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r8
    h: 22c9d8acfe1c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r25
    h: e91718897b34
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r4
    h: 2747c5d1bd14
  review: drafted
  review_note: 'support check: partial - Passages say to trace wirings of the faulted string for leakage,
    but never name DC cable specifically.'
- claim_id: c6
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r2
    h: 7a7bde079930
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=58.r3
    h: b7d515f0584f
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: tbl=59.r1
    h: f228faa0c6d0
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r3
    h: d12e0f8ca061
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r8
    h: 22c9d8acfe1c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r21
    h: cfce40c8d8f8
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r22
    h: 256f5fb37000
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r23
    h: 9bd05c6744d9
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r24
    h: 6a5eccf0d8b6
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r2
    h: 7a7bde079930
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r3
    h: d12e0f8ca061
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r8
    h: 22c9d8acfe1c
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r20
    h: 96b93ee16db5
  - src: src:chint-cps-sch275ktl-do-us-800-v2-user-manual-rev-1-7
    loc: tbl=27.r25
    h: e91718897b34
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=35.r4
    h: 2747c5d1bd14
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r2
    h: 7a7bde079930
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=32.r3
    h: d12e0f8ca061
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=42.r8
    h: 22c9d8acfe1c
  review: drafted
  review_note: 'review: partial - The passages give GFCIErr the Protection type and string-isolation troubleshooting
    steps, but none of them says the inverter trips or that production…'
- claim_id: c9
  rel: applies_to
  target: prod:chint-sch-100-125ktl
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=36.r9
    h: 146db02bba62
  review: drafted
---
