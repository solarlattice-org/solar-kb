---
id: state:standby
type: OperatingState
name: Standby
aliases:
- stand-by
- idle
category: Inverters
---
Standby is a normal waiting state. The inverter is ready but holds off operating until a condition is met, such as PV voltage being present. SMA inverters report why they are in standby: waiting for PV voltage, waiting for a valid AC grid, or energy saving mode. Huawei SUN2000 inverters go into standby when outside conditions do not meet operating requirements. They keep checking their status and switch to operating once the requirements are met. A shutdown command or a fault sends them to shutdown instead. Sungrow inverters go into standby when the DC input is not enough, and wait there for the standby duration. On SMA inverters, the change from off to standby happens when the standby conditions are met (for example, DC voltage is present) and the operator has enabled operation. The inverter returns to off when those conditions are no longer met. A Sunny Island can be stopped by hand into standby. It also switches to standby by itself when the state of charge falls below the level 1 threshold during the set time window.

<!-- review notes
- sentence 6: support check: partial - Level 1 switching to standby below the SOC threshold in the time window is stated, and a manual stop into standby is evidenced only by headings or entries without detail.
- sentence 1: review: partial - The passage supports that standby means waiting for an operating condition such as PV voltage, but it does not say that standby is a 'normal' state or that the inverter is 'ready'.
-->
