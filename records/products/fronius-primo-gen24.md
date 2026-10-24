---
id: prod:fronius-primo-gen24
type: Product
name: Fronius Primo GEN24
aliases:
- Primo GEN24 Plus
- GEN24 Plus
- GEN24
- GEN24 208-240
- Fronius Primo GEN24 208-240
category: Inverters
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: implements
  target: func:dc-arc-fault-protection
  note: PV DC arc-fault circuit protection Type 1 listed for the 3.8-6.0, 3.8-6.0 SC and 7.7-10.0 variants
    (standard and Plus).
  cite:
  - src: src:fronius-fronius-primo-gen24-208-240-quick-start-guide-42-0410-2417
    loc: tbl=1
    h: a58caae18877
  - src: src:fronius-fronius-primo-gen24-208-240-quick-start-guide-42-0410-2417
    loc: tbl=3
    h: 808f57fb9b73
  - src: src:fronius-fronius-primo-gen24-208-240-quick-start-guide-42-0410-2417
    loc: tbl=2
    h: e26efec2a04d
  review: drafted
- claim_id: c2
  rel: certified_to
  target: std:ul-1699b
  note: Arc-fault protection Type 1 according to UL1699B:2024.
  cite:
  - src: src:fronius-fronius-primo-gen24-208-240-quick-start-guide-42-0410-2417
    loc: tbl=1
    h: a58caae18877
  - src: src:fronius-fronius-primo-gen24-208-240-quick-start-guide-42-0410-2417
    loc: tbl=3
    h: 808f57fb9b73
  - src: src:fronius-fronius-primo-gen24-208-240-quick-start-guide-42-0410-2417
    loc: tbl=2
    h: e26efec2a04d
  review: drafted
  review_note: 'support check: partial - Passages say protection is Type 1 ''according to UL1699B:2024''
    but do not state certification of the product.; review: partial - The tables say the arc-fault protection
    is Type 1 ''according to UL1699B:2024'', which matches the note, but they never state that the product
    is certified to UL 1699B.'
- claim_id: c3
  rel: incompatible_with
  target: arch:it-earthing
  note: The inverter cannot be operated on ungrounded grids such as IT grids that have no ground conductor.
  cite:
  - src: src:kb-fronius-fronius-primo-gen24-3-8-6-0-208-240-emanual-status-codes
    loc: sec=h15
    h: 69d41c3d9ace
  - src: src:kb-fronius-fronius-primo-gen24-7-7-10-0-208-240-emanual-status-codes
    loc: sec=h15
    h: 222358ce8b33
  review: drafted
- claim_id: c4
  rel: requires
  target: tool:fronius-solar-start
  note: The communication connection is set up by following the steps in the Solar.start app.
  cite:
  - src: src:kb-fronius-fronius-primo-gen24-3-8-6-0-208-240-emanual-status-codes
    loc: tbl=1.r3
    h: 938e94ceb5df
  - src: src:kb-fronius-fronius-primo-gen24-7-7-10-0-208-240-emanual-status-codes
    loc: tbl=1.r3
    h: 938e94ceb5df
  review: drafted
  review_note: 'support check: partial - Passages say connection steps are done in the Solar.start app,
    but do not state the app is required in general.'
- claim_id: c5
  rel: uses_protocol
  target: proto:fronius-solar-api
  note: On new devices shipped with firmware 1.14.110-1 or later, Solar API is off by default and has
    to be enabled under Communication - Solar API. Updating an existing device does not turn it off.
  cite:
  - src: src:fronius-fronius-gen24-latest-news-user-information
    loc: tbl=2
    h: 5089ef85970e
  review: drafted
- claim_id: c6
  attr: rated_power
  value:
    min: 3.8
    max: 6
    unit: unit:KiloW
  conditions: Range of power classes covered by the 3.8-6.0 kW models (standard, Plus and SC)
  cite:
  - src: src:fronius-fronius-primo-gen24-208-240-quick-start-guide-42-0410-2417
    loc: sec=h17
    h: bb90d0101891
  review: disputed
  conflicts_with:
  - prod:fronius-primo-gen24#c7
- claim_id: c7
  attr: rated_power
  value:
    min: 7.7
    max: 10
    unit: unit:KiloW
  conditions: Range of power classes covered by the 7.7-10.0 kW 208-240 models (standard and Plus)
  cite:
  - src: src:kb-fronius-fronius-primo-gen24-7-7-10-0-208-240-emanual-status-codes
    loc: sec=h1
    h: a53cd2ddab52
  review: disputed
  conflicts_with:
  - prod:fronius-primo-gen24#c6
---
The Fronius Primo GEN24 208-240 is a family of Fronius inverters. It includes 3.8, 5.0, 6.0, 7.7 and 10.0 sizes, each in a standard and a Plus version, and the 3.8 to 6.0 sizes also come in SC versions. All variants have PV DC arc-fault circuit protection Type 1 according to UL 1699B. The inverter cannot run on ungrounded grids such as IT grids. Where the grid has a neutral conductor, the neutral must be connected and grounded, and it must be the same size as the live conductors. Lay the AC ground conductor longer than the other conductors, with a movement loop, so it is the last to be disconnected if there is a failure. Only battery configurations approved as suitable for GEN24 inverters may be used. The communication connection is set up with the Fronius Solar.start app, and the communication LED shows the connection status. Known issues include a GEN24 API incompatibility with Loxone and other third-party applications, fixed in firmware 1.14.110-1. Another known issue is the system showing as offline in Solar.web even with a working network; the fix is to switch the inverter off on the AC and DC sides for about two minutes and then back on. New devices shipped with firmware 1.14.110-1 or later have the Solar API turned off by default, so it must be enabled in the inverter user interface if needed.

<!-- review notes
- sentence 1: support check: partial - Size and variant listing is supported, but 'family of Fronius inverters' isn't stated and SC versions listed only for 3.8-6.0 implicitly.
- sentence 7: support check: partial - Loxone incompatibility fixed in 1.14.110-1 and offline fix are listed, but the offline issue's fix version and 'known issues' framing differ slightly; the fixed-in column supports Loxone item mainly.
- sentence 7: review: partial - Rows 8 and 9 support the Loxone/third-party API incompatibility and the roughly 2-minute AC/DC power-cycle fix for the Solar.web offline display, but the passages have no column headers, so reading 1.14.110-1 as the 'fixed in' version is an inference.
-->
