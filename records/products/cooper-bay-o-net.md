---
id: prod:cooper-bay-o-net
type: Product
name: Cooper Bay-O-Net fuse
aliases:
- Cooper Bay-O-Net
- Cooper BayONet
- bayonet fuse
- Bay-O-Net fuse link
category: Protection and BOS
make: cooper
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:cooper
  note: Sold as Eaton's Cooper Power series Bay-O-Net fuses.
  cite:
  - src: src:eq-equip-bos-fuse-xfmr-cooper-bayonet-instructions-mn132002en
    loc: sec=23
    h: dad49b479954
  - src: src:eq-equip-bos-fuse-xfmr-cooper-bayonet-instructions-mn132002en
    loc: sec=h21
    h: d17dda19ab55
  - src: src:eq-equip-transformers-ge-prolec-ca132009en
    loc: sec=h2
    h: 3c6cf33e2698
  review: drafted
- claim_id: c2
  attr: rated_output_current
  value:
    min: 3
    max: 140
    unit: unit:A
  conditions: Continuous current rating across Bay-O-Net fuse link catalog numbers 4000358C03 through
    4000358C18CB
  cite:
  - src: src:eq-equip-bos-fuse-xfmr-cooper-bayonet-ca132010en
    loc: tbl=2
    h: b7ed0a09a830
  review: drafted
  review_note: 'support check: partial - Table lists continuous current ratings 3-140 A for catalog numbers
    C03 through C18CB, but ''rated output current'' is a continuous current rating, which is fine; the
    range matches, though the table shows only discrete values.'
- claim_id: c3
  rel: compatible_with
  target: prod:cooper-elsp-backup-fuse
  note: Ideal use is in series with a coordinated current-limiting backup fuse; Bay-O-Net clears secondary
    faults and overloads, the current-limiting fuse clears high-level faults.
  cite:
  - src: src:eq-equip-bos-fuse-xfmr-cooper-bayonet-ca132010en
    loc: sec=h3
    h: 39b6ca614f2e
  - src: src:eq-equip-transformers-ge-prolec-ca132009en
    loc: sec=h2
    h: 3c6cf33e2698
  review: drafted
- claim_id: c4
  rel: requires
  target: prod:cooper-isolation-link
  conditions: When the Bay-O-Net fuse is not used in series with a current-limiting fuse
  cite:
  - src: src:eq-equip-bos-fuse-xfmr-cooper-bayonet-ca132010en
    loc: sec=h3
    h: 39b6ca614f2e
  - src: src:eq-equip-transformers-ge-prolec-ca132009en
    loc: sec=h2
    h: 3c6cf33e2698
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:iso-9001
  note: Listed under Standards as an ISO 9001 certified quality management system (manufacturer QMS).
  cite:
  - src: src:eq-equip-bos-fuse-xfmr-cooper-bayonet-instructions-mn132002en
    loc: sec=h21
    h: d17dda19ab55
  review: drafted
  review_note: 'support check: partial - The Standards section lists an ISO 9001 Certified Quality Management
    System, but it does not explicitly say the fuse is certified, only that the QMS is.'
---
The Cooper Bay-O-Net is a field-replaceable expulsion fuse family made by Eaton's Cooper Power series and used to protect distribution transformers and other apparatus. It is used on single-phase conventional and self-protected distribution transformers rated through 500 kVA and on three-phase equipment through 1500 kVA. Fuse links come in current sensing and dual sensing versions, with continuous current ratings from 3 A to 140 A depending on catalog number. The best application is in series with a coordinated current-limiting backup fuse such as the ELSP; the Bay-O-Net clears overloads and secondary faults, and the backup fuse operates only on internal equipment failure. If no current-limiting fuse is used in series, an isolation link is required, and where available fault current exceeds the interrupting rating, coordinated current-limiting fusing must be provided. Fuse holders are either sidewall-mounted or cover-mounted, and the cover-mounted type is limited to 23 kV maximum; re-fusing instructions cover 23 and 38 kV designs. During re-fusing, the holder is pulled from the Bay-O-Net housing and wiped clean of insulating fluid, and some catalog numbers are one integral link, cartridge and end plug assembly. The assembly can be damaged if it clears faults above its maximum interrupting current.

<!-- review notes
- sentence 1: support check: partial - Field-replaceable, Eaton Cooper Power series and protection of distribution transformers are stated, but 'expulsion' fuse type is not mentioned.
- sentence 2: support check: partial - Passage says 500 kVA applies to single-phase transformers and other apparatus, and 1500 kVA to three-phase equipment; the statement matches essentially, though the 500 kVA limit's scope is slightly different in wording (u16 gives no limits).
- sentence 3: support check: partial - Current sensing and dual sensing links and 3-140 A ratings appear, but the link between versions and ratings by catalog number is not fully stated; the table shows only one catalog series.
- sentence 1: review: partial - The passages support field-replaceable, the Eaton Cooper Power series and protection of distribution apparatus, but never call the fuse an 'expulsion' type.
-->
