---
id: comp:backup-generator
type: Component
name: Backup generator
aliases:
- Generator
- External generator
- Electric generators
---
A backup generator is an external, grid-forming energy source that can be added to a solar and battery system to cover long grid outages. In a SolarEdge Home Hub system, the generator only works when it is connected through the Backup Interface, and a two-wire dry contact controls its start and stop. Sunny Island systems can run as a stand-alone grid with a generator or as a battery-backup grid with a generator. Warning W401 (generator reverse power protection) means other AC sources, such as PV, are feeding power back into the running generator for too long. The Sunny Island blocks this to keep the generator from being destroyed. W401 can also appear when the reverse power threshold or duration is set too low. Compare the GnRvPwr and GnRvTm parameters with the generator's reverse power rating, and change them only in agreement with the generator manufacturer. Warning W402 means the generator management has switched into a locked error state. If a Sunny Backup 5000 will not connect to a running generator, first check the generator fuse. After a reverse power event, the generator connection stays blocked until it is acknowledged. Also check whether the generator start mode is set to manual instead of autostart. On SI2012 and SI2224 units with older firmware, the transfer relay wrongly stays closed after W401, so the generator is not protected. Update the firmware on these units.

<!-- review notes
- sentence 7: support check: partial - The passage lists checking the fuse, blocking until GnAck acknowledgement after reverse power and the manual start mode, but it does not say 'first' or define the order, and the blocking is for a set time.
- sentence 8: support check: partial - u1 states the relay incorrectly stays closed on firmware below 3.015/3.010 and recommends a firmware update, but 'the generator is not protected' is implied and not stated, and 'older firmware' is specific versions.
- sentence 7: review: partial - Checking the fuse first and the manual vs autostart setting are both stated, but the passage says the generator is blocked for a set time (with GnAck acknowledgement), not strictly until it is acknowledged.
-->
