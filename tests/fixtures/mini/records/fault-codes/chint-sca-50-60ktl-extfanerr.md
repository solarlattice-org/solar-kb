---
id: fc:chint-sca-50-60ktl-extfanerr
type: FaultCode
name: CPS SCA50-60KTL ExtFanErr
aliases: [ExtFanErr, CPS ExtFanErr, External fan error]
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: ExtFanErr
code_key: extfanerr
display_message: External fan error
vendor_severity: WARNING
page: 4
status: active
claims:
  - claim_id: c1
    rel: defined_in
    target: src:chint-fault-manual
    cite: [{src: "src:chint-fault-manual", loc: "tbl=2.r3", h: "2b3c4d5e6f70"}, {src: "src:chint-fault-manual", loc: "tbl=4.r1", h: "3c4d5e6f7081"}]
    review: drafted
  - claim_id: c2
    rel: has_event_class
    target: ec:warning
    note: from the Type column
    cite: [{src: "src:chint-fault-manual", loc: "tbl=2.r3", h: "2b3c4d5e6f70"}]
    review: drafted
  - claim_id: c3
    rel: has_production_effect
    target: ec:derate
    cite: [{src: "src:chint-fault-manual", loc: "tbl=2.r3", h: "2b3c4d5e6f70"}]
    review: drafted
  - claim_id: c4
    attr: output_limit
    value: {max: 50, unit: "unit:PERCENT"}
    conditions: basis=rated_power; while the external fan fault persists
    cite: [{src: "src:chint-fault-manual", loc: "tbl=2.r3", h: "2b3c4d5e6f70"}]
    review: drafted
  - claim_id: c5
    rel: has_recovery
    target: ec:service-required
    note: the fan is replaced by service
    cite: [{src: "src:chint-fault-manual", loc: "tbl=2.r3", h: "2b3c4d5e6f70"}]
    review: drafted
---
