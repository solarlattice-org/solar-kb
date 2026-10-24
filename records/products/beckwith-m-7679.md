---
id: prod:beckwith-m-7679
type: Product
name: Beckwith M-7679 recloser control
aliases:
- M-7679
- M-7679 R-PAC
- R-PAC
category: Protection and BOS
make: beckwith
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:beckwith
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: sec=h1
    h: f3fe9d886bcb
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-br-recloser-relay-cutsheet
    loc: sec=h5
    h: 36a767fa0789
  review: drafted
  review_note: 'support check: partial - Passages say ''Beckwith Electric'' M-2979 and M-2400 products
    and show M-7679 R-PAC, but never explicitly state Beckwith Electric makes the M-7679 (implied by branding
    only).'
- claim_id: c2
  rel: compatible_with
  target: prod:beckwith-m-2979
  note: The M-2979 cabinet houses the M-7679 R-PAC for complete replacement of switch, sectionalizer or
    recloser controls.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: sec=h3
    h: 9db135e729c7
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-br-recloser-relay-cutsheet
    loc: sec=h5
    h: 36a767fa0789
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-sp
    loc: sec=h6
    h: 7ce99b295f5b
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-ib
    loc: sec=h8
    h: 7ce99b295f5b
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:beckwith-m-2400
  note: Adapters allow retrofit of some popular controls inside the existing cabinet.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-br-recloser-relay-cutsheet
    loc: sec=h5
    h: 36a767fa0789
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-sp
    loc: sec=h6
    h: 7ce99b295f5b
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-ib
    loc: sec=h8
    h: 7ce99b295f5b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: compatible_with
  target: prod:tavrida-osm-recloser
  note: OSM AI_2 and AI_4 reclosers with 42-pin control cable listed in the compatibility table.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: tbl=1.r6
    h: 667e788f8801
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:siemens-sdr-recloser
  note: Listed with a 40-pin control cable.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: tbl=1.r5
    h: 8697db1ace61
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:abb-elastimold-mvr
  note: ABB (Thomas & Betts) Elastimold MVR recloser listed with a 32-pin control cable.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: tbl=1.r2
    h: 01e73402ab21
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:abb-gridshield
  note: Both 250 Vdc and 155 Vdc GridShield versions appear in the compatibility guide.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: sec=h3
    h: 9db135e729c7
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: fig=16
    h: f695ce255d6d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: compatible_with
  target: prod:yaskawa-load-break-switch
  note: Listed among compatible brands for the cabinet replacement solution.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-beckwith-m-7679-qrg
    loc: sec=h3
    h: 9db135e729c7
  review: drafted
- claim_id: c9
  rel: implements
  target: func:synchronism-check
  note: 25 Sync is listed among the recloser blocking functions, together with 27 BSVS and 27Vz1 undervoltage
    blocking.
  cite:
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-sp
    loc: tbl=11.r21
    h: 2db77105df23
  - src: src:eq-equip-relays-reclosers-beckwith-recloser-relay-m-7679-ib
    loc: tbl=11.r21
    h: 2db77105df23
  review: drafted
---
There are two ways to upgrade an existing control: replace the whole control with the M-2979 cabinet, or fit an M-2400 series adapter inside the existing cabinet. The M-2979 cabinet holds the M-7679 and includes the interface connections and external communications needed to replace three-phase or independent-phase recloser, switch or sectionalizer control cabinets. The quick reference guide lists compatible reclosers from Eaton Cooper (NOVA and traditional types), Tavrida OSM, Siemens SDR, ABB Elastimold MVR and ABB GridShield, as well as Yaskawa load break switches. Each is matched to a specific control cable pin count. The recloser relay blocking functions include 27 BSVS, 27Vz1 and 25 sync check.
