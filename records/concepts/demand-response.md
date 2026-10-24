---
id: concept:demand-response
type: Concept
name: Demand response
aliases:
- DR program
- DR
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:distributed-energy-resource
  scope:
    regions:
    - region:us-ca
  note: New California DR programs depend on DERs, which automate grid interaction so no manual shutdown
    is needed.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h30
    h: c21bb7df886f
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: tbl=2.r3
    h: 8d4a56017cac
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:virtual-power-plant
  scope:
    regions:
    - region:us-ca
  note: Utilities sign contracts with DER providers to form VPPs that earn DR revenue.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: tbl=2
    h: b2a6306c8105
  review: drafted
  review_note: 'support check: partial - Utilities contract with DER providers to create VPPs delivering
    DR earnings, but ''sign contracts'' and VPPs earning DR revenue is only shown via the Stem example.'
- claim_id: c3
  rel: related_to
  target: comp:battery-storage
  note: Distributed storage at customer facilities delivers bill savings plus DR earnings, for example
    under SCE's LCR agreement with Stem.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: tbl=2
    h: b2a6306c8105
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:demand-response-modes
  scope:
    regions:
    - region:au
  note: AS/NZS 4777.2 may require inverter DRM0/1/5 functions. DRM0 disconnects from the grid, DRM1 brings
    grid import to zero and DRM5 brings export to zero, each on a utility command.
  cite:
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=5.6.3.3
    h: e09106011ff8
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=3.10.5
    h: 1c41b1057c19
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:utility-rate-structures
  scope:
    regions:
    - region:us-ca
  note: Tariff-based DR programs such as SCE CPP and PG&E PDP are being shifted to different times and
    rate structures.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-ca-rate-changes-ebook-energ
    loc: sec=h30
    h: c21bb7df886f
  review: drafted
---
Demand response, often shortened to DR, covers utility and market programs that pay or reward customers for changing how much power they draw from the grid when the grid needs it. Some DR programs are built into tariffs, such as peak pricing events. Others are separate programs like capacity or demand bidding, and in California many of those are being phased out. Newer programs let commercial customers join the wholesale market with distributed energy resources, which handle grid interaction automatically so nobody has to shut equipment down by hand. Utilities also contract with providers of distributed energy resources to build virtual power plants. In these, battery storage at customer sites earns DR revenue on top of bill savings. Running residential DR at scale means tracking customer enrollment, home area network devices, participation rates and tariff limits, so utilities use dedicated management software. In Australia, AS/NZS 4777.2 defines inverter demand response modes. Depending on the mode, a utility command can disconnect the inverter or bring grid import or export to zero.

<!-- review notes
- sentence 1: support check: partial - Passages discuss DR programs and earnings but never define DR as rewarding customers for changing grid draw when needed.
- sentence 5: support check: partial - Passages list the tracking challenges and GE's DRMS management software, but don't say utilities use dedicated software generally.
-->
