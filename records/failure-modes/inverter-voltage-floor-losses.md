---
id: fm:inverter-voltage-floor-losses
type: FailureMode
name: Inverter Voltage Floor Losses
category: Inverters
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  note: The inverter's minimum DC input voltage stops MPPT from following the array Vmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c2
  rel: caused_by
  target: stressor:high-temperature
  note: Module voltage falls as cell temperature rises, so array Vmp can drop below the inverter's DC
    floor during hot periods.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: caused_by
  target: stressor:reactive-power-demand
  note: Reactive power operation can shift the inverter's effective operating voltage window.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: caused_by
  target: stressor:ac-voltage-hysteresis
  note: AC voltage behavior can change the effective inverter operating window.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: caused_by
  target: stressor:module-degradation
  note: Degraded modules can lower array Vmp below the inverter's DC input limit.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  rel: caused_by
  target: stressor:insufficient-string-voltage-margin
  note: A string design without enough voltage margin leaves little headroom above the inverter minimum.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: caused_by
  target: stressor:inverter-settings
  note: Inverter settings, transformer tap position or plant voltage control may be the root cause.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: presents_as
  target: symptom:expected-vs-measured-gap
  note: The power the array could deliver is higher than the power harvested at the inverter operating
    point.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - The gap between available and harvested power is stated, but
    ''persistent'' is not stated.'
- claim_id: c9
  rel: presents_as
  target: symptom:low-output-despite-irradiance
  note: Irradiance and inverter availability can look normal while output stays below expectation.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c10
  rel: presents_as
  target: symptom:dc-voltage-at-minimum
  note: Inverter DC voltage sits at or near its minimum operating threshold.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c11
  rel: presents_as
  target: symptom:operating-voltage-above-vmp
  note: The measured operating voltage stays above the IV-derived Vmp, and operating power stays below
    the IV-derived Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c12
  rel: detected_by
  target: method:iv-curve-tracing
  note: In-situ or string-level IV sweeps give an independent estimate of Vmp and Pmp to compare with
    the inverter operating point.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:performance-monitoring
  note: Look in SCADA operating points for intervals where DC voltage is pinned at the floor.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: drafted
  review_note: 'support check: partial - SCADA operating points are in detection, and u7 looks for DC
    voltage pinned at the minimum, but ''performance monitoring'' is not named explicitly.'
- claim_id: c14
  rel: detected_by
  target: method:reactive-power-review
  note: Check AC voltage and reactive power dispatch at the same timestamps as the suspected events.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c15
  rel: detected_by
  target: method:inverter-settings-review
  note: Compare the inverter's DC voltage limits with the operating data and module temperature.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c16
  rel: distinguished_from
  target: fm:inverter-clipping
  by: method:iv-curve-tracing
  note: Clipping is a power ceiling. Voltage flooring is an MPPT limit set by the DC voltage window. Reviewing
    DC voltage, AC voltage, reactive power and IV-derived Vmp together tells them apart.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: drafted
  review_note: 'support check: partial - Clipping vs. flooring and reviewing DC voltage, AC voltage, reactive
    power and IV-derived Vmp together are stated, but IV tracing is not specifically given as the distinguishing
    method.'
- claim_id: c17
  rel: mitigated_by
  target: mit:transformer-tap-adjustment
  note: Coordinate with the plant electrical engineer and the inverter supplier.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:inverter-parameter-change
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c19
  rel: mitigated_by
  target: mit:voltage-control-strategy
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:reactive-power-validation
  note: Confirm that reactive power obligations are still met after any change.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:string-voltage-margin-design
  note: Future string designs should keep voltage margin at both low and high temperatures.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c22
  rel: mitigated_by
  target: mit:mppt-recovery-retest
  note: Retest under high-temperature operation and compare against IV-derived Vmp and Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=front
    h: 568e994d4904
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h7
    h: 0329d3a61473
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c23
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss over summer 2025 at a 100 MW PV plant in California (Leeward Renewable
    Energy / OTT HydroMet poster); reported as about this value
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Inverter voltage floor losses happen when the array's maximum power point voltage falls below the inverter's minimum DC input voltage. The inverter stays online but cannot track the true Vmp, so some available energy is never harvested. It shows up mostly in hot weather, because module voltage drops as cells heat up. Degraded modules, a tight string design margin, or high reactive power demand make it worse. In monitoring data it can look like clipping or general underperformance. Inverter DC voltage sits at its minimum while output is lower than irradiance would support. To confirm it, compare the inverter operating voltage with an IV-derived Vmp from IV tracers or a temperature-corrected model. It is a voltage floor event if the operating voltage stays above Vmp and the operating power stays below Pmp. Rule out outages, curtailment, clipping, soiling and sensor faults first. Then check AC voltage and reactive power dispatch at the same timestamps. Work out fixes with the inverter supplier and the plant electrical engineer. Options include transformer tap changes, inverter parameter or voltage control changes, and more string voltage margin in future designs. After making changes, retest MPPT recovery in hot conditions against IV-derived Vmp and Pmp, and confirm reactive power obligations are still met.

<!-- review notes
- sentence 2: support check: partial - Hot-weather onset and the role of degraded modules, string margin and reactive power are stated, but 'mostly' is stronger than 'most likely' and 'tight' margin is only implied.
-->
