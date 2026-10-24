---
id: prod:fronius-datamanager
type: Product
name: Fronius Datamanager
aliases:
- Datamanager 2
- Datamanager 2.0
- Fronius Datamanager 2.0
- Fronius Data Manager 2.0
category: Monitoring and communications
make: fronius
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fronius
  cite:
  - src: src:kb-fronius-fronius-datamanager-2-0-emanual-troubleshooting
    loc: sec=front
    h: 7b1cd1544a28
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:monitoring-gateway
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:fronius-symo
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h58
    h: b55ec31467aa
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h54
    h: 7c1eebc4ddc8
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:fronius-smart-meter
  note: The inverter can be controlled using readings from connected meters.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:fronius-solar-net
  note: Several inverters can be linked in a Solar Net ring, with one Datamanager set as primary and the
    rest as secondary.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h54
    h: 7c1eebc4ddc8
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Used for inverter control.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:modbus-rtu
  note: Used for inverter control.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:wifi
  note: Connects to Solar.web over Wi-Fi; a temporary WLAN access point is used for commissioning.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:ethernet
  note: LAN connection to Solar.web.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c10
  rel: implements
  target: func:limit-active-power
  note: The user sets power limits for the inverter.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c11
  rel: implements
  target: func:scheduling
  note: Minimum, maximum or target operating times can be set.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
  review_note: 'support check: partial - Min/max/target operational times are listed, but scheduling of
    power values and modes is only loosely implied.'
- claim_id: c12
  rel: implements
  target: func:digital-input-power-reduction
  note: Uses a ripple control signal receiver to set reactive or active power.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
- claim_id: c13
  rel: implements
  target: func:export-limitation
  note: Dynamic power reduction that takes self-consumption into account.
  cite:
  - src: src:fronius-fronius-galvo-208-240-operating-instructions-42-0410-1934
    loc: sec=h39
    h: 9a8cde0d2d97
  review: drafted
  review_note: 'support check: partial - Dynamic power reduction considering self consumption is stated,
    but not called export limitation.'
- claim_id: c14
  attr: max_count
  value:
    max: 1
    unit: unit:NUM
  conditions: Datamanagers in primary operation per Fronius Solar Net ring; set the others to secondary
    or remove them
  cite:
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h54
    h: 7c1eebc4ddc8
  - src: src:fronius-fronius-symo-208-240-480-operating-instructions-42-0410-2124
    loc: sec=h246
    h: a5fc38e344b0
  review: drafted
---
The Fronius Datamanager 2.0 is a Fronius monitoring and communications unit. It comes as a plug-in card for the inverter or as a separate Datamanager Box 2.0 on the Solar Net ring. It runs its own website that shows live data and settings. It connects to Fronius Solar.web over Wi-Fi or LAN and can send service messages by SMS or e-mail when errors occur. It controls the inverter with power limits and operating-time schedules, Modbus TCP or RTU, Fronius Smart Meter readings, a ripple control receiver, and dynamic power reduction based on self-consumption. Only one Datamanager per Fronius Solar Net ring may run as primary. Set the others to secondary with the switch on the card, which turns their LEDs off, or remove them. For first start-up, put the device in service mode (IP switch to position A or via the inverter Setup menu) and use the Solar.start app. The WLAN access point stays open for one hour, and the end device must get its IP address by DHCP. If you run the Technician Wizard, write down the service password it assigns. You need it to configure the UC Editor and Meter menus. The inverter's Interface protocol type only works when no Datamanager card is installed, so the card must be removed to use it. On Symo inverters, the plug-in Datamanager 2.0 may switch off at night or when there is not enough DC voltage.

<!-- review notes
- sentence 4: support check: partial - One-primary rule and secondary/removal are stated, but the switch on the card is only implied for the LEDs-off detail, which is correctly given; passages say set switch as required, fairly consistent though the switch-causes-LEDs-off is inferred.
- sentence 8: support check: partial - Passage fragment mentions Datamanager 2.0 at night or insufficient DC voltage, but not Symo or the 'switch off' wording explicitly.
-->
