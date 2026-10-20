---
id: mit:arc-fault-circuit-interrupter
type: Mitigation
name: Arc fault circuit interrupter
aliases:
- AFCI
---
An arc fault circuit interrupter is a protection function built into the inverter. It detects electric arcs in the PV modules and in the module wiring of the connected strings. The NEC requires this protection for PV systems, and the UL 1699B standard sets the requirements for PV DC arc-fault protection devices. When it detects an arc, the inverter stops operating and halts the current flow so the arc is interrupted. With operation inhibition active, the inverter stays off after an arc until someone resets it manually. Without inhibition, the inverter restarts after a waiting period and checks again, and it disconnects once more if the arc is still there. The manufacturer reports that the function is very reliable and rarely trips falsely. Treat every arc alarm as a real fault in the PV circuit, and have qualified staff locate and fix it promptly. If arcs keep recurring and the cause cannot be found, take the inverter out of service until the fault is fixed. Repeated arcs can damage nearby conductors and can lead to uncontrolled arcs and fire. Whether arc detection is on by default depends on the country data set. If a self-test of arc detection fails because the interference level is too high, the cause must be determined by the manufacturer's service.
