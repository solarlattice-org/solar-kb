---
id: state:float-charge
type: OperatingState
name: Float charge
aliases:
- float charging
- Maintenance charge
- Float
- float charging process
category: Storage
product: prod:sma-sunny-island-us
claims:
- claim_id: c1
  rel: subclass_of
  target: state:battery-charging
  note: Float charge is a reduced-voltage constant-voltage charging phase that follows the absorption
    phase.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h640
    h: 1238d4052c9b
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5
    h: 165b6683fb63
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: part_of
  target: concept:battery-charging-stages
  scope:
    products:
    - prod:sma-sunny-island-us
  note: Final level of the Sunny Island IUoU charge control, entered after the constant voltage (absorption)
    phase.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=13.5
    h: 165b6683fb63
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
Float charge keeps a battery fully charged without overcharging it and without the early aging that overcharging causes. The battery inverter enters float charge once the boost, full or equalization charge with its constant voltage phase is finished. It then holds a much lower charging voltage, which battery management reaches by stepping the voltage down to the float setpoint. Float charge ends when the summed discharges reach 30% of nominal capacity or the state of charge falls below 70%. The unit then goes back to the constant current phase, or to silent mode if it is connected to the utility grid. Bringing a battery all the way to 100% on float charge takes several days, so this phase matters more for battery-backup systems than for stand-alone grids. The active charging process parameter BatChrgOp, or Mode on the display, shows Float while this phase is running. The switch into float charge is logged as event E203 or as status message 9319. If float charge starts before the generator cutoff limit is reached, the generator request is withdrawn.

<!-- review notes
- sentence 3: support check: partial - Passages say float ends at 30% discharged or SOC under 70% and switches to the constant current phase or optionally silent mode, but the 'goes back to constant current' is stated as switching; silent mode is only 'can also' on grid connection, and mostly consistent; minor wording on 'reach 30%' vs 'more than'.
-->
