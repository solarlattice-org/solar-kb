---
id: symptom:low-battery-charge
type: Symptom
name: Low battery state of charge
aliases:
- Low State of Energy
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-soc-start-event-message
  note: 'SMA event 9345: battery state of charge too low for the start procedure; the inverter can no
    longer recharge the battery on its own.'
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h78
    h: b90c48de821e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h796
    h: bfa3341c4bfc
  - src: src:sma-kb-event-9345-with-sbsx-x-10-us-10
    loc: sec=h1
    h: 5d38dbea68b5
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:battery-soc-reading-low
  note: The device display shows the battery state of charge in percent of capacity; a low value shows
    this symptom.
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=23
    h: 468a481db6c0
  - src: src:sma-doc-246498
    loc: tbl=29.r8
    h: f42aaa45f7e8
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h647
    h: e5f88b74ad20
  review: drafted
  review_note: 'support check: partial - The passages say the display shows state of charge in percent
    of capacity, but they don''t say a low value is a symptom.'
- claim_id: c3
  rel: observed_as
  target: meas:grid-request-low-soc
  note: 'Sunny Island event 1609 / E501 (GdSocOn): the device requests the grid because the battery state
    of charge is low.'
  cite:
  - src: src:sma-doc-278742
    loc: tbl=64.r9
    h: 10fe64e6ccd1
  - src: src:sma-doc-259761
    loc: tbl=60.r9
    h: 1af99460697e
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=40.r1
    h: 4d1506263beb
  review: drafted
  review_note: 'support check: partial - The passages give 1609/E501 as a grid request due to low battery
    state of charge, but they don''t say the device requests the grid, and the name ''Sunny Island'' appears
    nowhere in them.'
- claim_id: c4
  rel: observed_as
  target: meas:low-state-of-energy-alarm
  note: 'Megapack alarm point: at least one battery module has gone into its protective off state. Staying
    at low state of energy can damage cells.'
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r7
    h: 6b5a57f66a79
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r14
    h: 6b5a57f66a79
  review: drafted
---
The battery holds too little charge. On SMA storage inverters this is reported as an event saying the charge is too low for the start procedure. At this point the inverter can no longer recharge the battery by itself, so a qualified person must charge it right away. Check the state of charge on the device display, which shows the percentage of battery capacity, and compare it with the expected battery state. On off-grid systems a low state of charge can also show up as a grid request event or a battery undervoltage message. Reaching the lower SOC threshold opens the load contactor. Fix it by charging the battery, using emergency charge mode or an external charger, and by making sure DC loads are shed when the charge is low. For SMA batteries, contact SMA Service to have the battery charged manually. For other brands, contact the battery manufacturer. Do not leave a battery at a very low state of energy, because this can damage the cells.

<!-- review notes
- sentence 4: support check: partial - Grid request events, battery undervoltage and the load contactor opening at the lower SOC threshold are all stated. The passages don't say a low state of charge 'can also show up' as these on off-grid systems, and the undervoltage row names low battery voltage rather than low SOC.
-->
