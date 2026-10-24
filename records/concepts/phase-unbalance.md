---
id: concept:phase-unbalance
type: Concept
name: Phase unbalance
aliases:
- unbalanced load
- unbalanced load limit
- phase asymmetry
- phase imbalance
- voltage unbalance
- unbalance factor
- apparent power unbalance
category: Grid
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: concept:symmetrical-components
  note: Unbalance factor is expressed as the ratio of negative or zero sequence component to the positive
    sequence component, in percent.
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: sec=h115
    h: 9988fc3d8734
  review: drafted
- claim_id: c2
  rel: related_to
  target: meas:negative-sequence-voltage-imbalance
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: sec=h115
    h: 9988fc3d8734
  review: drafted
  review_note: 'support check: partial - Negative sequence ratio is mentioned for voltage/current unbalance,
    but not specifically a named negative-sequence voltage imbalance measure.'
- claim_id: c3
  rel: related_to
  target: meas:zero-sequence-imbalance
  cite:
  - src: src:eq-equip-meters-accuenergy-acuvim-ii-docs-acuvim-ii-meter-acuvim-ii-power-meter-user-manual-1040e130
    loc: sec=h115
    h: 9988fc3d8734
  review: drafted
  review_note: 'support check: partial - Zero-sequence ratio is mentioned within the unbalance factor,
    though not as a distinct zero-sequence imbalance measurement.'
- claim_id: c4
  rel: related_to
  target: concept:apparent-power
  note: Apparent power equations can be expanded to cover arbitrary unbalanced phase voltages and currents;
    single-phase inverter feed-in can be limited to cap apparent power unbalance.
  cite:
  - src: src:sma-doc-275857
    loc: sec=4.3
    h: a54d6137421f
  - src: src:book-handbook-of-power-system-engineering
    loc: sec=11.3
    h: 1fd7b958e5a8
  review: drafted
- claim_id: c5
  rel: related_to
  target: symptom:phase-imbalance
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h86
    h: 7dbc888afa3e
  - src: src:eq-equip-inverters-solaredge-design-installation-troubleshooting-addendum-for-installation-guide-v4
    loc: tbl=2.r18
    h: 11af0e17667a
  review: drafted
- claim_id: c6
  rel: related_to
  target: func:phase-balancing
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-troubleshooting-addendum-for-installation-guide-v4
    loc: tbl=2.r18
    h: 11af0e17667a
  review: drafted
  review_note: 'support check: partial - Passage only shows a Phase Unbalance fault with a Phase Balance
    disable setting; relation to phase balancing is implied but thin.'
- claim_id: c7
  rel: related_to
  target: mit:phase-load-balancing
  cite:
  - src: src:std-utilities-nstar-ma-requirements-for-electric-service
    loc: sec=h80
    h: 670d54db62d0
  - src: src:std-utilities-nat-grid-ma-ny-shared-constr-esb756
    loc: sec=h200
    h: 718fdbc3b9cf
  review: drafted
- claim_id: c8
  rel: related_to
  target: std:eversource-ma-requirements-for-electric-service
  note: Section 309 requires customer load to normally be balanced within 10 percent between phases on
    three-phase services.
  quote: the load will normally be balanced to within 10 percent between phases on three phase services
  quote_source: NSTAR Requirements for Electric Service §309
  cite:
  - src: src:std-utilities-nstar-ma-requirements-for-electric-service
    loc: sec=h80
    h: 670d54db62d0
  review: drafted
- claim_id: c9
  rel: related_to
  target: symptom:phase-loss
  note: Single-phasing (one phase open) produces unbalanced currents; inverter AC current unbalance faults
    call for checking for phase loss.
  cite:
  - src: src:ref-reference-short-circuit-calcs-bussman-sht-ckt-curr-calcs
    loc: sec=h52
    h: a0f7016484aa
  - src: src:sungrow-sungrow-sg3425ud-mv-sg3600ud-mv-user-manual-ver113-202502
    loc: tbl=50.r6
    h: cb0ca7cf1f72
  review: drafted
- claim_id: c10
  rel: related_to
  target: meas:grid-voltage-imbalance-fault
  cite:
  - src: src:eq-equip-inverters-sungrow-sg2500u-ti-sg2500u-sen-ver11-201706-install-manual
    loc: tbl=35.r27
    h: f88ae83d5006
  - src: src:eq-equip-inverters-sungrow-sg2500u-ti-sg2500u-sen-ver11-201706-install-manual
    loc: tbl=35.r28
    h: 98e22e627a15
  review: drafted
- claim_id: c11
  rel: related_to
  target: meas:unequal-phase-voltages
  cite:
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: tbl=27.r2
    h: b4a7e1d21118
  - src: src:eq-equip-meters-ge-kv2c-meters-geh-7285
    loc: tbl=28.r2
    h: b46619f3da41
  review: drafted
---
Phase unbalance means the voltages or currents of a three-phase system are not equal in magnitude, or the angles between the phases are not equal. Meters express it as an unbalance factor: the negative or zero sequence component divided by the positive sequence component, given as a percentage. This is based on symmetrical components. Unbalance is common on distribution feeders because many loads and generators are connected single-phase, so studies of high PV penetration need detailed unbalanced line models. Utilities set limits on unbalance. One service rulebook requires customer load to stay within 10 percent between phases, and another says voltage unbalance caused by a generator's unbalanced currents must not exceed 2%. If one phase opens (single-phasing), the currents become unbalanced and motors can overheat and fail. Inverters often trip on voltage or current unbalance, so check for phase loss when you see one of these faults. Meter diagnostics that flag voltage imbalance can point to a lost phase voltage, a blown VT fuse, a wrong VT ratio or a wiring error. In the field, have the phase conductors and neutral measured and the wiring rechecked. On three-phase microinverter branches, keep unused connectors to a minimum. Some inverters also have phase balance or apparent power unbalance limits that you can set.

<!-- review notes
- sentence 2: support check: partial - Ratio and percent are stated, but 'meters' (Acuview software) and 'based on symmetrical components' are only implied via sequence components.
- sentence 3: support check: partial - Passage says unbalance is common due to single-phase connections and detailed line models are needed, but 'many loads and generators' and high-PV studies mostly fit; unbalanced model need is stated generally.
- sentence 5: support check: partial - Single-phasing effects and phase loss check are stated, but 'inverters often trip on voltage or current unbalance' is only loosely supported by threshold settings and one fault.
-->
