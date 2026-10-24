---
id: arch:dc-coupled-storage
type: Architecture
name: DC-coupled storage
aliases:
- DC coupling
- DC-coupled battery
- DC coupled storage system
- Dcs
- DC coupled PV+Storage
- 'PV + BESS: DC-coupled'
- AC/DC-coupled
category: Storage
---
A DC-coupled system joins the PV array and the battery on the DC side of an inverter. The inverter is usually bidirectional, so it can also charge the battery from the grid where this is permitted. A charge controller or DC-DC converter controls the PV voltage used to charge the battery. It is an extra component that affects overall system efficiency. When the battery can charge from the grid as well as from the PV array, the setup is sometimes called AC/DC-coupled. In the Generac PWRcell system, the inverter connects PV Link optimizers and PWRcell Batteries over the REbus 380 VDC nanogrid. On its AC side it feeds the grid, home loads and, through the PWRcell ATS, backup loads. In contrast, AC-coupled sites join PV and storage only on the AC bus and use a separate storage inverter. In DC-coupled overbuild scenarios, storage durations of four hours or more are likely.
