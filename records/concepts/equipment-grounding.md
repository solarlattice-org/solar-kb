---
id: concept:equipment-grounding
type: Concept
name: Equipment grounding
aliases:
- EGC
- equipment grounding conductor
- bonding
- Equipment Ground Conductor
category: Safety
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:equipotential-bonding
  note: Equipment grounding relies on bonding module frames, racks, enclosures, junction boxes and conduit
    together so they stay at the same voltage.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=4.4
    h: cb6192e3e9e2
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h151
    h: 4b8c8bf3de00
  review: drafted
- claim_id: c2
  rel: related_to
  target: hazard:electric-shock
  note: Grounding exposed metal parts lowers the risk of shock to personnel.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=4.4
    h: cb6192e3e9e2
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h151
    h: 4b8c8bf3de00
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:grounding-electrode-system
  note: The grounding electrode conductor connects the EGC or the grounded system conductor to the grounding
    electrode system.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h151
    h: 4b8c8bf3de00
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:ground-fault-protection
  note: Inverter fault monitoring and detection depend on grounding. In PV systems that are not solidly
    grounded, the output EGC may serve as the ground connection for ground-fault protection.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=4.4
    h: cb6192e3e9e2
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h111
    h: 0e2ddb8366bb
  review: drafted
- claim_id: c5
  rel: related_to
  target: arch:ungrounded-pv-array
  note: Equipment grounding is still required when the inverter runs with an ungrounded PV array.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=h52
    h: 8c1e89a98c24
  - src: src:eq-equip-inverters-yaskawa-pvi-50-60tl-installation-operation-manual
    loc: sec=h51
    h: e37d55903117
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=4.4
    h: cb6192e3e9e2
  review: drafted
- claim_id: c6
  rel: related_to
  target: req:nfpa-70-2017-690-47
  scope:
    standard: std:nfpa-70-2017
  note: For PV systems that are not solidly grounded, the output EGC to distribution equipment may be
    the array's connection to ground.
  cite:
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h111
    h: 0e2ddb8366bb
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:overcurrent-protection
  note: The minimum EGC size follows from the rating of the upstream overcurrent device.
  cite:
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: tbl=3
    h: 3dda0f83f298
  - src: src:std-standards-nec-2014-nec2014-690
    loc: sec=h22
    h: 8cdfca5162dc
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h24
    h: 0a63fd9f8895
  review: drafted
- claim_id: c8
  rel: related_to
  target: concept:voltage-drop
  note: The code does not require the EGC to be upsized to address voltage drop.
  cite:
  - src: src:std-standards-nec-2014-nec2014-690
    loc: sec=h22
    h: 8cdfca5162dc
  - src: src:std-standards-nec-2017-nec2017-690
    loc: sec=h24
    h: 0a63fd9f8895
  review: drafted
- claim_id: c9
  rel: related_to
  target: mit:dissimilar-metal-insulation
  note: Copper grounding conductors should not touch aluminum frames directly. Special washers or lugs
    make the joint.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h151
    h: 4b8c8bf3de00
  review: drafted
- claim_id: c10
  rel: related_to
  target: std:ul-1703
  note: Module manufacturers must state their approved grounding methods in the listed installation instructions.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h151
    h: 4b8c8bf3de00
  review: drafted
- claim_id: c11
  rel: related_to
  target: std:ul-2703
  note: UL 2703 is the standard for module racking systems, which covers generic grounding and bonding.
  cite:
  - src: src:trn-amrc-cx-everything-training-and-knowledge-raw-nec-general-information-nabcep-pv-resource-guide-1
    loc: sec=h151
    h: 4b8c8bf3de00
  review: drafted
  review_note: 'support check: partial - Passage mentions UL2703 as a standard for module racking systems
    being revised to accommodate generic grounding, but does not clearly say it covers generic grounding
    and bonding.'
---
Equipment grounding connects the metal parts that normally carry no current to ground. In a PV system these include module frames, racks, enclosures, junction boxes and conduit. Bonding these parts together keeps them at the same voltage, which reduces shock risk. Grounding also limits lightning and surge effects and lets the inverter's fault detection work. Every PV system needs equipment grounding, including systems whose inverter runs an ungrounded array. Only some systems also need system grounding, which connects a current-carrying conductor to earth. The equipment grounding conductor (EGC) can be a wire, busbar, metallic raceway or structural component. Once the PV circuit conductors leave the array area, the EGC must run with them. The EGC is sized from the overcurrent device rating using NEC Table 250.122 and must be at least 14 AWG. It does not need to be upsized for voltage drop. Modules can be bonded with listed bonding washers, clips, lay-in lugs or identified bonding jumpers. On anodized or oxidized aluminum, simply bolting parts together may not make a good bond, and copper should not touch aluminum directly. Inverters have a marked equipment grounding terminal for the EGC. Use the conductor sizes and materials given in the product manual. Related concepts include equipotential bonding, the grounding electrode system and DC ground-fault protection. Equipment grounding conductors and system grounding conductors are bonded together only at the source of supply.

<!-- review notes
- sentence 6: support check: partial - Bonding washers, clips, lay-in lugs, bonding jumpers, anodized aluminum bolting issue and copper-aluminum contact are stated, but 'listed' applies to devices per NEC rather than all items named, a minor qualifier.
- sentence 7: support check: partial - Passages show marked equipment grounding terminal and conductor size tables, but differing products give differing sizes and the generalisation that all inverters have a marked terminal is not fully stated.
-->
