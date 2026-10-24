---
id: prod:sma-sb-tl-21
type: Product
name: Sunny Boy 3000-5000TL-21
aliases:
- SB-TL-21
- SB 3000TL-21
- SB 3600TL-21
- SB 4000TL-21
- SB 5000TL-21
- SB3000TL-21
- Sunny Boy 3000TL
- Sunny Boy 3600TL
- Sunny Boy 5000TL
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  note: Listed among SMA's Sunny Boy inverter manuals as SB3000TL-21 / SB3600TL-21 / SB4000TL-21 / SB5000TL-21.
  cite:
  - src: src:sma-kb-sunny-boy-manuals
    loc: sec=h1
    h: 21d1434a3c94
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - The page lists the SB3000TL-21 to SB5000TL-21 among SMA''s Sunny
    Boy manuals, but it doesn''t explicitly say SMA makes them. The SMA service site implies it.'
- claim_id: c2
  rel: uses_protocol
  target: proto:speedwire
  note: SB 3000TL-21, SB 3600TL-21 and SB 5000TL-21 are listed as inverters with a multifunction relay
    and Speedwire as the communication standard.
  cite:
  - src: src:sma-doc-278405
    loc: tbl=39.r6
    h: 20a986f90dbc
  - src: src:sma-doc-278405
    loc: tbl=39.r3
    h: 6186f48e2f5a
  - src: src:sma-doc-278405
    loc: tbl=39.r4
    h: 1056cba61adf
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The Sunny Boy 3000-5000TL-21 is a family of SMA single-phase string inverters that includes the SB3000TL-21, SB3600TL-21, SB4000TL-21 and SB5000TL-21. SMA still lists manuals for this family among its current Sunny Boy documents, while the older TL-20 generation appears with the archived manuals. One SMA compatibility table lists the TL-21 models as inverters with a multifunction relay that use Speedwire as their communication standard. Another SMA compatibility table groups the SB 3000TL-21 to SB 6000TL-21 together and gives inverter firmware 2.00.00.R as the minimum version for support. Before you connect the inverter to an SMA communication or energy-management product, check that its firmware is at or above that version.

<!-- review notes
- sentence 1: support check: partial - The passage lists the four models together as a Sunny Boy group, but it doesn't say they are single-phase string inverters. It only says they are in a string inverter category.
- sentence 5: support check: partial - The table gives the minimum firmware version, but it doesn't say to check it before connecting the inverter to a communication or energy-management product. That instruction is an inference.
- sentence 1: review: partial - The four TL-21 models are listed together under Sunny Boy and tagged 'String Inverters', but the passage never says they are single-phase.
-->
