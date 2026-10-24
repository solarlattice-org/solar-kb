---
id: concept:energy-arbitrage
type: Concept
name: Energy arbitrage
aliases:
- load shifting
- arbitrage
- HOEP Energy Arbitrage
category: Storage
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:curtailment
  note: One extension of arbitrage is charging storage with low-cost energy during excess renewable generation,
    which reduces renewable curtailment.
  cite:
  - src: src:trn-training-bess-nrel-bess-operating-faqs
    loc: sec=h6
    h: cc6e87105ea7
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:battery-storage
  note: Arbitrage is listed as one of the services a utility-scale battery can provide, with a service
    duration of hours.
  cite:
  - src: src:trn-training-bess-nrel-bess-operating-faqs
    loc: sec=h6
    h: cc6e87105ea7
  - src: src:trn-training-bess-nrel-bess-operating-faqs
    loc: tbl=1.r1
    h: cf8090720bcf
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:load-leveling
  note: Load-levelling is described as the form arbitrage takes in power systems without electricity markets.
  cite:
  - src: src:trn-training-bess-nrel-bess-operating-faqs
    loc: sec=h6
    h: cc6e87105ea7
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:demand-charge
  scope:
    regions:
    - region:us-az
  note: Energy arbitrage appears next to demand charge management as a storage value stream in market
    qualification guides.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-storage-qualification-guide
    loc: tbl=3.r3
    h: 0c109013d0db
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-storage-qualification-guide-2
    loc: tbl=2.r3
    h: 0c109013d0db
  review: drafted
  review_note: 'support check: partial - Value stream lists show Demand Charge Management and Energy Arbitrage,
    but the layout doesn''t clearly state adjacency or region AZ in the passage.'
- claim_id: c5
  rel: related_to
  target: concept:demand-response
  scope:
    regions:
    - region:ca-on
  note: In Ontario, HOEP energy arbitrage is listed next to demand response as a storage value stream.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-storage-qualification-guide
    loc: tbl=18.r3
    h: 248722cdd089
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-storage-qualification-guide-7
    loc: tbl=2.r3
    h: 248722cdd089
  review: drafted
  review_note: 'support check: partial - Demand Response and HOEP Energy Arbitrage appear together in
    the value streams list, but Ontario is not stated in the passage.'
---
Energy arbitrage means charging a battery when energy prices are low and discharging it during more expensive peak hours. For the storage operator this can be a source of income, because electricity prices can change throughout the day. It is a service measured in hours, and it is typically valued in US electricity markets. One extension of arbitrage is charging during periods of excess renewable generation and discharging when demand is high, which reduces curtailment. In power systems without electricity markets, the same idea is called load-levelling: operators charge batteries when there is excess generation and discharge them when there is excess demand. Storage market guides list energy arbitrage as a value stream next to demand charge management and demand response, for example HOEP energy arbitrage in Ontario. Hybrid inverter manuals, such as those for the Solis S6 series, include grid-tied layouts that do energy arbitrage, in some cases with backup.

<!-- review notes
- sentence 6: support check: partial - Lists include energy arbitrage with demand charge management and demand response, but Ontario is not stated, and the two lists are from different guides.
- sentence 7: support check: partial - Evidence shows Solis S6 hybrid energy arbitrage layouts and one with backup, but the generic claim about hybrid inverter manuals is only illustrated by Solis.
-->
