---
id: concept:listed-equipment
type: Concept
name: Listed equipment
aliases:
- NRTL listing
- listed
- certified equipment
category: Certification
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: std:eversource-ct-yellow-book
  note: The definition adds that the listing organization periodically inspects production and that the
    listing states the item meets identified standards or was tested and found suitable for a purpose.
  cite:
  - src: src:std-utilities-eversource-ct-ct-yellowbook
    loc: sec=h40
    h: cf7380980910
  review: drafted
- claim_id: c2
  rel: related_to
  target: org:ul
  note: UL is an example of an independent third-party certifier. In UL terms, 'UL Listed' means evaluated
    for all reasonably foreseeable safety hazards, and 'UL Classified' means evaluated for a limited range
    of hazards or conditions. Neither is the same as the code term 'listed'.
  cite:
  - src: src:ref-standards-nfpa-lightningprotectionag
    loc: sec=h8
    h: eb2e5b212940
  review: drafted
- claim_id: c3
  rel: related_to
  target: std:ul-1741
  note: FirstEnergy requires witness testing, such as synchronization and harmonics tests, for interconnection
    equipment that is not listed to UL 1741.
  cite:
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: tbl=1.r4
    h: 2ba925e11b1b
  - src: src:std-manuals-utility-first-energy-corp-commissioning-test-requirements
    loc: tbl=1.r11
    h: e98bb96dd03b
  review: drafted
- claim_id: c4
  rel: related_to
  target: std:ul-1741-sa
  note: HECO qualified equipment lists include advanced inverters certified to UL 1741 SA. A Tesla storage
    system is stated to be NRTL listed to UL 1741 SA.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-tesla-spec-s
    loc: tbl=5.r2
    h: 2dfed7267830
  - src: src:eq-equip-inverters-delta-heco-information-hawaii-heco-list-of-advanced-legacy-equipment
    loc: sec=h2
    h: 186d01479519
  - src: src:eq-equip-inverters-delta-heco-information-hawaii-heco-qualified-equipment-list
    loc: sec=h2
    h: 3801d4d2bd0a
  review: drafted
  review_note: 'support check: partial - Tesla NRTL listed to UL 1741 SA is stated, and the HECO list
    certifies advanced inverters to UL-1741 SA; the passages say ''certified'', not ''listed'', and the
    qualified list is called approved rather than described as listed equipment.'
- claim_id: c5
  rel: related_to
  target: std:ul-3741
  note: PV hazard control equipment can be listed to UL 3741. A listed PV hazard control system is only
    established when the required equipment is installed per the manufacturer's instructions.
  cite:
  - src: src:solis-solis-ul3741-installation-requirements-s6-eh1p-3-8-11-4-k-h-us-20240726
    loc: sec=front
    h: 17adc1e81ee5
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h49
    h: 75726c627db4
  review: drafted
- claim_id: c6
  rel: related_to
  target: std:ul-1642
  note: Lithium-ion cells in a Tesla storage product are stated to be NRTL listed to UL 1642.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-tesla-spec-s
    loc: tbl=5.r1
    h: e4caf933969c
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-tesla-spec-s
    loc: tbl=5
    h: 52e1602fef91
  review: drafted
- claim_id: c7
  rel: related_to
  target: std:ul-1973
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-tesla-spec-s
    loc: tbl=5.r2
    h: 2dfed7267830
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-tesla-spec-s
    loc: tbl=5
    h: 52e1602fef91
  review: drafted
- claim_id: c8
  rel: related_to
  target: std:ul-9540
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-tesla-spec-s
    loc: tbl=5.r2
    h: 2dfed7267830
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-tesla-spec-s
    loc: tbl=5
    h: 52e1602fef91
  review: drafted
- claim_id: c9
  rel: related_to
  target: concept:interconnection-process
  note: The utility reviews certified generator equipment packages in less detail, so review is faster
    and costs less.
  cite:
  - src: src:std-utilities-eversource-ct-exhibit-b-technical-requirements-06-01-18
    loc: sec=h48
    h: 7148d2ac6129
  review: drafted
- claim_id: c10
  rel: related_to
  target: concept:equipment-grounding
  note: Listed devices such as WEEBs may be used for grounding.
  cite:
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h108
    h: 0b3e42fc6d88
  review: drafted
- claim_id: c11
  rel: related_to
  target: concept:pv-hazard-control
  cite:
  - src: src:solis-solis-ul3741-installation-requirements-s6-eh1p-3-8-11-4-k-h-us-20240726
    loc: sec=front
    h: 17adc1e81ee5
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h49
    h: 75726c627db4
  review: drafted
---
Listed equipment is equipment that appears on a list published by an evaluation organization. That organization periodically inspects production and states that the item meets identified standards or is suitable for a stated purpose. In the codes, the word listed generally means the product was evaluated to the appropriate standards by an independent third-party certifier, such as a nationally recognized testing laboratory (NRTL). Do not confuse the code term listed with the UL marks: UL Listed covers all reasonably foreseeable safety hazards, while UL Classified covers only a limited range of hazards or conditions of use. The NEC requires PV equipment such as inverters, modules, combiners, dc-to-dc converters, rapid shutdown equipment and charge controllers to be listed, or to be field-evaluated and carry a field label. Testing laboratories do not issue letters confirming a listing, so the Listing Mark on the product is the best way to check it. A listing may cover a whole system only when it is installed as specified. For example, a UL 3741 PV hazard control system counts as listed only when the required components are installed per the manufacturer's instructions. A storage unit's listing may include the vendor-supplied harnesses and wire management. For utility interconnection, certified equipment such as UL 1741 or UL 1741 SA inverters speeds up the review. Equipment that is not listed may need witness tests, such as synchronization and harmonics tests.

<!-- review notes
- sentence 2: support check: partial - Passage says listed generally means evaluated by an independent third-party certification organization such as UL; NRTL is not named as the example in that passage.
- sentence 4: support check: partial - 690.4(B) lists the equipment and says listed or evaluated for the application with a field label; the 'dc combiners' etc. match, but 'field-evaluated' is paraphrase and the other passage says listed for PV application only; acceptable but rapid shutdown etc. covered in u7.
- sentence 7: support check: partial - Certified equipment speeds review and witness tests for non-UL 1741 listed equipment are stated, but the passages do not say 'UL 1741 inverters' specifically speed review beyond UL-1741 SA certified list approval.
-->
