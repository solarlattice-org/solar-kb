---
id: meas:ac-disconnect-open
type: Measurement
name: AC disconnect open position
aliases:
- AC disconnection unit
- AC disconnect switch
- AC service disconnect switch
- AC disconnect device
- main PV system AC disconnect
---
This signature is the physical position of the AC disconnect, read on the handle or knob, which shows whether the inverter is cut off from the AC side. On the ABB AC disconnection unit in SMA central inverters the handle has three positions: on means closed, the central position means the unit tripped and is open, and off means it is open. On SMA US string inverters, opening the main PV system AC disconnect starts the Rapid Shutdown function, so the off or open position shows that a rapid shutdown has been initiated. When this happens the inverter logs event 9033, which says Rapid Shutdown was triggered and the AC side was disconnected. With grid support enabled, the inverter can stay connected for a set ride-through time after the AC disconnect is operated, and only disconnects and starts the rapid shutdown if grid voltage does not come back. Some setups name a breaker as the initiator: a Generac SDS AC PV breaker turned off with its cover locked counts as the rapid shutdown initiator, and SMA inverters have a parameter that selects either the AC disconnect or a digital input. A dark display does not prove the inverter is off, because a failed internal part can also blank it, so check by eye that the AC and DC disconnects are in the OFF position.

<!-- review notes
- sentence 1: support check: partial - Passages describe AC disconnect positions (closed/open/tripped) and that AC disconnect must be off, but don't say it is read on a handle or knob as a signature, though the position states open/closed status.
- sentence 2: support check: partial - The three positions and meanings are stated for the ABB AC disconnection unit, but the passages don't mention SMA central inverters or a handle specifically.
- sentence 1: review: partial - The switch positions show whether the AC disconnection unit is open or closed, but the passages never say the position is read on a handle or knob.
-->
