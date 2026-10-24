---
id: func:string-monitoring
type: Function
name: String monitoring
aliases:
- string failure detection
- string current monitoring
- string performance alerts
- PV string fault detection
- PV string current monitoring
- String monitor
- PV string monitoring
category: Monitoring
function_kind: monitoring
claims:
- claim_id: c1
  attr: default_value
  value:
    nominal: 0.8
    unit: unit:UNITLESS
  conditions: AlsoEnergy LocusNOC String Performance Ratio, relative to the highest-performing string
    of the same component
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  attr: setting_range
  value:
    min: 0
    max: 1
    unit: unit:UNITLESS
  conditions: AlsoEnergy LocusNOC String Performance Ratio
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  attr: default_value
  value:
    nominal: 2
    unit: unit:HR
  conditions: AlsoEnergy LocusNOC String Performance Alert time threshold; only daylight hours counted
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c4
  attr: setting_range
  value:
    min: 0.25
    max: 168
    unit: unit:HR
  conditions: AlsoEnergy LocusNOC String Performance Alert time threshold
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  review: drafted
- claim_id: c5
  attr: default_value
  value:
    nominal: 2
    unit: unit:A
  conditions: AlsoEnergy LocusNOC DC current threshold that the highest-performing string must exceed
    before any alert is generated
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  review: drafted
- claim_id: c6
  attr: default_value
  value:
    nominal: 0.5
    unit: unit:HR
  conditions: AlsoEnergy LocusNOC sunrise/sunset buffer during which alert conditions are ignored
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c7
  attr: setting_range
  value:
    min: 0
    max: 4
    unit: unit:HR
  conditions: AlsoEnergy LocusNOC sunrise/sunset buffer
  cite:
  - src: src:alsoenergy-kb-string-performance-alerts
    loc: sec=h3
    h: d9fd72a0a2fa
  review: drafted
- claim_id: c8
  attr: setting_range
  value:
    min: 0
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:sma-stp-core1-us
  conditions: SMA string-failure detection tolerance parameter (Operation.StrFltDet.Tol)
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=6
    h: a8f7fae0e59e
  review: drafted
- claim_id: c9
  attr: setting_range
  value:
    min: 5
    max: 360
    unit: unit:MIN
  scope:
    products:
    - prod:sma-stp-core1-us
  conditions: SMA time until string-failure detection warning (Operation.StrFltDet.WrnTm)
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=6
    h: a8f7fae0e59e
  review: drafted
- claim_id: c10
  attr: setting_range
  value:
    min: 5
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:sma-stp-core1-us
  conditions: SMA activation threshold for string-failure detection, as share of nominal AC power (Operation.StrFltDet.WMinNom)
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=6
    h: a8f7fae0e59e
  review: drafted
---
String monitoring tracks the current of each PV string, or of each input, so that strings that are faulty or underperforming are flagged faster and more precisely than monitoring at the inverter level can manage. O&M guidelines recommend string monitoring equipment that measures every string continuously and logs at intervals of up to 15 minutes. One sensor may cover more than one string, but no more than two strings in parallel. Huawei SUN2000 inverters have a String monitor parameter that raises an alarm when a string is shaded or its yield drops. It defaults to Disable on the SUN2000-45KTL-US-HV-D0 and should stay disabled where strings shade easily, to avoid false alarms. On the SMA Sunny Tripower CORE1-US, string-failure detection is set up with these parameters: operating mode, comparison group, sensor sensitivity, tolerance, time until warning and an activation threshold based on nominal AC power. FIMER TRIO S2F/S2X versions can show the voltage and current of each string input and warn when a string fuse fails. String settings for FIMER equipment are configured in Aurora Manager LITE. In AlsoEnergy LocusNOC, String Performance Alerts compare each string's normalized DC current with the best string on the same component. They need at least two Normalized String DC Current data fields configured first.

<!-- review notes
- sentence 1: support check: partial - Passages support per-string current monitoring and more precise troubleshooting than inverter level, but 'faster' flagging is only loosely supported and 'or of each input' and flagging underperforming strings are not clearly stated.
- sentence 3: support check: partial - Alarm behavior, disable advice and Disable default are stated, but the default is from a generic table not tied to the 45KTL-US-HV-D0 specifically.
- sentence 5: support check: partial - Per-string voltage/current display and fuse warning for S2F/S2X are stated, but Aurora Manager LITE is only said to enable monitoring; string settings are in a Fuse Control Board tab, not clearly Aurora Manager LITE for all FIMER equipment.
- sentence 1: review: partial - Per-string current measurement, more precise troubleshooting than at inverter level, quick detection and alarms on yield drop are all supported, but the 'or of each input' alternative is not stated in the passages.
- sentence 4: review: partial - All six string-failure detection parameters are listed in the cited SMA table, but the passage never names the Sunny Tripower CORE1-US model.
-->
