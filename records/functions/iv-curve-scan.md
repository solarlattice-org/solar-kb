---
id: func:iv-curve-scan
type: Function
name: I-V curve scan
aliases:
- I-V curve diagnostic
- online I-V diagnosis
- smart I-V curve
- I-V Curve Diagnostic Function
- I/V Curve
- I-V generator diagnostics
- ScanIVCure
- Iv Scan
category: Monitoring
function_kind: monitoring
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 100
    max: 1400
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-185-255k
  conditions: Start_V, the start voltage of the I/V scan
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=h201
    h: e2ad187a9dba
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 100
    max: 1400
    unit: unit:V
  scope:
    products:
    - prod:solis-3p-5g-us
  conditions: Start_V, the start voltage of the I/V scan
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=7.5.15.1
    h: a16164e0a1e1
  review: drafted
- claim_id: c3
  attr: setting_range
  value:
    min: 300
    max: 1000
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-75-100k-t480gl02
  conditions: Start_V, the start voltage of the I/V scan
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: sec=6.7.16.1
    h: 539e85625c66
  review: drafted
- claim_id: c4
  attr: setting_range
  value:
    min: 850
    max: 1000
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-125ktl-gs-e
  conditions: Start_V, the start voltage of the I/V scan
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: sec=7
    h: 37c4a2c23c61
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 1
    max: 100
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-185-255k
    - prod:solis-3p-5g-us
    - prod:canadian-solar-75-100k-t480gl02
    - prod:canadian-solar-125ktl-gs-e
  conditions: Interval_V, the scanning voltage step between data points
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=h201
    h: e2ad187a9dba
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=7.5.15.1
    h: a16164e0a1e1
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: sec=6.7.16.1
    h: 539e85625c66
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: sec=7
    h: 37c4a2c23c61
  review: drafted
  review_note: 'support check: partial - Interval_V is 1-100V (001V-100V) in all four, but the passages
    tie them to products only loosely; the core range matches.'
- claim_id: c6
  attr: default_value
  value:
    nominal: 100
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-185-255k
  conditions: Start_V value shown on the Set I/V Curve screen figure
  note: Value shown in the manual's screen illustration; read as the displayed default.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=h201
    h: e2ad187a9dba
  review: drafted
- claim_id: c7
  attr: default_value
  value:
    nominal: 850
    unit: unit:V
  scope:
    products:
    - prod:canadian-solar-125ktl-gs-e
  conditions: Start_V value shown on the Set I/V Curve screen figure
  note: Value shown in the manual's screen illustration; read as the displayed default.
  cite:
  - src: src:csi-csi-installation-manual-csi-125ktl-gs-e-usa-v1-3
    loc: sec=7
    h: 37c4a2c23c61
  review: drafted
---
The I-V curve scan sweeps the PV input and records the current-voltage characteristic of the connected strings, so faults, damage or installation errors in the array can be found without a separate tracer. Sunny Tripower CORE1-US inverters measure one curve per MPPT input, so strings in parallel on that input show up as one combined curve, and the measured current cannot exceed the MPPT input current rating. On the CORE1-US, each scan briefly stops feed-in and runs the inverter at reduced power for about 20 seconds per MPPT input, and it can run at most 10 times per day unless the inverter is restarted. CORE1 results have over 200 data points per input, are stored until the next scan, can be saved to PDF, and show temperature and irradiance when the optional SMA Sensor Module is fitted. The function is listed for STP 33/50/62-US-41 from firmware 03.12.21.R, and the table lists firmware as not available for STP 50-US-40. On Canadian Solar CSI and Solis three-phase inverters, you set Start_V and Interval_V in the I/V Curve menu, then press ENT to start the scan. The display shows Scan OK when it finishes, and you then pick a string number to view its results. These CSI and Solis inverters record 60 data points per scan, and some models state a maximum scanning range of 100-1450V or 850-1450V. CPS inverters can start a scan over Modbus by writing 0xA801 to register 0x2B12. Reading the same register returns whether the scan is in progress, finished or failed. The Sunny Tripower X 12 to 25 datasheet lists I-V generator diagnostics as a feature.

<!-- review notes
- sentence 1: support check: partial - Scan of I/V curves per string and deviations indicating faults/errors are stated, and no extra measurement devices needed; but 'sweeps PV input' is paraphrase and it's mixed across products, mostly fine though 'damage' etc. are covered.
-->
