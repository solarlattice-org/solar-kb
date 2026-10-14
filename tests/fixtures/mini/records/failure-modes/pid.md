---
id: fm:pid
type: FailureMode
name: Potential-induced degradation
aliases: [PID, PID-s]
status: active
claims:
  - claim_id: c1
    rel: caused_by
    target: stressor:negative-voltage-to-ground
    conditions: worse with humidity and heat
    cite: [{src: "src:iea-t13-failures", loc: "sec=4.3"}, {src: "src:nrel-pid-guide", loc: "p=12"}]
    review: verified
    verified_by: reviewer
    verified_at: 2026-11-02
  - claim_id: c2
    rel: presents_as
    target: symptom:uniform-power-loss
    cite: [{src: "src:iea-t13-failures", loc: "sec=4.3"}]
    review: verified
  - claim_id: c3
    rel: presents_as
    target: symptom:darkened-cells-in-el
    cite: [{src: "src:iea-t13-failures", loc: "fig=12"}]
    review: verified
  - claim_id: c4
    rel: detected_by
    target: method:el-imaging
    cite: [{src: "src:iea-t13-failures", loc: "sec=4.3"}]
    review: verified
  - claim_id: c5
    rel: mitigated_by
    target: mit:pid-recovery
    cite: [{src: "src:nrel-pid-guide", loc: "p=20"}]
    review: drafted
  - claim_id: c6
    rel: affects
    target: comp:pv-module
    cite: [{src: "src:iea-t13-failures", loc: "sec=4.3"}]
    review: verified
  - claim_id: c7
    rel: distinguished_from
    target: fm:soiling
    by: method:el-imaging
    note: PID darkens cells in EL; soiling leaves no EL signature
    cite: [{src: "src:iea-t13-failures", loc: "sec=4.3"}]
    review: verified
  - claim_id: c8
    attr: typical_power_loss
    value: {min: 10, max: 30, unit: "unit:PERCENT"}
    conditions: p-type modules at the negative end of long strings
    cite: [{src: "src:nrel-pid-guide", loc: "tbl=2.r3"}]
    review: drafted
---
PID shunts cells in modules held at high negative potential [[stressors/negative-voltage-to-ground|negative voltage to ground]].
