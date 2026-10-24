---
id: prod:generac-pwrmanager
type: Product
name: Generac PWRmanager
aliases:
- PWRmanager
- G0080090
category: Protection and BOS
make: generac
product_level: family
claims:
- claim_id: c1
  rel: compatible_with
  target: prod:generac-pwrcell-inverter
  note: Manual states compatibility with the XVT series two-phase inverters.
  cite:
  - src: src:generac-generac-pwrmanager-install-manual
    loc: sec=h20
    h: c890ddb7fc2e
  review: drafted
  review_note: 'support check: partial - Passage says compatible with XVT series 2-phase inverters, but
    doesn''t name specific models X7602, XVT076A03, XVT114G03.'
- claim_id: c2
  rel: compatible_with
  target: prod:generac-pwrcell-ats
  scope:
    architecture: arch:whole-home-backup
    applications:
    - backup
  note: Recommended in addition to PWRmanager for whole home backup applications.
  cite:
  - src: src:generac-generac-pwrmanager-install-manual
    loc: sec=h20
    h: c890ddb7fc2e
  review: drafted
- claim_id: c3
  rel: certified_to
  target: std:ul-916
  cite:
  - src: src:generac-generac-pwrmanager-install-manual
    loc: tbl=12
    h: 34adac91ab3b
  - src: src:generac-generac-pwrmanager-owners-manual
    loc: tbl=11
    h: 34adac91ab3b
  - src: src:generac-generac-pwrmanager-install-manual
    loc: tbl=12.r1
    h: 3b5b2ba95e53
  - src: src:generac-generac-pwrmanager-owners-manual
    loc: tbl=11.r1
    h: 3b5b2ba95e53
  review: drafted
  review_note: 'support check: partial - Passages list UL916 under UL but don''t explicitly say certified/listed;
    core is stated.'
- claim_id: c4
  rel: requires
  target: role:installer
  note: The installer is expected to configure PWRmanager during installation; reconfiguration is done
    through its built-in web interface.
  cite:
  - src: src:generac-generac-pwrmanager-owners-manual
    loc: sec=h41
    h: 6e543d6d1fa7
  review: drafted
- claim_id: c5
  attr: rated_output_current
  value:
    max: 450
    unit: unit:A
  conditions: Maximum total current listed in the performance specifications
  cite:
  - src: src:generac-generac-pwrmanager-install-manual
    loc: tbl=10.r5
    h: 4b6fe8f0bc2f
  - src: src:generac-generac-pwrmanager-owners-manual
    loc: tbl=9.r5
    h: 4b6fe8f0bc2f
  review: drafted
  review_note: 'support check: partial - Passage gives Maximum Total Current 450 A, but not explicitly
    as rated output current.'
---
The Generac PWRmanager is a balance-of-system device sold as a unit under part number G0080090. It works with the Generac XVT series two-phase inverters. Generac also recommends the PWRcell ATS when the system is set up for whole home backup. The specifications give a maximum total current of 450 A. The device is listed to UL 916. The installer should configure it during installation. To change its automatic programming later, connect to the built-in web interface. If the app shows System Status as Error, the PWRmanager has an internal error. Contact the installer or technical support.

<!-- review notes
- sentence 1: support check: partial - Part number G0080090 for PWRmanager Unit is stated, but 'balance-of-system device' classification isn't in the passage.
- sentence 5: support check: partial - UL916 is listed in specs, though 'listed to' wording is not explicit.
- sentence 1: review: partial - Part number G0080090 for the PWRmanager Unit is stated, but the 'balance-of-system device' classification is not in the passage.
-->
