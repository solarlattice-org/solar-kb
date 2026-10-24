---
id: fm:meter-ct-ratio-misconfiguration
type: FailureMode
name: Meter CT ratio misconfiguration
aliases:
- incorrect CT ratio
- meter ratio issue
- Set Meter CT
- wrong CT primary setting
- Wrong Rating
claims:
- claim_id: c1
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:kb-solis-44002440996-acrel-dtsd1352-3ph-meter-ct-ratio
    loc: sec=h1
    h: 0d66e6ffa27f
  - src: src:kb-solis-44002271824-adjust-the-ct-ratio-of-an-acrel-dtsd-1352-meter
    loc: sec=h1
    h: 1203cf3b09d1
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h73
    h: bac2703ea970
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h63
    h: bac2703ea970
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: sec=5.5.2
    h: cccf40d33170
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:current-sensor
  note: The ratio entered must match the installed current transformer rating, e.g. 150A:5A or 300/5A.
  cite:
  - src: src:kb-solis-44002440996-acrel-dtsd1352-3ph-meter-ct-ratio
    loc: sec=h1
    h: 0d66e6ffa27f
  - src: src:kb-solis-44002848827-epm-configuration-and-validation-guide
    loc: sec=h12
    h: e808366309c0
  review: drafted
  review_note: 'support check: partial - Passages say the ratio must match the installed CT (e.g. 300/5A,
    150A:5A), but do not say misconfiguration affects the current sensor component itself.'
- claim_id: c3
  rel: presents_as
  target: symptom:unrealistic-meter-values
  note: Meter or point-of-connection readings look very low or very high compared with the real loads.
  cite:
  - src: src:kb-solis-44002440996-acrel-dtsd1352-3ph-meter-ct-ratio
    loc: sec=h1
    h: 0d66e6ffa27f
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h73
    h: bac2703ea970
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h63
    h: bac2703ea970
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: sec=5.5.2
    h: cccf40d33170
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:meter-configuration-error
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-06-home-hub-advanced-battery-concepts
    loc: sec=h18
    h: a0f0c0785d9a
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h73
    h: bac2703ea970
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h63
    h: bac2703ea970
  review: drafted
  review_note: 'support check: partial - Passages list wrong meter configuration info and wrong CT rating
    as common problems, but don''t explicitly state CT ratio misconfiguration is caused by it.'
- claim_id: c5
  rel: caused_by
  target: stressor:installation-error
  note: Fitting CTs other than the supplied ones without changing the default ratio on the meter.
  cite:
  - src: src:kb-solis-44002271824-adjust-the-ct-ratio-of-an-acrel-dtsd-1352-meter
    loc: sec=h1
    h: 1203cf3b09d1
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h245
    h: 79258fcfab76
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: sec=h249
    h: ef5f70060277
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:meter-configuration-check
  note: Check the CT and VT ratio on the meter, and make sure the monitoring platform uses the same ratio
    as the meter.
  cite:
  - src: src:kb-solis-44002440996-acrel-dtsd1352-3ph-meter-ct-ratio
    loc: sec=h1
    h: 0d66e6ffa27f
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h73
    h: bac2703ea970
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h63
    h: bac2703ea970
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: sec=5.5.2
    h: cccf40d33170
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:meter-configuration-correction
  note: Set the ratio to primary current divided by secondary current, for example 30 for 150A:5A CTs,
    then save it.
  cite:
  - src: src:kb-solis-44002440996-acrel-dtsd1352-3ph-meter-ct-ratio
    loc: sec=h1
    h: 0d66e6ffa27f
  - src: src:kb-solis-44002271824-adjust-the-ct-ratio-of-an-acrel-dtsd-1352-meter
    loc: sec=h1
    h: 1203cf3b09d1
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=6.4.9
    h: 4cdd77634b51
  - src: src:kb-solis-44002848827-epm-configuration-and-validation-guide
    loc: sec=h12
    h: e808366309c0
  review: drafted
---
This fault means the current transformer ratio stored in the energy meter does not match the CTs actually installed. It often happens when the installer fits their own CTs but leaves the meter's default ratio in place. The usual sign is meter or grid-connection readings that are much too low or too high for the real loads. To confirm it, read the CT and VT ratio set in the meter. Check that any monitoring platform uses the same ratio as the meter. The correct ratio is the CT primary current divided by its secondary current. For example, 150A:5A CTs need a ratio of 30. Enter the correct ratio through the meter's setup menu and save it. On systems with a meter, set the ratio on the meter itself, not on the inverter. If the current still reads only a small fraction of what you expect, check whether the CT shorting tabs are still engaged.

<!-- review notes
- sentence 1: support check: partial - Passages say the ratio entered must match installed CT spec and wrong information is a common problem, but don't define a specific 'fault' this way.
- sentence 2: support check: partial - Passages say own CTs require manually setting the ratio from the default, but nothing says this often happens or that installers leave the default.
-->
