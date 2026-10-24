---
id: prod:yaskawa-solectria-pvi-50-60tl
type: Product
name: Solectria PVI 50-60TL
aliases:
- PVI 50 60 TL
- PVI 50TL-480
- PVI 60TL-480
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h123
    h: 4a03dc1042e7
  review: drafted
  review_note: 'support check: partial - Passage says the PVI 50TL-480 and 60TL-480 are inverters, but
    never names a combined ''PVI 50-60TL'' product or explicitly says inverter class beyond calling them
    inverters; core is fine.'
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus
  note: Modbus carried over RS-485.
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h123
    h: 4a03dc1042e7
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: Third-party monitoring connects over a shielded twisted-pair RS-485 link.
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h129
    h: af1f2303e6d3
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h123
    h: 4a03dc1042e7
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:ethernet
  note: Only with the optional Ethernet Network Card, which SolrenView monitoring and YConnect Pro remote
    diagnostics need.
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h129
    h: af1f2303e6d3
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h123
    h: 4a03dc1042e7
  review: drafted
  review_note: 'support check: partial - Ethernet Network Card is optional and needed for SolrenView,
    and YConnect Pro data goes via it, but the passages don''t explicitly say YConnect Pro needs it or
    name Ethernet as a protocol.; review: partial - The passages say the optional Ethernet Network Card
    is needed for SolrenView and lets data go to YConnect Pro, but they do not say YConnect Pro requires
    the card.'
- claim_id: c5
  rel: implements
  target: func:remote-firmware-update
  note: Uses the optional Ethernet Network Card and the YConnect Pro portal.
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h123
    h: 4a03dc1042e7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c6
  attr: rated_power
  value:
    nominal: 50
    unit: unit:KiloV-A
  conditions: PVI 50TL-480 at the 50 kVA rating; the AC breaker selection table gives a minimum AC OCPD
    of 80 A
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=20
    h: de4c253cdee2
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions); possible conflict with c9 (same source; check the conditions)
- claim_id: c7
  attr: rated_power
  value:
    nominal: 55
    unit: unit:KiloV-A
  conditions: PVI 50TL-480 at the 55 kVA rating; the AC breaker selection table gives a minimum AC OCPD
    of 90 A
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=20
    h: de4c253cdee2
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions); possible conflict with c9 (same source; check the conditions)
- claim_id: c8
  attr: rated_power
  value:
    nominal: 60
    unit: unit:KiloV-A
  conditions: PVI 60TL-480 at the 60 kVA rating; the AC breaker selection table gives a minimum AC OCPD
    of 100 A
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=20.r5
    h: 360a994aba0c
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=20
    h: de4c253cdee2
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: rated_power
  value:
    nominal: 66
    unit: unit:KiloV-A
  conditions: PVI 60TL-480 at the 66 kVA rating; the AC breaker selection table gives a minimum AC OCPD
    of 100 A
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=20.r6
    h: 0b0b4eb82f08
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=20
    h: de4c253cdee2
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
---
The Solectria PVI 50-60TL is a family of three-phase string inverters made up of the PVI 50TL-480 and PVI 60TL-480 models. The breaker selection table lists the PVI 50TL-480 at 50 or 55 kVA and the PVI 60TL-480 at 60 or 66 kVA. The suggested maximum AC breaker is 125 A. For AC overcurrent protection, the PVI 50TL-480 needs at least an 80 A breaker at 50 kVA or a 90 A breaker at 55 kVA. The PVI 60TL-480 needs at least a 100 A breaker at either of its ratings. The inverters support standard Modbus communication over RS-485, and third-party data acquisition systems must connect through a shielded twisted-pair RS-485 link. Monitoring through SolrenView requires the optional Ethernet Network Card. The same card can send data to the YConnect Pro portal, which handles remote diagnostics and automatic firmware upgrades.

<!-- review notes
- sentence 1: support check: partial - Models 50TL-480 and 60TL-480 are listed, but 'three-phase string inverter' family is not stated in the passages.
- sentence 1: review: partial - The passages list the PVI 50TL-480 and PVI 60TL-480 models, but none of them say these are three-phase string inverters.
-->
