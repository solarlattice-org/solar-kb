---
id: concept:point-of-interconnection
type: Concept
name: Point of interconnection
aliases:
- POI
- PCC
- point of common coupling
- point of connection
- Netzverknüpfungspunkt
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:point-of-common-coupling
  note: SMA glossaries define PCC as the point of interconnection on the utility grid that other customers
    are or could be connected to.
  cite:
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=16.r12
    h: 86f28a2fdf58
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=52.r1
    h: c47274b301a2
  - src: src:sma-doc-shp75-10-stp60-10-ia-xx-20
    loc: tbl=138.r1
    h: e2f9fbaac88a
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:area-eps
  note: The PCC is where a Local EPS connects to the Area EPS.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=6.7.8.7
    h: d1eef2171235
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: sec=6.7.8.7
    h: d1eef2171235
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: sec=6.7.8.7
    h: d1eef2171235
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:local-electric-power-system
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=6.7.8.7
    h: d1eef2171235
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:reference-point-of-applicability
  note: Grid connection requirements may apply at the point of interconnection or at the inverter terminals;
    the grid operator or local regulations decide which.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=67.r1
    h: 17b46bbe5322
  - src: src:sma-doc-275857
    loc: sec=3.1.1
    h: 966ed9478873
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=3.1.1
    h: 5183f1d450b3
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:short-circuit-ratio
  note: Inverter configuration limits for weak grids are given in terms of the SCR at the POI.
  cite:
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=3.r1
    h: 4ad59069af20
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=4.r1
    h: 3cdd438fcc23
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=5.r1
    h: 9bc470babdfa
  - src: src:yaskawa-xgi-1500-configuration-limits-low-grid-scr
    loc: tbl=6.r7
    h: 51d38b6fdf9b
  review: drafted
  review_note: 'support check: partial - Passages show SCR values at the POI for inverter configurations,
    but do not clearly state weak-grid limits; the tables are fragmentary.'
- claim_id: c6
  rel: related_to
  target: comp:energy-meter
  note: For Tesla Utility Hybrid systems, one busway meter at the point of interconnection is required.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=h179
    h: a205806a98f4
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:islanding
  note: An island is energized by Local EPSs through their associated PCCs.
  cite:
  - src: src:std-manuals-jersey-power-and-light-customer-interconnection-guide-three-phase
    loc: sec=2.0
    h: d26db103fe48
  review: drafted
---
The point of interconnection (POI), often called the point of common coupling (PCC), is where a customer's local electric power system connects to the utility's area electric power system. It is the point on the utility grid that other customers are connected to, or could be connected to. In most cases the PCC matches the service point as defined in the NEC and the NESC. It is different from the point of DER connection, which is where the DER unit itself connects inside the local system. Grid connection rules say whether a requirement applies at the point of interconnection or at the inverter terminals, and the grid operator or local regulations choose which reference point to use. Inverters often have settings tied to this point, such as a Voltage PCC Set value required under Rule 21, or the nominal apparent power at the PCC. Large plants also use the POI for metering and for grid strength checks: a revenue busway meter may be required at the POI, and inverter limits are given in terms of short-circuit ratio at the POI. Under the NEC, each interactive system's point of interconnection with other sources must be labeled at the disconnecting means. Examples include AC combining panels, AC disconnects and backfed breakers.

<!-- review notes
- sentence 6: support check: partial - Busway meter at POI is required for Utility Hybrid systems, and SCR at POI appears in inverter tables, but 'revenue' meter and 'large plants' are not stated.
-->
