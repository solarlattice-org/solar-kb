---
id: method:fuse-check
type: DetectionMethod
name: Fuse inspection
claims:
- claim_id: c1
  rel: produces
  target: meas:open-fuse
  note: A multimeter check of string fuses on the fuse boards shows one or more open fuses when the inverter
    reports a string current error (W017). For a grounding fuse fault, the removed negative grounding
    fuse is checked to see whether it has blown.
  cite:
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=51.r4
    h: bfc22e660bc0
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=37.r5
    h: b91e58f0f23d
  - src: src:abb-fimer-uno-dm-6-0-tl-plus-us-q-product-manual-revb
    loc: tbl=35.r5
    h: b91e58f0f23d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
Fuse inspection means checking a protection fuse in the inverter to see whether it has opened or blown, then replacing it if it has. For string protection fuses, use a multimeter to check each fuse on the fuse boards when the inverter reports a string current error, because damaged fuses can cause this alarm. If a string fuse is open, replace it and confirm that the string input current does not exceed the fuse rating, for example where strings have been paralleled outside the inverter. If no string fuse is damaged and the alarm stays on, check whether the configured settings match the strings actually connected. For a grounding fuse fault, wait until the capacitor has fully discharged, remove the negative grounding fuse and check whether it has blown. If it has, check the transformer neutral point connections and grounding. A sudden strong residual current from a ground fault destroys the grounding fuse, so find and clear the ground fault before you inspect or replace the fuse. Before you start, disconnect the inverter on the AC and DC sides. Opening the AC and DC switches can still leave DC input voltage on the fuse board, so wear suitable PPE and wait at least 30 minutes for stored energy to discharge.

<!-- review notes
- sentence 6: support check: partial - Passages say intense residual current destroys the fuse and that the ground fault is eliminated before inspecting/replacing it, but 'clear the fault before inspecting' is mostly implied by the sequence; the procedure does not say it as a required precaution beyond that.
- sentence 7: support check: partial - Disconnecting AC and DC, PPE, residual DC voltage on the fuse board and 30-minute wait are in the passages, but they come from different procedures (grounding fault vs string fuse replacement) and are merged.
-->
