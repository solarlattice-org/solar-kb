---
id: prod:sma-sunny-central-up-us
type: Product
name: Sunny Central UP-US
aliases:
- Sunny Central UP US
- SC UP US
- SC2-3XXXUP-US
- SC2xxx
- Sunny Central UP
- SC UP
- SC2xxxUP
- SC-UP series
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
  review_note: 'support check: partial - The SMA service article lists SC UP manuals as SMA''s, but never
    mentions the UP-US variant specifically.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: The SC UP test document calls the Sunny Central UP the inverter.
  cite:
  - src: src:sma-sc-up-scs-up-eze-sg-en-10
    loc: tbl=4
    h: 0df7cb0f753a
  review: drafted
  review_note: 'support check: partial - The document calls Sunny Central UP ''Sunny Central or inverter'',
    but says nothing about the UP-US variant.'
- claim_id: c3
  rel: compatible_with
  target: prod:sma-sunny-webbox
  note: The Sunny WebBox manual lists all Sunny Central devices under the SMA-NET protocol setting. It
    does not name the UP series specifically.
  cite:
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25.r1
    h: 493c54ad9641
  - src: src:sma-doc-swebbox-ba-en-36
    loc: tbl=25
    h: 628b7b7a4c10
  review: drafted
  review_note: 'support check: partial - The passages say all Sunny Central devices are under SMA-NET,
    which implies compatibility, but they don''t name UP-US specifically (the statement''s own note concedes
    this).'
---
The Sunny Central UP is a family of SMA central inverters. SMA's manual archive lists it as SC UP, or SC2xxxUP. The SMA test instructions cover the SC 4000 UP, SC 4200 UP, SC 4400 UP and SC 4600 UP models. The same document also covers the Sunny Central Storage UP and UP-XT models. SMA publishes test instructions for the power-generating unit protection test on the Sunny Central UP and Sunny Central Storage UP. These instructions refer to the medium-voltage transformer as the MV transformer. SMA training videos on the Sunny Central user interface and on derating and cooling start from the 1850 kVA power class. They do not include every feature of the current SC-UP series, so check the relevant manual. The Sunny WebBox manual lists all Sunny Central devices under its SMA-NET communication setting.
