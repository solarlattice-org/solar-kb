---
id: func:battery-grid-charging
type: Function
name: Battery charging from the grid
aliases:
- grid charging
- emergency grid charge
- force charge
- AC2BAT
- Grid to Battery
- Allow grid charging
- Charging from Grid
- Emergency charging mode
- emergency charge mode
- power grid charging
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 4
    unit: unit:PERCENT
  scope:
    products:
    - prod:solis-s6-eh3p-75-150k-us
  conditions: Force charge SOC setting; upper end is the set over-discharge value. Below this SOC the
    grid charges the battery.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=22.r5
    h: 2a0b2541ee46
  review: drafted
---
Grid charging lets the AC side or utility grid charge the battery, not only PV. Solis tells installers to allow grid charging during self-use setup of the RHI-48ES-5G and S5-EH1P hybrids. The Off-Grid mode charges from PV only. The CPS single-phase hybrid has an emergency charging mode that force charges the battery from PV and grid to full SOC. Its EMS parameters set the maximum grid charging power, grid charging start and end times, and the grid charging enable. The SMA Sunny Island can charge its battery automatically from the utility grid when SOC is low. Set GdSocEna to Enable and GdManStr to Auto, and set SOC thresholds for two time windows. In an SMA charging period, any energy PV cannot supply is drawn from the grid, and battery discharge is blocked until the period ends.
