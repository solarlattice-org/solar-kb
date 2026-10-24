---
id: concept:power-purchase-agreement
type: Concept
name: Power purchase agreement
aliases:
- PPA
category: Market
concept_kind: finance
claims:
- claim_id: c1
  rel: related_to
  target: arch:behind-the-meter
  note: When the PPA is a behind-the-meter retail sale, the contract is usually between the third-party
    developer and the site host.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=h123
    h: 64f741781581
  review: drafted
- claim_id: c2
  rel: related_to
  target: arch:front-of-the-meter
  note: In wholesale sales the PPA is signed directly with an electric utility acting as the offtaker.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=h123
    h: 64f741781581
  - src: src:trn-training-very-basics-of-pv-lesson-1
    loc: sec=h41
    h: dfb13034d547
  review: drafted
- claim_id: c3
  rel: related_to
  target: prog:us-federal-itc
  note: Third-party developers using PPAs can take federal tax credits, and the benefit can reach public
    entities through a lower PPA price.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nrel-best-practices-solar
    loc: sec=h123
    h: 64f741781581
  review: drafted
  review_note: 'support check: partial - Passage says developers use federal tax credits and public entities
    benefit via low PPA price, but it doesn''t name the ITC specifically.'
- claim_id: c4
  rel: related_to
  target: comp:battery-storage
  note: One recommended contract structure for storage is to embed it in a PPA.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-storage-qualification-guide-3
    loc: tbl=2.r1
    h: 61ac9080ed18
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-storage-qualification-guide
    loc: tbl=5.r1
    h: 61ac9080ed18
  review: drafted
- claim_id: c5
  rel: related_to
  target: region:in
  note: In India, PPAs under the MNRE generation-based incentive policy are signed with state utilities.
    Under the draft National Solar Mission guidelines, NVVN signs for projects above 5MW.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=8.3.1
    h: 5e8c1d76b9ed
  review: drafted
- claim_id: c6
  rel: related_to
  target: org:sma
  note: SMA offers PPAs through its SMA Join product, available only in German.
  cite:
  - src: src:sma-kb-does-sma-offer-a-power-purchase-agreement
    loc: sec=h1
    h: 22c133ae254c
  review: drafted
---
A power purchase agreement (PPA) is a contract to sell the electricity from a solar project at a negotiated rate over a fixed period of time. The PPA sets how much the offtaker pays the project company for each unit of energy, so it is the project's source of revenue. A third-party developer usually finances, builds, owns and runs the system, then sells the power to the site host in a behind-the-meter retail deal, or to a utility in a wholesale deal. For homeowners, a PPA is similar to a lease, but the customer pays for the electricity the system actually produces instead of a flat monthly fee. PPA terms usually run 20 to 25 years. Having a PPA in place is a key early requirement for showing that a utility-scale project is viable. The EPC contractor has to design and build the plant to meet the technical conditions in the PPA and in the grid connection agreement. A battery storage system can also be paid for by embedding it in a PPA.

<!-- review notes
- sentence 6: support check: partial - The passage calls the PPA an important requirement for viability, but it is India-specific and doesn't say 'utility-scale' or 'key'.
- sentence 8: support check: partial - Evidence lists 'Embedded in PPA' as a recommended storage contract structure, but doesn't explicitly say it's a way of paying for the system.
-->
