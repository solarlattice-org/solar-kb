---
id: symptom:warm-cells-near-frame
type: Symptom
name: Warm cells near frame
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-warm-cells-bottom-frame
  note: Seen in IR thermography of operating modules in sunlight near maximum power point; affected cells
    near the lower frame run warmer than upper and middle cells. Pattern is not detectable at open circuit,
    and is strongest for modules near the negative (or one) pole of the string.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=14.r4
    h: 7f105cf3f7e6
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=36
    h: 78e443f42ff2
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.2
    h: 9b2ddc8cc5ec
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h61
    h: e78071080be3
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ir-patchwork-pattern
  note: Alternative PID-s IR signature in which warm cells are scattered across the module in a patchwork.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.2
    h: 9b2ddc8cc5ec
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=h61
    h: e78071080be3
  review: drafted
  review_note: 'support check: partial - Patchwork patterns are named as a PID-s IRT pattern, but ''warm
    cells scattered across the module'' is not described.'
- claim_id: c3
  rel: observed_as
  target: meas:ir-cold-area
  note: With current injected in the dark (lab or night-time string test), PID-s affected cells appear
    cooler than unaffected ones, the reverse of the sunlight pattern.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.2
    h: 9b2ddc8cc5ec
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: observed_as
  target: meas:el-dim-cell
  note: PID-s affected cells near the module frame show reduced luminescence, most visible at low current
    bias around one tenth of rated current.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.3.2
    h: 9b2ddc8cc5ec
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:fill-factor-reduction
  note: Module power and fill factor drop; low-light performance is hit harder than at STC.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=14.r4
    h: 7f105cf3f7e6
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
- claim_id: c6
  rel: observed_as
  target: meas:low-voc
  note: PID-s lowers shunt resistance, fill factor and Voc on the IV curve.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=15.r1
    h: 6e2cec50e730
  review: drafted
---
In IR images of modules running in sunlight, single cells along the bottom frame look warmer than the cells in the upper and middle parts of the module. This pattern, or a patchwork of warm cells, strongly suggests potential induced degradation of the shunting type (PID-s), especially when the affected modules sit near the negative pole of the string. Take the IR images under clear sky with the system running near maximum power, because the pattern disappears at open circuit. If you inject current at night or in the dark, the affected cells look cooler instead of warmer, and EL images show them darker, most clearly at low current bias. Confirm with IV curves: PID-s lowers fill factor, Voc and shunt resistance, and the loss shows up more in low light than at STC. This is different from one clearly hot cell, which points to shading, a defective cell or delamination, and from a partly warm cell, which points to a broken cell or a failed interconnect. Possible remedies include changing the array grounding conditions or recovering the modules with reverse voltage.

<!-- review notes
- sentence 4: support check: partial - Cooler IRT and darker EL in the dark are stated, but the low current bias clarity is stated for EL generally, not specifically tied to the injected-current test; the 1/10 bias is mentioned only in u18.
-->
