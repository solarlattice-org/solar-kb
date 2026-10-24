---
id: symptom:battery-charge-capped
type: Symptom
name: Battery charge capped below full
aliases:
- Does not charge to 100%
- Limited to a maximum charge level of 75% (SOC)
- Self-consumption range cannot be set above 75%
- SOC holds at 99%
claims:
- claim_id: c1
  rel: observed_as
  target: meas:soc-below-full-after-full-charge
  note: The displayed battery SOC stays under 100% even though the full-charge phase has finished. The
    SMA documents say loads drew so much power before the full charge ended that the battery could not
    reach 100%.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h979
    h: 2a543f30380c
  - src: src:sma-doc-259761
    loc: sec=h850
    h: ee387738d66f
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: sec=h192
    h: 81126f37319b
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h592
    h: 1c911f608962
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:full-charge-status-event
  note: SMA event 9321 or E205 marks the change to full charge. Use it to confirm that a full charge was
    actually started before reading a capped SOC as abnormal.
  cite:
  - src: src:sma-doc-278742
    loc: tbl=76.r12
    h: 17df887c13dc
  - src: src:sma-doc-259761
    loc: tbl=72.r12
    h: 17df887c13dc
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=38.r2
    h: bfc8cc968771
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=133.r4
    h: 71f3d966459d
  review: drafted
  review_note: 'support check: partial - Events 9321 and E205 mark the change to full charge, but the
    passages do not say to use them to confirm a full charge before judging a capped SOC.'
- claim_id: c3
  rel: observed_as
  target: meas:max-charge-soc-setpoint-reached
  note: Charging stops at the configured maximum or cut-off SOC, or at a time-slot charge SOC. Generac's
    MaxSoCAbs can be set from 10 to 100% and defaults to 100%.
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=20.r2
    h: 8ec93b949f11
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=19.r6
    h: 26535068e24d
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=21.r3
    h: 016b064975eb
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h294
    h: fda63069986b
  review: drafted
---
The battery stops charging, or reports its state of charge, below full even when a full charge seems to have finished. On SMA Sunny Island systems, look in the event log for the change to full charge. If SOC is still below 100% afterwards, the loads may have drawn too much power before the full charge ended. For that case, set a longer full charge time, also called the absorption period. Check the charge limit settings first. A maximum or cut-off charge SOC, or a time-slot charge SOC, set below 100% makes the battery stop charging at that value. On the Sunny Boy Storage SBS2.5-1VL-10, older firmware does not allow the self-consumption range above 75%. Updating to firmware 3.11.10.R or later sets it to 90%. Seasonal self-consumption ranges also change automatically how much of the battery capacity is used through the year. Incorrect battery parameters can also be the cause, such as the battery type, the nominal capacity or the full and equalization charge settings, so compare them with the battery manufacturer's recommendations. The SOC shown is an estimate from ampere-hour counting plus voltage recalibration. The goal of a full charge is a state of charge of at least 95%, not exactly 100%.

<!-- review notes
- sentence 1: support check: partial - SOC below 100% after full charge is stated, but the passages don't say the battery stops charging below full.
- sentence 2: support check: partial - Event codes and the high-load explanation are in the passages, but not the instruction to check the event log for the change to full charge.
- sentence 4: support check: partial - Max/cut-off and time-slot SOC stopping charging are stated, but not the advice to check them first or that a value below 100% is the cause of a capped SOC.
- sentence 7: support check: partial - u32 lists BatTyp, BatCpyNom, full and equalization charge parameters to check, and other passages say to set them per manufacturer recommendations, but the passages don't link the manufacturer comparison to this symptom.
- sentence 8: support check: partial - The passages state the SOC method (Ah counting plus voltage recalibration) and the 95% minimum goal, but not 'estimate' or 'not exactly 100%'.
-->
