---
id: func:rapid-shutdown
type: Function
name: PV rapid shutdown
aliases:
- rapid shutdown
- RSD
- PVRSS
- module-level rapid shutdown
- PV hazard control
- PV Rapid Shutdown System
- PV Hazard Control System
category: Protection
function_kind: protection
claims:
- claim_id: c1
  rel: requires
  target: prod:generac-pv-link
  scope:
    products:
    - prod:generac-snaprs
  note: SnapRS devices must be paired with the Generac S2502 PV Link to make a complete PVRSS under NEC
    690.12.
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h13
    h: 47cb3f937df4
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h34
    h: 6272feef1a7c
  review: drafted
- claim_id: c2
  rel: requires
  target: prod:enphase-iq-system-controller
  scope:
    products:
    - prod:enphase-iq8
  note: Applies only when IQ8 is commissioned in multimode with IQ System Controller 2. A DPST rapid shutdown
    switch wired to the controller then initiates the shutdown.
  cite:
  - src: src:kb-enphase-how-is-rapid-shutdown-initiated-in-an-enphase-system-with-iq8-series-microinver
    loc: sec=h1
    h: c48b7a84e4fd
  - src: src:enphase-enphase-iq8-series-grid-formation-tech-brief
    loc: sec=h5
    h: 43e7a83bbfc8
  review: drafted
- claim_id: c3
  rel: requires
  target: proto:sunspec-rapid-shutdown-signal
  note: Applies when SunSpec-compliant PV array disconnect switches are installed. The inverter sends
    a permission-to-operate signal over the DC conductors and stops sending it when shutdown is initiated.
  cite:
  - src: src:kb-sma-stpxxus50-rapid-shutdown-equipment
    loc: sec=h1
    h: 46538d48fa94
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.10
    h: aea2d80fffb7
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h76
    h: f47c5bb7909c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h80
    h: 813c727c3285
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h68
    h: eea7971c997d
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  attr: trip_threshold
  value:
    max: 30
    unit: unit:V
  conditions: DC conductors after rapid shutdown, complete PVRSS built around an SMA US inverter
  cite:
  - src: src:kb-sma-stpxxus50-rapid-shutdown-equipment
    loc: sec=h1
    h: 46538d48fa94
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.10
    h: aea2d80fffb7
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h76
    h: f47c5bb7909c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h80
    h: 813c727c3285
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h68
    h: eea7971c997d
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  review: drafted
- claim_id: c5
  attr: trip_time
  value:
    max: 30
    unit: unit:SEC
  conditions: Time for an SMA-based PVRSS to bring DC conductors below 30 V
  cite:
  - src: src:kb-sma-stpxxus50-rapid-shutdown-equipment
    loc: sec=h1
    h: 46538d48fa94
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.10
    h: aea2d80fffb7
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h76
    h: f47c5bb7909c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h80
    h: 813c727c3285
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h68
    h: eea7971c997d
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  attr: trip_time
  value:
    max: 15
    unit: unit:SEC
  conditions: PV array disconnect switches disconnecting the array from an SMA inverter after initiation
  cite:
  - src: src:kb-sma-stpxxus50-rapid-shutdown-equipment
    loc: sec=h1
    h: 46538d48fa94
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=4.5.10
    h: aea2d80fffb7
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h76
    h: f47c5bb7909c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h80
    h: 813c727c3285
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h68
    h: eea7971c997d
  - src: src:kb-sma-sbsexx-us-50-rapid-shutdown-equipment
    loc: sec=h1
    h: fbcb8e01281b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  attr: trip_threshold
  value:
    max: 30
    unit: unit:V
  conditions: Controlled conductors leaving the array, as Generac reports the NEC 2014 requirement
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=9.r2
    h: 5fa721a7779b
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9.r2
    h: 5fa721a7779b
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9
    h: 81b573c049b6
  review: drafted
- claim_id: c8
  attr: trip_time
  value:
    max: 10
    unit: unit:SEC
  conditions: Controlled conductors leaving the array, as Generac reports the NEC 2014 requirement
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=9.r2
    h: 5fa721a7779b
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9.r2
    h: 5fa721a7779b
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9
    h: 81b573c049b6
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  attr: trip_threshold
  value:
    max: 30
    unit: unit:V
  conditions: Controlled conductors leaving the array, as Generac reports the NEC 2017/2020 requirement
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=9.r3
    h: 92c7a0443ae4
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9.r3
    h: 92c7a0443ae4
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9
    h: 81b573c049b6
  review: drafted
- claim_id: c10
  attr: trip_threshold
  value:
    max: 80
    unit: unit:V
  conditions: Controlled conductors inside the array boundary or within 1 m (3 ft) of the building penetration
    point, as Generac reports the NEC 2017/2020 requirement
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=9.r3
    h: 92c7a0443ae4
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9.r3
    h: 92c7a0443ae4
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9
    h: 81b573c049b6
  review: drafted
- claim_id: c11
  attr: trip_time
  value:
    max: 30
    unit: unit:SEC
  conditions: Controlled conductors inside and outside the array, as Generac reports the NEC 2017/2020
    requirement
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=9.r3
    h: 92c7a0443ae4
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9.r3
    h: 92c7a0443ae4
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=9
    h: 81b573c049b6
  review: drafted
- claim_id: c12
  attr: trip_threshold
  value:
    max: 80
    unit: unit:V
  scope:
    products:
    - prod:generac-snaprs
  conditions: Controlled conductors within the 1 ft (305 mm) array boundary, SnapRS used with PV Link
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h31
    h: 59459794ebbe
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h48
    h: aa7cf8059dca
  review: drafted
- claim_id: c13
  attr: trip_time
  value:
    max: 30
    unit: unit:SEC
  scope:
    products:
    - prod:generac-snaprs
  conditions: SnapRS used with PV Link, measured from rapid shutdown initiation
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h31
    h: 59459794ebbe
  review: drafted
- claim_id: c14
  attr: response_time
  value:
    max: 10
    unit: unit:SEC
  scope:
    products:
    - prod:generac-pv-link
    - prod:generac-snaprs
  conditions: PV Link and SnapRS response after rapid shutdown initiation (shutdown time of the RS801,
    RS801A and RS802)
  cite:
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: tbl=4.r6
    h: b8913ecab63a
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h48
    h: aa7cf8059dca
  - src: src:generac-generac-pv-link-snaprs-802-install-manual
    loc: sec=h47
    h: 2355b3727d6a
  review: drafted
- claim_id: c15
  attr: trip_threshold
  value:
    max: 30
    unit: unit:V
  scope:
    products:
    - prod:enphase-iq8
  conditions: Rapid shutdown state of IQ8 microinverters after initiation through IQ System Controller
    2
  cite:
  - src: src:enphase-enphase-iq8-series-grid-formation-tech-brief
    loc: sec=h5
    h: 43e7a83bbfc8
  review: drafted
- claim_id: c16
  attr: trip_time
  value:
    max: 30
    unit: unit:SEC
  scope:
    products:
    - prod:enphase-iq8
  conditions: Transition of IQ8 microinverters to the rapid shutdown state
  cite:
  - src: src:enphase-enphase-iq8-series-grid-formation-tech-brief
    loc: sec=h5
    h: 43e7a83bbfc8
  review: drafted
---
Rapid shutdown lowers the voltage on PV conductors after an initiator is operated. Its purpose is to reduce shock hazard for first responders working in and near the array. SMA US inverters are listed under UL 1741 as rapid shutdown equipment only. A complete system also needs PV array disconnect switches and an initiator, which is usually the AC disconnect. When shutdown starts, the inverter stops sending the SunSpec permission-to-operate signal. On the Sunny Boy Smart Energy, the parameter Operation.RSSInitiator selects the initiator: either the AC disconnect or a digital input. Generac PV Link handles shutdown of the conductors leaving the array. For 2017 and 2020 NEC compliance, one SnapRS per module must be added and the Enable PVRSS setpoint turned on (it ships off). Enphase IQ8 systems without an IQ System Controller can use the PV or service disconnect as the initiator. In multimode with IQ System Controller 2, the Enphase DPST System Shutdown Switch is required instead. If the IQ System Controller stays in rapid shutdown or reports a rapid shutdown error, check the wiring of the rapid shutdown switch.

<!-- review notes
- sentence 1: support check: partial - Passages say rapid shutdown protects first responders and reduces shock hazard in the array, but voltage reduction after initiator operation is only implied.
- sentence 2: support check: partial - Listing as PVRSE, complete system components, AC disconnect initiator and signal stop are stated, but 'only' and 'usually the AC disconnect' for US inverters are not exactly stated.
- sentence 6: support check: partial - u34 says to test the wiring if the controller stays in rapid shutdown; u17 mentions the error but neither explicitly says to check wiring for the error case.
-->
