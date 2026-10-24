---
id: prod:enphase-iq9n
type: Product
name: Enphase IQ9N Microinverters (IQ9N-A, IQ9N-HPB)
aliases:
- IQ9N
- IQ9N-A
- IQ9N-HPB
- IQ9N-A-US
- IQ9N-A-DOM-US
- IQ9N-A-DOM-US-HPB
- IQ9N Microinverter
category: Inverters
make: enphase
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:enphase
  cite:
  - src: src:kb-enphase-what-is-the-main-difference-between-iq9n-microinverter-and-iq8-series-microinve
    loc: sec=front
    h: 1d8cf1b81c4b
  - src: src:kb-enphase-can-iq9n-microinverters-be-installed-with-iq6-iq7-iq8-microinverters-in-the-sam
    loc: sec=front
    h: '872086193757'
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:microinverter
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-4041
    loc: tbl=1.r1
    h: 6f9179659aef
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=h1
    h: cac314d4998b
  review: drafted
- claim_id: c3
  rel: requires
  target: prod:enphase-iq-gateway
  note: An IQ Gateway or IQ Combiner must be connected; system software periodically checks the link and
    microinverters may stop working without it.
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
- claim_id: c4
  rel: requires
  target: prod:enphase-iq-cable
  conditions: IQ9N-HPB variant; AC port connects to IQ Cable or IQ Field Wireable Connector
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
- claim_id: c5
  rel: requires
  target: prod:staubli-mc4
  conditions: IQ9N-HPB DC port must be mated with Staubli MC4 cable couplers evaluated by UL for intermateability
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
- claim_id: c6
  rel: requires
  target: tool:enphase-installer-app
  conditions: Used to scan microinverter serial numbers and connect to the IQ Gateway during installation
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
  review_note: 'support check: partial - The passage says to scan serial numbers with the Installer App
    and connect to the IQ Gateway, but it never states the app is required.'
- claim_id: c7
  rel: compatible_with
  target: prod:enphase-iq8
  scope:
    applications:
    - on-grid
    - backup
  conditions: IQ9N can be added to existing IQ8 systems on the same IQ Gateway and IQ System Controller,
    grid-tied or grid-forming with backup
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-4041
    loc: tbl=1.r1
    h: 6f9179659aef
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5422
    loc: tbl=1.r1
    h: 582d03bd08a2
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5425
    loc: tbl=1.r1
    h: 2ee88d08ba8b
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5421
    loc: tbl=1.r1
    h: 149e0f77dfe8
  review: drafted
- claim_id: c8
  rel: compatible_with
  target: prod:enphase-iq7
  scope:
    applications:
    - on-grid
    - backup
  conditions: IQ9N can be added to existing IQ7 systems on the same IQ Gateway and IQ System Controller,
    grid-tied or with backup
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-4041
    loc: tbl=1.r1
    h: 6f9179659aef
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5422
    loc: tbl=1.r1
    h: 582d03bd08a2
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5425
    loc: tbl=1.r1
    h: 2ee88d08ba8b
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5421
    loc: tbl=1.r1
    h: 149e0f77dfe8
  review: drafted
- claim_id: c9
  rel: incompatible_with
  target: prod:enphase-iq7
  conditions: Mixed systems including IQ7 Series do not support Sunlight Jump Start; IQ7 cannot be added
    to a site with existing IQ9N-HPB on the same gateway
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-4041
    loc: tbl=1.r1
    h: 6f9179659aef
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5422
    loc: tbl=1.r1
    h: 582d03bd08a2
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
  review_note: 'support check: partial - The passages say IQ7 cannot be added to a site with existing
    IQ9N-HPB and mixed systems lose Sunlight Jump Start, but they also say IQ9N can be added to IQ7 systems,
    so ''incompatible'' overstates it.'
- claim_id: c10
  rel: compatible_with
  target: prod:enphase-iq-system-controller
  scope:
    applications:
    - backup
  conditions: Grid-forming (with backup) configurations; IQ System Controller, 2/3/3G/3M
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-4041
    loc: tbl=1.r1
    h: 6f9179659aef
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
- claim_id: c11
  rel: compatible_with
  target: prod:enphase-iq-battery
  conditions: Solar Plus Battery with IQ Battery 3/10, 3T/10T, 5P or 10C; combined PV continuous output
    limited to 150% of battery rated power (200% for IQ8 plus IQ9N-HPB mixed systems) unless PV shedding
    is used
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
- claim_id: c12
  rel: implements
  target: func:grid-forming
  conditions: Sunlight Jump Start, only in systems of IQ8 Series and IQ9N microinverters with no IQ7 Series
  cite:
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-4041
    loc: tbl=1.r1
    h: 6f9179659aef
  - src: src:kb-enphase-iq-gateway-software-release-notes-8-3-5422
    loc: tbl=1.r1
    h: 582d03bd08a2
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
- claim_id: c13
  rel: implements
  target: func:ground-fault-protection
  conditions: Class II double-insulated; requires PV modules with DC cables labeled PV wire or PV cable
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: sec=2
    h: cf62ab044a50
  review: drafted
- claim_id: c14
  attr: rated_power
  value:
    nominal: 440
    unit: unit:V-A
  conditions: Maximum continuous output power, IQ9N-A-DOM-US-HPB at 240 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r14
    h: 8904b6fdc7b8
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r13
    h: 82f5eba61eb3
  review: drafted
  review_note: 'support check: partial - The table shows 440 and 415 and the headers show 240 V and 208
    V, but the power row''s columns are not labeled by voltage, so the 440-to-240 V mapping is only implied
    by order.; possible conflict with c15 (same source; check the conditions)'
- claim_id: c15
  attr: rated_power
  value:
    nominal: 415
    unit: unit:V-A
  conditions: Maximum continuous output power, IQ9N-A-DOM-US-HPB at 208 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r14
    h: 8904b6fdc7b8
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r13
    h: 82f5eba61eb3
  review: drafted
  review_note: 'support check: partial - 415 is the second value and 208 V the second column, but the
    power row does not label the voltages, so the mapping is only implied by order.; possible conflict
    with c14 (same source; check the conditions)'
- claim_id: c16
  attr: rated_output_current
  value:
    nominal: 1.83
    unit: unit:A
  conditions: Maximum continuous output current, IQ9N-A-DOM-US-HPB at 240 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=9.r1
    h: e680bf12c00e
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions)
- claim_id: c17
  attr: rated_output_current
  value:
    nominal: 2
    unit: unit:A
  conditions: Maximum continuous output current, IQ9N-A-DOM-US-HPB at 208 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=9.r1
    h: e680bf12c00e
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions)
- claim_id: c18
  attr: nominal_voltage
  value:
    nominal: 240
    unit: unit:V
  conditions: IQ9N-A-DOM-US-HPB AC output configuration; grid voltage range 211-264 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r13
    h: 82f5eba61eb3
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r16
    h: 7e880ce98f43
  review: drafted
  review_note: 'support check: partial - The grid range 211-264 V is the first value in the row and 240
    V is the first column, but the range columns are unlabeled and 240 V nominal is only implied.; possible
    conflict with c19 (same source; check the conditions)'
- claim_id: c19
  attr: nominal_voltage
  value:
    nominal: 208
    unit: unit:V
  conditions: IQ9N-A-DOM-US-HPB AC output configuration; grid voltage range 183-229 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r13
    h: 82f5eba61eb3
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=8.r16
    h: 7e880ce98f43
  review: drafted
  review_note: 'support check: partial - The 183-229 V range is the second value and 208 V the second
    column, but the range columns are unlabeled and 208 V nominal is only implied.; possible conflict
    with c18 (same source; check the conditions)'
- claim_id: c20
  attr: efficiency
  value:
    nominal: 97.8
    unit: unit:PERCENT
  conditions: Peak efficiency, IQ9N-A-DOM-US-HPB at 240 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=9.r11
    h: d111a480f064
  review: drafted
  review_note: possible conflict with c21 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c21
  attr: efficiency
  value:
    nominal: 97.7
    unit: unit:PERCENT
  conditions: Peak efficiency, IQ9N-A-DOM-US-HPB at 208 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=9.r11
    h: d111a480f064
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c22
  attr: efficiency
  value:
    nominal: 97.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, IQ9N-A-DOM-US-HPB at 240 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=9.r12
    h: fe8f12c91a82
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c21 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c23
  attr: efficiency
  value:
    nominal: 97
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, IQ9N-A-DOM-US-HPB at 208 V
  cite:
  - src: src:enphase-enphase-iq9n-hpb-microinverter-installation-and-operation-manual
    loc: tbl=9.r12
    h: fe8f12c91a82
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c21 (same source; check the conditions); possible conflict with c22 (same source; check the conditions)
---
The Enphase IQ9N is a family of GaN-based residential microinverters that includes the IQ9N-A-US, IQ9N-A-DOM-US and IQ9N-HPB variants. The IQ9N-A-DOM-US-HPB delivers up to 440 VA continuous at 240 V and 415 VA at 208 V, with maximum continuous output currents of 1.83 A and 2.0 A. Its peak efficiency is 97.8 percent at 240 V and 97.7 percent at 208 V. CEC weighted efficiency is 97.5 and 97.0 percent. The microinverter must stay connected to an IQ Gateway or IQ Combiner, or it may stop operating. The HPB variant uses the IQ Cable on its AC side and needs Staubli MC4 connectors on its DC port. IQ9N units can be added to existing IQ7 or IQ8 systems on the same gateway and IQ System Controller, both grid-tied and with backup. Adding IQ7 or IQ8 units to an existing IQ9N-HPB site is not allowed. Sunlight Jump Start grid-forming PV works only when the system contains IQ8 and IQ9N units and no IQ7 Series microinverters. The unit is Class II double-insulated and includes ground fault protection. A solid red LED indicates a DC Resistance Low, Power Off condition, which triggers when PV-to-earth resistance drops below roughly 7 kilohms.

<!-- review notes
- sentence 1: support check: partial - Passages show IQ9N-A-US, IQ9N-A-DOM-US and an IQ9N-HPB manual with GaN architecture and residential use, but they don't explicitly say the HPB is a variant in the same family.
- sentence 2: support check: partial - The currents are labeled by voltage, but the power values 440 and 415 are not explicitly labeled 240 V and 208 V, and 'up to' is only implied by 'maximum'.
-->
