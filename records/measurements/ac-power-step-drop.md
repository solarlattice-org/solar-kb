---
id: meas:ac-power-step-drop
type: Measurement
name: Sudden AC power drop
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: sudden step decrease equal to the power of one string, with irradiance unchanged
- point: model_103.A
  unit: unit:A
  pattern: AC current drops to zero when the AC side disconnects
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: plane-of-array irradiance stays at a usable level while power is low
- point: model_103.DCA
  unit: unit:A
  pattern: DC input current falls to zero when the inverter shuts down
---
