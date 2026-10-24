---
id: prod:sma-sunny-home-manager-2
type: Product
name: Sunny Home Manager 2.0
aliases:
- SHM 2.0
- Home Manager 2.0
- HM-20
- Sunny Home Manager
category: Monitoring and communications
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-sunny-home-manager-2-0-manual
    loc: sec=h1
    h: 5a8e8a3590fd
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:energy-meter
  note: Can be added as the energy meter in the SMA EV Charger web interface.
  cite:
  - src: src:sma-kb-ev-charger-how-to-add-the-sunny-home-manager-2-0-as-energy-meter
    loc: sec=h1
    h: 48786c69352f
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:speedwire
  note: The EV Charger finds the Home Manager by searching for SMA Speedwire devices.
  cite:
  - src: src:sma-kb-ev-charger-how-to-add-the-sunny-home-manager-2-0-as-energy-meter
    loc: sec=h1
    h: 48786c69352f
  review: drafted
  review_note: 'support check: partial - EV Charger is shown searching for SMA Speedwire devices to add
    the HM, implying Speedwire, but it''s not stated outright.'
- claim_id: c4
  rel: implements
  target: func:forecast-based-charging
  cite:
  - src: src:sma-kb-is-a-sunny-home-manager-necessary-when-using-sunny-tripower-smart-energy
    loc: sec=h1
    h: 41421c337584
  - src: src:sma-kb-sunny-home-manager-2-0-kompatibel-mit-niko-home-control
    loc: sec=h1
    h: 448fabb566f1
  review: drafted
- claim_id: c5
  rel: implements
  target: func:remote-firmware-update
  note: Automatic updates through Sunny Portal are switched on by default.
  cite:
  - src: src:sma-kb-setting-automatic-firmware-updates-for-the-sunny-home-manager
    loc: sec=h1
    h: 2355fd18c118
  review: drafted
- claim_id: c6
  rel: requires
  target: tool:sma-sunny-portal
  note: Communicates directly with Sunny Portal; firmware checks and settings are done in the portal.
  cite:
  - src: src:sma-doc-sunnyportalennexos-ba-en-16
    loc: sec=5.1.4.1
    h: f7ef80cf899b
  - src: src:sma-kb-checking-the-firmware-version-of-the-sunny-home-manager
    loc: sec=h1
    h: aa2a544a3008
  - src: src:sma-kb-setting-automatic-firmware-updates-for-the-sunny-home-manager
    loc: sec=h1
    h: 2355fd18c118
  review: drafted
  review_note: 'support check: partial - Passages show direct communication with Sunny Portal and firmware
    checks there, but not that it is required.'
- claim_id: c7
  rel: requires
  target: role:installer
  note: Must be installed by solar power professionals.
  cite:
  - src: src:sma-kb-who-can-install-the-sunny-home-manager-2-0
    loc: sec=h1
    h: d01badd80a53
  review: drafted
- claim_id: c8
  rel: requires
  target: role:administrator
  conditions: When replacing the Home Manager in a PV system
  cite:
  - src: src:sma-kb-replacing-the-sunny-home-manager-2-0-in-a-pv-system
    loc: sec=h1
    h: 27f344d33490
  review: drafted
- claim_id: c9
  rel: compatible_with
  target: prod:sma-energy-meter
  cite:
  - src: src:sma-doc-278405
    loc: sec=2.1.1.1
    h: 99414370801c
  - src: src:sma-doc-244194
    loc: sec=6
    h: 0c85658428c0
  - src: src:sma-doc-259463
    loc: tbl=13.r3
    h: 174f0e41ed72
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:sma-sunny-tripower-smart-energy
  note: Not required for basic battery operation, but recommended for the full feature set.
  cite:
  - src: src:sma-kb-is-a-sunny-home-manager-necessary-when-using-sunny-tripower-smart-energy
    loc: sec=h1
    h: 41421c337584
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:sma-ev-charger
  cite:
  - src: src:sma-kb-ev-charger-how-to-add-the-sunny-home-manager-2-0-as-energy-meter
    loc: sec=h1
    h: 48786c69352f
  review: drafted
- claim_id: c12
  rel: compatible_with
  target: prod:niko-home-control
  scope:
    regions:
    - region:be
    firmware_min: 2.11.5.R
  conditions: Only selected Niko plugs are supported
  cite:
  - src: src:sma-kb-sunny-home-manager-2-0-kompatibel-mit-niko-home-control
    loc: sec=h1
    h: 448fabb566f1
  review: drafted
- claim_id: c13
  rel: compatible_with
  target: prod:avm-fritz-dect-200
  cite:
  - src: src:sma-kb-sunny-home-manager-hm-20-functions-of-the-radio-controlled-socket
    loc: sec=h1
    h: 62efe9abed5b
  review: drafted
- claim_id: c14
  rel: compatible_with
  target: prod:avm-fritz-dect-210
  cite:
  - src: src:sma-kb-sunny-home-manager-hm-20-functions-of-the-radio-controlled-socket
    loc: sec=h1
    h: 62efe9abed5b
  review: drafted
- claim_id: c15
  rel: compatible_with
  target: prod:edimax-sp-2101w
  conditions: Original SP-2101W with socket firmware up to 4.08; SP-2101W V2 from socket firmware 1.00
  cite:
  - src: src:sma-kb-sunny-home-manager-hm-20-functions-of-the-radio-controlled-socket
    loc: sec=h1
    h: 62efe9abed5b
  review: drafted
- claim_id: c16
  attr: max_count
  value:
    max: 1
    unit: unit:NUM
  conditions: Sunny Home Manager 2.0 units per system in Sunny Portal powered by ennexOS
  cite:
  - src: src:sma-doc-sunnyportalennexos-ba-en-16
    loc: sec=h22
    h: f6efa1d696c2
  review: drafted
  review_note: 'support check: partial - Says 1 Home Manager 2.0 per system but the passage doesn''t mention
    ennexOS explicitly (though presumably Sunny Portal); ''up to 1'' fits roughly.'
---
The Sunny Home Manager 2.0 (HM-20) is an SMA energy management and monitoring device. It controls connected devices, monitors the system and handles communication with Sunny Portal. It works with the SMA Energy Meter. It can also be added over Speedwire as the grid connection point meter in the SMA EV Charger. It offers forecast-based energy management and battery charging. SMA recommends it with the Sunny Tripower Smart Energy when heat pumps, EVs or several inverters are involved. It can switch and read supported smart plugs: AVM FRITZ!DECT 200 and 210, and Edimax SP-2101W. From firmware 2.11.5.R it also works with Niko Home Control, for the Belgian market only. A third-party energy meter can be used for generator measurement but not for load monitoring. The Home Manager can be used without a PV system. Only one Home Manager 2.0 is allowed per system. Firmware updates install automatically through Sunny Portal by default. Known issue: after updating to firmware 2.6.6.R, battery inverters may not charge correctly in zero-export systems. Update to 3.30.12.R or higher to fix this. After a FRITZ!Box update to version 7.26, communication with AVM plugs can stop. To fix it, set the login type in Sunny Portal to FRITZ!Box user and password.

<!-- review notes
- sentence 2: support check: partial - Works with SMA Energy Meter is supported, but 'as grid connection point meter' via Speedwire is only implied by the setting for meter at point of interconnection.
- sentence 7: support check: partial - Charging problem after 2.6.6.R and fix with 3.30.12.R or higher are stated, but 'zero-export' is only in the title and 'may not' is slightly softer.
-->
