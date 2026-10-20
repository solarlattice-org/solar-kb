---
id: fc:chint-sca-36ktl-isolationerr
type: FaultCode
name: CPS SCA36KTL IsolationErr
aliases: [IsolationErr, CPS IsolationErr, Insulation resistance low]
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
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
    review: drafted
---
