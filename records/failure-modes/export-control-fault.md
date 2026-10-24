---
id: fm:export-control-fault
type: FailureMode
name: Export limitation control fault
aliases:
- zero export instability
- unsuitable energy meter
- fluctuating control commands
- no data from feed-in meter
- active power limitation deactivated
- Backflow Control
- active power limitation
claims:
- claim_id: c1
  rel: presents_as
  target: symptom:export-limit-exceeded
  note: Plant stays at full power and exports to the grid, or the monitoring status bar turns red above
    the export limit. A brief red bar after a sudden load increase is normal.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h60
    h: 23ee56cf49ec
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h57
    h: d6e8f90be636
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: presents_as
  target: symptom:zero-feed-in-reading
  note: The S0 feed-in meter reports 0 W for 24 hours, and power limitation cannot work if the meter is
    faulty.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h475
    h: b26580197ffc
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:unrealistic-meter-values
  note: Point of connection measurements on the control status page are very low or very high.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h63
    h: bac2703ea970
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:control-fallback-operation
  note: Each inverter holds its output at the fallback set point after the meter link is lost or the limit
    cannot be reached. A red status bar is one trigger.
  cite:
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h35
    h: a2fa68991134
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h57
    h: d6e8f90be636
  review: drafted
- claim_id: c5
  rel: caused_by
  target: fm:meter-ct-ratio-misconfiguration
  note: If the CT or VT settings are wrong, the meter does not read the real power flowing to the grid.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h60
    h: 23ee56cf49ec
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h63
    h: bac2703ea970
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h38
    h: 8034e54fab20
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: caused_by
  target: fm:energy-meter-installation-error
  note: The meter must sit at the point of connection. Installing it anywhere else causes control failures.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h38
    h: 8034e54fab20
  review: drafted
- claim_id: c7
  rel: caused_by
  target: fm:energy-meter-failure
  note: A faulty feed-in meter, or lost communication with the meter, stops normal limitation.
  cite:
  - src: src:sma-doc-246498
    loc: sec=h475
    h: b26580197ffc
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h35
    h: a2fa68991134
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:meter-configuration-error
  note: The meter's reference system does not match the generator reference system, or generation mode
    is not enabled on an M2M meter.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h60
    h: 23ee56cf49ec
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h53
    h: 21c81091eb99
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:inverter-settings
  note: The export limitation flag is not switched on, or the configuration was not saved and applied.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h60
    h: 23ee56cf49ec
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h53
    h: 21c81091eb99
  review: drafted
- claim_id: c10
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sma-doc-246498
    loc: sec=h475
    h: b26580197ffc
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h38
    h: 8034e54fab20
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c11
  rel: affects
  target: comp:inverter
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h57
    h: d6e8f90be636
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h35
    h: a2fa68991134
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:export-control-monitoring
  note: Compare exported, generated and consumed power. Check the colored status bar and each inverter's
    state flags and derating set point.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h57
    h: d6e8f90be636
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:inverter-settings-review
  note: Confirm the export limitation flag, the meter CT/VT settings and the reference system.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h60
    h: 23ee56cf49ec
  review: drafted
  review_note: 'support check: partial - u11 says to check CT/VT, reference system and export flag, but
    doesn''t call it an inverter settings review method.'
- claim_id: c14
  rel: mitigated_by
  target: mit:meter-configuration-correction
  note: Set the correct CT and VT ratios, align the reference system, and enable generation mode on M2M
    meters.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h60
    h: 23ee56cf49ec
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h63
    h: bac2703ea970
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h38
    h: 8034e54fab20
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: Stop the control, adjust its parameters, enable the export limitation flag and save the settings.
  cite:
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h57
    h: d6e8f90be636
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h53
    h: 21c81091eb99
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:communication-fallback-configuration
  note: Enable a fallback plan so the inverters hold a safe set point. Do not set the guard band to 0%
    when fallback is enabled.
  cite:
  - src: src:abb-fimer-pvm-tl-us-energy-policy-app-note-reva
    loc: sec=h35
    h: a2fa68991134
  - src: src:abb-fimer-export-limitation-app-note-revd
    loc: sec=h53
    h: 21c81091eb99
  review: drafted
---
Export limitation control uses a site meter to hold the power fed to the grid at a set point just below an export limit. This fault means the control is not holding that limit. Typical signs are a plant that runs at full power and exports to the grid, a red status bar above the export limit, or meter readings that look far too low or too high. A feed-in meter that reports zero watts for a long time may be faulty, and in that case limitation cannot work. Common causes are wrong CT or VT settings on the meter, a meter installed away from the point of connection, a reference system that does not match the generator reference, or the export limitation flag left off. To confirm, use the control status page to check exported, generated and consumed power and the state flags of each inverter. Then review the meter and limitation settings. Fix the meter ratios and reference system, enable and save the limitation, and set up a fallback plan so the inverters hold a safe output if the meter link is lost.

<!-- review notes
- sentence 1: support check: partial - Passages state control limits export below a limit via a set point, but no mention of a site meter in u2/u9/u4 and the fault meaning is inferred.
- sentence 1: review: partial - The passages describe holding export at a set point below the export limit, but none of the cited passages mention a site meter, and the meaning of the fault is only inferred.
-->
