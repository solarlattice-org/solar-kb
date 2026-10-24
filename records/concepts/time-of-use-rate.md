---
id: concept:time-of-use-rate
type: Concept
name: Time-of-use rate
aliases:
- TOU
- time-of-use tariff
- time-of-use pricing
- Time of Use
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: func:time-of-use-optimization
  note: A battery function can be scheduled to charge in low-cost periods and discharge when energy costs
    are high. It is usable only in battery storage systems.
  cite:
  - src: src:sma-doc-278879
    loc: sec=h206
    h: c291453bc4cb
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:battery-storage
  note: Time-of-use savings come from charging the battery cheaply and discharging it during expensive
    periods.
  cite:
  - src: src:sma-doc-278879
    loc: sec=h206
    h: c291453bc4cb
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:energy-meter
  note: 'Revenue meters can do TOU metering: they record energy and demand per rate period and show the
    active TOU rate and season.'
  cite:
  - src: src:sel-735-im-20250228
    loc: sec=h414
    h: 44f5090e058f
  - src: src:eq-equip-meters-ge-kv2c-meters-metermate-5-51-files-software-instruction-manuals-geh-5082x-mmprofile
    loc: sec=h483
    h: f34ff04c3b7e
  - src: src:eq-equip-meters-ion-8650-ion-8650-user-guide
    loc: tbl=65
    h: '730971e13202'
  review: drafted
  review_note: 'support check: partial - Passages show TOU metering, rate selection and active TOU rate/season
    screens on meters, but do not say energy and demand are recorded per rate period or that these are
    revenue meters in this passage.'
---
A time-of-use rate is a utility tariff where the price of grid electricity depends on the time of day, so energy costs most during certain periods. Utilities are moving the expensive TOU periods later into the afternoon and evening. At those times solar output falls, peaker plants come online and the grid is under more stress. Storage systems can lower energy costs under a TOU rate by charging the battery during cheap periods and discharging it when prices are high. On some SMA systems these periods are set as schedules in the LCS-Tool. SMA advises leaving this Time of Use function off in PV-only plants, because it only works when a battery is present. TOU meters split energy and demand by rate period, labeled Rate A, Rate B and so on. Some meters also show the active TOU rate and season on the front panel. Home energy displays can colour-code the grid purchase tariff, showing red for expensive periods and green for good-value ones. This helps owners move consumption to cheaper times.

<!-- review notes
- sentence 2: support check: partial - Passage says TOU periods shift later, the sun sets, peaker plants and grid stress rise; it does not literally say solar output falls, though the sunset implies it.
- sentence 5: support check: partial - Rate A–D periods and front-panel active TOU rate/season screens are present, and TOU metering of energy and demand is named, but splitting by rate period is only implied.
- sentence 6: support check: partial - Passage states red is expensive and green is good value for the purchase tariff, but not that this helps owners shift consumption.
-->
