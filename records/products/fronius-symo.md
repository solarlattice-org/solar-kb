---
id: prod:fronius-symo
type: Product
name: Fronius Symo
aliases:
- Symo
- Symo 24.0-3 480
category: Inverters
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:fronius-solar-net
  note: Fronius Solar Net is the factory-set protocol type; the alternative setting is Interface.
  cite:
  - src: src:fronius-fronius-symo-advanced-ul-operating-instructions-42-0410-0192
    loc: sec=h114
    h: f71195c8bc01
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h112
    h: f71195c8bc01
  review: drafted
  review_note: 'support check: partial - Passages show Fronius Solar Net is the factory-set protocol type
    with Interface as the alternative, but don''t explicitly tie it to Symo in the passage text.'
- claim_id: c2
  rel: incompatible_with
  target: prod:fronius-datamanager
  conditions: Only when the protocol type is set to Interface
  note: With the Interface protocol type, any Fronius Datamanager card fitted in the inverter must be
    taken out.
  cite:
  - src: src:fronius-fronius-symo-advanced-ul-operating-instructions-42-0410-0192
    loc: sec=h114
    h: f71195c8bc01
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h112
    h: f71195c8bc01
  review: drafted
---
The Fronius Symo is a family of Fronius inverters, and the 480 V models include the Symo 15.0-3 480, 17.5-3 480 and 24.0-3 480. The firmware changelog also covers the Symo 3.0-3-S to 4.5-3-S, 3.0-3-M to 8.2-3-M and 10.0-3-M to 20.0-3-M models. Data communication uses Fronius Solar Net, which is the factory-set protocol type, and Interface is the other option. The Interface protocol type only works without a Fronius Datamanager card, so take out any installed Datamanager card before you use it. Status code 103 means the AC voltage is too low, and status code 106 means the AC frequency is too low. The operating instructions include a section on FCC and RSS compliance.

<!-- review notes
- sentence 1: support check: partial - The passages list the 480 models under Fronius Symo, but they don't say Symo is a family of Fronius inverters in so many words.
-->
