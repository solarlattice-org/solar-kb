---
id: symptom:insufficient-dc-power
type: Symptom
name: Insufficient DC input power
aliases:
- Power low
- LOW PV POWER
- DC power too low
- Unstable operation
claims:
- claim_id: c1
  rel: observed_as
  target: meas:dc-bus-voltage-low
  note: Fronius Galvo status 306 (LOW PV POWER) is raised when the intermediate circuit voltage falls
    below the threshold the inverter needs to feed the grid.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  review: drafted
  review_note: 'support check: partial - Status 306 and the intermediate circuit voltage dropping below
    threshold are stated, but the dawn/dusk DC-voltage and DC-power signal wording is only loosely covered
    (dawn/dusk is stated for the code, not for DCV/DCW specifically).'
- claim_id: c2
  rel: observed_as
  target: meas:zero-ac-output
  note: The inverter briefly stops feeding the grid and goes back to startup or standby. On SMA STP-TL-US
    units it can no longer connect to the grid.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h187
    h: ce98c4366db9
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h184
    h: ece357161bcb
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r6
    h: 886bc9e881d2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  review: drafted
  review_note: 'support check: partial - Feed-in interruption and return to startup, and the SMA ''can
    no longer connect'' wording, are stated, but nothing about AC power dropping to zero, the irradiance
    signal, or ''standby'' appears in the passages.'
- claim_id: c3
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Reported as Fronius status code 306 and as SMA events 3901 (DC power too low) and 9005 (Waiting
    for main CPU).
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17
    h: 2e256223844f
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: tbl=1.r21
    h: e42785cf51d2
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h66
    h: 92d20275c7ad
  review: drafted
---
The inverter reports that the PV array is not delivering enough DC power to feed the grid, so it briefly stops feed-in and goes back to its startup phase. On Fronius inverters this is status code 306, which is raised when the intermediate circuit voltage drops below the level needed to feed the grid. SMA inverters report it as event 3901, DC power too low. The code appears normally every morning and evening because irradiance is low. At those times it is not a fault, and it clears by itself. Snow on the modules or too little irradiation can also starve the DC input. The inverter then cannot connect to the grid. Some inverters show related messages: SMA event 9005 can mean the DC voltage is too low to run the main computer, and Sungrow units drop into standby when DC input is too low. First compare the event times with irradiance and look for snow cover. Then check that at least the DC start voltage is present; on SMA units the green LED should be flashing, pulsing or on. If the code keeps coming back while irradiance is good, contact the system installer.

<!-- review notes
- sentence 6: support check: partial - Snow and irradiation causes and the SMA DC start voltage/green LED check are stated, but comparing event times with irradiance and the ordering are not.
-->
