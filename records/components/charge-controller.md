---
id: comp:charge-controller
type: Component
name: PV charge controller
aliases:
- Sunny Island Charger
- charge controller
---
In SMA Sunny Island battery systems, the Sunny Island Charger is the PV charge controller. It sits between the PV array and the battery bank. A system can have several of these units, numbered from charger 1 to charger 4, and each one reports its own values to the Sunny Island. Each charger reports total and daily PV energy, PV power and PV voltage. In expert mode it also reports battery voltage, battery current and heat sink temperature. An overtemperature warning, level 1, means the charger is reporting battery overtemperature. Another level 1 warning covers undertemperature: either the charger temperature sensor has an error, or the charger is reporting battery undertemperature. For these temperature warnings, the manual says to set the charger to the operating mode SMA operation, following the charge controller installation manual.

<!-- review notes
- sentence 1: support check: partial - Passages show Sunny Island Charger is a PV charge controller reporting PV power/voltage, but nothing states it sits between the PV array and the battery bank (battery values are reported though).
- sentence 2: support check: partial - Chargers 1 to 4 each have their own data points, but the passages do not state they report to the Sunny Island or that a system can have several.
-->
