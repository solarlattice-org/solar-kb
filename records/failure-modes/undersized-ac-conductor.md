---
id: fm:undersized-ac-conductor
type: FailureMode
name: Undersized AC conductor voltage rise
aliases:
- insufficient line cross-section
- AC line too thin
- excessive line resistance
- voltage drop on AC cable
- AC line voltage rise
- VRise
- voltage drop
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:undersized-component
  note: AC conductor cross-section too small for the inverter output current, so line resistance is too
    high.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.1
    h: 3d4e798a2e94
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:long-ac-cable-run
  note: Distance from the inverter or microinverters to the point of common coupling adds resistance and
    voltage rise.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.2
    h: 375bb72cfcef
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:high-grid-voltage
  note: Chronically high utility voltage leaves less margin for wiring voltage rise before trip limits
    are reached.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:poor-connector-contact
  note: Transition resistance at terminals and fuse elements, such as trapped insulation or loose breaker
    screws, adds to the voltage rise.
  cite:
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-doc-278742
    loc: sec=h760
    h: f38aeee9fa0e
  - src: src:sma-doc-259761
    loc: sec=h679
    h: f38aeee9fa0e
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c7
  rel: affects
  target: comp:microinverter
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.2
    h: 375bb72cfcef
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.1
    h: 3d4e798a2e94
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:grid-voltage-out-of-range
  note: Voltage sensed at the inverter terminals goes past the IEEE 1547 limits, which gives an AC voltage
    out-of-range condition.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.2
    h: 375bb72cfcef
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:inverter-shutdown
  note: The inverter disconnects or stops exporting power (nuisance tripping) until the voltage returns
    to range, so energy is lost.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.2
    h: 375bb72cfcef
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.1
    h: 3d4e798a2e94
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:ac-voltage-rise-calculation
  note: Calculate the voltage rise or drop for each wire section at rated operation and check the total
    against the design limit.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.1
    h: 3d4e798a2e94
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.4.1
    h: d2261a2268b4
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:grid-voltage-measurement
  note: Measure the voltage drop during rated operation. A utility data logger at the PCC can record service
    voltage.
  cite:
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  review: drafted
  review_note: 'support check: partial - The passages say to calculate and/or measure voltage drop at
    rated operation and that a utility data logger at the PCC can record voltage, but they do not tie
    these to detecting undersized conductors.'
- claim_id: c12
  rel: mitigated_by
  target: mit:conductor-upsizing
  note: Size the AC conductor cross-section correctly. Going up one AWG size often costs little.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h760
    h: f38aeee9fa0e
  - src: src:sma-doc-259761
    loc: sec=h679
    h: f38aeee9fa0e
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.1
    h: 3d4e798a2e94
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:center-feed-branch
  note: Splitting a microinverter branch into two sub-branches on one OCPD reduces the voltage rise at
    the last microinverter.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.1
    h: 3d4e798a2e94
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:wiring-terminal-check
  note: Fix trapped insulation, loose screw connections and poorly assembled AC connection points.
  cite:
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
  review_note: 'support check: partial - SMA says to optimize connection conditions, naming trapped insulation,
    loose screws and poorly assembled connection points as causes, but it does not explicitly say to fix
    them.'
- claim_id: c15
  rel: mitigated_by
  target: mit:transformer-tap-adjustment
  note: The utility can change the tap on the distribution transformer to give more voltage margin.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: 'Only with grid operator permission: the grid interface voltage limits can be changed, which may
    affect other loads.'
  cite:
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:utility-consultation
  note: The grid operator may adjust voltage, expand the grid or offer a different feed-in point.
  cite:
  - src: src:enphase-enphase-ac-line-voltage-rise-iq-series-tech-brief
    loc: sec=1.3
    h: 19725e2aaa1d
  - src: src:sma-kb-background-information-about-grid-incidents
    loc: sec=h1
    h: af4516340071
  review: drafted
---
When the AC conductor between the inverter and the feed-in point is too small or too long, line resistance gets too high, so the inverter raises its output voltage to export its power. This can push the voltage measured at the inverter terminals above the permitted limit, and the inverter then disconnects or stops exporting power, which shows up as nuisance overvoltage or voltage out-of-range trips. High utility voltage and extra resistance at terminals, fuses and breakers make the problem worse. To confirm it, calculate the voltage rise for each wire section, then measure the voltage drop at rated operation and compare it with the voltage at the feed-in point. Fix it by sizing the AC conductor cross-section correctly, center-feeding long microinverter branches, and tightening or remaking poor terminal connections. If the grid voltage is chronically high, ask the utility about a transformer tap change or a different feed-in point. Change inverter grid limits only with the grid operator's permission.

<!-- review notes
- sentence 4: support check: partial - The passages say to calculate voltage rise per component and to calculate and/or measure the drop at rated operation, but they do not say to compare it with the voltage at the feed-in point.
- sentence 5: support check: partial - Correct conductor sizing and center-feeding are supported, but the passages do not say to tighten or remake terminals, only to optimize the connection conditions, and center-feeding is not limited to long branches.
-->
