---
id: mit:inverter-replacement
type: Mitigation
name: Inverter replacement
aliases:
- Inverter repowering
---
For the external fan error (ExtFanErr) at more than 50% of rated output, replace the inverter if the fan is still spinning, because the fault is then in the sensing circuit. If the fan is not spinning, measure its supply voltage: below 6 VDC, replace the inverter; above 6 V, replace only the fan. For bus overvoltage (Protect0110), Mini MCU fault (Protect0150) and open-loop self-check failure (Fault0150), first try a restart. Switch AC and DC off, wait 1 minute (5 minutes for Fault0150), then switch both back on. Replace the inverter only if the fault does not clear. Before removing the unit, turn off the AC breaker and the DC switch. Then remove any padlock and the side screws, undo the four screws that hold the inverter to the wiring box, and lift the enclosure off the wiring box. If no replacement unit is on hand, fit the cover on the wiring box connector. The cover is not watertight, so the box must also be sealed some other way until the new inverter goes in. Whether to repair or replace depends on inverter size and type, how quickly the manufacturer can repair it, and cost. Replacement is preferred when repair parts are hard to get, but a newer model may not match the old size, footprint or wiring. If the new inverter is a different model or power class, check mounting, ventilation clearances, grounding, string sizing and AC-side protection against the new manufacturer's requirements. Include possible inverter replacement in the O&M budget. A manufacturer warranty may cover the unit but not the labour, and poor ventilation can void an inverter warranty.

<!-- review notes
- sentence 6: support check: partial - Passage covers mounting, ventilation, grounding, string length and AC protection, but says these checks apply to manufacturer requirements mainly for mounting/grounding/DC, and ties AC re-engineering to different sizes; stated as a general checklist is slightly broader.
-->
