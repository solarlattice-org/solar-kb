---
id: func:phase-angle-jump-ride-through
type: Function
name: Voltage phase angle change ride-through
aliases:
- phase jump ride-through
- RPAC
- Voltage phase angle change
category: Grid support
function_kind: grid-support
---
Voltage phase angle change ride-through means the DER keeps operating when the grid voltage phase angle jumps suddenly, instead of tripping offline. Single-phase DER must stay in operation for phase angle changes of up to 60 electrical degrees within a sub-cycle-to-cycle time frame. After the disturbance, current oscillations that are positively damped are acceptable. So is momentary cessation lasting no more than 0.5 s. Compliance is shown by type tests on the DER system. For composite systems, the design must also be evaluated and commissioning tests may be needed. One utility settings document accepts UL 1741 SB certification as sufficient proof that an individual inverter meets this requirement. The same document does not allow relays, controllers or any other site equipment outside the certified inverter to have phase angle change trip settings enabled, and the utility may check for such settings.

<!-- review notes
- sentence 1: support check: partial - The passage gives the ride-through requirement (remain in operation for angle changes) but does not define it generically or say 'instead of tripping offline'; the meaning is largely implied.
- sentence 4: support check: partial - Type tests required for DER system is stated, but for composite the type tests are 'L' and commissioning 'D', design 'R'; 'may be needed' for commissioning is not clearly supported by the codes, which are undefined in passages.
-->
