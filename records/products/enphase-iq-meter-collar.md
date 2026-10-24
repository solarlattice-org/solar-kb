---
id: prod:enphase-iq-meter-collar
type: Product
name: Enphase IQ Meter Collar
aliases:
- Meter Collar
- MC-200-011-V01
category: Protection and BOS
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: implements
  target: func:surge-protection
  note: Surge protection is built into the meter collar.
  cite:
  - src: src:kb-enphase-how-is-the-iq-meter-collar-protected-from-grid-surges
    loc: sec=h1
    h: 3dc4758a23ec
  review: drafted
- claim_id: c2
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:kb-enphase-how-is-the-iq-meter-collar-protected-from-grid-surges
    loc: sec=h1
    h: 3dc4758a23ec
  review: drafted
- claim_id: c3
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:kb-enphase-how-is-the-iq-meter-collar-protected-from-grid-surges
    loc: sec=h1
    h: 3dc4758a23ec
  review: drafted
- claim_id: c4
  rel: implements
  target: func:grid-forming
  scope:
    products:
    - prod:enphase-iq-battery
  conditions: With IQ Battery 10C; the collar takes over the grid-forming role of the IQ System Controller
  cite:
  - src: src:kb-enphase-how-does-the-iq-meter-collar-differ-from-the-iq-system-controller-for-backup
    loc: sec=h1
    h: 2ffb06141b55
  review: drafted
- claim_id: c5
  rel: implements
  target: func:backup-power
  scope:
    products:
    - prod:enphase-iq-combiner
    - prod:enphase-iq-battery
    applications:
    - backup
  conditions: Grid-forming (with backup) systems with IQ Combiner 6C and IQ Battery 10C
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5598
    loc: sec=h1
    h: 1738287721c6
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
  review_note: 'support check: partial - Release notes list grid-forming (with backup) systems with Combiner
    6C, Battery 10C and collar, implying backup, but do not explicitly say the collar implements backup
    power.'
- claim_id: c6
  rel: compatible_with
  target: prod:enphase-iq-system-controller
  conditions: IQ System Controller 3M with IQ Battery 5P (third-generation Enphase Energy System)
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=4.r3
    h: 164f69c7999a
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3.r3
    h: dd6a05816a8e
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3
    h: 5c9484e9e29a
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: sec=h1
    h: d19bd945c9fa
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:enphase-iq-battery
  conditions: IQ Battery 5P (third generation) or IQ Battery 10C (fourth generation)
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=4.r3
    h: 164f69c7999a
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3.r3
    h: dd6a05816a8e
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3
    h: 5c9484e9e29a
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: prod:enphase-iq-combiner
  conditions: IQ Combiner 6C with IQ Battery 10C (fourth-generation system); IQ Combiner 5/5C or 4/4C
    in IQ System Controller 3M systems
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=4.r3
    h: 164f69c7999a
  - src: src:enphase-enphase-iq9n-microinverter-installation-and-operation-manual
    loc: tbl=3.r3
    h: dd6a05816a8e
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: sec=h1
    h: d19bd945c9fa
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5598
    loc: sec=h1
    h: 1738287721c6
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c9
  rel: compatible_with
  target: prod:enphase-iq-gateway
  conditions: IQ Gateway with Communications Kit 2, IQ System Controller 3M and IQ Battery 5P
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: sec=h1
    h: d19bd945c9fa
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:enphase-iq9n
  conditions: Systems with IQ Battery 10C and IQ Combiner 6C
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5598
    loc: sec=h1
    h: 1738287721c6
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:enphase-iq8
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: sec=h1
    h: d19bd945c9fa
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5598
    loc: sec=h1
    h: 1738287721c6
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: prod:enphase-iq7
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: sec=h1
    h: d19bd945c9fa
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5598
    loc: sec=h1
    h: 1738287721c6
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
- claim_id: c13
  rel: compatible_with
  target: prod:enphase-iq6
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: sec=h1
    h: d19bd945c9fa
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5598
    loc: sec=h1
    h: 1738287721c6
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
- claim_id: c14
  rel: compatible_with
  target: fw:enphase-iq-gateway-8-3-5566
  scope:
    regions:
    - region:us
    - region:pr
  conditions: IQ Combiner 6C and IQ Battery 10C systems
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=h1
    h: fa4802b86cb0
  review: drafted
- claim_id: c15
  rel: compatible_with
  target: fw:enphase-iq-gateway-8-3-5598
  scope:
    regions:
    - region:us
    - region:pr
    - region:ca
  conditions: IQ Combiner 6C and IQ Battery 10C systems
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5598
    loc: sec=h1
    h: 1738287721c6
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c16
  rel: compatible_with
  target: fw:enphase-iq-gateway-8-3-5290
  scope:
    regions:
    - region:us
  conditions: Systems with IQ System Controller 3M and IQ Battery 5P; release improves robustness with
    the collar
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: sec=h1
    h: d19bd945c9fa
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5290
    loc: tbl=1
    h: ae35c46246c3
  review: drafted
---
The Enphase IQ Meter Collar is an adapter that fits into the utility meter socket. It has a microgrid interconnection device (MID) and an energy meter built in. It works with third-generation Enphase systems that use the IQ System Controller 3M and IQ Battery 5P. It also works with fourth-generation systems that use the IQ Combiner 6C and IQ Battery 10C. With the IQ Battery 10C, the collar does the grid-forming job the IQ System Controller used to do, so no backup subpanel is needed. Backup-ready grid-tied systems that use the collar also need a pair of external consumption CTs. Surge protection is built in, and the collar is listed to UL 1741 SA/SB. Supported systems include IQ9N, IQ8, IQ7 and IQ6 microinverters. They can also include legacy Enphase or compatible third-party PV inverters. IQ Gateway software 8.3.5290 was pushed remotely to US systems that have the IQ System Controller 3M and the collar. It improves how robustly those systems run. Releases 8.3.5566 and 8.3.5598 add stability and security fixes for IQ Combiner 6C and IQ Battery 10C systems with the collar.

<!-- review notes
- sentence 1: support check: partial - Meter socket adapter with integrated MID and energy meter is stated; 'fits into the utility meter socket' is a paraphrase, roughly fine, but supported mostly.
-->
