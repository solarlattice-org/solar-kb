---
id: symptom:inverter-overvoltage
type: Symptom
name: Inverter overvoltage
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ac-output-voltage-high
  note: On Sunny Island / Sunny Backup the event is raised once the RMS inverter voltage at AC1 sits 10%
    above the expected AC voltage. This is a trigger threshold, not a measured rise.
  quote: The event is displayed as soon as the root-mean-square value of the inverter voltage is 10% above
    the expected AC voltage.
  cite:
  - src: src:sma-kb-event-1707-f121-w122-w123-or-w124-on-sunny-island-or-sunny-backup
    loc: sec=h1
    h: 7b409fc35b19
  review: drafted
---
Inverter overvoltage is reported by Sunny Island battery inverters as fault F121 on the master and as level 1 warnings W122, W123 and W124 on slaves 1, 2 and 3. The message means an overvoltage occurred at the AC1 connection. It appears once the RMS inverter voltage is 10% above the expected AC voltage. Check this first: make sure the AC cables are de-energized, remove all cables from terminals AC1 and AC2, then restart the device. On a Sunny Backup, disconnect the grid, generator and loads from the automatic switch box instead. If the device does not start with the AC side disconnected, the inverter itself is defective and must be replaced. If it does start, the cause is external. In practice this is usually loads that are too high or extra feed-in devices on the AC side. Find the external source by measuring and reconnecting the AC sources and loads one at a time.

<!-- review notes
- sentence 1: support check: partial - The table lists F121 as Inverter overvoltage and W122, W123 and W124 as slaves 1, 2 and 3 at level 1, but it doesn't say F121 is the master or that the device is a Sunny Island (F121 is level 3).
- sentence 3: support check: partial - The passages give the removal of cables from AC1 and AC2, de-energized cables, restart, and the Sunny Backup disconnection, but 'check this first' is implied only by the step order, and the Sunny Backup also needs AC2 disconnected from voltage sources.
- sentence 1: review: partial - The table gives F121 (level 3) and W122/W123/W124 (level 1, slaves 1-3) as inverter overvoltage, but the cited rows do not say F121 is the master or that the device is a Sunny Island battery inverter.
-->
