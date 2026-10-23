---
id: symptom:battery-overvoltage
type: Symptom
name: Battery overvoltage
aliases:
- OV-Vbatt-H
- BatVtgHiWarn
- XA02DcHiVolt
- Battery overvoltage hardware fault
- Battery overvoltage warning
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'Battery or hybrid inverters report battery overvoltage as a warning or error code. Examples:
    SMA W210 BatVtgHiWarn and F208/W209; Solis OV-Vbatt-H, which the Solis manuals pair with OV-BUS-H
    under code 1051.'
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=53.r4
    h: e04a9cacc1e2
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r14
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=18.r15
    h: 0e5e55559815
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r6
    h: 5fd46c8d9e47
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r7
    h: 736a37a25fc3
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r11
    h: 686e06868ba3
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=28.r15
    h: 967a5dcdb11c
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r11
    h: 686e06868ba3
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r8
    h: 9c16b8c7869e
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:bms-error-message
  note: SMA Sunny Island units relay a battery overvoltage reported by the external battery management
    system over SiCom (F921 error, W937 warning).
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=82.r8
    h: abb8e139c3c0
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r4
    h: 81514a4bc426
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r3
    h: 89527f8af382
  review: drafted
---
Battery overvoltage is reported by the battery or hybrid inverter as a warning or error code when the battery voltage is too high, sometimes only for a short time. On SMA Sunny Island units it shows as warning W210 (BatVtgHiWarn) or as F208 and W209 battery overvoltage errors. If the code arrives over SiCom (F921 or W937), the external battery management system detected the overvoltage, so fix the cause there using the battery manufacturer's documentation. On SMA W210, the corrective measure refers to the country data set configured for stand-alone grid operation, so check that setting. Solis hybrid inverters report a hardware-level battery overvoltage as OV-Vbatt-H. For OV-Vbatt-H, first check whether the battery breaker or fuses in the battery input circuit have tripped, then check the battery for damage, and restart the inverter.

<!-- review notes
- sentence 4: support check: partial - The corrective measure fragment mentions the country data set for stand-alone grid operation, but the text is truncated and does not say to check that setting.
- sentence 5: support check: partial - OV-Vbatt-H is a battery overvoltage hardware failure/fault, but the passages don't name hybrid inverters specifically; Solis is implied by the message names.
- sentence 6: support check: partial - The passages give breaker/fuse check, battery damage check and restart, but the order is partly from different rows and restart appears only in the u8/u11 rows, not alongside the damage check.
- sentence 4: review: partial - The W210 corrective-measure text is cut off and mentions only the country data set for stand-alone grid operation, so the instruction to check that setting is inferred rather than stated.
-->
