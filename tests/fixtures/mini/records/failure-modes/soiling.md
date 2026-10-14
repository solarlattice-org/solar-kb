---
id: fm:soiling
type: FailureMode
name: Soiling
claims:
  - claim_id: c1
    rel: presents_as
    target: symptom:uniform-power-loss
    cite: [{src: "src:iea-t13-failures", loc: "sec=6.1"}]
    review: drafted
  - claim_id: c2
    rel: distinguished_from
    target: fm:pid
    by: method:el-imaging
    note: soiling leaves no EL signature
    cite: [{src: "src:iea-t13-failures", loc: "sec=4.3"}]
    review: verified
---
