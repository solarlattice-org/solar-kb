---
id: func:backup-reserve
type: Function
name: Backup reserve
aliases:
- reserve state of charge
- backup energy reserve
- minimum SoC
- Reserve SOC
- Reserved SOC
- battery reserve
- energy reserve
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 10
    max: 100
    unit: unit:PERCENT
  conditions: Reserved SOC setting in SolisCloud remote control (Self Use mode), effective only when the
    Battery Reserve Switch is enabled
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h8
    h: ebff7df97e38
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 300
    max: 10000
    unit: unit:W
  conditions: SolisCloud Grid Charging Power Limit, the maximum grid power drawn to maintain the reserved
    SOC; effective only when the Battery Reserve Switch is enabled
  cite:
  - src: src:kb-solis-44002638862-solis-cloud-remote-control-settings-desktop-version
    loc: sec=h8
    h: ebff7df97e38
  review: drafted
---
Backup reserve keeps part of the battery capacity available at all times. Regular operation is normally not allowed to discharge that part. The reserve provides backup energy during grid outages and protects battery life by preventing deep discharges. On Solis systems the Reserve SOC applies in all operating modes. The Peak Shaving Baseline SOC is a separate, usually higher floor that only limits discharge for peak shaving. In SolisCloud the Battery Reserve Switch enables the reserve and the Reserved SOC sets its percentage. The reserved energy is only used if the grid fails, and Allow Grid Charging lets the system recharge from the grid to hold the reserve. On the SMA Sunny Boy Smart Energy, you set the battery reserve under the backup settings in Energy management or with the SMA 360° commissioning wizard. For SolarEdge Home Hub systems, the energy available for backup depends on the reserve percentage and the minimum state of energy. When choosing the reserve, think about when an outage might happen, for example a weather event or a utility shutoff. To size the reserve, subtract the expected PV yield from the daily household demand. In an SMA planning example this gave 45% of a 10 kWh battery as the winter outage reserve.

<!-- review notes
- sentence 3: support check: partial - Reserve SOC applying to all modes and peak shaving baseline limiting only peak shaving are stated, and the baseline is described as generally more conservative (higher), but the passages don't state this is specific to Solis systems.
- sentence 5: support check: partial - Passage says backup settings including battery reserve are in Energy management or the SMA 360° wizard, but doesn't name the Sunny Boy Smart Energy product.
- sentence 6: support check: partial - Backup reserve energy depends on reserve percentage and minimum state of energy and outage timing considerations are listed, but the passage doesn't name Home Hub specifically (only SolarEdge Home Battery) and the considerations are phrased as questions.
- sentence 7: support check: partial - The example subtracts PV yield from demand giving 4.5 kWh = 45% of 10 kWh for winter grid failure, but the passage doesn't explicitly state it as a general sizing rule or name SMA.
-->
