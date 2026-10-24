---
id: tool:phase-rotation-tester
type: Tool
name: Phase rotation tester
aliases:
- phase sequence tester
- phase rotation meter
category: Instruments
tool_kind: instrument
---
A phase rotation tester is a field instrument for checking the order in which the phases of a three-phase AC connection were wired. It is used for the phase rotation test in inverter commissioning. Several three-phase string inverter manuals recommend a phase rotation test after AC wiring. The test sits under AC configuration checks, next to line-to-ground and line-to-line voltage and frequency measurements. Solis and Canadian Solar inverters do not need any particular phase rotation. The local utility may still require a specific rotation, or a record of how the phases were configured, so write the result down. On that inverter, wrong rotation does not damage the unit, but it will not run until the rotation is corrected. Smart meters and CTs need the same check. If a phase voltage reference is paired with a CT from another phase, the meter shows wrong power factor and active power readings. Phase rotation errors at the meter can make batteries charge or discharge unexpectedly, trip the system, or push generation over the limit when export is restricted. Protection relays have a phase rotation setting that must match the real system rotation. For example, a system can run with ACB rotation, and the relay setting must be ACB too.

<!-- review notes
- sentence 1: support check: partial - Passages describe the phase rotation test but never mention a 'phase rotation tester' instrument or define it as a field instrument.
- sentence 3: support check: partial - Passages state both brands need no specific rotation and utility may require it or a record; the advice to 'write the result down' is an inference, though reasonable.
- sentence 4: support check: partial - The passage says improper rotation won't damage and the inverter won't operate until corrected, but it's an unnamed inverter, not tied to 'that inverter' (Solis/Canadian Solar, which don't require rotation).
- sentence 5: support check: partial - u12 supports the wrong PF and active power from mismatched CT pairing, but 'smart meters and CTs need the same check' is only loosely implied by the Solis guide.
-->
