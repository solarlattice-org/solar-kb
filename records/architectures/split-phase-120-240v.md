---
id: arch:split-phase-120-240v
type: Architecture
name: 120/240 V split-phase service
aliases:
- 240 V split-phase
- split phase
- 120/240V
- 240 V split-phase system
- 240 VAC split-phase
- US 240 SPLIT
- 240/120 three-wire
- Single phase 120/240 v
- 120 V Split Phase
- 240V Split-Phase
category: Grid service
---
A 120/240 V split-phase service has two hot legs and a neutral. You get 240 V between the two legs and 120 V from either leg to neutral. It is the normal service for homes. Utility service tables list it as a single-phase, three-wire service. The two legs are 180 degrees apart, so the neutral carries only the difference between the two leg currents. Standard panels feed alternate breaker spaces from opposite legs. A 240 V circuit uses two adjacent breakers joined by a bridge clip so that both trip together. This is not the same as a 208 V or 220 V service, where the two lines are phases of a three-phase system 120 degrees apart. The Enphase IQ System Controller supports only split-phase service and cannot be installed on 208 V or 220 V line-to-line services. Grid-tied inverters for this service connect to L1, L2 and N. For example, the Solis RHI hybrid inverters are rated 240 V line-to-line and 120 V line-to-neutral. Enphase microinverters on a 240 V split-phase service accept 211 to 264 VAC between L1 and L2. Inverters must be set to the matching grid setting at commissioning. For example, SMA inverters use the UL1741/2016/120 country data set for a 240 V split-phase system.

<!-- review notes
- sentence 8: support check: partial - The data set UL1741/2016/120 for 240 V split-phase is stated, but the passages don't say the setting must be made at commissioning or that it's SMA-specific beyond implication.
-->
