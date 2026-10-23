---
id: symptom:pv-array-not-connected
type: Symptom
name: PV array not connected
aliases:
- Generator connection not carried out
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-warm-module
  note: One module appears warmer than the others; the module may be open circuited and not connected
    to the system, though it is normally fully functional. Check wiring.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=23.r1
    h: 05ebb35b256e
  review: drafted
---
The inverter reports event 9037 when the PV array disconnect switches have not connected the PV generator to it. Before commissioning, make sure there is a way to disconnect the inverter from the PV array and that every conductor is connected correctly. If the inverter does not run even though production conditions are good, check the inverter display or the monitoring data log for fault codes. At module level, an infrared image in which one module is warmer than the others can mean that module is open circuited and not connected to the system, even though the module itself is usually fine. In that case, check the wiring first.

<!-- review notes
- sentence 5: support check: partial - Remarks say check wiring, but 'first' priority ordering is not stated.
-->
