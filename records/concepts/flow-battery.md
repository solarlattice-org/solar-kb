---
id: concept:flow-battery
type: Concept
name: Flow battery
aliases:
- redox flow battery
- pumped electrolyte ESS
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:battery-storage
  note: A flow battery is an energy storage component used in an ESS.
  cite:
  - src: src:std-standards-nec-2017-nec2017-706
    loc: sec=h13
    h: 0687151e40e8
  - src: src:std-standards-nfpa-855-20-pdf
    loc: sec=B.4
    h: e4e8e43f7e1d
  review: drafted
- claim_id: c2
  rel: related_to
  target: hazard:battery-electrolyte
  note: Vanadium redox electrolyte is sulfuric-acid based and zinc bromide electrolyte is corrosive and
    toxic (NFPA 704 hazard level 3); exposure risk during electrolyte handling, maintenance or spills.
  cite:
  - src: src:std-standards-nfpa-855-20-pdf
    loc: sec=B.4
    h: e4e8e43f7e1d
  review: drafted
- claim_id: c3
  rel: related_to
  target: hazard:battery-vented-gas
  note: Under abnormal overheating, corrosive liquids can boil off or off-gas flammable gases such as
    hydrogen.
  cite:
  - src: src:std-standards-nfpa-855-20-pdf
    loc: sec=B.4
    h: e4e8e43f7e1d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: related_to
  target: hazard:moving-parts
  note: Exposed pump parts or fans with missing guards can present physical hazards under abnormal conditions.
  cite:
  - src: src:std-standards-nfpa-855-20-pdf
    loc: sec=B.4
    h: e4e8e43f7e1d
  review: drafted
---
A flow battery is a storage component that works somewhat like a fuel cell: its active materials are liquid electrolytes kept in tanks outside the reactor. In use, the electrolytes move back and forth between the reactor and the storage tanks, so the system relies on pumps, other fluid handling equipment and flow controls. Two commercial types exist: zinc bromine and vanadium redox. A vanadium redox battery holds vanadium salts in a sulfuric acid electrolyte, and charging or discharging changes the oxidation state of the vanadium. In a zinc bromine battery, charging stores energy as zinc metal in the cell and as polybromide in the cathode reservoir. On discharge the zinc is oxidized and the bromine is reduced to bromide. During maintenance, wear the right protection when handling or topping up electrolyte, and watch for exposed pump parts or fans that are missing their guards.

<!-- review notes
- sentence 2: support check: partial - The passages say the electrolytes are transferred between reactor and tanks, and they list 706.43 Flow Controls and 706.44 Pumps and Other Fluid Handling Equipment. They do not say the electrolytes move back and forth, or that the system relies on those items.
- sentence 5: support check: partial - The passages mention corrosive electrolyte handling and replenishing during maintenance, and missing guards on pump parts and fans. The PPE instruction appears only for vented lead-acid batteries, not flow batteries, and the guard point is a hazard under abnormal conditions, not a maintenance instruction.
-->
