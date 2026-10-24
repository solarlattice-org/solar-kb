---
id: prod:sma-sunny-central-cp-us
type: Product
name: Sunny Central CP-US
aliases:
- SC CP-US
- SC 500CP-US/CA
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-sunny-central-inverter-manuals
    loc: sec=h1
    h: 7bce9861625b
  review: drafted
  review_note: 'support check: partial - Page is SMA''s Sunny Central manuals list including CP-US/CA
    models, implying SMA makes them, but it doesn''t explicitly state manufacturer.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:sma-kb-sunny-central-inverter-manuals
    loc: sec=h1
    h: 7bce9861625b
  review: drafted
  review_note: 'support check: partial - Page lists CP-US/CA as Sunny Central inverter manuals, implying
    inverter, but no explicit statement of component type.'
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-webbox
  note: The WebBox manual lists all Sunny Central devices under its SMA-NET communication setting.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25.r1
    h: 493c54ad9641
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25
    h: 628b7b7a4c10
  review: drafted
  review_note: 'support check: partial - WebBox SMA-NET setting lists all Sunny Central devices, implying
    compatibility, but CP-US is not named specifically.'
- claim_id: c4
  rel: compatible_with
  target: prod:sma-hybrid-controller
  note: The Hybrid Controller data sheet lists Sunny Central inverters generically as optional devices
    it can work with.
  cite:
  - src: src:sma-doc-ppm-10-ds-en-22
    loc: tbl=2.r13
    h: 60b27eba1709
  review: drafted
  review_note: 'support check: partial - Hybrid Controller lists Sunny Central generically (and CP-XT),
    not CP-US specifically.'
- claim_id: c5
  rel: has_hazard
  target: hazard:stored-capacitor-energy
  note: 'SMA safety training for Sunny Central inverters in general: the DC link capacitors can stay charged
    after shutdown, so measure between the DC switch and the inverter stacks.'
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c6
  rel: has_hazard
  target: hazard:dc-arc-flash
  note: 'SMA safety training for Sunny Central inverters in general: arcing when DC is disconnected under
    load, for example by pulling a DC fuse.'
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
- claim_id: c7
  rel: has_hazard
  target: hazard:electric-shock
  note: 'SMA safety training for Sunny Central inverters in general: there are two AC sources (the grid
    and the auxiliary supply) and the DC sources, and all must be isolated and tested.'
  cite:
  - src: src:sma-video-sicherheitsunterweisung-f-r-sunny-central-wechselrichter-wbt-1-safety-instruction-86472045
    loc: sec=h1
    h: 6e003b43d936
  review: drafted
---
The Sunny Central CP-US is a family of SMA central PV inverters for the US and Canadian markets. The family covers the SC 500CP-US/CA, a 600V version of the 500CP-US/CA, and the 630, 720, 750, 800, 850 and 900CP-US/CA models. SMA lists this family among its past Sunny Central inverters, and its manuals are in the archived section of the SMA download area. The Sunny WebBox manual lists all Sunny Central devices under its SMA-NET communication setting. The SMA Hybrid Controller data sheet lists Sunny Central inverters as optional devices. According to SMA safety training for Sunny Central inverters, the DC link capacitors can stay charged after shutdown, so test for zero voltage between the DC switch and the inverter stacks. Before working inside the unit, isolate, lock out and test both AC sources (the grid and the auxiliary supply) and the DC source. Never pull DC fuses under load, because this can cause an arc flash.

<!-- review notes
- sentence 1: support check: partial - CP-US/CA models are listed as Sunny Central inverters from SMA, with US/CA in names, but 'family for US and Canadian markets' and central PV are not explicitly stated.
- sentence 5: support check: partial - Source says 'Hybrid Controller (optional): ... Sunny Central' but it's unclear it's a data sheet listing optional devices; the text is ambiguous.
-->
