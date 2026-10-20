---
id: fc:chint-sca-50-60ktl-gfcierr
type: FaultCode
name: CPS SCA50-60KTL GFCIErr
aliases:
- GFCIErr
- gfcierr
- CPS GFCIErr
- leakage current high
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: GFCIErr
code_key: gfcierr
display_message: leakage current high
vendor_severity: PROTECTION
page: 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r2
    h: aa54fddbab59
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r2
    h: aa54fddbab59
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:leakage-current
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r2
    h: aa54fddbab59
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r2
    h: aa54fddbab59
  review: drafted
  review_note: 'support check: partial - PV wiring/strings are checked for leakage, but DC cable isn''t
    explicitly named.'
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r2
    h: aa54fddbab59
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r2
    h: aa54fddbab59
  review: drafted
---
