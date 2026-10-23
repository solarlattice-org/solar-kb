---
id: symptom:unbalanced-mppt-connection
type: Symptom
name: Unbalanced MPPT string connection
aliases:
- MPPT connection unbalance alarm
- String Mismatch
claims:
- claim_id: c1
  rel: observed_as
  target: meas:negative-string-current
  note: Seen before grid connection. It means the two strings on one MPPT have unbalanced voltages, for
    example because one string has more panels than the other.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=h267
    h: 563fa8a2d1c7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - The note supports negative string current before grid connection
    meaning unbalanced voltages between the two strings, but the signal wording about model_160 ''while
    strings unequal'' and ''flat'' details is beyond it; core is stated.'
- claim_id: c2
  rel: observed_as
  target: meas:flat-output-below-available-power
  note: Spreading strings unevenly across MPPTs (for example 3:1 instead of 3:2) is not recommended and
    may cause unnecessary power clipping.
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: sec=h65
    h: 0ba4b32276a8
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h90
    h: d0d015ba0da1
  - src: src:chint-cps-25kw-user-manual-rev-2-1
    loc: sec=h56
    h: a4b5e3fe61fa
  review: drafted
  review_note: 'review: partial - All three passages say an uneven split of strings across MPPTs (3:1
    rather than 3:2) is not recommended and may cause unnecessary power clipping, which supports the note;
    but the claim that this shows up as a flat plateau at…'
---
First open the AC and DC switches. Then check that each MPPT on each heatsink has PV strings connected to it. If the alarm comes back after the inverter has been running on the grid for a while, contact Sungrow service. If a string shows negative current before grid connection, the two strings on that MPPT have unbalanced voltages. A likely cause is that one string has more panels than the other. Compare the strings on the same MPPT. They should have the same module count, the same module type and the same tilt and azimuth. Mixing module brands or models on one MPPT may not damage the inverter, but it leads to poor system performance. Across MPPTs, the string counts should differ by no more than one. A larger imbalance can cause unnecessary power clipping, which shows up as flattened output at peak times. Huawei inverters report a related abnormal string connection alarm. In that case, check the strings for reverse or cross connection between MPPTs.

<!-- review notes
- sentence 6: support check: partial - Difference of at most one and unnecessary clipping are stated, but 'flattened output at peak times' is not stated in the passages, and the passages use 'not recommended/may' rather than 'can cause'.
- sentence 7: support check: partial - The Huawei alarm 413 'Abnormal PV String Connection' with suggestion to check reverse and cross connection is stated, but nothing says it is specifically related to MPPT unbalance.
- sentence 7: review: partial - The Huawei row confirms alarm 413 Abnormal PV String Connection, whose causes are strings not properly connected to the MPPT circuits, and its suggestion is to check for reverse and cross connection; the passage does not say the alarm is…
-->
