---
id: concept:area-eps
type: Concept
name: Area electric power system
aliases:
- Area EPS
- Local EPS
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: subclass_of
  target: concept:electric-power-system
  note: Area EPS is defined as an EPS that serves Local EPSs; the EPS covers both the area EPS and the
    local EPS.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=3.1
    h: 68ae59f1e15e
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:local-electric-power-system
  note: The Area EPS serves Local EPSs; a Local EPS sits within one premises or group of premises and
    is usually customer-owned.
  cite:
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=3.1
    h: 68ae59f1e15e
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c3
  rel: related_to
  target: concept:point-of-common-coupling
  note: The PCC is where the Area EPS and the Local EPS connect.
  cite:
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:islanding
  note: An island is a part of the Area EPS that is cut off from the rest of the Area EPS and energized
    only by Local EPSs.
  cite:
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:distributed-energy-resource
  note: Interconnection is the process of adding DER to an Area EPS.
  cite:
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  review: drafted
- claim_id: c6
  rel: related_to
  target: role:area-eps-operator
  note: This is the entity that designs, builds, operates and maintains the Area EPS.
  cite:
  - src: src:std-standards-ieee-ieee1547
    loc: sec=3.1
    h: e8ed72d87b6b
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=3.1
    h: 68ae59f1e15e
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:cease-to-energize
  note: The DER must cease to energize the Area EPS when there are faults on the Area EPS circuit it is
    connected to.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=6.2.1
    h: 0059dd9068ea
  - src: src:std-standards-ieee-ieee1547
    loc: sec=4.2.1
    h: 225f360a8595
  review: drafted
---
The Area electric power system, or Area EPS, is an electric power system that serves Local EPSs. It usually belongs to and is run by the distribution utility, while the Local EPS on the customer premises usually belongs to the customer. An Area EPS typically has primary access to public rights-of-way and is subject to regulatory oversight. The Area EPS and the Local EPS meet at the point of common coupling, and adding a distributed energy resource to the Area EPS is called interconnection. For short-circuit faults on the Area EPS circuit section it is connected to, the DER must cease to energize and trip unless the Area EPS operator specifies otherwise. A DER can make utility fault detection less sensitive, so protection settings may need adjusting, and a ground source in the Local EPS can backfeed the distribution system.
