---
id: concept:current-transformer-operation
type: Concept
name: Current transformer operation
aliases:
- CT ratio
- how CTs work
- current transformer
- CT
- CTR
- Current transformer ratio
category: Monitoring
concept_kind: electrical
claims:
- claim_id: c1
  rel: subclass_of
  target: concept:transformer-winding-configuration
  note: Not a subclass. The unit only shows that CT connections must reproduce the delta-wye phase shift
    of the power transformer.
  cite:
  - src: src:std-standards-mv-committee-ieee-standards-mv-equipment-ieee-std-c37-91-2008-protecting-power-transfo
    loc: sec=7.3.3
    h: 501c89583fb2
  review: drafted
  review_note: 'support check: partial - Passage says CTs must be connected to reproduce the transformer''s
    phase shift (delta-wye), but doesn''t state a kind-of relation to winding configuration; the note
    says not a subclass, so only the note part is supported.'
- claim_id: c2
  rel: explains
  target: fm:meter-ct-ratio-misconfiguration
  note: The device must be set to the CT ratio actually installed. A relay alarm flags a CT ratio setting
    that may be wrong.
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=6.4.9
    h: 4cdd77634b51
  - src: src:man-sel-synchrowave-application-guides-troubleshooting-transformer-relay-installations-with-synchrow
    loc: tbl=6.r13
    h: 1b255185492e
  review: drafted
  review_note: 'support check: partial - Passages give a CT ratio setting and a BAD.CT.RATIO alarm, but
    the ''meter'' misconfiguration link and that device must match installed CT are only loosely implied.'
- claim_id: c3
  rel: related_to
  target: comp:current-sensor
  cite:
  - src: src:book-electric-power-system-basics
    loc: sec=h111
    h: d7c0c7992d32
  - src: src:enphase-enphase-ct-installation-guidelines-tech-brief
    loc: sec=h9
    h: 580f7999fed2
  review: drafted
- claim_id: c4
  rel: related_to
  target: func:consumption-metering
  note: The gateway uses CT readings to report consumption.
  cite:
  - src: src:enphase-enphase-ct-installation-guidelines-tech-brief
    loc: sec=h9
    h: 580f7999fed2
  review: drafted
- claim_id: c5
  rel: related_to
  target: func:production-metering
  note: The gateway uses CT readings to report production.
  cite:
  - src: src:enphase-enphase-ct-installation-guidelines-tech-brief
    loc: sec=h9
    h: 580f7999fed2
  review: drafted
- claim_id: c6
  rel: related_to
  target: prod:solis-epm
  note: Has a CT ratio setting from 20:1 to 9900:1.
  cite:
  - src: src:solis-solis-manual-epm3-5g-pro-20250724
    loc: sec=6.4.9
    h: 4cdd77634b51
  review: drafted
  review_note: 'support check: partial - The CT ratio range 20:1 to 9900:1 is stated for a meter setting,
    but the passage doesn''t name the Solis Export Power Manager.'
---
A current transformer (CT) scales a large conductor current down to a small current that an instrument can safely measure. For example, 1,000 A on the primary side can be measured as 5 A in the secondary circuit. When a CT is placed around a live wire, the current in that wire induces a current in the CT's secondary winding. This secondary current is proportional to the primary current, and the meter calculates its measurements from it. The turns ratio is the scale factor that links the measured secondary current to the actual conductor current. Some CTs have taps so the ratio can be matched to the operating current. The meter or controller must be set to the ratio of the CT that is actually installed. On one export power manager, a 1000:5 A CT is entered as 200:1. Gateways in PV and battery systems use CT readings to report energy production and consumption. If the CT ratio setting is wrong, the readings are wrong, and protective relays can raise a bad-CT-ratio alarm. How well a CT performs depends on the burden on its secondary, which is set by the wiring, the connected impedances and the relay or meter. In transformer differential protection, CTs are often connected in delta on the transformer's wye side and in wye on its delta side, so the CT currents match the transformer's phase shift.

<!-- review notes
- sentence 2: support check: partial - Induction and proportionality are stated, but 'the meter' calculating is only the gateway using it for measurements.
- sentence 4: support check: partial - The 1000:5 A entered as 200:1 example is stated, but 'must be set to the actually installed CT' is only implied, and the device isn't named an export power manager.
- sentence 5: support check: partial - Gateway use of CT readings and the BAD.CT.RATIO alarm are stated, but the wrong-ratio-gives-wrong-readings link and the PV/battery scope are not stated.
-->
