---
id: comp:single-axis-tracker
type: Component
name: Single-axis tracker
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Extra annual production loss from wind stow when gust-driven tracker response is modelled,
    compared with models that use hourly wind data alone (2026 kWh Analytics Solar Risk Assessment)
  quote: annual production losses can increase by up to 4% compared with models that rely on hourly wind
    data alone
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: drafted
---
A single-axis tracker turns PV modules about one axis of rotation. Each tracker type has its own performance expectations and O&M costs. A tracker row relies on a torque tube, slew drive, bearings, dampers and linked mechanical segments to hold all modules in one common plane. An actuator or control group, called a motor block, can drive several rows to the same angle. Routine O&M includes checking the motor and controller connections and grounding braids, calibrating the anemometer, inspecting the inclinometer and limit switch, and lubricating the slew gear, screw jack and bearings. Tracker twist is when one section of a row sits at a different tilt from the rest of the row. It causes cosine loss, row-to-row shading and electrical mismatch. On rolling ground, terrain undulation upsets the backtracking geometry. Rows can shade each other, or be driven further off sun than needed, even while they follow their commands. Wind stow moves rows to a protective angle when measured wind goes above the controller threshold. This protects the structure but cuts irradiance capture until the rows return to tracking. Wind damage linked to torsional instability or galloping, combined with badly designed or badly torqued hardware, has occurred at gust speeds below the design wind speed. Before a storm, do a torque audit on fasteners and stow the trackers as the manufacturer specifies. Tracker performance availability counts as downtime any period when the tilt deviates from the set point by more than the accepted angle.

<!-- review notes
- sentence 1: support check: partial - Passage says single-axis trackers rotate on a single axis and each sub-category has differing performance expectations and O&M costs, but it doesn't say 'turns PV modules' explicitly; mostly supported.
-->
