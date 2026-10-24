---
id: concept:feed-in-tariff
type: Concept
name: Feed-in tariff
aliases:
- FIT
- feed-in remuneration
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:self-consumption
  note: A pure feed-in system exports all PV energy to earn the tariff instead of using it on site; energy
    management software can take a separate self-consumption tariff alongside the feed-in tariff.
  cite:
  - src: src:sma-doc-259463
    loc: sec=h37
    h: 3c12068ee416
  - src: src:sma-doc-246498
    loc: sec=h376
    h: fbdf27194d31
  review: drafted
  review_note: 'support check: partial - Passages show a feed-in system exports all PV energy for the
    tariff and a separate self-consumption tariff can be entered, but ''energy management software'' wording
    is implicit and the link is loosely stated.'
- claim_id: c2
  rel: related_to
  target: comp:energy-meter
  note: In a feed-in system, the energy meter has to be placed so that household loads cannot use PV energy
    directly.
  cite:
  - src: src:sma-doc-259463
    loc: sec=h37
    h: 3c12068ee416
  review: drafted
---
A feed-in tariff is the payment the PV system operator gets for energy fed into the utility grid. A feed-in system is set up to export all of the PV energy it generates so the operator earns this tariff. Exporting everything makes sense when the feed-in tariff is well above the price of buying power from the grid. In that case, energy management adds little value. In a feed-in system, place the energy meter so that household loads cannot use the PV energy directly. Some inverters let you enter the feed-in tariff as a rate per unit of energy fed into the grid. The default value depends on the country setup. In SMA energy management, you enter the feed-in tariff per kWh with a currency, along with a self-consumption tariff and electricity tariffs. These values must be set before some functions can be used. The abbreviation FIT is common in O&M guidelines and inverter manuals.

<!-- review notes
- sentence 7: support check: partial - Passages show FIT means feed-in tariff in acronym keys, but not that it is common in O&M guidelines and inverter manuals specifically.
- sentence 7: review: partial - One O&M guideline and one inverter manual each list FIT as Feed-in tariff, but two instances do not show the abbreviation is 'common' in those document types.
-->
