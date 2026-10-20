---
id: fm:surge-protector-exhausted
type: FailureMode
name: Surge protector exhausted
aliases:
- Fault overvoltage protector
- DC SPD
- AC SPD
- surge arresters have tripped
claims:
- claim_id: c1
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h281
    h: 3b4b16a8ddf5
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r4
    h: f5dbb90220ad
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h198
    h: 3b4b16a8ddf5
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:inverter
  note: The inverter's built-in surge protection modules are replaced when needed. The CPS inverter raises
    warnings Warn0040 (DC SPD) and Warn0100 (AC SPD).
  cite:
  - src: src:doe-femp-om-small-pv
    loc: sec=h29
    h: ecaae89914de
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r4
    h: f5dbb90220ad
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c3
  rel: caused_by
  target: stressor:voltage-surge
  note: Eaton gives a significant surge event as the probable cause when the SPD shows its red indicator.
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: presents_as
  target: symptom:spd-indicator-red
  note: On CPS inverters a red indicator means the SPD module must be replaced. A green indicator points
    to a seating problem.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r4
    h: f5dbb90220ad
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: presents_as
  target: symptom:spd-audible-alarm
  cite:
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: detected_by
  target: method:visual-inspection
  note: Look at the SPD status indicator.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r4
    h: f5dbb90220ad
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=2.r4
    h: f5dbb90220ad
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=55.r4
    h: f5dbb90220ad
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: detected_by
  target: method:spd-alarm-contact-monitoring
  note: Dry contacts switch to alarm if a thermal protector or fuse inside the SPD opens or a phase loses
    power. Normally-closed wiring is recommended because it also detects a cut wire.
  cite:
  - src: src:siemens-siemens-im-surgeprotection-tps4
    loc: sec=h52
    h: 9fa81ff271b9
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: mitigated_by
  target: mit:spd-replacement
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r4
    h: f5dbb90220ad
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h282
    h: 99a29cc4279e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h199
    h: 99a29cc4279e
  - src: src:eaton-eaton-spd
    loc: tbl=7.r6
    h: 4f67694d74a3
  - src: src:eaton-eaton-spd
    loc: tbl=7.r8
    h: e5d6e169f09a
  - src: src:eaton-eaton-spd
    loc: tbl=7.r4
    h: 0296e9cdc4cc
  - src: src:doe-femp-om-small-pv
    loc: sec=h29
    h: ecaae89914de
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:spd-reseating
  note: Applies when the indicator is green or the arrester may not be inserted correctly.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r4
    h: f5dbb90220ad
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h282
    h: 99a29cc4279e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h199
    h: 99a29cc4279e
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Use this if replacing or reseating the module does not clear the warning.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=3.r2
    h: '176220009679'
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=31.r4
    h: f5dbb90220ad
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
An exhausted or tripped surge protection device has used up its protection, usually after a significant surge event, and no longer protects the inverter. The inverter raises an SPD warning, for example Warn0040 for the DC SPD or Warn0100 for the AC SPD on CPS inverters. SMA inverters show a fault overvoltage protector message. Check the SPD module by eye. A red indicator, sometimes with an audible alarm, means the SPD has been used up. The same warning can appear if the arrester is just not seated properly. A green indicator points to this. Replace any SPD module that shows red or has tripped. If the indicator is green, remove the module and seat it again in its socket. If the warning still does not clear, contact the manufacturer's service team. Some SPDs have dry alarm contacts that can report a failed unit remotely to a monitoring system.

<!-- review notes
- sentence 1: support check: partial - Tripped arresters and a significant surge event cause are stated, but 'no longer protects the inverter' is not stated.
-->

<!-- review workflow 2026-10-20: dropped as unsupported
- c4 caused_by stressor:installation-error: The SMA passage says the message appears when "surge arresters have tripped or one or more surge arresters are not inserted correctly": incorrect insertion is presented as a separate trigger of the same message, not as a cause of the arrester being exhausted, so the causal relation claimed is not stated (the note itself concedes "the same SMA message also appears").
-->
