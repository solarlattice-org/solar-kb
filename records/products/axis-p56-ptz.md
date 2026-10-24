---
id: prod:axis-p56-ptz
type: Product
name: AXIS P56 PTZ network cameras
aliases:
- P5654-E
- P5655-E
- AXIS P56 Series
- AXIS P5654-E
- AXIS P5655-E
category: Security
make: axis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:axis
  cite:
  - src: src:eq-equip-cameras-axis-axis-2021-q4-product-comparison
    loc: tbl=21.r16
    h: 3a0463306da3
  - src: src:eq-equip-cameras-axis-axis-p5654-e-ptz-user-manual
    loc: sec=h23
    h: 2c2a6368be46
  review: drafted
  review_note: 'support check: partial - Passages show P56 series models and P5654-E camera, but nothing
    states Axis Communications as maker explicitly (only the AXIS brand name).'
- claim_id: c2
  rel: implements
  target: func:ptz-control
  note: Event conditions include PTZ malfunctioning, PTZ movement, preset position reached and PTZ ready
    (P5654-E cut sheet).
  cite:
  - src: src:eq-equip-cameras-axis-axis-p5654-e-ptz-cut-sheet
    loc: tbl=1.r22
    h: dc8c0bcd830e
  review: drafted
- claim_id: c3
  rel: certified_to
  target: std:en-62368-1
  note: Listed as IEC/EN/UL 62368-1 on the P5655-E cut sheet.
  cite:
  - src: src:eq-equip-cameras-axis-axis-p5655-e-ptz-cut-sheet
    loc: sec=h3
    h: 3e0265d02345
  review: drafted
  review_note: 'support check: partial - The P5655-E lists IEC/EN/UL 62368-1, but this covers only the
    P5655-E, not clearly the whole P56 family, and ''certified'' is not stated.'
- claim_id: c4
  rel: certified_to
  target: std:iec-60950-22
  note: Listed as IEC/EN/UL 60950-22 on the P5655-E cut sheet.
  cite:
  - src: src:eq-equip-cameras-axis-axis-p5655-e-ptz-cut-sheet
    loc: sec=h3
    h: 3e0265d02345
  review: drafted
  review_note: 'support check: partial - IEC/EN/UL 60950-22 is listed for the P5655-E only, and ''certified''
    is not stated.'
- claim_id: c5
  rel: certified_to
  target: std:is-13252
  note: Listed on the P5655-E cut sheet.
  cite:
  - src: src:eq-equip-cameras-axis-axis-p5655-e-ptz-cut-sheet
    loc: sec=h3
    h: 3e0265d02345
  review: drafted
  review_note: 'support check: partial - IS 13252 is listed for the P5655-E only, and ''certified'' is
    not stated.'
---
The AXIS P56 Series is a family of outdoor PTZ network cameras from Axis, and it includes the P5654-E and P5655-E models. Both models carry IP66 and NEMA 4X outdoor approvals, support day and night operation and have Lightfinder 2.0. The P5654-E runs on PoE Class 4 only. The P5655-E can be powered by PoE Class 4, by AC or by DC. According to the comparison table, the P5655-E has four configurable input/output ports and the P5654-E has none. The P5654-E can raise events from pan-tilt-zoom states such as a PTZ malfunction or reaching a preset position, and it can record video to an SD card or to network storage. The P5655-E cut sheet lists IEC/EN/UL 62368-1, IEC/EN/UL 60950-22 and IS 13252. When troubleshooting, first check the firmware version from the help menu on the camera's webpage, because a newer version may fix the problem.

<!-- review notes
- sentence 1: support check: partial - The P56 Series includes P5654-E and P5655-E, but 'outdoor PTZ' is only partly shown (IP66/NEMA is not in these passages; the P5655-E is called a PTZ camera, the P5654-E only a network camera).
- sentence 4: support check: partial - The table shows 4 ports for P5655-E and '-' for P5654-E, but 'configurable' is only in a different passage, and '-' is read as none.
-->
