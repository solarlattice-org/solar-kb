---
id: prod:enphase-iq-combiner
type: Product
name: Enphase IQ Combiner
aliases:
- IQ Combiner 4
- IQ Combiner 4C
- IQ Combiner 6C
- IQ Combiner 5
- IQ Combiner 5C
- IQ Combiner 5 HDK
- IQ Combiner 3
- IQ Combiner Series
- IQ Combiner+
- X-IQ-AM1-240-4
- X-IQ-AM1-240-4C
category: Protection and BOS
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  cite:
  - src: src:kb-enphase-what-load-and-der-configurations-does-the-iq-combiner-6c-support
    loc: sec=front
    h: 81bd94933e18
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
  review_note: 'support check: partial - Passages show Enphase make and IQ Combiner models but don''t
    explicitly state the manufacturer as Enphase Energy; make ''Enphase'' is implied.'
- claim_id: c2
  rel: compatible_with
  target: prod:enphase-iq8
  conditions: IQ8 PV backup configurations use IQ Combiner 4 or 4C
  cite:
  - src: src:enphase-enphase-design-and-installation-parameters-iq8-tech-brief
    loc: tbl=1.r12
    h: 99d97f0e2b3a
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:enphase-iq7
  conditions: IQ7 backup configurations use IQ Combiner 3/3C or 4/4C
  cite:
  - src: src:enphase-enphase-design-and-installation-parameters-iq8-tech-brief
    loc: tbl=1.r12
    h: 99d97f0e2b3a
  review: drafted
  review_note: 'support check: partial - Backup config line states Combiner 3/3C or 4/4C for IQ7, but
    the passage doesn''t explicitly name IQ7, IQ7+, IQ7X, IQ7A series compatibility beyond that.'
- claim_id: c4
  rel: compatible_with
  target: prod:enphase-iq-battery
  conditions: Wireless communication with the IQ Battery needs the Communication Kit installed in the
    combiner
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:enphase-iq-system-controller
  conditions: Wireless communication with the IQ System Controller needs the Communication Kit installed
    in the combiner
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:enphase-iq-gateway
  conditions: Integrated IQ Gateway
  note: The IQ Gateway is built into the IQ Combiner and uses the same setup as the standalone gateway.
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  - src: src:enphase-enphase-storage-3-3t-10-10t-troubleshooting-guide
    loc: sec=h80
    h: 09cdb657363f
  - src: src:kb-enphase-does-the-iq-combiner-6c-include-integrated-monitoring-capabilities
    loc: sec=h1
    h: fa3d2419b1e6
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: arch:microinverter-system
  conditions: IQ Microinverter systems with an IQ Combiner or PV subpanel
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.4
    h: 26989e59d94b
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: tbl=2.r3
    h: e8e8d376cf5d
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: arch:ac-coupled-storage
  conditions: PV plus IQ Battery AC-coupled storage installations
  cite:
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: sec=4.10
    h: f7cd077495f5
  review: drafted
- claim_id: c9
  rel: implements
  target: func:monitor-key-data
  conditions: 'Through the integrated IQ Gateway: real-time PV production, battery usage and system performance
    shown in the Enphase App or Enlighten'
  cite:
  - src: src:kb-enphase-does-the-iq-combiner-6c-include-integrated-monitoring-capabilities
    loc: sec=h1
    h: fa3d2419b1e6
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c10
  rel: implements
  target: func:production-metering
  conditions: Revenue-grade, using solid-core CTs
  cite:
  - src: src:enphase-enphase-ct-installation-guidelines-tech-brief
    loc: sec=h10
    h: 3b30ab2a2742
  review: drafted
- claim_id: c11
  rel: implements
  target: func:consumption-metering
  conditions: Using split-core or clamp-style CTs
  cite:
  - src: src:enphase-enphase-ct-installation-guidelines-tech-brief
    loc: sec=h10
    h: 3b30ab2a2742
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: fw:enphase-iq-gateway-8-3-5427
  conditions: Release notes list IQ Combiner 4/4C and 5/5C
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5427
    loc: sec=front
    h: 276ba18bb06b
  review: drafted
- claim_id: c13
  rel: compatible_with
  target: fw:enphase-iq-gateway-8-3-5289
  conditions: Release notes list IQ Combiner 4/4C and 5/5C
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5289
    loc: sec=front
    h: ade7d6992843
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c14
  rel: compatible_with
  target: fw:enphase-iq-gateway-8-3-5566
  conditions: Release notes list IQ Combiner 6C
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5566
    loc: sec=front
    h: 593055a79146
  review: drafted
- claim_id: c15
  rel: compatible_with
  target: fw:enphase-iq-gateway-8-3-6087
  conditions: Release notes list IQ Combiner 5/5C
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-6087
    loc: sec=front
    h: d3dc27727799
  review: drafted
---
The Enphase IQ Combiner is a family of residential AC combiner panels. Each one puts the interconnection equipment for Enphase PV and storage systems into a single pre-wired enclosure. Models in the family include the IQ Combiner 3, 4/4C, 5/5C and 6C. The IQ Combiner 3 combines up to four AC branch circuits of IQ Microinverters and/or IQ Batteries in an outdoor-rated NEMA type 3R enclosure. Every combiner contains an IQ Gateway, and that gateway is set up the same way as a standalone IQ Gateway. Through it you get monitoring in the Enphase App or Enlighten. The combiner supports solid-core CTs for revenue-grade production metering and split-core or clamp CTs for consumption and battery metering. Tighten CT terminal connections to 5 in-lbs. For IQ8 PV backup configurations use an IQ Combiner 4 or 4C. IQ7 backup configurations use an IQ Combiner 3/3C or 4/4C. To talk wirelessly with the IQ Battery and IQ System Controller, you must install a Communication Kit in the combiner. The combiners receive IQ Gateway software updates, for example releases 8.3.5427 and 8.3.5566.

<!-- review notes
- sentence 3: support check: partial - Gateway inclusion, same setup, and monitoring are stated, but 'every combiner' monitoring is only shown for 6C and general inclusion; mostly supported.
- sentence 6: support check: partial - Passage says install the Communication Kit to enable wireless communication, but 'must' is slightly stronger than stated.
- sentence 4: review: partial - The CT types for production, consumption and battery metering are stated, but the 5 in-lbs torque appears only in the IQ Combiner 5/5C/4 steps and is presented as a general rule for every combiner.
-->
