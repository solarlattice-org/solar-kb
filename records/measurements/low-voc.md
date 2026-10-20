---
id: meas:low-voc
type: Measurement
name: Low open-circuit voltage
status: proposed
signals:
- point: model_502.V
  unit: unit:V
  pattern: module voltage lower than at comparable modules, by roughly one substring's share
- point: model_160.DCV
  unit: unit:V
  pattern: string or MPPT input voltage lower than at comparable strings under the same irradiance
- point: model_403.DCV
  unit: unit:V
  pattern: string voltage persistently below peer strings under the same irradiance
---
