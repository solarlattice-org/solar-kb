---
id: comp:rapid-shutdown-initiator
type: Component
name: Rapid shutdown initiator
aliases:
- RSI
- system shutdown switch
- rapid shutdown switch
- DPST shutdown switch
- rapid shutdown initiator device
- Rapid Shutdown initiation device
- external rapid shutdown initiator
---
The rapid shutdown initiator is the switch or device that starts a rapid shutdown. A complete PV Rapid Shutdown System is made up of the inverter, the PV module switches and this initiator. On SMA inverters, the initiator can be the inverter AC fuse, the main PV system AC disconnect, or an external initiator wired to the digital input GSI. You choose which one with the parameter Operation.RSSInitiator. The inverter's DC load-break switch can also act as an initiator, but it switches off only that one inverter, not the whole system. Up to 3 inverters must be wired in parallel to a single external rapid shutdown initiator. An AC breaker used as the initiator must be easy to reach and clearly marked as the National Electrical Code requires. When it is in the Off (open) position, a rapid shutdown has been started. On the Enphase IQ Combiner 6C, the factory-installed PV aggregate breaker is the initiator. If the combiner is hard to reach, an external disconnect wired to the AC sense header can be used instead. The inverter is listed as PV Rapid Shutdown Equipment under UL 1741. The complete system must meet NEC (NFPA 70) and bring the DC conductors below 30 V within 30 seconds, and the module switches must disconnect the array within 15 seconds. A misconfigured rapid shutdown mode is risky. If the function is turned on but no PV module switches are installed, the inverter cannot discharge its DC input conductors during a shutdown and can be damaged.

<!-- review notes
- sentence 2: support check: partial - Initiator options (AC fuse, main AC disconnect, external initiator on digital input GSI) and the Operation.RSSInitiator parameter are present, but the parameter's settings are only 'AC disconnect PV system' and 'Digital input', so it doesn't select the AC fuse as a separate option.
-->
