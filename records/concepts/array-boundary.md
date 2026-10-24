---
id: concept:array-boundary
type: Concept
name: Array boundary
aliases:
- inside the array boundary
- outside the array boundary
category: Safety
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: func:rapid-shutdown
  note: The array boundary decides which rapid shutdown voltage limits apply to controlled conductors.
  cite:
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h8
    h: f17153ed396e
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h64
    h: 1ad7e6a2a61c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c2
  rel: related_to
  target: req:nfpa-70-2017-690-12-b-2
  note: Inside the boundary, the options are a listed rapid shutdown PV array, or controlled conductors
    limited to 80 V within 30 s, or the exemption for arrays with no exposed wiring or conductive parts.
  cite:
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h8
    h: f17153ed396e
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h36
    h: 492035765b4e
  review: drafted
- claim_id: c3
  rel: related_to
  target: comp:pv-array
  note: The boundary is measured from the array in all directions.
  cite:
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h64
    h: 1ad7e6a2a61c
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h8
    h: f17153ed396e
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:ul-3741
  note: A Solis guide describes an upper array that meets the inside-boundary requirement through a UL
    3741 listing without MLPEs.
  cite:
  - src: src:solis-ul3741-commercial-implementation-guide-pe-tb-0001-r00
    loc: sec=h19
    h: e20bdf616837
  review: drafted
- claim_id: c5
  rel: related_to
  target: arch:module-level-power-electronics
  note: In the guide's example, MLPEs control the circuits on a lower sub-array to meet 690.12(B)(1) and
    (B)(2).
  cite:
  - src: src:solis-ul3741-commercial-implementation-guide-pe-tb-0001-r00
    loc: sec=h19
    h: e20bdf616837
  review: drafted
- claim_id: c6
  rel: related_to
  target: hazard:electric-shock
  note: Rapid shutdown, which is organized around the array boundary, reduces shock hazard for emergency
    responders.
  cite:
  - src: src:std-standards-nec-2017-nec-2017-690-solar
    loc: sec=h8
    h: f17153ed396e
  review: drafted
---
The array boundary is a term from the NEC rapid shutdown rules: the zone extending 305 mm (1 ft) from the PV array in all directions. Where a controlled conductor sits relative to this boundary decides which rapid shutdown limit applies to it: 690.12(B)(1) outside, 690.12(B)(2) inside. Outside the boundary, or more than 1 m (3 ft) past the point of entry into a building, controlled conductors must drop to 30 volts or less within 30 seconds of rapid shutdown initiation. Voltage is measured between any two conductors and between any conductor and ground. Inside the boundary, the system can use a listed or field-labeled rapid shutdown PV array. Otherwise, controlled conductors must drop to 80 volts or less within 30 seconds. In one manufacturer's commercial guide, the inverter DC input circuits stay inside the array boundary. The AC output circuits run outside it and meet the outside-boundary limit once the AC breaker or AC disconnect is opened. Ways to comply include module-level power electronics or a UL 3741 listed array, and sub-arrays can be kept within the same array boundary. The purpose of rapid shutdown is to reduce shock hazard for emergency responders working on buildings with PV.

<!-- review notes
- sentence 4: support check: partial - The listed or field-labeled rapid shutdown array option and the 80 V in 30 s option are stated, but the statement omits the third exemption, and the 80 V limit is tied to the boundary or 1 m from the penetration point.
- sentence 4: review: partial - The listed or field-labeled rapid shutdown array option and the 80 V within 30 s limit are both stated, but 'otherwise' leaves out the third option (the exemption for arrays with no exposed wiring or conductive parts) and leaves out…
-->
