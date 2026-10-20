---
id: symptom:mpp-shift
type: Symptom
name: Shifted maximum power point
aliases:
- MPP
claims:
- claim_id: c1
  rel: observed_as
  target: meas:temperature-derated-output
  note: When an overheating inverter reaches its maximum component temperature, it moves its operating
    point to lower power in steps. It returns to the optimal operating point once the components cool.
    This is a deliberate move away from the MPP, not a change in the array's own MPP.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=33.r5
    h: ed5c231ad047
  review: drafted
  review_note: 'support check: partial - Passages state stepwise power reduction at max component temperature,
    return on cooling, but not the signals (high irradiance, TmpSnk/TmpCab), nor the explicit ''not a
    change in the array''s MPP'' note.'
---
The maximum power point is the spot on a string's or array's current-voltage curve where current times voltage is highest. A shorted bypass diode keeps lowering the output of its own module. It also pushes the other modules in the same string off their maximum power point. Bypass diode problems can be found with IV curve signatures, infrared thermography, a visual check for burn marks and junction box checks, which show whether the diode is open or shorted. Do not confuse this with inverter overheating. In that case the inverter itself moves its operating point to lower power in steps, then returns to the optimal point once its components cool down. If the loss follows inverter temperature, suspect overheating. If it stays constant on one string, suspect a module or bypass diode fault. On inverters that offer it, a manual MPPT scan makes the inverter search its whole MPPT range again for the maximum power point.

<!-- review notes
- sentence 5: support check: partial - Passages describe overheating derating with temperature recovery and continuous loss from shorted bypass diodes, but give no diagnostic rule about constant loss on one string versus following inverter temperature.
-->
