---
id: fc:fronius-symo-463
type: FaultCode
name: Fronius Symo 463
aliases:
- '463'
- Fronius 463
- AC polarity reversed, AC connector plugged in incorrectly
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '463'
code_key: '463'
display_message: AC polarity reversed, AC connector plugged in incorrectly
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r34
    h: 2014e3ab07d3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-polarity-reversed
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r34
    h: 2014e3ab07d3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r32
    h: 2014e3ab07d3
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:inverter-installation-defect
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r34
    h: 2014e3ab07d3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r32
    h: 2014e3ab07d3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-connector
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r34
    h: 2014e3ab07d3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r32
    h: 2014e3ab07d3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r34
    h: 2014e3ab07d3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r32
    h: 2014e3ab07d3
  review: drafted
  review_note: 'support check: partial - The passages imply the connector is wrongly plugged in but give
    no remedy, so a connection check is only implied.'
---
