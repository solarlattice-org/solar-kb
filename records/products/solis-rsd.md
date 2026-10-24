---
id: prod:solis-rsd
type: Product
name: Solis RSD rapid shutdown
aliases:
- RSD1L
- Solis RSD
- Solis-RSD1L-1G
- Solis-RSD2L-1G
- Solis Rapid Shutdown Device
- RSD
category: MLPE
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  note: Units name the maker as Ningbo Ginlong Technologies / Ginlong Solis.
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=h1
    h: 09304e0928fb
  - src: src:solis-service-bulletin-rsd-removal-of-dc-and-ac-connectors
    loc: sec=h2
    h: 827323bdbf34
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:rapid-shutdown-device
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  - src: src:solis-service-bulletin-rsd-removal-of-dc-and-ac-connectors
    loc: sec=h2
    h: 827323bdbf34
  review: drafted
  review_note: 'support check: partial - It is an RSD mounted under a module, but the passages never call
    it ''module-level'' explicitly (also usable within 5 ft of the array).'
- claim_id: c3
  rel: implements
  target: func:rapid-shutdown
  note: AC power holds normally-open relays closed in the PV source circuits; removing AC power opens
    them.
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  - src: src:solis-service-bulletin-rsd-removal-of-dc-and-ac-connectors
    loc: sec=h2
    h: 827323bdbf34
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  review: drafted
- claim_id: c5
  rel: certified_to
  target: req:nfpa-70-2014-690-12
  scope:
    standard: std:nfpa-70-2014
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  - src: src:solis-service-bulletin-rsd-removal-of-dc-and-ac-connectors
    loc: sec=h2
    h: 827323bdbf34
  review: drafted
  review_note: 'support check: partial - Passages say it complies with/meets 2014 NEC 690.12 requirements,
    not that it is ''certified'' to it.'
- claim_id: c6
  rel: compatible_with
  target: prod:solis-2-5-5k-2g-us
  note: One of only two inverter series the RSD was qualified or tested with.
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=1.1
    h: 589ca577d9c1
  review: drafted
- claim_id: c7
  rel: requires
  target: role:qualified-person
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: sec=h14
    h: e36d82b1d180
  review: drafted
- claim_id: c8
  attr: nominal_voltage
  value:
    min: 220
    max: 240
    unit: unit:V
  conditions: AC power source to which the RSD AC control circuit cable is landed
  cite:
  - src: src:solis-service-bulletin-rsd-removal-of-dc-and-ac-connectors
    loc: sec=h2
    h: 827323bdbf34
  review: drafted
- claim_id: c9
  attr: max_count
  value:
    nominal: 1
    unit: unit:NUM
  conditions: Rapid shutdown devices per package, per the parts list
  cite:
  - src: src:solis-solis-rsd-1-2-l-1g-manual-v1-1
    loc: tbl=2.r1
    h: b09bba679559
  review: drafted
---
The Solis RSD is a module-level rapid shutdown device sold in single-channel and dual-channel versions, Solis-RSD1L-1G and Solis-RSD2L-1G. It sits in a NEMA 4X enclosure, mounted under a PV module or within 5 feet of the array on a support rail. An AC control signal keeps relays in the positive and negative PV conductors closed. When first responders cut AC power, the relays open and the array drops to a safe low voltage within 10 seconds. A green LED on the unit means it is getting AC power and its PV output circuits may be live. The AC control cable gets its power from a 220-240 VAC source. The RSD is certified to UL 1741 and meets the 2014 NEC 690.12 rapid shutdown requirements. It has only been qualified with the Solis-(2.5-5)K-2G-US and Solis-1P(2.5-10)K-4G-US inverters. Do not use it with inverters from other manufacturers. Only qualified personnel may install it. Disconnect AC and DC before you start, and put up a permanent label saying the system has rapid shutdown. You may remove the factory DC and AC connectors in the field without voiding the warranty. Leave at least 4 inches of cable when you do.

<!-- review notes
- sentence 1: support check: partial - Models RSD1L-1G/RSD2L-1G and single/dual-channel configurations are stated, but mapping of models to channels and 'module-level' are not explicit.
- sentence 3: support check: partial - AC closes relays in positive and negative circuits and removal opens them with shutdown in under 10 s, but 'first responders cut AC' is in the passage; 'safe low voltage' is 30 VDC, fine; mostly supported though relays 'AC control signal' phrasing is loose.
-->
