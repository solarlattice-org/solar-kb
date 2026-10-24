---
id: mit:plc-transmitter-consolidation
type: Mitigation
name: PLC transmitter consolidation and conductor separation
aliases:
- single external PLC transmitter
- disable integrated transmitters
- separate array blocks
- DC wire management
- single PLC signal transmitter
- external PLC signal transmitter
- discrete separated blocks
---
This action prevents rapid shutdown PLC signal crosstalk at sites where several inverters or transmitters send signals over nearby PV DC conductors. The most effective option is to use one PLC transmitter for the site. Turn off the transmitters built into the inverters and fit a single external transmitter that sends the signal over the DC conductors of all the inverters. If a large array needs more than one transmitter, split it into separate blocks. Each block gets its own inverters, DC wiring and transmitter, and DC wiring from neighbouring blocks must not run close together. The 4-foot fire access pathways are a good place to draw the block boundaries. Keep wire bundles, conduit and tray belonging to different transmitters at least 1 foot apart, and preferably 4 feet. Keep each signal loop under 1000 feet round trip. Run the positive and negative conductors of each string together and twist them lightly, and in a cable tray lay only conductors from the same transmitter. Some integrated transmitters can be daisy-chained so their signals stay in sync, which removes crosstalk without an external transmitter box. Not every integrated transmitter can be disabled, and the RSD switch must not be used to disable one. Signals are induced even through thick insulation or separate metal tubing, and induction is easier between conductors of the same polarity. Crosstalk should be expected wherever conductors from different transmitters run close together. Without enough separation, rapid shutdown receivers can shut down unexpectedly or overheat, and the site can see arc-fault alarms, inverter shutdowns and low production. The installer should therefore test the rapid shutdown system at commissioning and watch inverter performance for several days afterwards.

<!-- review notes
- sentence 1: support check: partial - Passages say a single transmitter is the best way to eliminate crosstalk, but 'prevents' is stronger and the action is unspecified; roughly supported.
- sentence 4: support check: partial - Most items are supported, but the 'at least 1 foot' is 'as far as possible (minimum 1 foot)' and 'under 1000 feet' is fine; all stated, yet tray rule is supported only loosely—acceptable but the minimum/recommendation framing is the same, so main detail matches with slight paraphrase.
-->
