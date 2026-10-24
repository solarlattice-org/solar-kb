---
id: func:black-start
type: Function
name: Black start
aliases:
- battery black start
- Jumpstart
- Sunlight Jumpstart
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  rel: requires
  target: func:grid-forming
  note: Tesla says black start works only on systems designed to grid-form, and Tesla must enable it at
    commissioning.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=96.r5
    h: 6624176f34e5
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=5.r3
    h: f4c49093e4f1
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=108
    h: 6540876af49d
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=169.r6
    h: fa5b23cb84d6
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=118.r1
    h: 22c134ccd4e1
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=213.r7
    h: fa5b23cb84d6
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=148.r4
    h: 22c134ccd4e1
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=108.r1
    h: 6624176f34e5
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=255.r6
    h: fa5b23cb84d6
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 0
    max: 1
    unit: unit:UNITLESS
  conditions: 'Tesla Black Start Request enum setpoint, Modbus register 21005: 0 = No Black Start, 1 =
    Black Start Now'
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=118.r1
    h: 22c134ccd4e1
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=148.r4
    h: 22c134ccd4e1
  review: drafted
---
Black start lets a battery system bring the inverter and the site back up when there is no grid, using energy stored in the battery. The SMA Home Storage has a black start function that is switched on by hand at the battery, and the hybrid inverters in the system start operating on their own at sunrise. In SMA battery-backup systems, a standard switch can be installed for manual black start. When the inverter and battery are asleep during a grid failure, the switch takes energy from an auxiliary battery to wake them so backup operation can begin. At least one battery that supports black start must be connected to input A. Tesla control inputs include User Start, which starts a black start attempt, and Restart Black Start Attempt Count, which resets the counter. Monitoring points show whether black start is allowed and how many attempts remain. In Tesla's Grid-Connected Only mode, the Black Start Request is not supported. In backup and microgrid modes, black start is done through the islanding controls.

<!-- review notes
- sentence 1: support check: partial - The passages say the battery is used to black start with no grid, but the SMA text says an auxiliary battery supplies the start energy. Neither passage says the whole site is brought back up, and the second passage says not all batteries support black start.
- sentence 1: review: partial - The passages say the inverter can use the battery to black start with no grid, but SMA says an auxiliary battery supplies the start energy and nothing says the whole site is brought back up.
-->
