---
id: fc:fronius-primo-460
type: FaultCode
name: Fronius Primo 460
aliases:
- '460'
- Fronius 460
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '460'
code_key: '460'
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r29
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reference-voltage-out-of-tolerance
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r31
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r29
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r16
    h: d4d51e4531d2
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r31
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r29
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r16
    h: d4d51e4531d2
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:fronius-primo
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r29
    h: b9bd723471f5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
---
