---
id: func:self-consumption-optimization
type: Function
name: Self-consumption optimization
aliases:
- self-use mode
- self-consumption mode
- maximize self-consumption
- self-use
- Self Supply
- increased self-consumption
- Self consumption
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  attr: default_value
  value:
    nominal: 30
    unit: unit:PERCENT
  scope:
    products:
    - prod:generac-pwrcell-battery
  conditions: Factory default of the MinSocRsrv minimum reserve setting, the level to which the battery
    discharges daily when operating in Self Supply mode while grid connected
  note: Leaves at least this share of capacity for Island Mode during a utility outage.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h153
    h: 605116649bc1
  review: drafted
- claim_id: c2
  rel: requires
  target: func:consumption-metering
  note: Generac Self Supply needs CTs installed and calibrated first; SMA requires energy meters placed
    so household loads draw PV energy ahead of the grid-connection point.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h153
    h: 605116649bc1
  - src: src:sma-doc-259463
    loc: sec=h36
    h: 335e0ec8708d
  review: drafted
---
Self-consumption optimization keeps PV energy on site. PV power feeds the building loads first, any surplus charges the battery, and power goes to the grid only once the battery is full and the loads are covered. To set up self-use on the Solis RHI-48ES-5G and S5-EH1P hybrids, open the advanced settings and check that the correct standard is selected. Then pick the battery and the meter placement, set the storage mode to self-use, allow grid charging, and turn backup off if it is not used. In Generac PWRcell Self Supply mode, the inverter tries to hold a zero reading at its CTs, which must be installed and calibrated beforehand. The battery discharges each day down to the MinSocRsrv reserve, which defaults to 30 percent. On SMA battery systems, set the parameter Rise in self-consumption switched on to Yes, then set the battery areas of application. On an SMA hybrid controller, setting both Consumption Limit and Feed-in Limit to 0 gives plain increased self-consumption without peak shaving. The SMA Sunny Home Manager raises self-consumption by switching loads on radio-controlled sockets or Miele devices on and off. It chooses favorable times from the yield forecast and the load profile, and a slider set toward ecological gives the highest self-consumption. FIMER UNO-DM-TL-PLUS-US inverters offer a Self consumption management mode that manages power flows automatically. With the optional COM KIT, the Load Manager Relay can switch a specific load to raise the self-consumption ratio further. Install the energy meters so that household loads can use PV energy before the feed-in point. The result is shown as the self-consumption quota, which is the current ratio of self-consumption to PV power.

<!-- review notes
- sentence 2: support check: partial - The video summary lists the steps (advanced settings, standard, battery, meter placement, self-use, grid charging, disable backup), but the order and 'then' sequencing are not stated and it describes a video, not explicit instructions.
- sentence 5: support check: partial - Sockets and Miele control using yield forecast and load profile, and ecological slider are supported, but the 'highest self-consumption' is stated as the goal of the slider, and the hybrid-controller device isn't relevant; mostly fine, though the claim it 'gives the highest' is paraphrase-level.
- sentence 6: support check: partial - Self consumption mode and Load Manager Relay with optional COM KIT are stated, but the model name UNO-DM-TL-PLUS-US/FIMER is not in the passages.
-->
