---
id: prod:sma-sunny-tripower-smart-energy
type: Product
name: Sunny Tripower Smart Energy
aliases:
- STP SE
- STP 5.0-10.0-3SE-40
- STPxx-3SE-40
- STP-3SE-40
- STPxxx-3SE-40
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-event-6422-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: f45be8f2c0e9
  review: drafted
  review_note: 'support check: partial - Passage refers to ''your SMA inverter'' and sma-service.com but
    never explicitly says SMA makes the Sunny Tripower Smart Energy; it''s strongly implied.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Three-phase hybrid inverter for DC coupling of high-voltage batteries
  cite:
  - src: src:sma-kb-market-launch-sunny-tripower-smart-energy-stp5-10se
    loc: sec=h1
    h: 0b67b4231da4
  - src: src:sma-kb-perform-a-firmware-update-for-sunny-tripower-smart-energy
    loc: sec=h1
    h: 0419be46ccc7
  review: drafted
- claim_id: c3
  rel: implements
  target: func:backup-power
  note: Integrated three-phase battery-backup function; handles unbalanced loads in backup operation
  cite:
  - src: src:sma-kb-market-launch-sunny-tripower-smart-energy-stp5-10se
    loc: sec=h1
    h: 0b67b4231da4
  - src: src:sma-kb-is-the-backup-power-supply-of-sunny-tripower-smart-energy-three-phase
    loc: sec=h1
    h: c67c65845763
  - src: src:sma-kb-is-the-sunny-tripower-smart-energy-fully-capable-of-handling-unbalanced-loads
    loc: sec=h1
    h: b01da04dc3c8
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:byd-battery-box-premium-hv
  note: BYD HVS and HVM series compatible at market launch
  cite:
  - src: src:sma-kb-market-launch-sunny-tripower-smart-energy-stp5-10se
    loc: sec=h1
    h: 0b67b4231da4
  review: drafted
  review_note: 'support check: partial - HVS and HVM series from BYD are stated compatible at launch,
    but the passage doesn''t name ''Battery-Box Premium'' explicitly.'
- claim_id: c5
  rel: compatible_with
  target: prod:sma-sunny-tripower-x
  conditions: Operated as subordinate device under a Sunny Tripower X 25 acting as System Manager; Sunny
    Tripower X 25 needs firmware 03.14.20.R or later
  cite:
  - src: src:sma-kb-is-the-sunny-tripower-x-as-a-system-manager-compatible-with-the-sunny-tripower-smar
    loc: sec=h1
    h: 639dfc70649d
  - src: src:sma-kb-can-the-sunny-tripower-x-be-integrated-into-a-single-system-along-with-sunny-tripow
    loc: sec=h1
    h: 64fe4446d3f9
  review: drafted
- claim_id: c6
  rel: compatible_with
  target: prod:sma-sunny-home-manager-2
  note: Recommended for energy management and forecast features
  cite:
  - src: src:sma-kb-can-the-sunny-tripower-x-be-integrated-into-a-single-system-along-with-sunny-tripow
    loc: sec=h1
    h: 64fe4446d3f9
  - src: src:sma-doc-259463
    loc: tbl=15.r6
    h: b52491138cdc
  review: drafted
- claim_id: c7
  rel: compatible_with
  target: prod:sma-energy-meter
  note: Energy meter alone supports dynamic active power limitation but not intelligent load control
  cite:
  - src: src:sma-doc-259463
    loc: tbl=10.r2
    h: 3c43e3fe37ce
  - src: src:sma-doc-259463
    loc: tbl=10.r3
    h: 5c872b7c72fb
  review: drafted
- claim_id: c8
  rel: incompatible_with
  target: prod:sma-sunny-boy-storage
  conditions: Combination in one system not permitted
  cite:
  - src: src:sma-doc-259463
    loc: tbl=18
    h: ded43b6910ab
  review: drafted
- claim_id: c9
  rel: lacks
  target: func:system-manager
  cite:
  - src: src:sma-doc-275857
    loc: tbl=5.r1
    h: 26750d7c2568
  - src: src:sma-doc-275857
    loc: tbl=5
    h: 3616ff4f03a2
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:can-bus
  note: Battery communication over CAN; Cat5e or better, twisted pair, at most 10 m
  cite:
  - src: src:sma-kb-event-9308-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: 311f00d8060a
  - src: src:sma-kb-event-9339-with-sunny-tripower-smart-energy
    loc: sec=h1
    h: 6a386298ab76
  review: drafted
- claim_id: c11
  rel: implements
  target: func:export-limitation
  conditions: Dynamic active power limitation with SMA Energy Meter or Sunny Home Manager
  cite:
  - src: src:sma-doc-259463
    loc: tbl=10.r3
    h: 5c872b7c72fb
  review: drafted
  review_note: 'support check: partial - Dynamic active power limitation is shown supported with Energy
    Meter and Home Manager, but the passage doesn''t explicitly equate it with export limitation.'
- claim_id: c12
  attr: rated_power
  value:
    max: 10
    unit: unit:KiloW
  scope:
    applications:
    - backup
  conditions: Backup power supply for loads, total over all three phases, depending on device type
  cite:
  - src: src:sma-kb-is-the-backup-power-supply-of-sunny-tripower-smart-energy-three-phase
    loc: sec=h1
    h: c67c65845763
  review: drafted
- claim_id: c13
  attr: rated_power
  value:
    max: 3.3
    unit: unit:KiloW
  scope:
    applications:
    - backup
  conditions: Backup power supply for loads, per phase, depending on device type
  cite:
  - src: src:sma-kb-is-the-backup-power-supply-of-sunny-tripower-smart-energy-three-phase
    loc: sec=h1
    h: c67c65845763
  review: drafted
---
The Sunny Tripower Smart Energy is a three-phase SMA hybrid inverter for home PV systems with DC-coupled high-voltage batteries. It comes as the STP5.0, STP6.0, STP8.0 and STP10.0-3SE-40. Its built-in battery-backup function is three-phase and can supply loads up to 10 kW across all phases and up to 3.3 kW per phase, depending on the model. It handles unbalanced loads in backup operation. It may only be run with an intrinsically safe lithium-ion battery that SMA has approved. At launch the approved batteries were the BYD HVS and HVM series. The battery communicates over a CAN cable, which must be at least Cat5e, twisted pair and no longer than 10 meters. It has no System Manager function. It can run as a subordinate device under a Sunny Tripower X 25 System Manager, and SMA recommends pairing it with Sunny Home Manager 2.0 for energy management. It must not be combined with Sunny Boy Storage, Sunny Island, third-party PV inverters or SMA micro inverters. Other PV inverters are allowed only if they work with the Sunny Home Manager. Software algorithms prevent impermissible overcurrent. The listed maximum miniature circuit breaker characteristic of B32 applies only to parallel grid operation. Known issues include energy data tables not matching the energy balance graphic in Sunny Portal or the WebUI, and display errors on the day an energy meter is replaced. SMA says a future firmware update will fix both. Firmware updates need the installer password. Battery communication events such as 9308 and 9339 point to cabling or CAN wiring problems. Event 6422 is a device fault: disconnect the inverter, wait 15 minutes and recommission it, and replace the inverter if the event comes back.

<!-- review notes
- sentence 1: support check: partial - Three-phase hybrid inverter, DC coupling of HV batteries and the model variants are stated; 'SMA' manufacturer is only implied.
- sentence 3: support check: partial - Approved intrinsically safe Li-ion battery requirement, BYD HVS/HVM at launch, and Cat5e/10 m/twisted pair for CAN are stated, but 'CAN cable' for the battery communication is via the event 9339 text and fine; 'may only be run' with approved battery is stated—though 'approved batteries were BYD only at launch' slightly overstates since others were planned.
- sentence 6: support check: partial - Software algorithms prevent overcurrent and tripping characteristics are only relevant for parallel grid operation, and B32 is listed; stated as 'only relevant' rather than 'maximum'—largely matches.
- sentence 8: support check: partial - Event 6422 handling is stated and 9339/9308 involve battery cable/CAN checks, but 9308 isn't explicitly said to be a wiring issue beyond cabling checks (title mentions wiring); mostly supported.
-->
