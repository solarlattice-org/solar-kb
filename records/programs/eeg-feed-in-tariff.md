---
id: prog:eeg-feed-in-tariff
type: Program
name: EEG feed-in tariff
aliases:
- EEG remuneration
- EEG 20-year feed-in
- EEG subsidy
- FIT scheme
category: Incentive
program_kind: incentive
claims:
- claim_id: c1
  attr: warranty_term
  value:
    nominal: 20
    unit: unit:YR
  scope:
    regions:
    - region:de
  conditions: Duration of the statutory EEG funding for a PV system, counted from installation
  cite:
  - src: src:sma-kb-ue20
    loc: sec=h1
    h: 2654a34e2c6f
  review: drafted
  review_note: 'support check: partial - The passage says EEG funding for PV systems lasts 20 years, but
    it doesn''t say the term is counted from installation (it only implies this) and it doesn''t call
    the term a warranty.'
- claim_id: c2
  rel: applies_to
  target: region:de
  note: Statutory feed-in remuneration under the German Renewable Energy Sources Act (EEG)
  cite:
  - src: src:sma-kb-ue20
    loc: sec=h1
    h: 2654a34e2c6f
  - src: src:sma-doc-278879
    loc: sec=h93
    h: aa851dc0134d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
The EEG feed-in tariff is the payment guaranteed by law under Germany's Renewable Energy Sources Act (EEG) for electricity that PV systems feed into the grid. The funding runs for 20 years, so the earliest PV systems stopped receiving it at the end of 2020. Once a system is more than 20 years old, it no longer gets the usual guaranteed payment for the energy it exports. Such systems are often called UE20 systems. Under EEG 2021, these systems may keep running after their funding ends. SMA offers a German-language planning guide on options for them. A German FNN note says that systems eligible for EEG or KWKG remuneration must not feed energy from storage units into the public grid. On SMA systems, this means the Consumption Limit value must not be set to a negative number. In Sunny Portal with a Sunny Home Manager, the installer enters the feed-in tariff per kWh under the PV system properties. The portal uses this value for load control and recommended actions.

<!-- review notes
- sentence 5: support check: partial - The FNN note and the rule that the Consumption Limit input must not be negative are stated, but the passages don't say 'SMA systems', and 'public grid' is a minor paraphrase.
-->
