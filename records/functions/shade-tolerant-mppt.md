---
id: func:shade-tolerant-mppt
type: Function
name: Global MPP scan
aliases:
- ShadeFix
- OptiTrac Global Peak
- shade management
- global peak tracking
- MPPT Multi-peak Scanning
- MPPT global scanning
- SMA OptiTrac Global Peak
- SMA ShadeFix
- MPPT Scan
- Multi-max scan
- Multiple Max Scan
- multi-MPP tracking
- MPPT global scan
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: subclass_of
  target: func:mppt
  note: Global scan is described as an extension of MPP tracking that finds several power maxima under
    partial shading.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h64
    h: b8c91c5707de
  - src: src:abb-uno-dm-6-0-tl-plus-us-product-manual-reva
    loc: sec=h230
    h: 82dc537ec426
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: sec=13
    h: 154a08a362a3
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h159
    h: ff0824ba155f
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 600
    max: 10800
    unit: unit:SEC
  conditions: MPPT Multi-peak Scan Interval set through the SolisCloud remote control advanced settings
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h50
    h: 2f904674e9d7
  review: drafted
- claim_id: c3
  attr: setting_range
  value:
    min: 180
    max: 3600
    unit: unit:SEC
  scope:
    products:
    - prod:sma-sbse-us-50
  conditions: Cycle time of SMA ShadeFix, parameter DcCfg.MPPShdw.CycTms
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=33
    h: 004d364b23b6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: tbl=33.r1
    h: 50485e5136fe
  review: drafted
  review_note: 'support check: partial - The 180–3600 s range for Cycle time of SMA ShadeFix is given,
    but the passages don''t tie it to the specific product sma-sbse-us-50.'
- claim_id: c4
  attr: default_value
  value:
    nominal: 6
    unit: unit:MIN
  scope:
    products:
    - prod:sma-stp-core1-us
  conditions: SMA ShadeFix time interval, enabled by default; the manual says the interval is usually
    6 minutes
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h82
    h: f1f39012a7ab
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h78
    h: f1f39012a7ab
  review: drafted
  review_note: 'support check: partial - Manual says interval usually 6 minutes and enabled by default,
    but the passages don''t name the Core1 product.'
- claim_id: c5
  attr: default_value
  value:
    nominal: 3600
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sch-125ktl-aio
  conditions: MPPTTime (MPPT Scan Cycle) value under the IEEE-1547, Rule 21 and ISO-NE grid codes
  note: The table gives the value without printing a unit; seconds is assumed.
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=24.r26
    h: 2c4e8910eca9
  review: drafted
---
A global MPP scan sweeps the PV operating range from time to time to find the true maximum power point. This matters when partial shading or modules at different angles create several power peaks on the curve. During each scan the inverter does not run at the maximum power point, so output drops briefly. Shorter scan intervals therefore cost more energy, and on ABB/FIMER units each scan takes roughly 2 seconds. On Solis inverters, SolisCloud has a switch that turns multi-peak scanning on or off and a scan interval setting of 600 to 10,800 seconds. SMA calls this function OptiTrac Global Peak on the Sunny Tripower TL-US, set with the parameters MPPShdw.IsOn and MPPShdw.CycTms. Its manual says the ideal interval is usually six minutes. Newer SMA inverters use SMA ShadeFix, which is enabled by default and usually checks the operating point every 6 minutes. On the Sunny Boy Smart Energy, its cycle time can be set from 180 s to 3600 s. ABB UNO-DM and FIMER TRIO inverters have a menu setting to enable or disable the scan and set the scan interval. The TRIO also lets you start a scan manually. On Yaskawa Solectria PVI inverters, MPPT scan is enabled by default with a 60 minute period. It searches in 5 V steps and can also be started from the MPPT SCAN menu.

<!-- review notes
- sentence 4: support check: partial - OptiTrac Global Peak, MPPShdw.IsOn, MPPShdw.CycTms and six-minute ideal interval are stated, but the Sunny Tripower TL-US model is not named in the passages.
- sentence 5: support check: partial - ShadeFix default-on and 6 min and the 180–3600 s range are stated, but the Sunny Boy Smart Energy and 'newer inverters' aren't in the passages.
- sentence 6: support check: partial - Enable/disable and interval and manual scan appear in menus, but the passages don't name UNO-DM or TRIO models; manual scan only in one menu (u19).
- sentence 7: support check: partial - Default enabled, 60 min period, 5 V step and MPPT SCAN menu are stated, but Yaskawa Solectria PVI isn't named in the passages.
-->
