---
id: concept:ampacity
type: Concept
name: Ampacity
aliases:
- conductor ampacity
- current-carrying capacity
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:overcurrent-protection
  note: The rating of the overcurrent protective device is one of the inputs that set the required conductor
    ampacity.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h102
    h: 411df3b860c3
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:short-circuit-current
  note: Rated module Isc values are used when sizing PV circuit conductors and overcurrent devices.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h70
    h: 0e13bed67f14
  review: drafted
---
Ampacity is a conductor's current-carrying capacity: the current it can carry continuously under its conditions of use. The ampacity a conductor needs depends on the maximum circuit current, the size of the overcurrent device, the ambient temperature, the conductor and insulation type, conduit fill, and any limits set by the terminals. Ampacity also changes with conductor material and size. For example, one design table lists aluminum conductors at 75 °C, with size 4 rated at 65 A and size 4/0 at 180 A. Wire sizing in PV systems is among the most complex because many factors must be considered, and rated module short-circuit current is used to size PV circuit conductors. Ampacity calculations should be checked against the NEC articles on overcurrent protection, conductors and PV systems.

<!-- review notes
- sentence 1: support check: partial - Passages call ampacities 'current-carrying capacities' but do not state the 'carry continuously under conditions of use' definition.
- sentence 5: support check: partial - u9 cites NEC Articles 240, 310, and 690 for confirming conductor ampacity calculations, but the article topics (overcurrent, conductors, PV) are not stated and the u2 passage cites Article 480.
-->
