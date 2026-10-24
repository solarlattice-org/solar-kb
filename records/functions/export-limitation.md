---
id: func:export-limitation
type: Function
name: Export limitation
aliases:
- export limit
- feed-in limitation
- export control
- active power feed-in limitation at PCC
- power export limit
- PEL
- Export Limiting
- Export Power Control
- Export limitation control
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: requires
  target: prod:sma-data-manager-m
  scope:
    products:
    - prod:sma-sunny-tripower-core2
  note: The Data Manager (EDMM-10) is the master device, and the CORE2 inverter is added under it.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  review: drafted
- claim_id: c2
  rel: requires
  target: prod:sma-energy-meter
  scope:
    products:
    - prod:sma-sunny-tripower-core2
    - prod:sma-sunny-tripower-x
  note: EM-20 is the example meter. For CORE2 the article says other meters can also be used.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  - src: src:sma-kb-sma-sunny-tripower-x-stp-xx-50-meter-configuration-and-setting-up-export-limit
    loc: sec=h1
    h: db43b2733021
  review: drafted
  review_note: 'support check: partial - CORE2 article lists the EM-20 as needed and says other meters
    can be used; STP X article only uses EM-20 as illustration and doesn''t say it''s required.'
- claim_id: c3
  rel: requires
  target: role:installer
  scope:
    products:
    - prod:generac-pwrcell-inverter
  note: A qualified installer sets the Export Limit value.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h132
    h: d13c4334af8a
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: sec=h120
    h: c0453e93ffaf
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: requires
  target: func:consumption-metering
  note: Consumption CTs or an external meter at the service measure import and export.
  cite:
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: sec=h6
    h: 2c048dcf225d
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: sec=4.1.2
    h: 89d203535ae7
  review: drafted
  review_note: 'support check: partial - Enphase uses Consumption CTs and Solis uses a meter with CTs
    measuring consumed and imported power, but the passages don''t say they measure export or that consumption
    metering is required generally.; review: partial - Enphase checks export against its Consumption CT
    readings and Solis curtails based on its meter''s CT data, but the Solis meter is described as measuring
    consumed and imported power (not export), and neither passage says metering is required in general.'
- claim_id: c5
  rel: requires
  target: prod:enphase-iq-gateway
  scope:
    products:
    - prod:enphase-iq8-commercial
  note: IQ Gateway Commercial 2 uses production and consumption CTs to limit PV output.
  cite:
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: sec=h6
    h: 2c048dcf225d
  review: drafted
- claim_id: c6
  attr: setting_range
  value:
    min: 10
    unit: unit:SEC
  scope:
    products:
    - prod:enphase-iq8-commercial
  conditions: Communication loss time limit setting of the Enphase power export limit on IQ Gateway Commercial
    2
  cite:
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: sec=h6
    h: 2c048dcf225d
  review: drafted
---
Export limitation caps the active power that the generators feed into the grid at the point of connection. Network operators often impose such a cap to meet grid code requirements. A meter at the grid connection measures export. When available PV power is greater than the site load, the inverter reduces its output and the excess power is lost. A sudden change in load can still cause brief overshoot above the limit, but the control limits how long it lasts. Fail-safe fallback settings keep export within the limit when parts of the system fail. On SMA CORE2 and Sunny Tripower X, you configure the meter channels and then set the active power to closed loop control with manual signal source. The active power setpoint is a percentage of total system power, where 0% gives zero export. Setting time and active power gradient adjust how fast the limit is reached. Enphase IQ8 Commercial systems set the power export limit through the grid profile. The settings are a watt threshold, enable or disable, per-phase or aggregate limit, export response time, and communication loss time. If export stays above the limit for longer than the response time, the Enphase gateway ramps PV down to zero. On Generac PWRcell inverters, an Export Limit of 0 works as zero export. Export Limiting can be set only once and the value can only be decreased. If the inverter loses communication with its CTs, it ramps its output down until export stops. Solis S6 hybrids can enable export power control with or without a battery, using the energy meter supplied with the inverter. Fronius Datamanager, SMA Sunny Tripower Smart Energy and FIMER inverters with a meter also provide this function.

<!-- review notes
- sentence 2: support check: partial - Inverter reduces output with excess lost is stated, but a meter specifically at the grid connection measuring export is not explicitly stated (Solis meter measures consumed and imported; FIMER says meter at Point of Connection only implicitly).
- sentence 3: support check: partial - Overshoot on sudden load change with time constrained is stated; fail-safe is only defined as capability to satisfy the limit in failure scenarios, and the fallback settings figure has no content.
- sentence 8: support check: partial - Solis and FIMER are supported, SMA Sunny Tripower Smart Energy lists zero export as a function; Fronius Datamanager passage shows only a table of contents with no export function.
-->
