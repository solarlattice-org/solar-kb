---
id: symptom:remote-power-limit
type: Symptom
name: Remote power limit
aliases:
- Active Power Limit
- Maximum Active Power Limit
- Solar Real Power Limit
- Solar Power Limit
- Curtailment
claims:
- claim_id: c1
  rel: observed_as
  target: meas:flat-output-below-available-power
  note: An output cap, whether from inverter saturation or curtailment, holds power at a fixed maximum.
    In the daily power trend this shows up as a flat top, and the output stops following irradiance.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.2.3
    h: 426525e43b7d
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r2
    h: 0372516e81ca
  review: drafted
  review_note: 'support check: partial - Passage describes flat plateaus at daily power peaks from saturation/curtailment,
    but doesn''t mention remote power limits specifically or the POAI rising signal.'
---
A remote power limit is a cap on real power sent to the plant from outside. It is given as a fraction of nameplate maximum real power, in per-unit. Plant or solar controllers can also calculate a real power limit for the solar assets and send it to them in watts. In monitoring data, the daily power curve has a flat top. Output stays fixed and does not rise with irradiance. Check first for an active power limit command or setpoint in the controller before you look for a hardware fault. Leave limited intervals out of any performance analysis, because the output during those intervals does not reflect the weather. Where a battery is involved, an alert can flag that the requested real power is above nominal power or above the operator limits. That alert means the setpoint was capped and could not be fully met.

<!-- review notes
- sentence 1: support check: partial - Passage gives a power limit as a percentage of nameplate max real power in pu, but doesn't say it is a cap sent from outside the plant.
- sentence 4: support check: partial - Passage supports excluding saturated/limited data from modeling, but nothing about checking controller setpoints before hardware faults.
-->
