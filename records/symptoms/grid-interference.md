---
id: symptom:grid-interference
type: Symptom
name: Grid interference
aliases:
- GRID-INTF01/02
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Solis and CSI inverters report this condition with the alarm message GRID-INTF01/02, described
    as grid interference.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r12
    h: 02f61ff2da17
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r12
    h: 02f61ff2da17
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r7
    h: 08b308fe3d39
  review: drafted
  review_note: 'support check: partial - Alarm text GRID-INTF01/02 and ''Grid interference'' are stated,
    but the passages don''t name Solis/CSI brands or say it is observed on the inverter fault code display.'
---
Grid interference shows up as an inverter alarm: Solis and CSI string inverters display it as GRID-INTF01 or GRID-INTF02. The first step is to restart the inverter and see whether the alarm clears. If the alarm does not clear after a restart, the manufacturer says to replace the power board, which points to a fault inside the inverter hardware.

<!-- review notes
- sentence 1: support check: partial - The alarm message and description are present, but the passages don't identify Solis/CSI string inverters or the display.
- sentence 3: support check: partial - Change power board as step 2 is stated, but the passages don't say it's conditional on the alarm persisting or that it indicates an internal hardware fault.
-->
