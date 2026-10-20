---
id: meas:overvoltage-power-derating
type: Measurement
name: Volt-watt power derating
aliases:
- Grid Over Voltage Derating
- Volt-Watt
- grid overvoltage derating
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power falls below available power as AC voltage rises above the derating start voltage
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC voltage elevated into the volt-watt derating band
---
Volt-watt derating is an open-loop limit on real power that responds when the grid voltage goes too high. Grid voltage is measured at the point of interconnection meter. A programmable curve sets how far output is limited as the voltage rises. The derating takes effect over a set open-loop response time, which defaults to 10 seconds under IEEE1547-2018 and 5 seconds under Rule21. In the Tesla controls, the first real power limit is fixed at 1 per unit. A read-only register reports the power limit worked out from the Volt-Watt curve, so trend that register alongside grid voltage. On Solis inverters Volt-watt is one of several working modes and can run together with Volt-var. The working mode display shows which of the two takes priority.

<!-- review notes
- sentence 4: support check: partial - Real power limit 1 fixed at 1 pu and the read-only Volt-Watt Real Maximum register are stated, but the advice to trend it alongside grid voltage is not in the passages.
-->
