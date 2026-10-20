---
id: meas:iv-low-isc
type: Measurement
name: Lowered Isc on IV curve
status: proposed
signals:
- point: model_160.DCA
  unit: unit:A
  pattern: slow, long-term decline in irradiance-normalized string current
- point: model_502.A
  unit: unit:A
  pattern: affected modules show lower current than neighbours at the same irradiance
- point: model_403.InDCA
  unit: unit:A
  pattern: affected string current below peer strings
---
