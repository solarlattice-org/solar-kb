---
id: concept:smart-inverter
type: Concept
name: Smart inverter
aliases:
- advanced inverter functions
- grid support utility interactive
- smart inverter functions
- grid support utility interactive inverter
- grid support interactive inverter
- Utility Support Grid Interactive Inverter
- advanced inverter function
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:inverter
  note: A smart inverter is an inverter that, beyond DC-to-AC conversion, modulates its output to support
    the grid.
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h85
    h: 595988bd997f
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-gridservices-techinfo
    loc: sec=1.2
    h: 41f924383b1b
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:ul-1741-sa
  scope:
    products:
    - prod:sma-sb-us-41
    - prod:sma-sb-us-40
    - prod:sma-stp-tl-us
    - prod:sma-stp-core1-us
    - prod:sma-shp-peak3
    - prod:delta-electronics-m36u-m42u
  note: Grid support utility interactive inverters are tested and certified to UL 1741 SA.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h67
    h: 208f7a4ad586
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h62
    h: 35c537013497
  - src: src:eq-equip-inverters-sma-stp-core1-50-stp-core-1-user-manual-v1-1-50-62
    loc: sec=h57
    h: ba1fbb7d1b5d
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h66
    h: 35c537013497
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-gridservices-techinfo
    loc: sec=1.2
    h: 41f924383b1b
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: tbl=34.r1
    h: ea5ce33291a4
  review: drafted
- claim_id: c3
  rel: related_to
  target: std:ul-1741-sb
  note: Newer grid support inverters are tested to UL 1741 SB together with IEEE 1547-2018.
  cite:
  - src: src:kb-sma-stpsxxus-20-grid-management-services
    loc: sec=h1
    h: 744efc955684
  review: drafted
  review_note: 'support check: partial - u16 states testing to UL 1741 SB / IEEE 1547-2018 for a grid
    support inverter, but doesn''t call it a smart inverter or say ''newer'' inverters.'
- claim_id: c4
  rel: related_to
  target: std:ieee-1547-2018
  note: Smart inverter functions are enabled by default under the IEEE 1547-2018 setting profile in some
    inverters.
  cite:
  - src: src:kb-sma-stpsxxus-20-grid-management-services
    loc: sec=h1
    h: 744efc955684
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=7.r3
    h: b48d25397b25
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=7.r9
    h: 09860dc4ab65
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=7.r7
    h: 6fd4084777b5
  review: drafted
- claim_id: c5
  rel: related_to
  target: func:volt-var
  note: Listed as intelligent volt-var control among EPRI smart inverter functions.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=3.2.2.3.1
    h: 49d0e514c815
  review: drafted
- claim_id: c6
  rel: related_to
  target: func:volt-watt
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=3.2.2.3.1
    h: 49d0e514c815
  review: drafted
- claim_id: c7
  rel: related_to
  target: func:low-voltage-ride-through
  note: Modeling LVRT requires interfacing with network fault calculations.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=3.2.2.3.1
    h: 49d0e514c815
  review: drafted
- claim_id: c8
  rel: related_to
  target: func:high-voltage-ride-through
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=3.2.2.3.1
    h: 49d0e514c815
  review: drafted
- claim_id: c9
  rel: related_to
  target: func:voltage-ride-through
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h85
    h: 595988bd997f
  review: drafted
- claim_id: c10
  rel: related_to
  target: func:frequency-ride-through
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h85
    h: 595988bd997f
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=7.r3
    h: b48d25397b25
  review: drafted
- claim_id: c11
  rel: related_to
  target: func:dynamic-voltage-support
  note: Described as dynamic reactive current support or dynamic reactive/real power support.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=3.2.2.3.1
    h: 49d0e514c815
  - src: src:std-manuals-sce-rule-21
    loc: sec=h85
    h: 595988bd997f
  review: drafted
- claim_id: c12
  rel: related_to
  target: func:ramp-rate-control
  cite:
  - src: src:std-manuals-sce-rule-21
    loc: sec=h85
    h: 595988bd997f
  review: drafted
- claim_id: c13
  rel: related_to
  target: concept:power-factor
  note: Power factor adjustment is one of the listed smart inverter functions.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=3.2.2.3.1
    h: 49d0e514c815
  - src: src:eq-equip-inverters-sma-shp-peak-3-125-150-shp-peak3-125-150-gridservices-techinfo
    loc: sec=1.2
    h: 41f924383b1b
  review: drafted
- claim_id: c14
  rel: related_to
  target: func:enter-service
  note: Soft-start reconnection is listed as a smart inverter function enabled under IEEE 1547-2018, Rule
    21 and ISO-NE settings.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=7.r9
    h: 09860dc4ab65
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=7.r7
    h: 6fd4084777b5
  review: drafted
---
A smart inverter is an inverter with functions that, once activated, can support the grid on their own when voltage or frequency moves outside normal conditions. Besides converting DC to grid-compliant AC and disconnecting when grid limits are exceeded, it can modulate its output, for example by changing its power factor, to help keep the grid stable. Typical smart inverter functions include power factor adjustment, low- and high-voltage ride-through, volt-watt control, dynamic reactive current support and volt-var control. In product documentation these devices are called grid support utility interactive inverters, and they are tested to UL 1741 SA or, more recently, UL 1741 SB with IEEE 1547-2018. Inverters certified this way need no extra grid monitoring equipment to connect to the utility grid. Some manuals give a default state for each function per grid profile, with ride-through and soft-start reconnection enabled under IEEE 1547-2018, Rule 21 and ISO-NE.
