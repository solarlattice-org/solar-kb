---
id: proto:sunspec-model-160
type: Protocol
name: SunSpec model 160 Multiple MPPT Inverter Extension Model
aliases:
- SunSpec 160
- model 160
- mppt
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: SolarEdge's SunSpec implementation note gives it model ID 160 in the SunSpec register map.
  cite:
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h40
    h: ce50d850a6f6
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: tbl=8.r2
    h: 62b50a67e448
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Model 160 ID value and name in SolarEdge''s map are stated, but
    the passages don''t say it is part of the SunSpec information models family explicitly (implied only).'
---
SunSpec model 160 is the Multiple MPPT Inverter Extension Model. It is an information model that reports data for each maximum power point tracker input of an inverter. SolarEdge supports model 160 on its Synergy inverters running firmware 4.13.xx or later. In the SolarEdge register map, the model ID register holds the value 160. It sits at address 40121 when counting from 0, or 40122 when counting from 1, and the model length register comes right after it. The model repeats one block for each Synergy unit, starting with Synergy Unit #0 and then Synergy Unit #1. Each block has an input ID and an eight-register input ID string. SolarEdge does not support some points in this model, including TmsPer, DCWH, DCSt and DCEvt, and these points read as 0.

<!-- review notes
- sentence 1: support check: partial - Name and ID are given, but the passages don't state it reports data per MPPT input of an inverter beyond the name implying it.
- sentence 4: support check: partial - Synergy Unit #0 and #1 blocks with ID and 8-size IDStr are shown, but the passages don't say the model repeats a block per unit or that only two exist; the IDStr of unit #1 isn't shown.
- sentence 1: review: partial - The name and model ID 160 are stated, but that it reports data for each MPPT input is only implied by the name.
- sentence 4: review: partial - The rows show ID registers for Synergy Unit #0 and #1 and an 8-register IDStr, but they don't state that the model repeats one block per unit, and an IDStr is shown only after Unit #0.
-->
