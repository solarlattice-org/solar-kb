---
id: symptom:driver-supply-undervoltage
type: Symptom
name: Driver supply undervoltage
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Primo and Symo inverters report this condition as status code 476, which their status
    code tables describe as the driver supply voltage being too low.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r35
    h: 6316eb4991a3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r37
    h: 6316eb4991a3
  review: drafted
  review_note: 'support check: partial - Passages give code 476 as ''Supply voltage for driver too low'',
    but don''t name Fronius Primo/Symo or say it is shown on the inverter fault code display.'
---
Fronius Primo and Fronius Symo inverters report this condition as status code 476. In both status code tables, the code means the supply voltage to the driver is too low. The technician sees it as a status code on the inverter, not as a pattern in array data or images. The source tables give only the code and its description, so they list no causes or troubleshooting steps for this code.

<!-- review notes
- sentence 1: support check: partial - Code 476 with this description appears in two tables, but the passages don't identify Primo or Symo as the models.
- sentence 2: support check: partial - Both passages say code 476 is 'Supply voltage for driver too low', but they don't identify them as the Primo and Symo tables.
- sentence 3: support check: partial - The passages show a code and description, which implies a status code, but they don't say how the technician sees it or contrast it with array data or images.
-->
