---
id: prog:solarcoin
type: Program
name: SolarCoin
aliases:
- SolarCoin reward
- SolarCoin grants
category: Incentive
program_kind: incentive
claims:
- claim_id: c1
  rel: issued_by
  target: org:solarcoin-foundation
  cite:
  - src: src:sma-kb-solarcoin-claim-rejection-or-refusal-by-solarcoin-foundation
    loc: sec=h1
    h: c6dae177f01f
  - src: src:sma-kb-solarcoins-on-sunny-portal
    loc: sec=h1
    h: 4e77dd24d230
  - src: src:sma-kb-how-many-solarcoins-can-be-earned-per-mwh
    loc: sec=h1
    h: 783990b3b6e3
  review: drafted
  review_note: 'support check: partial - Passages say the Foundation grants/rewards SolarCoin (1 per MWh),
    but never state it ''issues'' the coin in a way beyond granting; roughly supported by grants wording.'
- claim_id: c2
  rel: applies_to
  target: prod:sma-sunny-home-manager
  note: Plants linked to Sunny Portal through a Sunny Home Manager can claim SolarCoins; Home Managers
    with Bluetooth inverters connected through WebConnect are named as eligible.
  cite:
  - src: src:sma-kb-solarcoins-on-sunny-portal
    loc: sec=h1
    h: 4e77dd24d230
  - src: src:sma-kb-which-systems-can-earn-solarcoins
    loc: sec=h1
    h: b0214a915455
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-webbox
  note: Plants linked to Sunny Portal through a Sunny WebBox can get the reward; SMA does not advise claiming
    through systems that do not use WebConnect.
  cite:
  - src: src:sma-kb-solarcoins-on-sunny-portal
    loc: sec=h1
    h: 4e77dd24d230
  review: drafted
- claim_id: c4
  attr: warranty_term
  value:
    nominal: 35
    unit: unit:YR
  conditions: Period over which the SolarCoin Foundation plans to keep distributing SolarCoin, as of the
    November 2022 article
  cite:
  - src: src:sma-kb-solarcoin-claim-rejection-or-refusal-by-solarcoin-foundation
    loc: sec=h1
    h: c6dae177f01f
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: warranty_term
  value:
    nominal: 40
    unit: unit:YR
  conditions: Overall length of the SolarCoin Foundation mission
  cite:
  - src: src:sma-kb-solarcoin-claim-rejection-or-refusal-by-solarcoin-foundation
    loc: sec=h1
    h: c6dae177f01f
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
---
SolarCoin is a free reward that the SolarCoin Foundation grants to solar energy producers for the clean energy they generate. The grants are non-recourse. The Foundation grants 1 SolarCoin per 1 MWh, so a 5 kWp system earns about 5 coins a year. SMA plants connected to Sunny Portal through Webconnect, a Sunny Home Manager or a Sunny WebBox can claim SolarCoins. SMA does not advise claiming through systems that do not use WebConnect. To register, a user with admin rights logs in to Sunny Portal, fills in the plant address and the owner/operator and installer fields, then ticks the consent box for the SolarCoin program under Data Releases and saves. A system registered through Sunny Portal must not also be registered with the Foundation or the SolarCoin Explorer, because a duplicate registration blocks participation. You no longer need a wallet to claim, and the wallet ID field in Sunny Portal must stay empty. The Foundation holds the coins until the user redeems them. SolarCoin has moved to the Ethereum-based Energy Web Chain, and claims may take longer to process during the migration. The Foundation can refuse a grant without giving a reason. Possible reasons include unsupported countries, incomplete data, missing power of attorney documents, duplicate claims and suspected fraud.

<!-- review notes
- sentence 7: support check: partial - u2 says wallet software is replaced by Energy Web Chain (Ethereum-based) and u8 says claims take longer during migration, but 'has moved' is only implied.
-->
