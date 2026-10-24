---
id: concept:dc-link
type: Concept
name: DC link
aliases:
- intermediate circuit
- DC bus
category: Inverters
concept_kind: electrical
claims:
- claim_id: c1
  rel: part_of
  target: comp:inverter-bridge
  note: The fault text names the DC link of the inverter bridge.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r12
    h: 6ae12d09ad40
  review: drafted
- claim_id: c2
  rel: explains
  target: symptom:dc-bus-overvoltage
  note: Inverters report DC link overvoltage as a fault or alarm, which can have internal or external
    causes.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h516
    h: 749a6098bfa9
  - src: src:eq-equip-inverters-abb-mfa-scada-modbustcp-link-ds-magnolia-default
    loc: tbl=49
    h: 77476d8807e8
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r12
    h: 6ae12d09ad40
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:precharge-circuit
  note: The DC link has a pre-charging circuit.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:precharge-circuit-failure
  note: One error message reports that the DC link pre-charging circuit is defective.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r10
    h: adcbdb84beb6
  review: drafted
---
The DC link is the internal DC stage of an inverter that feeds the inverter bridge. The inverter monitors the DC link and reports a fault when it detects overvoltage there. The cause can be inside the inverter or outside it. Central inverters can report DC link overvoltage as its own alarm bit over SCADA, separate from the DC input overvoltage alarm. The DC link is charged through a pre-charging circuit before operation. Inverters flag both a defective pre-charging circuit and a DC link that could not be charged enough. For these DC link faults, the corrective step given is to contact the manufacturer's service line.

<!-- review notes
- sentence 1: support check: partial - The passage mentions the DC link of the inverter bridge, but it does not say the DC link is an internal DC stage that feeds the bridge.
- sentence 4: support check: partial - Both the defective pre-charging circuit and the DC link that could not be charged enough are flagged, but no passage says the DC link is charged through a pre-charging circuit before operation.
-->
