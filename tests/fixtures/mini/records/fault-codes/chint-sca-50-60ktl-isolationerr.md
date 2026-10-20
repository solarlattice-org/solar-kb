---
id: fc:chint-sca-50-60ktl-isolationerr
type: FaultCode
name: CPS SCA50-60KTL IsolationErr
aliases: [IsolationErr, isolationerr, CPS IsolationErr, Insulation resistance low]
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: IsolationErr
code_key: isolationerr
display_message: Insulation resistance low
vendor_severity: PROTECTION
page: 6
status: active
claims:
  - claim_id: c1
    rel: defined_in
    target: src:chint-fault-manual
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r1", h: "1a2b3c4d5e6f"}]
    review: drafted
  - claim_id: c2
    rel: has_event_class
    target: ec:fault
    note: from the Type column
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r1", h: "1a2b3c4d5e6f"}]
    review: drafted
  - claim_id: c3
    rel: reports
    target: symptom:low-insulation-resistance
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r1", h: "1a2b3c4d5e6f"}]
    review: verified
    verified_by: reviewer
    verified_at: 2026-10-19
  - claim_id: c4
    rel: indicates
    target: fm:insulation-loss
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r1", h: "1a2b3c4d5e6f"}]
    review: drafted
  - claim_id: c5
    rel: affects
    target: comp:dc-cable
    note: the PV wiring and its connection to ground
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r1", h: "1a2b3c4d5e6f"}]
    review: drafted
  - claim_id: c6
    rel: detected_by
    target: method:insulation-resistance-test
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r1", h: "1a2b3c4d5e6f"}]
    review: drafted
  - claim_id: c7
    rel: has_recovery
    target: ec:manual-reset
    note: restart after the wiring is repaired
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r1", h: "1a2b3c4d5e6f"}]
    review: drafted
---
<!-- review notes: FC0 fixture, mirrors the Plan 4d example record -->
