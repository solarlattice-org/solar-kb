---
id: meas:dc-input-overcurrent-event
type: Measurement
name: DC input overcurrent event
status: proposed
signals:
- point: model_160.DCA
  unit: unit:A
  pattern: input current on the affected PV input reaches the inverter's overcurrent limit just before
    the event
- point: model_103.W
  unit: unit:W
  pattern: AC output briefly drops to zero while feed-in is interrupted, then resumes
---
