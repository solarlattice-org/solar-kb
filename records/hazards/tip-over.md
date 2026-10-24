---
id: hazard:tip-over
type: Hazard
name: Equipment tip-over
aliases:
- tip-over
- heavy cabinet
- Tip-over or Crush Hazard
- top heavy
category: Mechanical
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:proper-lifting-technique
  scope:
    products:
    - prod:powin-stack360e
    - prod:powin-stack750
    - prod:powin-stack230e
  note: Powin's install procedures say to use proper lift-safety technique so the equipment cannot fall
    onto anyone working nearby. They state that failing to do so can cause serious injury or death.
  cite:
  - src: src:powin-powin-pi-s360e-stack360e-install-procedure-rev-5
    loc: sec=h21
    h: 0ba3073959a8
  - src: src:powin-pi-s750e-stack750e-install-procedure-rev-a02-pre-production
    loc: sec=h11
    h: 0e55f4a268fa
  - src: src:powin-pi-s750e-stack750e-install-procedure-rev-a02-pre-production
    loc: sec=h15
    h: 0ba3073959a8
  - src: src:powin-powin-pi-s230e-stack230e-install-procedure-rev-0
    loc: sec=h19
    h: c887e8df4ff5
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:proper-lifting-technique
  scope:
    products:
    - prod:solaredge-backup-interface
  note: Training material calls for a two-person lift because the cabinet is notably top heavy, with a
    component mounted in its upper part.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h18
    h: f56b1a988902
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:avoid-uneven-surface-transport
  scope:
    products:
    - prod:powin-stack360e
    - prod:powin-stack750
    - prod:powin-stack230e
  note: The warnings tell installers not to lift or move the product over uneven ground.
  cite:
  - src: src:powin-powin-pi-s360e-stack360e-install-procedure-rev-5
    loc: sec=h21
    h: 0ba3073959a8
  - src: src:powin-pi-s750e-stack750e-install-procedure-rev-a02-pre-production
    loc: sec=h15
    h: 0ba3073959a8
  - src: src:powin-powin-pi-s230e-stack230e-install-procedure-rev-0
    loc: sec=h19
    h: c887e8df4ff5
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: mit:mount-with-cover-on
  scope:
    products:
    - prod:solaredge-backup-interface
  note: The cover stays on during mounting to keep the cabinet stable.
  cite:
  - src: src:se-academy-home-hub-technical-essentials-na-technical-08-backup-interface-installation-and-wiring
    loc: sec=h18
    h: f56b1a988902
  review: drafted
---
Equipment tip-over is the danger of heavy equipment falling over and crushing someone working nearby. Powin battery stack install procedures label this a tip-over or crush hazard and warn that it can cause serious injury or death. Risk goes up when the product is lifted or moved over uneven surfaces, so avoid uneven ground during handling. Use proper lift-safety technique so the equipment cannot fall onto anyone around it. Some cabinets are top heavy because a component sits in the upper part of the cabinet, as SolarEdge notes for its backup interface. For that cabinet, lift with two people and leave the cover on while mounting to keep it stable.

<!-- review notes
- sentence 3: support check: partial - Passages say avoid uneven surfaces, but do not explicitly state that risk increases there (only implied).
-->
