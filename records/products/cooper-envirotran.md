---
id: prod:cooper-envirotran
type: Product
name: Cooper Envirotran transformer
aliases:
- Envirotran
- Envirotran Solar
category: Transformers
make: cooper
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:cooper
  note: Later published as Eaton's Cooper Power Systems business.
  cite:
  - src: src:eq-equip-transformers-cooper-envirotran-solar-b21010040
    loc: sec=h1
    h: 7eceb20f2c6d
  - src: src:eq-equip-transformers-cooper-envirotran-solar-b21010040
    loc: sec=h7
    h: 4a4577efe14c
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h33
    h: a85b5f316487
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h36
    h: fbeda3f2b924
  review: drafted
- claim_id: c2
  rel: requires
  target: prod:cargill-envirotemp-fr3
  note: Every Envirotran Solar unit and FM Approved Envirotran unit is filled with Envirotemp FR3 dielectric
    fluid, a biodegradable, less-flammable seed-oil fluid.
  cite:
  - src: src:eq-equip-transformers-cooper-envirotran-solar-b21010040
    loc: sec=h1
    h: 7eceb20f2c6d
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h33
    h: a85b5f316487
  - src: src:std-standards-fm-global-standards-2019-01-22-factory-mutual-labeled-transformers
    loc: sec=h22
    h: c15f41459d1b
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h36
    h: fbeda3f2b924
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c3
  rel: certified_to
  target: std:fm-3990
  note: FM Approved versions are built in strict compliance with FMRC Standard 3990; the FM Approved logo
    appears on the unit and nameplate.
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h33
    h: a85b5f316487
  - src: src:std-standards-fm-global-standards-2019-01-22-factory-mutual-labeled-transformers
    loc: sec=h22
    h: c15f41459d1b
  review: drafted
- claim_id: c4
  rel: certified_to
  target: req:nfpa-70-2008-450-23
  scope:
    standard: std:nfpa-70-2008
  conditions: FM Approved versions, or UL Listed transformer combined with UL Classified less-flammable
    liquid
  note: FM approval makes compliance with the less-flammable liquid-filled transformer requirements for
    indoor and outdoor locations easy to verify.
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h33
    h: a85b5f316487
  - src: src:std-standards-fm-global-standards-2019-01-22-factory-mutual-labeled-transformers
    loc: sec=h22
    h: c15f41459d1b
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h39
    h: 11f1bf37314d
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:iso-9001
  note: Stated for Cooper Power Systems transformer products in general.
  cite:
  - src: src:eq-equip-transformers-cooper-3p-pad-mount-compartmental-type-21012
    loc: sec=h2
    h: 09e9ac97bfe2
  review: drafted
  review_note: 'support check: partial - Passage says Cooper Power Systems transformer products are ISO
    9001 compliant, not certified.'
---
The Cooper Envirotran is a family of liquid-filled transformers from Cooper Power Systems, later part of Eaton, and includes a Solar version built for medium-voltage solar PV applications. Envirotran Solar units come filled with Envirotemp FR3, a biodegradable dielectric fluid made from seed oil, which the maker says extends the life of the insulation. FR3 has a fire point above 300 °C, which the maker contrasts with 155 °C for mineral oil, so pool fires are much less likely. The solar line can be custom-rated for the site's temperature profile, altitude, solar profile and required system life. It is offered as standard step-up units and as dual-secondary designs with 4-winding or 3-winding arrangements. FM Approved versions are built to FMRC Standard 3990 and carry the FM Approved logo on the unit and its nameplate. The approval makes it easy to show compliance with the 2008 NEC Section 450.23 rules for less-flammable liquid-filled transformers, indoors and outdoors. The transformer can also be ordered UL Listed and Labeled and/or UL Classified, which is another route to meeting Section 450.23. When the unit is decommissioned, nearly all of its materials can be recycled or reclaimed, including the core and cabinet steel and the fluid.

<!-- review notes
- sentence 3: support check: partial - The passage gives fire point above 300 °C versus 155 °C for mineral oil, but says fire likelihood is nearly nonexistent and long-term risk is minimized, not specifically 'pool fires much less likely'. The pool fire claim is only about field experience.
-->
