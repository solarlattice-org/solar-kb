---
id: hazard:electrostatic-discharge-damage
type: Hazard
name: Electrostatic discharge damage
aliases:
- ESD damage
- ESD
category: Equipment
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:body-static-discharge
  note: The technician grounds themselves, for example by touching grounded elements or the grounded enclosure,
    before touching electronic components.
  cite:
  - src: src:sma-doc-275752
    loc: sec=h38
    h: 944beea53acf
  - src: src:sma-sc-wa-en-31
    loc: sec=h127
    h: 38cbff740b50
  - src: src:sma-doc-edmm-wago-io-ia-en-11
    loc: sec=h27
    h: 944beea53acf
  - src: src:sma-sc-wa-en-31
    loc: sec=2.1.1
    h: 88ee41b1d427
  - src: src:sma-doc-278742
    loc: sec=h50
    h: ae83f5db0121
  - src: src:sma-doc-278742
    loc: sec=h121
    h: ae83f5db0121
  - src: src:sma-doc-278742
    loc: sec=h728
    h: ae83f5db0121
  - src: src:sma-doc-278742
    loc: sec=h738
    h: ae83f5db0121
  - src: src:sma-doc-259761
    loc: sec=h49
    h: ae83f5db0121
  - src: src:sma-doc-259761
    loc: sec=h115
    h: ae83f5db0121
  - src: src:sma-doc-259761
    loc: sec=h653
    h: ae83f5db0121
  - src: src:sma-doc-259761
    loc: sec=h663
    h: ae83f5db0121
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h287
    h: 4333eca59268
  - src: src:sma-doc-stx-intfan-rm-xx-11
    loc: sec=h38
    h: ae83f5db0121
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h51
    h: ae83f5db0121
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h44
    h: ae83f5db0121
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:body-static-discharge
  scope:
    products:
    - prod:sma-sunny-central-cp-xt
  note: The CP XT manual says to touch grounded enclosure parts or other grounded elements before handling
    electronic components.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=h45
    h: f42be40b2a32
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=h142
    h: f42be40b2a32
  review: drafted
  review_note: 'support check: partial - Passages u3/u6 give the wording about grounded enclosure parts
    or other grounded elements, but they do not name the CP XT model; the CP XT scope is not stated in
    those passages.'
- claim_id: c3
  rel: controlled_by
  target: mit:esd-safe-handling
  note: Follow the ESD safety regulations whenever working on the product or handling its components.
  cite:
  - src: src:sma-doc-275752
    loc: sec=h38
    h: 944beea53acf
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=h45
    h: f42be40b2a32
  - src: src:sma-doc-edmm-wago-io-ia-en-11
    loc: sec=h27
    h: 944beea53acf
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=h142
    h: f42be40b2a32
  - src: src:sma-sc-wa-en-31
    loc: sec=2.1.1
    h: 88ee41b1d427
  review: drafted
---
Electrostatic discharge can damage or destroy electronic components inside inverters and related equipment. It usually happens when a technician who is carrying a static charge touches electronic components inside the inverter. Manuals warn about it for central inverters such as the Sunny Central CP XT, for string inverters, and for the Sunny Island, where even inserting or removing the SD memory card is a risk. Follow the ESD safety regulations whenever you work on the product or handle its components. Before you touch any electronic component, ground yourself by touching grounded enclosure parts or other grounded elements. Wear suitable personal protective equipment for all work on the product.

<!-- review notes
- sentence 1: support check: partial - ESD damaging or destroying electronic components is stated, but 'inside inverters and related equipment' is only loosely covered (product/inverter/Sunny Central).
- sentence 2: support check: partial - Passages say touching electronic components can cause ESD damage, but nothing about it usually happening or about a technician carrying a static charge.
- sentence 3: support check: partial - Sunny Central (CP XT title in u9) and Sunny Island SD card warnings are present, but string inverters are not identified and the CP XT link is only via a title line.
-->
