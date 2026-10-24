---
id: concept:thin-film-pv
type: Concept
name: Thin-film PV
aliases:
- thin film
- CdTe
- CIGS
- amorphous silicon
- a-Si
- CIS
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:crystalline-silicon
  note: PV cell technologies are grouped as crystalline or thin film; thin film costs less but is less
    efficient.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.3
    h: 278122ccbfb2
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.1
    h: f7fb67df3e72
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=h62
    h: c4ba2e7330fc
  review: drafted
- claim_id: c2
  rel: related_to
  target: stressor:cell-reverse-bias
  note: Thin-film cells are very sensitive to reverse bias. Junction breakdown forms shunt paths that
    lead to hot spots.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.3.2
    h: eeffb36464ce
  review: drafted
- claim_id: c3
  rel: related_to
  target: stressor:partial-shading
  note: In thin-film modules, reverse bias is usually caused by shading.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.3.2
    h: eeffb36464ce
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:module-hotspot
  note: Shunt hot spots heat a single point and can badly damage thin-film modules.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.3.2
    h: eeffb36464ce
  review: drafted
- claim_id: c5
  rel: related_to
  target: comp:bypass-diode
  note: In thin-film modules, bypass diodes may not be usable to limit reverse voltage at affected cells.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.3.2
    h: eeffb36464ce
  review: drafted
- claim_id: c6
  rel: related_to
  target: method:el-imaging
  note: EL imaging easily shows shunts in thin-film cells.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.3.2
    h: eeffb36464ce
  review: drafted
- claim_id: c7
  rel: related_to
  target: std:iec-61646
  note: Hot-spot testing of thin-film modules is done in accordance with IEC 61646.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=6.3.2
    h: eeffb36464ce
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:temperature-coefficient
  note: CdTe modules are described as having good low-light response and good temperature response coefficients.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=h62
    h: c4ba2e7330fc
  review: drafted
- claim_id: c9
  attr: efficiency
  value:
    min: 6
    max: 8
    unit: unit:PERCENT
  conditions: Overall efficiency of an amorphous silicon (a-Si) thin-film module, as reported in NREL
    landfill guidance
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=3.2.1.2
    h: aff70a9b72e8
  review: disputed
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions)
  conflicts_with:
  - concept:thin-film-pv#c14
- claim_id: c10
  attr: efficiency
  value:
    min: 11
    max: 14
    unit: unit:PERCENT
  conditions: Overall efficiency of a CIGS thin-film module, as reported in NREL landfill guidance
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=3.2.1.2
    h: aff70a9b72e8
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c12
    (same source; check the conditions)
- claim_id: c11
  attr: efficiency
  value:
    min: 11
    max: 12
    unit: unit:PERCENT
  conditions: Overall efficiency of a CdTe thin-film module, as reported in NREL landfill guidance
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=3.2.1.2
    h: aff70a9b72e8
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c12
    (same source; check the conditions)
- claim_id: c12
  attr: efficiency
  value:
    max: 9
    unit: unit:PERCENT
  conditions: Amorphous silicon thin-film products (NREL landfill guidance, product section)
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=5.4.3
    h: 878a98426819
  review: disputed
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions)
  conflicts_with:
  - concept:thin-film-pv#c14
- claim_id: c13
  attr: efficiency
  value:
    max: 12
    unit: unit:PERCENT
  conditions: CdTe thin-film modules (NREL landfill guidance, product section)
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=5.4.3
    h: 878a98426819
  review: drafted
- claim_id: c14
  attr: efficiency
  value:
    min: 10
    max: 15
    unit: unit:PERCENT
  conditions: Typical efficiency of a CdTe thin-film module, given as an example in SMA leakage-capacitance
    guidance
  cite:
  - src: src:sma-doc-237302
    loc: sec=h8
    h: 052970e32ad1
  review: disputed
  conflicts_with:
  - concept:thin-film-pv#c9
  - concept:thin-film-pv#c12
---
Thin-film PV modules are made by depositing a thin layer of semiconductor onto a low-cost substrate, rather than by cutting cells from silicon wafers. The main thin-film types are amorphous silicon (a-Si), cadmium telluride (CdTe) and copper indium (gallium) diselenide (CIGS or CIS), with active layers only a few micrometers thick or less. Thin-film modules usually cost less to make than crystalline silicon modules, but they are less efficient, so they need more land area and more balance-of-system material for the same power. Some thin-film modules are flexible, which allows mounting options such as solar covers on landfills. Others are rigid and can go on fixed-tilt or tracking structures. Thin-film cells are very sensitive to reverse bias, which is usually caused by shading. A shaded cell can form a shunt path that overheats at a single spot, and bypass diodes may not be able to protect the cells. Shunts from manufacturing defects or from hot-spot operation can be seen with electroluminescence imaging or lock-in thermography. There is much less field experience with thin-film modules than with crystalline silicon, and many failures are specific to one manufacturer. Some string inverter manuals list thin-film modules without grounding as allowed PV string types.
