---
id: comp:microinverter
type: Component
name: Microinverter
aliases:
- micro-inverter
- MLPE microinverter
- module-level inverter
- Micros
---
A microinverter is a small inverter that connects directly to one or two PV modules. It is usually plugged into the module's factory leads and either fixed to the module frame or mounted right next to the module. It turns the DC output of its module into AC power that meets grid requirements. Each microinverter runs its own maximum power point tracking for its module. Shading, soiling, orientation or mismatch on one module therefore does not pull down the output of the other modules. In SMA systems that use micro inverters, each PV array is a single module, because only one module can be connected to each micro inverter. On some models there is a status LED on the underside. Solid green means normal startup, flashing red means no grid is present (the AC breaker is off), and solid red means the microinverter failed to start. A complete inverter failure can come from a faulty hardware or software component, a grounding fault such as high humidity inside the unit, or a firmware problem. It is found through monitoring, visual inspection, IV curve checks and open-circuit voltage checks. Each module's energy is converted at the module itself, so any energy above the microinverter's continuous power rating is lost as clipping. Newer models rated for up to 14 A of continuous DC input current are made for higher-current modules. Check that the module current is within the microinverter's input rating.

<!-- review notes
- sentence 4: support check: partial - The passage states that a PV array is one module with micro inverters, but it doesn't mention SMA specifically.
- sentence 5: support check: partial - The LED colors and meanings are given, but the passage doesn't say it's only on some models (it lists the LED on the underside without that qualifier).
- sentence 8: support check: partial - The passage supports the 14 A models being suited to higher-current modules, but the advice to check module current against the input rating isn't stated, and 'newer' isn't stated.
-->
