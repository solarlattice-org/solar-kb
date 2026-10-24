---
id: prod:fronius-tauro
type: Product
name: Fronius Tauro
aliases:
- Tauro
category: Inverters
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fronius
  cite:
  - src: src:kb-fronius-fronius-tauro-emanual-status-codes
    loc: sec=front
    h: 55621bbe6e7f
  review: drafted
- claim_id: c2
  rel: requires
  target: role:installer
  note: Only installers or service technicians from authorized specialist companies may do fault analysis
    and repair work, following national standards and regulations.
  cite:
  - src: src:kb-fronius-fronius-tauro-emanual-status-codes
    loc: sec=h19
    h: b33a93958ad2
  - src: src:kb-fronius-fronius-tauro-emanual-status-codes
    loc: sec=h23
    h: b33a93958ad2
  review: drafted
- claim_id: c3
  rel: requires
  target: tool:fronius-solar-web
  note: Use the Fronius Solar.web live app for the fault-handling steps and to set up the communication
    connection.
  cite:
  - src: src:kb-fronius-fronius-tauro-emanual-status-codes
    loc: tbl=2.r1
    h: 94307febd482
  - src: src:kb-fronius-fronius-tauro-emanual-status-codes
    loc: tbl=2.r3
    h: 364265db92ba
  - src: src:kb-fronius-fronius-tauro-emanual-status-codes
    loc: tbl=2
    h: 30c6958cda19
  review: drafted
---
The Fronius Tauro is a Fronius inverter family. The same operating instructions cover the Tauro and the Tauro Eco. The inverter has an operating status LED and a communications LED. It also has an optical sensor that you work by touching it with a finger. A steady green operating LED means normal operation and a flashing green one means the inverter is starting. A steady red light means a network error while the inverter keeps running, and a flashing blue light means an update is in progress. For faults and for setting up the connection, follow the steps in the Fronius Solar.web live app. An optional AC disconnector can break the connection between the inverter and the grid. The status codes include an arc-detection event, which means an arc was found at a specific point on the PV system. Only installers or service technicians from authorized specialist companies may carry out fault analysis and repairs.

<!-- review notes
- sentence 6: support check: partial - Passage gives the cause 'An arc was detected at a specific point on the PV system' but doesn't show it is a status code entry or name the event.
-->
