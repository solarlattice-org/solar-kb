---
id: concept:dynamic-tariff
type: Concept
name: Dynamic electricity tariff
aliases:
- dynamic tariff
- real-time pricing
- dynamic energy contract
- RTP
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:energy-arbitrage
  note: Solis Peak-Valley Arbitrage mode charges the battery below one price threshold and exports above
    another, using dynamic tariffs.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: drafted
- claim_id: c2
  rel: related_to
  target: func:battery-grid-charging
  note: With dynamic tariffs, the system can charge the battery from the grid when prices are low or negative.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c3
  rel: related_to
  target: stressor:negative-pricing
  note: Dynamic prices can go negative. The inverter then limits export to 0 W, or shuts down PV completely
    below the negative offset.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  rel: related_to
  target: func:export-limitation
  note: Export is automatically limited when dynamic prices are negative.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: related_to
  target: concept:time-of-use-rate
  note: The Solis Cloud tab that shows dynamic prices is labelled TOU Tariff (Dynamic Tariff).
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:feed-in-tariff
  note: A feed-in rate can be set as the market price plus an offset, for example the pure EPEX price.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: drafted
- claim_id: c7
  rel: related_to
  target: tool:solis-soliscloud
  note: Dynamic tariff settings and daily prices are configured and viewed in Solis Cloud.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: drafted
- claim_id: c8
  rel: related_to
  target: func:time-of-use-optimization
  note: Smart control runs appliances and charges the battery during the cheapest hours.
  cite:
  - src: src:kb-solis-44002688537-inverter-control-solis-ai-more
    loc: sec=h1
    h: f0aea101b8c9
  review: drafted
---
A dynamic electricity tariff is an energy contract in which the price changes every hour or every quarter hour instead of staying fixed. Prices often come from the day-ahead market, such as the EPEX price. The next day's rates are loaded automatically into the energy management system. The raw market price can be adjusted with a coefficient or a fixed amount to cover extra costs such as transport charges or VAT. Purchase and feed-in rates can each have their own offset. With a battery, the system can charge from the grid when prices are low or negative and discharge or export when prices are high. This is the basis of energy arbitrage. When prices turn negative, the inverter can limit export to zero or shut PV down completely to avoid extra costs. This means a planned power limit is not necessarily a fault. Some revenue meters have a real-time pricing mode. While a control signal or input is active, the meter keeps a second, separate set of energy and demand totals. Home energy managers also use the tariff data you enter to plan load control and recommended actions. Related concepts include time-of-use rates, feed-in tariffs and self-consumption.

<!-- review notes
- sentence 1: support check: partial - Passage says dynamic contract prices change every hour/quarter, but does not explicitly contrast with fixed prices (though fixed rate is mentioned separately).
- sentence 4: support check: partial - Charging at low/negative prices and discharging/exporting at high prices is stated, but the passage does not call it the basis of energy arbitrage (only names the Peak-Valley Arbitrage mode).
- sentence 5: support check: partial - Limiting export or shutting PV down under negative prices to avoid costs is stated, but the claim that a planned limit is not a fault is not stated.
- sentence 7: support check: partial - Tariff values affect recommended actions and load control, but time-of-use rates and feed-in tariff/self-consumption as related concepts are only loosely supported (feed-in and self-consumption tariffs appear; TOU not).
- sentence 7: review: partial - SMA says the tariff values entered drive recommended actions and Sunny Home Manager load control, and feed-in and self-consumption tariffs appear, but time-of-use rates as a related concept are not in the passages.
-->
