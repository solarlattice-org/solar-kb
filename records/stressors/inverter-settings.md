---
id: stressor:inverter-settings
type: Stressor
name: Inverter parameter settings
aliases:
- Parameter configuration
- operating parameters
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring at a 100 MW California PV plant during
    summer 2025; voltage or setting adjustments were estimated to recover a large share of it
  note: This loss belongs to inverter voltage floor losses as a whole. Inverter settings are one of several
    contributors, so not all of it comes from settings.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
---
Inverter parameter settings are the configurable values that control how an inverter operates. They ship at factory defaults and can be changed through the app or user interface to optimize performance. Wrong settings can put the inverter into an exception state. Only qualified personnel should change them, and some sensitive grid parameters are locked behind an access code. Settings are one possible root cause of inverter voltage floor losses, alongside plant voltage control, transformer tap position and grid support requirements. In these events the inverter is held above the array maximum power point, so available DC power is not fully harvested. These losses show up mostly during hot periods, when module voltage drops. They can get worse when reactive power demand or AC voltage behavior shifts the inverter's effective operating window. Imported inverters may arrive with manufacturer default settings that do not suit the local climate. Setting climate-specific values is therefore an important part of commissioning. A missing country data set stops feed-in. A country data set that is wrong for the site can disturb the PV system and cause problems with the grid operator. Parameter changes are not saved if the utility grid is disconnected before the DC side. Disconnect the DC side first, wait, then disconnect the grid.

<!-- review notes
- sentence 1: support check: partial - Passages say parameters have default values and can be set via the App to optimize performance, but 'ship at factory defaults' and 'user interface' are only loosely covered and the definition is inferred.
-->
