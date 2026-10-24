---
id: prog:sma-repowering
type: Program
name: SMA Repowering
aliases:
- SMA Repowering Component package
- repowering team
- Repowering Component
category: Service
program_kind: service
claims:
- claim_id: c1
  rel: issued_by
  target: org:sma
  cite:
  - src: src:sma-kb-is-it-possible-to-repower-sma-trafo-inverters
    loc: sec=h1
    h: 39ea8049d591
  - src: src:sma-kb-can-you-repower-a-plant-with-trafo-inverters-of-other-manufacturers
    loc: sec=h1
    h: 9627b03c9b42
  - src: src:sma-kb-how-can-a-new-inverter-be-integrated-into-an-existing-communication-system
    loc: sec=h1
    h: fd9da736375e
  review: drafted
- claim_id: c2
  rel: applies_to
  target: arch:grounded-pv-array
  negated: true
  note: SMA's article on repowering plants that use other manufacturers' Trafo inverters says repowering
    is not possible when the plant needs grounding.
  cite:
  - src: src:sma-kb-can-you-repower-a-plant-with-trafo-inverters-of-other-manufacturers
    loc: sec=h1
    h: 9627b03c9b42
  review: drafted
---
SMA Repowering is an SMA service that gets existing Trafo inverters working again by replacing modules inside them, using the Repowering Component package. To get an offer, contact the SMA repowering team by email or call the SMA Service Line. For plants with Trafo inverters from other manufacturers, the repowering team handles technical questions, but repowering is not possible if the plant needs grounding. There are no standard solutions for connecting a new inverter to an existing communication system during repowering, so each case is worked out individually with the repowering team. System compatibility used to be checked with the SMA Repowering App. That app has been removed from the app stores, and SMA plans to move its functions into the SMA 360° App and the SMA website.

<!-- review notes
- sentence 1: support check: partial - The passage says the inverter can be made functional again by replacing modules via the 'Repowering Component' package, but it doesn't call this a service or say the modules are inside the inverters. It's about SMA Trafo inverters.
- sentence 5: support check: partial - The passage says compatibility can be checked with the SMA repowering app, but 'used to be' is only supported by the other article saying the app is no longer available.
-->
