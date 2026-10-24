---
id: state:sma-no-country-data-set
type: OperatingState
name: No country data set
aliases:
- no country data set configured
- country data set not set
- No country data set set
category: Inverters
make: sma
product: prod:sma-stp-x-us-50
claims:
- claim_id: c1
  rel: subclass_of
  target: state:stopped
  note: Operation and feed-in stay stopped until a country data set is configured.
  cite:
  - src: src:kb-sma-stpxxus50-led-signals
    loc: tbl=1.r1
    h: 0401ed7eeab4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h61
    h: 389cf210374f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: tbl=15.r1
    h: 5c476c936f5d
  review: drafted
---
This state means the inverter has no country data set (grid code) configured yet, so it does not operate or feed in. It is normal during first commissioning, because a country data set has to be set before the inverter can start feed-in. The inverter shows this state by flashing its green and red LEDs at the same time, 2 s on and 2 s off. To clear it, set the country data set, for example with the commissioning wizard or through a System Manager. When the configuration is finished, the inverter leaves this state and starts operating by itself. Pick the data set that matches the installation site and how the system will be used. A wrong choice can disturb the PV system and cause problems with the grid operator, so ask the grid operator if you are not sure which one applies.

<!-- review notes
- sentence 1: support check: partial - No country data set and stopped operation/feed-in are stated, but the passages never equate the country data set with 'grid code'.
- sentence 2: support check: partial - Passages say a country data set must be set during commissioning before feed-in, but they don't state that the state is 'normal'.
-->
