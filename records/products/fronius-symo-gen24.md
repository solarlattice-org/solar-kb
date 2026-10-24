---
id: prod:fronius-symo-gen24
type: Product
name: Fronius Symo GEN24
aliases:
- Symo GEN24
- GEN24
category: Inverters
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fronius
  cite:
  - src: src:fronius-fronius-gen24-latest-news-user-information
    loc: tbl=2
    h: 5089ef85970e
  review: drafted
  review_note: 'support check: partial - Passages mention Fronius URLs and Symo GEN24 but never explicitly
    state that Fronius manufactures it; only implied by the domain.'
- claim_id: c2
  rel: uses_protocol
  target: proto:fronius-solar-api
  scope:
    firmware_min: 1.14.110-1
  note: On new GEN24 devices shipped with firmware 1.14.110-1 or later, Solar API is off by default and
    must be switched on in the inverter web interface under Communication - Solar API. Updating an already
    installed device to that version does not turn it off.
  cite:
  - src: src:fronius-fronius-gen24-latest-news-user-information
    loc: tbl=2
    h: 5089ef85970e
  review: drafted
- claim_id: c3
  rel: incompatible_with
  target: prod:loxone
  scope:
    firmware_min: 1.9.7-0
  note: Fronius lists the GEN24 API as not compatible with Loxone and other third-party applications,
    starting at firmware 1.9.7-0. The issue is marked Solved, and version 1.14.110-1 also appears in the
    entry.
  cite:
  - src: src:fronius-fronius-gen24-latest-news-user-information
    loc: tbl=2
    h: 5089ef85970e
  - src: src:fronius-fronius-gen24-latest-news-user-information
    loc: tbl=2.r2
    h: c5953e0b512a
  review: drafted
  review_note: 'support check: partial - Row 9 states the GEN24 API not compatible with Loxone from 1.9.7-0,
    marked Solved, with 1.14.110-1 listed, but ''incompatible'' as a current state conflicts with Solved
    status and the firmware column meaning is ambiguous.'
---
The Fronius Symo GEN24 is a Fronius inverter family that belongs to the GEN24 platform. On new GEN24 units shipped with firmware 1.14.110-1 or later, the Solar API interface is off by default. Turn it on in the inverter web interface under Communication, then Solar API. Updating an installed unit does not turn it off. Fronius listed the GEN24 API as not compatible with Loxone and other third-party applications starting at firmware 1.9.7-0. Fronius marks this issue as solved and points users to its compatibility flyer. A known issue, marked solved, made the system show as offline in Solar.web even though the inverter was connected to a working home network. The fix for the offline display is to switch the Symo GEN24 off on both the AC and DC sides for about two minutes and then switch it back on.

<!-- review notes
- sentence 1: support check: partial - Passages use 'Symo GEN24' and 'GEN24' interchangeably, implying family membership, but don't explicitly state it belongs to a GEN24 platform or is made by Fronius.
- sentence 3: support check: partial - Row 9 gives the incompatibility, Solved status, 1.9.7-0 and the compatibility flyer link, but 'starting at 1.9.7-0' is an interpretation of the column and 'Fronius listed' attribution is implied.
-->
