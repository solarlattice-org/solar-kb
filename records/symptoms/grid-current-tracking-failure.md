---
id: symptom:grid-current-tracking-failure
type: Symptom
name: Grid current tracking failure
aliases:
- IGFOL-F
- Grid current tracking fail
- Grid current tracking is abnormal
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Solis and CSI inverters show the alarm message IGFOL-F for a grid current tracking failure.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r11
    h: faefc527751c
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r11
    h: faefc527751c
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r11
    h: b1d7bf4d96b3
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=26.r11
    h: faefc527751c
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=13.r8
    h: '23e710312339'
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=14.r8
    h: '23e710312339'
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r9
    h: 7a4cbb7ed3ad
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=12.r16
    h: 94e94c8bc64c
  review: drafted
  review_note: 'support check: partial - Passages give IGFOL-F as grid current tracking failure but never
    name Solis or CSI brands or the display channel.'
---
A grid current tracking failure shows up on the inverter as the alarm IGFOL-F. It is documented for Solis hybrid and string inverters and for CSI inverters. The alarm means the inverter cannot track the grid current properly. First check whether the utility grid itself is abnormal. Next, confirm the AC cable is connected properly and inspect the installation. Then restart the system and see if the fault comes back. If the alarm persists after a restart and the grid and wiring check out, contact the installer or replace the inverter.

<!-- review notes
- sentence 1: support check: partial - IGFOL-F as the alarm is stated, but the passages do not mention Solis hybrid/string or CSI product families.
- sentence 6: support check: partial - Contacting the installer and replacing the inverter appear as solutions, but the passages do not state the conditional sequence 'if it persists after restart and grid and wiring check out'.
-->
