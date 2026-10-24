---
id: concept:crystalline-silicon
type: Concept
name: Crystalline silicon PV
aliases:
- c-Si
- monocrystalline
- polycrystalline
- multicrystalline
- multi-crystalline
- poly-crystalline
category: Modules
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:thin-film-pv
  note: Wafer-based crystalline silicon is the other main PV technology class, alongside thin-film deposition
    technologies.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.2
    h: 153861606c8a
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.1
    h: f7fb67df3e72
  review: drafted
- claim_id: c2
  rel: related_to
  target: comp:solar-cell
  note: Crystalline silicon modules are made of interconnected PV cells encapsulated between a front sheet
    and a backing.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=2.3.2
    h: 153861606c8a
  review: drafted
- claim_id: c3
  rel: related_to
  target: fm:light-induced-degradation
  note: LID and LeTID mainly affect p-type mono and multi crystalline silicon modules.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:potential-induced-degradation
  note: Testing for PID is described for crystalline silicon PV modules.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=2.r29
    h: 46b5b160cf61
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:perc
  note: LeTID was first seen when PERC modules came to market.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c6
  attr: degradation_rate
  value:
    max: 1
    unit: unit:PERCENT-PER-YR
  conditions: Long-term performance degradation of silicon modules from field exposure
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=3.2.1.1
    h: cddff06cd0e8
  review: drafted
  review_note: 'support check: partial - Source says degradation is under 1 percent per year, which is
    close to but not exactly ''up to 1''; the condition matches.'
- claim_id: c7
  attr: efficiency
  value:
    min: 12
    max: 18
    unit: unit:PERCENT
  conditions: Typical overall module efficiency of silicon solar modules (NREL landfill guide)
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=3.2.1.1
    h: cddff06cd0e8
  review: drafted
- claim_id: c8
  attr: efficiency
  value:
    max: 20
    unit: unit:PERCENT
  conditions: Overall efficiency demonstrated by some monocrystalline module manufacturers, described
    as nearing this value
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=3.2.1.1
    h: cddff06cd0e8
  review: drafted
- claim_id: c9
  attr: efficiency
  value:
    max: 17
    unit: unit:PERCENT
  conditions: Poly-crystalline silicon modules
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=5.4.2
    h: b9e435502fd2
  review: drafted
- claim_id: c10
  attr: efficiency
  value:
    min: 15
    max: 20
    unit: unit:PERCENT
  conditions: Typical efficiency of a standard module with monocrystalline or polycrystalline cells (SMA
    document)
  cite:
  - src: src:sma-doc-237302
    loc: sec=h7
    h: 033da7168dd7
  review: drafted
- claim_id: c11
  attr: typical_power_loss
  value:
    min: 1
    max: 3
    unit: unit:PERCENT
  conditions: LID in c-Si modules, occurring within the first days of sun exposure
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: drafted
- claim_id: c12
  attr: typical_power_loss
  value:
    max: 10
    unit: unit:PERCENT
  conditions: LeTID in c-Si modules at temperatures above 50 °C, adding to LID loss
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h69
    h: bdc3ce4bcd6c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Crystalline silicon (c-Si) PV modules are built from silicon wafer cells. The cells are connected together and sealed between a transparent front, usually glass, and a plastic or glass backing. The technology comes in two types, monocrystalline and multi-crystalline (polycrystalline). The difference is whether the cell material has grain boundaries, which depends on the raw material and how the cells are made. Monocrystalline wafers are cut from one large single-crystal ingot, which is costly. Multi-crystalline wafers are cheaper, for example sliced from cast poly-silicon, but they are usually less efficient. Typical module efficiency is around 12 to 18 percent in one source and 15 to 20 percent in another. Poly-crystalline modules reach up to 17 percent. Silicon modules have a long field record. They usually lose under 1 percent per year and carry power warranties of about 25 to 30 years. As of January 2010, about 78 percent of installed PV plant capacity used c-Si. The rest used thin-film modules. Mainly p-type c-Si modules can lose power to light induced degradation (LID) and LeTID. Crystalline silicon modules are also tested for potential induced degradation (PID). Crystalline silicon reference sensors have the same spectral response as c-Si plant modules, so they are used to estimate a plant's STC power. Over a year they record about 2 to 4 percent less irradiation than pyranometers.

<!-- review notes
- sentence 8: support check: partial - The passage supports the same spectral response assumption and 2-4% less irradiation, but this is an average for Germany and the equal spectral response is an assumption, not a given.
-->
