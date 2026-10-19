---
id: fc:chint-sca-50-60ktl-protect90
type: FaultCode
name: CPS SCA50-60KTL Protect0090
aliases: [Protect0090, protect90, CPS Protect0090, Bus over voltage]
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Protect0090
code_key: protect90
display_message: Bus over voltage
vendor_severity: PROTECTION
page: 7
status: active
claims:
  - claim_id: c1
    rel: defined_in
    target: src:chint-fault-manual
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r2", h: "6f708192a3b4"}]
    review: drafted
  - claim_id: c2
    rel: has_event_class
    target: ec:fault
    note: from the Type column
    cite: [{src: "src:chint-fault-manual", loc: "tbl=8.r2", h: "6f708192a3b4"}]
    review: drafted
---
