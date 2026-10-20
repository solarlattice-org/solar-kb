---
id: meas:daily-power-plateau
type: Measurement
name: Flat plateau at power peak
signals:
- point: model_103.W
  unit: unit:W
  pattern: flat plateau at the inverter AC rating around midday peaks
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance keeps rising while AC power stays flat
- point: model_103.DCW
  unit: unit:W
  pattern: available DC power exceeds the inverter AC rating; inverter limits DC production
---
In the production data, this signature shows up as output held at a flat or controlled level that stays below the power the irradiance could support. It appears when the plant could produce more power than it is allowed to export, which is the grid curtailment loss mode. The cap can come from grid operator dispatch, an interconnection constraint, a plant controller command, a response to negative prices, or an export limit at the site. Inverters and trackers can look fully available during the plateau, so the pattern is easy to misread as underperformance. To confirm curtailment, check the setpoints and dispatch signals against the flat section of the curve. On some inverters, the active power control mode can be set to disabled, remote dispatch or local control, so check which mode is in use.
