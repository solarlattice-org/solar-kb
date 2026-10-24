---
id: concept:virtual-power-plant
type: Concept
name: Virtual power plant
aliases:
- VPP
- virtual multimegawatt power plant
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:demand-response
  note: Joining a VPP lets the site earn demand response revenue.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-stem-overview-booklet-c-i-9
    loc: sec=h10
    h: 336b20eadd9a
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-stem-overview-booklet-c-i-9-2
    loc: sec=h9
    h: 336b20eadd9a
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:distributed-energy-resource
  note: Neighborhoods of small residential PV systems (distributed generation) add up to a virtual power
    plant several megawatts in size.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=1
    h: 6071f58ccb27
  review: drafted
- claim_id: c3
  rel: related_to
  target: arch:rooftop-pv
  note: Residential rooftop PV systems in a neighborhood add up to a virtual power plant.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=1
    h: 6071f58ccb27
  review: drafted
- claim_id: c4
  rel: related_to
  target: org:stem
  note: Stem gives its partners access to its virtual power plant network.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-stem-overview-booklet-c-i-9
    loc: sec=h10
    h: 336b20eadd9a
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-misc-collateral-the-stem-pa
    loc: sec=h7
    h: 7609af7ab4aa
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
A virtual power plant, or VPP, is a group of many small distributed systems that together act like one larger power plant. For example, small residential PV systems in some neighborhoods add up to virtual power plants of several megawatts. Commercial sites with battery storage can join a VPP and earn demand response revenue without disrupting their operations. VPPs are promoted as a way to avoid building new carbon-emitting generation, improve reliability and cut emissions across a community. Good monitoring and fault detection matter for a VPP: they help the grid manager forecast what the neighborhood will produce, raise its availability and lower its forced outage rate. Related concepts include demand response and distributed energy resources.

<!-- review notes
- sentence 1: support check: partial - Passages say small residential systems aggregate to a VPP, but no explicit definition of a VPP acting like one larger plant.
- sentence 3: support check: partial - VPP, DR revenue and no operational disruption are stated, but commercial sites with battery storage are not mentioned.
- sentence 6: support check: partial - Demand response is tied to VPPs and distributed generation is linked to the VPP neighborhood, though the passages never state a general 'related concepts' relation to the DER concept.
-->
