---
id: symptom:low-battery-temperature
type: Symptom
name: Low battery temperature
aliases:
- Battery undertemperature
- Low battery temperature warning
- Battery low temperature fault
- BatTmpLoWarn
claims:
- claim_id: c1
  rel: observed_as
  target: meas:battery-undertemperature-message
  note: On Sunny Island this shows as W211, a level 1 warning. When the external battery management reports
    it over SiCom, it shows as F924 or F926 (level 3 errors) or as W940 or W942 (level 1 warnings). F926
    and W942 refer to charge mode. SMA event 9313 reports a battery low temperature fault.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r9
    h: 6042b279a4bd
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r6
    h: d3559cba2236
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r8
    h: 21c1466beb86
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r7
    h: d499d43d67b1
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r9
    h: 4a366fe1c88b
  - src: src:sma-kb-event9313
    loc: sec=h1
    h: ebc977e1fc6b
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=53.r5
    h: b5f38cadf359
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:reduced-battery-charge-current
  note: On SMA Homestorage, temperature derating lowers the charging current step by step between 15°C
    and 0°C, and charging stops below 0°C. For lithium-ion batteries, the battery management can also
    limit charging power.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h985
    h: 32a04faf0161
  - src: src:sma-kb-stpx-x-3se-40-batterie-wird-mit-niedrigem-ladestrom-geladen
    loc: sec=h1
    h: 6712225021a3
  review: drafted
---
Low battery temperature appears in the Sunny Island event list as warning W211. When the external battery management reports it over SiCom, it appears as F924, F926, W940 or W942, and F926 and W942 apply to charge mode. Sunny Island gives this warning when a lead-acid battery falls below -10°C, or when a NiCd battery falls below -20°C. A cold battery is also charged more slowly. On SMA Homestorage, charging current is reduced between 15°C and 0°C, and charging stops below 0°C, so low charging power in cold weather may simply be temperature derating. The usual cause is a battery room that is too cold. First check that the battery's ambient temperature meets the battery manufacturer's requirements, then review the battery management settings. Check the temperature measurement path before assuming the battery is really cold. Lead-acid systems use a sensor connected only to the cluster master, while lithium-ion systems get the temperature from the external battery management. A wiring fault at the sensor is reported differently. A short circuit or broken cable raises its own sensor events and should be fixed by checking the sensor connection. If the low temperature fault remains, the installer should agree the next steps with the battery manufacturer.

<!-- review notes
- sentence 2: support check: partial - u20 states lead-acid below -10°C and NiCd below -20°C, but u14 only says below -10°C generally; the warning is not explicitly tied to W211, though the core is stated.
- sentence 4: support check: partial - Passages give the corrective measures (warm battery room, check ambient temperature requirements, battery management settings), but don't say it is the 'usual' cause or set an order of checks.
- sentence 5: support check: partial - Passages support the lead-acid sensor at master only and lithium-ion temperature from external battery management, but not the advice to check the measurement path before assuming the battery is cold.
- sentence 4: review: partial - The passages give the corrective steps (make sure the battery room is warm enough, check ambient temperature requirements, check battery management settings), but they don't say a cold room is the 'usual' cause or require that order.
-->
