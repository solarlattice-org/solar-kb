---
id: fm:insulation-loss
type: FailureMode
name: Insulation loss
category: Wiring
claims:
  - claim_id: c1
    rel: presents_as
    target: symptom:low-insulation-resistance
    cite: [{src: "src:iea-t13-failures", loc: "sec=7.1", h: "a1b2c3d4e5f6"}]
    review: verified
  - claim_id: c2
    rel: distinguished_from
    target: fm:leakage-current
    by: method:insulation-resistance-test
    note: insulation loss measures low Riso dry; leakage current only when the array is wet
    cite: [{src: "src:iea-t13-failures", loc: "sec=7.1", h: "a1b2c3d4e5f6"}]
    review: drafted
---
