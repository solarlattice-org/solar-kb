---
id: stressor:reactive-power-demand
type: Stressor
name: High reactive power demand
aliases:
- reactive power operation
---
High reactive power demand comes from grid or plant requirements. It can shift the inverter's effective voltage behavior and change its usable operating window. Together with degraded modules, high temperature or a tight string design margin, reactive power operation can push array Vmp below the inverter's minimum DC input voltage. When that happens, the inverter has to run above the array's maximum power point. Some available DC power is then not converted, which is the failure mode called inverter voltage floor losses. The effect shows up most during hot periods, because module voltage falls as cell temperature rises. From production data alone, the loss can look like clipping or general underperformance. Review DC voltage, AC voltage, reactive power dispatch and IV-derived Vmp at the same timestamps.
