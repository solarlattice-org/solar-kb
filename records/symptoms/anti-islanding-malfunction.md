---
id: symptom:anti-islanding-malfunction
type: Symptom
name: Anti-islanding function malfunction
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Primo and Fronius Symo inverters report this condition as status code 456, which says
    the anti-islanding function is no longer running properly.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r26
    h: 78b3b6a48dd1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r27
    h: 78b3b6a48dd1
  review: drafted
  review_note: 'support check: partial - Passages give code 456 and the anti-islanding description, but
    don''t name Fronius Primo/Symo models or the ''inverter fault code display'' channel.'
---
This symptom shows up as status code 456 on Fronius Primo and Fronius Symo inverters. The code means the inverter's anti-islanding function is no longer running as it should. Anti-islanding is a grid-protection function that inverters must have. One manufacturer states that its anti-islanding protection meets the UL1741 and IEEE1547 requirements. Several inverters detect islanding actively by shifting the frequency. Monitoring the largest frequency change is described as an addition to islanding detection. The sources give no root cause or fix for this code. Use the manufacturer's status code documentation as the reference when the code appears.

<!-- review notes
- sentence 1: support check: partial - Code 456 meaning is stated, but the passages don't mention Primo or Symo models.
- sentence 2: support check: partial - The UL1741/IEEE1547 compliance claim is stated, but not that anti-islanding is a function inverters must have.
- sentence 4: support check: partial - Passages give no cause or fix (consistent), but nothing in them recommends the manufacturer's documentation as the reference.
-->
