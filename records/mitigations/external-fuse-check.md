---
id: mit:external-fuse-check
type: Mitigation
name: External fuse check
aliases:
- pre-fuse
---
An external fuse check confirms that the fuse feeding the device from outside is switched on and intact. When the matching event appears, the corrective steps are to reactivate the pre-fuse and then measure the supply voltage at terminal AC2 of the master in the main cluster. For other related events, switch the fuse back on and replace it if needed. The same event text says the utility grid may be running outside the set system limits, so a healthy fuse does not rule out a grid-side cause. Before any hands-on inspection, switch the device off and make sure it is voltage-free. Then look at the fuses and the tension springs on the fuse holders, and replace any fuse or spring that is discolored or looks changed. Each fuse should come out of its holder easily with a fuse extractor. If one sticks, or its contact surfaces have hardened grease on them, clean the contacts and apply fresh grease. If the insulation or terminals around the fuses are discolored, contact the manufacturer instead of carrying on yourself. Where an inverter flags its own DC or branch fuses as abnormal, check whether they have blown. If they have, contact the manufacturer and have the fuses replaced. O&M guidelines list a yearly fuse status check as a minimum requirement for electrical cabinets, inverters and MV switchgear.

<!-- review notes
- sentence 1: support check: partial - The corrective steps (reactivate pre-fuse, check AC2 voltage at master in main cluster) are stated, but the passages don't describe the external fuse check or its meaning.
- sentence 3: support check: partial - The passages state the grid may not work within set system limits, but the inference that a healthy fuse doesn't rule out a grid cause is not stated.
-->
