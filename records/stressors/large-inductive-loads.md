---
id: stressor:large-inductive-loads
type: Stressor
name: Large inductive load switching
aliases:
- large electric consumer loads
- shifted neutral point
- air conditioners, pumps, large motors, lifts
- larger loads (machines or industrial plant)
- inductive load
- three-phase motors
- large loads
---
Large inductive loads such as motors and pumps can draw a very high startup power when they are switched on. On hybrid inverters this startup surge on the backup output can trigger a load overload fault, and the guidance is to remove some backup load or take the inductive load off the backup circuit. Battery inverters can also report an overload on a line conductor when the connected loads draw more power than the unit can deliver. Exposure is reduced by staggering when loads are used and, where needed, choosing an appliance with a lower starting current. Three-phase motors that need all phases at once should be switched by a single actuator driving a three-phase contactor, not by separate per-phase switches. Large loads such as a big pump or a three-phase heater can be started through a relay or contactor controlled by a radio-controlled socket. Switching a load on and off too often can damage it, so set switching frequency within the load manufacturer's limits.

<!-- review notes
- sentence 1: support check: partial - Passages say inductive load startup power can be too large for the backup output, but not that motors/pumps specifically draw very high startup power.
-->
