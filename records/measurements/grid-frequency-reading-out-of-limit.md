---
id: meas:grid-frequency-reading-out-of-limit
type: Measurement
name: Grid frequency outside limits
aliases:
- GridF.OutLim
- Grid incident
- Grid overfrequency
- Grid Uncompliant
signals:
- point: model_103.Hz
  unit: unit:HZ
  pattern: measured grid frequency above the max or below the min protection threshold while the alarm
    is active
---
This signature is a grid frequency reading at the inverter's AC terminals that falls outside the permitted operating window. The inverter then disconnects from the utility grid. The reference is the nominal grid frequency, which is 60 Hz or 50 Hz. Inverters have separate over-frequency and under-frequency protection thresholds, often set at several levels, each with its own trip time and recovery threshold. These limits can be adjusted within ranges set by the grid code profile. For example, an SMA STP-US-41 inverter rated at 60 Hz operates between 54 Hz and 66 Hz, and it measures frequency to within 0.1 Hz. Some inverters report this event under a combined code meaning the grid frequency is abnormal or no grid is detected at all. Other units raise a grid incident when they detect a stand-alone grid or a very large change in frequency. Battery systems may report frequency outside their hardware trip thresholds as part of a general grid non-compliance status that also covers voltage faults. The inverter usually reconnects once the grid frequency returns to normal. If the trip happens repeatedly, measure the actual grid frequency and contact the local utility.

<!-- review notes
- sentence 7: support check: partial - Reconnect and measure frequency are stated, but the passage cuts off at 'contact the local electric power company for', and the statement's reconnection is for overfrequency code only.
-->
