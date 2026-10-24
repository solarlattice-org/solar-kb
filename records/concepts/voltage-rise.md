---
id: concept:voltage-rise
type: Concept
name: Voltage rise
aliases:
- AC voltage rise
- voltage rise at point of connection
- VRise
- AC line voltage rise
category: Design
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:voltage-drop
  note: Same conductor calculation as voltage drop. It is called voltage rise because inverters generate
    current instead of drawing it.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1
    h: 2497b072ee88
  review: drafted
- claim_id: c2
  rel: related_to
  target: method:ac-voltage-rise-calculation
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1
    h: 2497b072ee88
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.4.1
    h: d2261a2268b4
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.4.7
    h: 90a9fa30bb76
  review: drafted
- claim_id: c3
  rel: explains
  target: symptom:grid-voltage-out-of-range
  note: Too much voltage rise can cause nuisance voltage out-of-range trips under high line voltage.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1
    h: 2497b072ee88
  review: drafted
- claim_id: c4
  rel: related_to
  target: mit:ac-voltage-rise-limit
  note: Enphase guidance aims for a total voltage rise below 2%, with 1% for the section from the combiner
    or PV subpanel to the PCC.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.4.1
    h: d2261a2268b4
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: tbl=2.r3
    h: e8e8d376cf5d
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:point-of-common-coupling
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: tbl=2.r3
    h: e8e8d376cf5d
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:power-quality
  note: On feeders with high PV penetration, voltage rise and fluctuation affect power quality and the
    operation of voltage control devices.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=2.3
    h: a5381672d7b9
  review: drafted
- claim_id: c7
  rel: related_to
  target: func:voltage-trip
  note: Some vendors call their overvoltage protection 'rise-in-voltage protection'. In SMA inverters
    it monitors the 10-minute average AC voltage.
  cite:
  - src: src:sma-doc-275857
    loc: sec=h111
    h: 628ba6583df0
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: sec=h104
    h: 5b040ecb869c
  - src: src:eq-equip-bess-tesla-tesla-powerpack2-installation-manual
    loc: tbl=13
    h: 7bebc0d0f0ee
  review: drafted
  review_note: 'support check: partial - The 10-minute average monitoring is stated, but the passages
    never say that other vendors call overvoltage protection ''rise-in-voltage protection'', and SMA is
    not named. The relation to the voltage trip concept is also only implied by the U>/U>> relay settings.'
- claim_id: c8
  rel: related_to
  target: concept:grid-impedance
  note: The inverter disconnects when grid voltage or grid impedance at its connection point is too high.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h237
    h: 797da27ddf22
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h235
    h: 797da27ddf22
  - src: src:eq-equip-inverters-sma-sma-stp-core1-programming-stp33-62-us-41-ba-en-12-iom
    loc: sec=h217
    h: 797da27ddf22
  review: drafted
---
Voltage rise is the increase in voltage at an inverter's AC terminals that happens because the inverter generates current and pushes it out through the resistance of the wiring. For load circuits the same calculation is called voltage drop. For PV inverters it is called voltage rise because they supply power instead of using it. Getting the voltage rise right at design time helps prevent nuisance trips for voltage out of range when line voltage is high. Lower conductor resistance also means less power loss, less heat at terminals and better system performance. Enphase's method calculates the rise for each wire section separately and checks that the total stays below 2%. If you design to that limit, the small extra losses at terminals, connectors and breakers can be ignored. For the run from the IQ Combiner or PV subpanel to the point of common coupling, Enphase's tables give the maximum conductor lengths that keep that section at 1% rise. On the utility side, large amounts of PV can raise feeder voltage and make it fluctuate. This is worst near the end of long, lightly loaded feeders, and it affects power quality and voltage regulating equipment. If grid voltage or grid impedance at the connection point is too high, an inverter can disconnect from the grid. Some inverters also have a rise-in-voltage protection that watches the 10-minute average AC voltage.

<!-- review notes
- sentence 1: support check: partial - Passage says voltage rises at the AC terminals because inverters generate electricity, but does not explicitly say current is pushed through wiring resistance, though it mentions conductor resistance.
- sentence 1: review: partial - The passage says voltage rises at each inverter's AC terminals because inverters generate electricity, but it does not state the mechanism of current pushed through wiring resistance.
-->
