---
id: symptom:low-battery-health
type: Symptom
name: Low battery state of health
aliases:
- SOH
- BatSOH70Warn
- Warning SOH < 70%
claims:
- claim_id: c1
  rel: observed_as
  target: meas:battery-soh-reading-low
  note: On Sunny Island the battery management reports SOH (display value 320.01 Soh) as usable capacity
    relative to nominal capacity. Warning W220 / event 9324 (BatSOH70Warn) is raised when SOH falls below
    the 70% threshold. The 70% figure is a warning threshold, not a measured loss.
  quote: Current battery capacity (SOH) is below 70%.
  cite:
  - src: src:sma-kb-event-number-9324-w220
    loc: sec=h1
    h: 7a32d7616ea9
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=143.r12
    h: 24e6e18fe368
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=53.r8
    h: 699991ef3802
  - src: src:sma-doc-278742
    loc: sec=h914
    h: cef6dae20c1d
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h328
    h: 8141f769b40c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
Sunny Island inverters raise warning W220 (event 9324) when the battery's current capacity, its state of health (SOH), drops below 70% of its nominal capacity. SOH is shown as display value 320.01 Soh. It is the usable capacity as a percentage of nominal capacity, and the inverter learns it over several charging cycles, starting from 100% at commissioning. A slow drop of a few percent per year or per 100 cycles is normal battery aging. A drop of several tens of percent within the first months after commissioning points to a possible error. Usable capacity can also shrink after frequent insufficient charging. The reported capacity is lowered automatically when battery temperature is below 68°F (20°C). The SOH estimate is only accurate to about ±15%, so an exact value needs a capacity measurement to DIN EN 60896, done by qualified staff such as the battery manufacturer's service. Check first that the warning is plausible. Compare Health (SOH) and Cycle on the Sunny Remote Control with expected values, confirm the nominal capacity (C10) is set correctly, and check the battery ambient temperature and battery management settings. If the low capacity is confirmed, contact the battery manufacturer and replace the battery if needed. SOH itself does not affect how the Sunny Island operates.

<!-- review notes
- sentence 4: support check: partial - Insufficient charging reducing capacity is stated, and capacity is adjusted downward below 68°F (20°C), but it says the 'current capacity' is adjusted, not explicitly the reported SOH.
- sentence 6: support check: partial - Passages cover plausibility check, Health/Cycle comparison, C10 nominal capacity, ambient temperature and battery management settings, but the Cycle comparison is of throughput and C10 check is tied to SOH above 100%, not specifically to this warning.
-->
