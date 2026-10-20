---
id: symptom:substring-loss
type: Symptom
name: Bypassed substring
aliases:
- OC substrings
- open substrings
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-warm-substring
  note: A whole substring appears overheated in thermography. With a short-circuited bypass diode or substring
    the heating pattern can be irregular. Open-circuit substrings from cold solder joints in the junction
    box (failure modes B and C) show up in IRT, but failure mode A does not.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=23.r3
    h: dc57025a460a
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  attr: temperature_rise
  value:
    min: 5
    max: 10
    unit: unit:K
  conditions: Open-circuit substrings or module strings caused by unreliable junction box connections,
    compared with active strings during IRT inspection
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: observed_as
  target: meas:low-voc
  note: When a substring is lost, module Voc drops. In one batch, defective modules with unstable junction
    box connections delivered only 2/3 of normal voltage and power.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=23.r3
    h: dc57025a460a
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:high-string-reverse-voltage
  note: Night string test applying a small reverse current (3% to 5% of rated Isc). An unusually high
    reverse voltage points to an open or unconnected bypass diode or failure mode A. Night IR then shows
    the slightly warmed substring.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.2
    h: a48c6a4339a6
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
A bypassed or lost substring means one section of a module no longer delivers power. The current either flows through the bypass diode or the substring is cut off, and the module loses that share of its output. In infrared images, a whole substring looks warmer than its neighbours. Open-circuit substrings from bad junction box connections typically run 5 to 10 K hotter than active ones. In electrical data and IV traces, module open-circuit voltage is lower. Affected modules can show only about two thirds of normal voltage and power. Possible causes include a shorted or open bypass diode, cold solder joints or other junction box failures, and broken cell interconnections that block current in a cell string and force the diode to conduct. Snow or soiling covering part of the array can also cause substring mismatch. In that case the loss follows the weather: it starts abruptly after snowfall and fades as the snow melts or slides off. To find the cause, compare IR, EL, IV curves and a visual check of the junction box for burn marks. An open diode or failure mode A does not show in normal IR, so run a night string reverse-bias test and look for unusually high reverse voltage. Treat one confirmed junction box connection failure as a fleet risk. These defects tend to affect a whole production batch and can lead to arcing or fire, so test all modules.

<!-- review notes
- sentence 1: support check: partial - Substring power loss is stated (u12) but the general description of current flowing through diode or substring cut off, losing that share of output, is only loosely supported.
- sentence 5: support check: partial - Snow causing abrupt onset after snowfall and gradual melt/slide-off with partial-string mismatch is supported, but soiling is not covered and substring mismatch is only implied.
-->
