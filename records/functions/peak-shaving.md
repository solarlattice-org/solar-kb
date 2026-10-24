---
id: func:peak-shaving
type: Function
name: Peak shaving
aliases:
- peak load shaving
- demand charge reduction
- load peak capping
- Grid peak shaving
- Peak-Shaving Mode
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 0
    max: 10000
    unit: unit:W
  conditions: Max Usable Grid Power, the grid import limit during peak shaving, set in SolisCloud remote
    control settings
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h14
    h: d370ce63f0ce
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 10
    max: 100
    unit: unit:PERCENT
  conditions: Baseline SOC for Solis peak-shaving mode, set in SolisCloud remote control settings
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h14
    h: d370ce63f0ce
  review: drafted
- claim_id: c3
  attr: default_value
  value:
    nominal: 2
    unit: unit:UNITLESS
  scope:
    products:
    - prod:solis-s6-eh3p-75-150k-us
  conditions: Grid peak shaving grid draw limit, as a multiple of the inverter's rated power; enabled
    by default
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=25.r3
    h: ce91120e52dd
  review: drafted
  review_note: 'support check: partial - Passage says default enabled, default 2 times rated power, limiting
    grid draw, but it doesn''t name the product in the text; the multiple-of-rated-power meaning is stated.'
- claim_id: c4
  rel: requires
  target: tool:sma-lcs-tool
  note: The SMA document configures peak load shaving with increased self-consumption (multi-use) in the
    LCS-Tool.
  cite:
  - src: src:sma-doc-278879
    loc: fig=51
    h: 6d1865511782
  - src: src:sma-doc-278879
    loc: sec=5.2.10
    h: 8ee2447d0601
  - src: src:sma-doc-278879
    loc: sec=h199
    h: 06c2109b18e1
  review: drafted
  review_note: 'support check: partial - Passages show only headings that the LCS-Tool is used for setting
    Peak Load Shaving; they don''t explicitly say it is required.'
- claim_id: c5
  rel: requires
  target: func:battery-grid-charging
  note: Below the baseline SOC, the system charges the battery from the grid with whatever headroom is
    left under the import limit; grid charging can also be switched on or off.
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h14
    h: d370ce63f0ce
  review: drafted
  review_note: 'support check: partial - Passage says the system charges the battery with the available
    difference below baseline and grid charging can be enabled or disabled, but doesn''t state peak shaving
    requires grid charging (the on/off switch suggests it doesn''t).'
---
Peak shaving discharges the battery when demand is high, which cuts peaks in grid import and so lowers demand charges. On Solis systems, Max Usable Grid Power sets the most power that may be drawn from the grid while peak shaving runs. A peak-shaving switch turns the mode on or off, and it works only with lithium batteries that have communication. The Peak Shaving Baseline SOC is the lowest charge level that peak shaving may discharge to. It applies only in peak shaving mode, while Reserve SOC applies in every operating mode and holds energy back for backup. Once the battery reaches the baseline SOC, peak shaving stops and the grid supplies any extra load. If self-consumption is enabled, it can keep discharging down to the Reserve SOC. If the charge falls below the baseline and grid import is still under the limit, the system uses the spare headroom to recharge the battery up to the baseline.
