---
id: stressor:transport-damage
type: Stressor
name: Transport damage
aliases:
- transportation/handling errors
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 1.5
    unit: unit:PERCENT
  conditions: Maximum Pmax change after truck transport simulation (ASTM D4169/4728) of two complete module
    shipping stacks
  quote: resulted in changes of the electrical power at a maximum degradation of ΔpMAX= 1.5%
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.1.2
    h: 965925e2642f
  review: drafted
  review_note: 'support check: partial - Passage gives a maximum degradation of 1.5% after transport simulation
    of two stacks, but this is a maximum, not a ''typical'' value.'
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 2.8
    unit: unit:PERCENT
  conditions: Pmax degradation after transport simulation followed by environmental tests (100 thermal
    cycles and dynamic wind loads)
  note: Lab test sequence, not field data; the follow-on tests did not worsen the mechanical failures
    from transport.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=7.1.2
    h: 965925e2642f
  review: drafted
  review_note: 'support check: partial - Passage says power degradation up to 2.8% after transport plus
    thermal cycling and dynamic loads, and that the follow-on tests did not worsen mechanical failures,
    but it is an upper bound and not a typical value; the ''lab test, not field'' note is implied.'
---
Transport damage is mechanical harm done to modules by vibrations and shocks while they are shipped, and it can break the front glass or crack cells inside the laminate. Common causes are a module falling over, a pallet that is not stiff enough touching the bottom module, and transport corners so tight that a module lifts and drops when the one above it is removed. Someone stepping on a module is another cause. Cells can crack even during normal transport in well-designed containers. Broken glass is easy to trace back to transport, but transport cell cracks are usually not visible. A power check right after the damage often misses them, so electroluminescence or lock-in thermography is needed to find them. Cells cracked in transport or a backsheet damaged in handling can later combine with shading, open bypass diodes or reverse current. Parts weakened this way can break and overheat, which leaves burn marks. In a lab truck transport simulation, a few modules showed single cell cracks, but the power loss at STC was small. To reduce exposure, avoid mechanical stress during transport and installation and keep watch on cracked modules in case the cracks spread. Also look for handling as a root cause when you find broken glass. Inspect equipment for shipping damage as soon as it arrives. If rough handling is evident, file a claim with the carrier right away.
