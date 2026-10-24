---
id: arch:functionally-grounded-pv-array
type: Architecture
name: Functionally grounded PV array
aliases:
- functional grounding
- functionally grounded
- Functional Grounded PV System
- Grounded, Functionally
- DC Grounded
category: Earthing
---
A functionally grounded PV array has an electrical reference to ground, but it is not solidly grounded. The ground connection is usually made through a fuse, a circuit breaker, a resistance device, a non-isolated grounded AC circuit, or electronics inside the inverter that are part of a listed ground-fault protection system. Conductors that normally sit at ground potential can carry voltage to ground during a fault, so test them before you touch them. The NEC lists a 2-wire PV array with one functionally grounded conductor as an allowed system grounding configuration, next to bipolar, ungrounded and solidly grounded arrays. Most modern string inverters are functionally grounded and non-isolated. Most legacy systems installed before 2011 had one DC pole solidly bonded to ground in the inverter. Solectria XGI 1500-1MW and XGI 1500-DCG inverters ground the DC input or DC negative, for example through the GFDI breaker. This prevents potential induced degradation in modules that are susceptible to it. On the XGI 1500-1MW, you can switch the DC input to floating in the user interface. Floating is the normal setting for DC-coupled storage, where the battery must float. When you retrofit a site whose modules need positive or negative grounding, ask the module manufacturer before you install a functionally grounded inverter. The change may expose the modules to potential induced degradation.

<!-- review notes
- sentence 2: support check: partial - The note lists the same means (fuse, breaker, resistance device, non-isolated grounded ac circuit, electronic means in a listed ground-fault protection system), but it doesn't say the electronics are inside the inverter. Only the u30 note mentions internal inverter electronics, and that note doesn't mention listing.
- sentence 3: support check: partial - The passages say conductors normally at ground potential may have voltage to ground during faults. They don't give the instruction to test them before touching.
- sentence 5: support check: partial - The passage says 'most legacy' systems installed before 2011 are solidly grounded with one DC pole bonded in the inverter. It says modern string inverters are 'generally' functionally grounded and non-isolated, not 'most'. This is close but the wording is slightly stronger.
-->
