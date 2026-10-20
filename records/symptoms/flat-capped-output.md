---
id: symptom:flat-capped-output
type: Symptom
name: Flat capped output
claims:
- claim_id: c1
  rel: observed_as
  target: meas:flat-output-below-available-power
  note: 'Grid curtailment signature: output held at a flat or controlled level below what irradiance supports,
    while inverter and tracker availability may look normal.'
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: observed_as
  target: meas:export-below-available-power
  note: 'Curtailment: meter export limited below the reconstructed available plant power; compare with
    setpoints, active power limits and dispatch signals.'
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=front
    h: 874f05be8763
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: drafted
  review_note: 'support check: partial - Passages say curtailment limits export below available plant
    power and to compare with setpoints and dispatch, but they don''t tie meter export or a reconstructed
    available power to a flat capped output signature beyond that.'
- claim_id: c3
  rel: observed_as
  target: meas:daily-power-plateau
  note: 'Inverter clipping (saturation): power stays at the inverter AC maximum and does not rise further
    when irradiance or DC power increases, giving flat tops on daily power curves.'
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.2.3
    h: 426525e43b7d
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r2
    h: 0372516e81ca
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.4
    h: 69ccb977fc01
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Flat capped output means the plant or inverter power trace runs as a flat line during good sun and does not follow rising irradiance. When the flat top sits at the inverter AC rating on sunny days, it points to inverter clipping, where the array can supply more DC power than the inverter can deliver as AC. Clipping is often a planned design choice that buys extra morning and evening yield, so it is not always a fault. When the flat level sits below the inverter rating, or below the power the irradiance should support, it points to grid curtailment from operator dispatch, an interconnection limit, a plant controller command, a reaction to negative prices or a site export cap. During curtailment, inverter and tracker availability can look normal, so it is easy to log as underperformance by mistake. Check plant setpoints, inverter active power limits, dispatch records, meter output, battery charging behavior and curtailment flags before looking for equipment faults. Do not confuse this with an inverter voltage floor: clipping caps power, while voltage flooring is an MPPT limit caused by the DC voltage window.

<!-- review notes
- sentence 1: support check: partial - Flat or non-rising output at high irradiance is supported, but the passages don't say 'good sun' explicitly. They do say saturation occurs at high irradiance and that output doesn't follow rising irradiance.
- sentence 4: support check: partial - The listed curtailment causes and the flat output below available power are stated, but the passage doesn't contrast this with the inverter rating or say a flat level below the rating points to curtailment.
- sentence 6: support check: partial - The detection method lists the items to compare, but the passages don't say to check them before looking for equipment faults. The workflow sorts constrained intervals by cause, and u9 only warns against chasing false equipment problems.
-->
