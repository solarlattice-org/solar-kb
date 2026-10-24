---
id: symptom:battery-not-detected
type: Symptom
name: Battery not detected by inverter
aliases:
- battery is not detected in installation wizard
- cannot detect batteries or backup box
- battery not recognized
- Battery not recognized by inverter
- no detection of the battery
- no communication with battery
claims:
- claim_id: c1
  rel: observed_as
  target: meas:bus-termination-resistance-infinite
  note: Measured between pin 1 and pin 3 of the COM connector with the inverter disconnected on AC and
    DC sides; about 120-140 ohm is expected, while a reading toward infinity points to the internal COM
    plug having come loose.
  cite:
  - src: src:sma-kb-stpx-x-3se-40-no-battery-connection
    loc: sec=h1
    h: b824bf67f107
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: observed_as
  target: meas:com-supply-voltage-missing
  note: With the inverter switched on and the COM connector unplugged, about 11-12 V is expected between
    pin 2 and pin 4; if it is absent, suspect a loose internal COM plug.
  cite:
  - src: src:sma-kb-stpx-x-3se-40-no-battery-connection
    loc: sec=h1
    h: b824bf67f107
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c3
  rel: observed_as
  target: meas:rebus-voltage-low
  note: 'Generac PWRcell: the REbus terminals should show at least 360 V between RE+ and RE-. The REbus
    voltage can also be checked on the inverter control panel home screen.'
  cite:
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=24.r9
    h: 15256b156d74
  - src: src:generac-generac-pwrcell-3ph-inverter-install-and-owners-manual-a0001515563-rev-b
    loc: tbl=24
    h: 81626a967eb0
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The passages give the 360 V minimum between RE+ and RE- and say
    REbus voltage can be verified on the inverter control panel home screen. They don''t name Generac
    PWRcell, though the REbus and PLM terms point to it.'
---
This symptom shows up during commissioning or in the installation wizard: the hybrid or storage inverter cannot find the connected battery, and sometimes it cannot find the backup box either. The most common cause is a communication bus fault: the battery-to-inverter cabling is wrong, the communication cable is not suitable, the CAN termination is faulty, or the Enable and GND lines are miswired. Other possible causes are an inverter that is not grounded correctly, inverter firmware that is out of date, an incomplete battery firmware update, or a defect in the CAN interface of the inverter or of the battery management system. If the wiring checks out, the internal COM plug may have come loose. Signs of this are a missing supply voltage between pins 2 and 4 of the COM connector, or an open (very high) resistance between pins 1 and 3. On REbus-based systems, start with the basics: the inverter must be enabled, the DC disconnect must be on, connections must be secure, the inverter and battery must use the same PLM channel, and the REbus voltage must be high enough. A CAN interface functional test does not need the battery connected. It can rule out an inverter defect, but it is not a full check of the CAN bus. If the battery side is still suspected, contact the battery manufacturer.

<!-- review notes
- sentence 2: support check: partial - The passages list wrong cabling, an unsuitable cable, faulty termination and miswired Enable/GND lines as possible causes. They never call these the most common cause.
-->
