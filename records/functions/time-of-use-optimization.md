---
id: func:time-of-use-optimization
type: Function
name: Time-of-use optimization
aliases:
- TOU mode
- price-optimised charging
- dynamic tariff optimisation
- energy arbitrage mode
- TOU
- TOU-SCD
- Energy Arbitrage
- price-optimised battery charging
- Peak-Valley Arbitrage mode
- TOU scheduling
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  rel: requires
  target: prod:generac-pwrcell-battery
  note: Generac PWRcell TOU energy management through the REbus Beacon needs a PWRcell Battery in the
    system.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h117
    h: c1bc5b9108e2
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: sec=h105
    h: 15224b3a4312
  review: drafted
- claim_id: c2
  rel: requires
  target: proto:ethernet
  note: Generac PWRcell TOU needs a reliable Internet connection over Ethernet to a router.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h117
    h: c1bc5b9108e2
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: sec=h105
    h: 15224b3a4312
  review: drafted
- claim_id: c3
  rel: requires
  target: tool:solis-soliscloud
  note: Solis TOU-SCD and Solis AI control the storage through the SolisCloud platform; TOU-SCD is off
    by default and is enabled by a support ticket.
  cite:
  - src: src:kb-solis-44002545113-soliscloud-smart-charge-discharge-function
    loc: sec=h1
    h: eee52baaee60
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: drafted
  review_note: 'support check: partial - TOU-SCD controls storage through SolisCloud and is off by default,
    enabled via a support ticket; Solis AI''s use of SolisCloud is shown only via monitoring/Timed plans,
    and ''requires'' is implied rather than stated.'
- claim_id: c4
  rel: requires
  target: prod:sma-sunny-home-manager-2
  conditions: SMA price-optimised battery charging; Sunny Home Manager 2.0 must run firmware version 2.18.XX
  cite:
  - src: src:sma-kb-optimale-einstellungen-f-r-die-nutzung-dynamischer-strompreise-mit-dem-sunny-home-m
    loc: sec=h1
    h: 83824a4ed36b
  review: drafted
- claim_id: c5
  rel: requires
  target: tool:sma-sunny-portal
  note: All settings for SMA price-optimised charging are made in Sunny Portal powered by ennexOS.
  cite:
  - src: src:sma-kb-optimale-einstellungen-f-r-die-nutzung-dynamischer-strompreise-mit-dem-sunny-home-m
    loc: sec=h1
    h: 83824a4ed36b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c6
  rel: requires
  target: func:battery-grid-charging
  note: For Solis AI, enabling battery charging from the grid is strongly recommended.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: drafted
  review_note: 'review: partial - The passage says grid charging is ''strongly recommended'' for Solis
    AI to function properly, which matches the note, but it does not say time-of-use optimization in general
    ''requires'' grid charging.'
---
Time-of-use optimization charges the battery when electricity is cheap and discharges it when prices are high, which lowers the customer's energy costs. On Generac PWRcell systems, the REbus Beacon provides TOU energy management. It needs a PWRcell Battery and an Ethernet Internet connection, and the Beacon should be enabled only when TOU scheduling is used. To set up the Generac TOU schedule, open Mod. Settings on the Beacon device page, enter the access code, then set the TOU Schedule code and the time zone and save. The display then shows when the next mode change will happen. Solis TOU-SCD pulls day-ahead prices from Nordpool or Octopus. It charges the battery from the grid when the price is below a user-set threshold and discharges it when the price is above another threshold. It is off by default and is switched on through a support ticket. Solis advises that if feed-in power earns no payment in your territory, the system should be set never to discharge based on price. Some older 5G and S5 single-phase low-voltage models do not support TOU-SCD. Solis AI and the semi-automatic Peak-Valley Arbitrage mode in SolisCloud control the battery from dynamic tariffs. They respect the set import and export limits and limit export when prices are negative. With the SMA Sunny Home Manager 2.0, price-optimised charging is set up in Sunny Portal: choose the Economical optimisation target and enable predictive battery charging. Time-slot charging, load peak capping, Modbus battery control and EEBUS communication switch off or restrict this function. CPS single-phase hybrid inverters have a TOU function that selects a different running mode for each day and hour of the year.

<!-- review notes
- sentence 4: support check: partial - Day-ahead prices from Nordpool/Octopus, thresholds, off by default and ticket enabling are stated, but the grid-charging below one threshold and discharging above another is only an example setting, and the exact behavior is user-configured.
- sentence 5: support check: partial - Never-discharge advice is stated, and 5G/S5 single-phase low-voltage models are listed as not supported, but 'older' is an unstated characterization.
- sentence 6: support check: partial - Solis AI respects import/export limits, and Peak-Valley mode limits injection at negative rates and uses dynamic tariffs; but the import limit is stated for Peak-Valley only as charge power, and export-limit respect is stated only for Solis AI.
-->
