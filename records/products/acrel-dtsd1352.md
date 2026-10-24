---
id: prod:acrel-dtsd1352
type: Product
name: Acrel DTSD1352 meter
aliases:
- DTSD1352
- Acrel DTSD 1352
- Solis 3phase Meter DTSD1352
- 3Phase meter DTSD1352
category: Metering
make: acrel
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:acrel
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  - src: src:kb-solis-44002271824-adjust-the-ct-ratio-of-an-acrel-dtsd-1352-meter
    loc: sec=h1
    h: 1203cf3b09d1
  review: drafted
  review_note: 'support check: partial - Passages name it an Acrel DTSD1352 meter, but none state that
    Acrel is its manufacturer explicitly beyond the naming.'
- claim_id: c2
  rel: implements
  target: func:export-limitation
  note: Gives Solis three-phase grid-tied inverters the meter input they need for their internal export
    power limit function.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c3
  rel: implements
  target: func:consumption-metering
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:acrel-akh-0-66-k24
  conditions: Three 150A:5A CTs are supplied with the meter (external CT, 5 A secondary variant).
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  - src: src:kb-solis-44002271824-adjust-the-ct-ratio-of-an-acrel-dtsd-1352-meter
    loc: sec=h1
    h: 1203cf3b09d1
  - src: src:kb-solis-44002440996-acrel-dtsd1352-3ph-meter-ct-ratio
    loc: sec=h1
    h: 0d66e6ffa27f
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:solis-s5-gr3p-3-20k
  conditions: Inline 80 A version for sites under 40 kW, or with external 5 A CTs.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:solis-s5-gc-25-40k
  conditions: Inline 80 A version for sites under 40 kW, or with external 5 A CTs.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:solis-s6-gc3p-25-36k03-nv-nd
  conditions: Inline 80 A version for sites under 40 kW, or with external 5 A CTs.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: prod:solis-3p-3-20k-4g
  conditions: Inline or external 5 A CT versions.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c9
  rel: compatible_with
  target: prod:solis-s6-gc-80-125k
  conditions: Only the external 5 A CT version, using 300 A CTs.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:solis-s6-eh1p-3-8k-plus
  conditions: External 5 A CT version, only when the hybrid inverters run in parallel.
  cite:
  - src: src:kb-solis-44002687170-solis-meter-and-ct-compatibility-guide
    loc: sec=h1
    h: 0caa9c940137
  review: drafted
  review_note: 'support check: partial - S6-EH1P(3-8)K-PLUS is listed under the external CT DTSD1352 entry
    ''when parallel'', but the ''only'' and 5A-version phrasing is inferred; the entry lists the DTSD1352
    with 5A CT secondary, which broadly fits.'
---
The Acrel DTSD1352 is a three-phase energy meter that Solis lists as a supported meter for its three-phase grid-tied inverters. It comes in two versions: an inline 80 A version for sites under 40 kW, and a version that uses external CTs with a 5 A secondary. Connected to a compatible Solis inverter, the meter supports the inverter's internal export power limit and consumption monitoring. Examples are the S5-GR3P, S5-GC and S6-GC3P series. Larger S6-GC models use 300 A CTs. The meter ships with three Acrel AKH-.66 K24 150A:5A CTs, so the CT ratio should be 30, which is primary current divided by secondary current. Change the ratio if you use other 5 A CTs. If the meter readings do not match the actual loads, check the CT ratio. You set it through the In and CT menus and must save it on the Save screen, or the change is lost. The sources give different setup codes: one gives an initial password of 0001, another says to enter 0008. For a three-phase three-wire LV network, set the wiring system to 3P3L in the PL screen of the SYS menu, then save.

<!-- review notes
- sentence 5: support check: partial - Passages say to check the CT ratio if readings look wrong and describe In/CT menus and saving, but do not explicitly say the change is lost if not saved.
-->
