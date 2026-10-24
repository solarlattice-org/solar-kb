---
id: prod:sma-sunny-tripower-core2
type: Product
name: Sunny Tripower CORE2
aliases:
- STP 110-60
- CORE2
- STP110-60
- Sunny Tripower 110-60
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:sma-kb-update-firmware-of-sunny-tripower-core2-inverter
    loc: sec=h1
    h: db3be204ec68
  - src: src:sma-kb-stp110-60-core2-inverter-commissioning-checklist
    loc: sec=h1
    h: cd96a02fc932
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: The SMA Data Manager controls and monitors the inverter over SunSpec Modbus. Register it with
    the SunSpec profile and Unit ID 1.
  cite:
  - src: src:sma-kb-registering-sunny-tripower-core2-in-sma-data-manager-m
    loc: sec=h1
    h: a17fc3cdf3cc
  - src: src:sma-kb-stp110-60-core2-inverter-commissioning-checklist
    loc: sec=h1
    h: cd96a02fc932
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:ethernet
  note: For a direct Ethernet connection the default inverter IP is 169.254.12.3. If DHCP gives no address,
    the board falls back to that address or the next free local address.
  cite:
  - src: src:sma-kb-update-firmware-of-sunny-tripower-core2-inverter
    loc: sec=h1
    h: db3be204ec68
  - src: src:sma-kb-communication-board-reset-for-sunny-tripower-core2
    loc: sec=h1
    h: 6fa40dc62ba3
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:sma-data-manager-m
  scope:
    firmware_min: 1.00.04.R
  conditions: Before registration, update the inverter firmware to 1.00.04.R or later and the Data Manager
    M firmware to 1.09.06.R or later. Follow the commissioning steps in the stated order.
  cite:
  - src: src:sma-kb-registering-sunny-tripower-core2-in-sma-data-manager-m
    loc: sec=h1
    h: a17fc3cdf3cc
  - src: src:sma-kb-sunny-tripower-core2-and-sma-data-manager-m-commissioning-notes
    loc: sec=h1
    h: 624f3b810331
  - src: src:sma-kb-stp110-60-core2-inverter-commissioning-checklist
    loc: sec=h1
    h: cd96a02fc932
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:sma-energy-meter
  conditions: For export limitation through the Data Manager. The source uses the EM-20 as its example
    and says other meters can also be used.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  review: drafted
- claim_id: c6
  rel: requires
  target: prod:sma-data-manager-m
  conditions: Export limitation and control need an SMA Data Manager (EDMM-10) acting as master.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  review: drafted
  review_note: 'support check: partial - The passages say a Data Manager (EDMM-10) is needed for export
    limitation and control, but they do not say the CORE2 requires it in general; the Data Manager is
    described as optional.'
- claim_id: c7
  rel: implements
  target: func:export-limitation
  conditions: Configured in the Data Manager. Use closed-loop control, and set the active power setpoint
    as a percentage of total system power.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  review: drafted
- claim_id: c8
  rel: implements
  target: func:active-power-setpoint
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  - src: src:sma-kb-zero-feed-in-power-with-sunny-tripower-stp110-60-core2
    loc: sec=h1
    h: 5a8fe0a4eb3f
  review: drafted
- claim_id: c9
  rel: implements
  target: func:zero-export
  scope:
    firmware_min: 1.01.03.R
  conditions: With the parameter WlimitShutdownENA set to On, a 0% setpoint disconnects the inverter from
    the grid. With it set to Off, the inverter regulates down to a minimum of 1-2 kW. Requires firmware
    1.01.03.R or later.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  - src: src:sma-kb-zero-feed-in-power-with-sunny-tripower-stp110-60-core2
    loc: sec=h1
    h: 5a8fe0a4eb3f
  review: drafted
- claim_id: c10
  rel: implements
  target: func:communication-loss-fallback
  conditions: Sets a waiting time (minimum 20 seconds) and a fallback value for when communication with
    the Data Manager fails. In fallback, the inverter cannot be set to disconnect from the grid.
  cite:
  - src: src:sma-kb-zero-feed-in-power-with-sunny-tripower-stp110-60-core2
    loc: sec=h1
    h: 5a8fe0a4eb3f
  review: drafted
- claim_id: c11
  rel: implements
  target: func:ramp-rate-control
  conditions: With firmware 1.00.08.R or earlier, set the active power gradient at the inverter web interface.
    Set it right after the grid code is first set, so it is not overwritten.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  - src: src:sma-kb-active-power-gradient-ramp-rate-at-stp-110-60-web-interface
    loc: sec=h1
    h: c9124120d168
  review: drafted
- claim_id: c12
  rel: implements
  target: func:shade-tolerant-mppt
  note: SMA ShadeFix. Since March 2023 it can be scheduled with the parameter MPPSHdwTime in the group
    Extended Model 2-1 RW.
  cite:
  - src: src:sma-kb-can-i-set-the-time-interval-for-sma-shadefix-in-the-core2
    loc: sec=h1
    h: 7f5b5bf6b179
  review: drafted
- claim_id: c13
  rel: requires
  target: role:installer-access-level
  conditions: Firmware updates are done after logging in to the inverter user interface as Installer.
    The country data set must be configured as part of the procedure.
  cite:
  - src: src:sma-kb-update-firmware-of-sunny-tripower-core2-inverter
    loc: sec=h1
    h: db3be204ec68
  review: drafted
  review_note: 'support check: partial - The passages show that the firmware update procedure uses an
    Installer login and a mandatory country data set, but they do not say the CORE2 generally requires
    installer access.'
---
The Sunny Tripower CORE2, also called STP110-60, is a three-phase string inverter family from SMA. The SMA Data Manager M controls and monitors it over SunSpec Modbus, using the SunSpec profile and Unit ID 1. Before commissioning, update the inverter and the Data Manager M firmware, then register the inverter. Do these steps in the stated order. To update the firmware, log in as Installer and set the country data set first. Do the update while there is enough sunlight, because AC supply alone is not sufficient. Export limitation and zero export are set up through the Data Manager with an energy meter, using closed-loop active power setpoints. At a 0% setpoint the inverter can either disconnect from the grid or regulate down to a minimum of 1-2 kW. The parameter WlimitShutdownENA selects which. A fallback value applies if communication with the Data Manager is lost. The communication board can be reset in two ways. A short button press restarts the communication processor without changing settings. A press of about 30 seconds does a factory reset, which clears passwords and network settings. The grounding conductor needs a low-impedance connection within the specified cross-section range. Poor grounding can cause transient overvoltages that damage the device, and that damage is not covered by the warranty.

<!-- review notes
- sentence 1: support check: partial - The passages show STP110-60 is the CORE2 and that it is an SMA string inverter, but they do not say it is three-phase.
-->
