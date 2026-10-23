---
id: fc:fronius-galvo-306
type: FaultCode
name: Fronius Galvo 306
aliases:
- '306'
- Fronius 306
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '306'
code_key: '306'
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r11
    h: ac6a586a10ac
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h20
    h: 5571d6749f75
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-dc-power
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r6
    h: 886bc9e881d2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r11
    h: ac6a586a10ac
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r6
    h: 886bc9e881d2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r11
    h: ac6a586a10ac
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Normal at dawn and dusk; contact installer only if recurring with sufficient irradiance.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r6
    h: 886bc9e881d2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r11
    h: ac6a586a10ac
  review: drafted
---
