---
id: fc:fronius-symo-572
type: FaultCode
name: Fronius Symo 572
aliases:
- '572'
- Fronius 572
- Power limitation due to power module
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '572'
code_key: '572'
display_message: Power limitation due to power module
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r16
    h: f6ca444fea91
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r16
    h: f6ca444fea91
  review: drafted
  review_note: 'support check: partial - Power limitation is stated, but the ''derating'' symptom matches
    only loosely; cause is the power module.'
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r16
    h: f6ca444fea91
  review: drafted
  review_note: 'support check: partial - Power module is named, but inverter bridge is not specifically
    stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: No limit value stated.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r16
    h: f6ca444fea91
  review: drafted
---
