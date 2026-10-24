---
id: symptom:backup-unit-overtemperature
type: Symptom
name: Backup unit overtemperature
aliases:
- Backup module bimetal switch
- backup module overtemperature state
- bimetal switch tripped
- Backup module overtemperature
- overtemperature state
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Sunny Boy Storage SBSx.x-US-10 battery inverters this shows as event 9207 (backup module bimetal
    switch tripped) or event 9211 (backup module overtemperature). Both point to the automatic transfer
    switching device.
  cite:
  - src: src:sma-kb-event-9207
    loc: sec=h1
    h: 5231fa52240d
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  - src: src:sma-kb-event-9211-with-sbsx-x-10-us-10
    loc: sec=h1
    h: 2b4ecc10ed34
  review: drafted
---
This symptom is reported by the battery inverter when the backup module (backup box) inside the automatic transfer switching device gets too hot or its bimetal switch trips. On Sunny Boy Storage units it appears in the event log as event 9207 for the bimetal switch or event 9211 for backup module overtemperature. The bimetal switch normally opens because of high temperature, but the trip is not always caused by the box or ambient temperature, so it can also point to a fault in the transfer switching device itself. The backup box is approved for use between -25°C and 60°C, so first check that the site temperature stays within that range. For an overtemperature message, check how the backup module is installed. For a bimetal switch message, check the bimetal switch itself. An external heat source can overheat the transfer switching device so that its lid locks. Remove the heat source and let the unit cool back into its allowed range. If the message is still there after these checks, contact the manufacturer of the automatic transfer switching device, because the fault is treated as a fault of that unit.

<!-- review notes
- sentence 3: support check: partial - Passage says the switch usually opens on high temperature but not always related to box/ambient temperature; it does not say it points to a fault in the transfer switching device itself (though the event list calls 9207 an 'Automatic transfer switching device error').
- sentence 4: support check: partial - The -25°C to 60°C approval range is stated, but the passage does not instruct checking site temperature first; it says to check the bimetal switch.
-->
