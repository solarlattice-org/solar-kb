---
id: symptom:battery-undervoltage
type: Symptom
name: Battery undervoltage
aliases:
- BatVtgLow
- Low battery voltage
- Battery cell undervoltage fault
- OV-Vbatt
claims:
- claim_id: c1
  rel: observed_as
  target: meas:battery-voltage-low
  note: Measure battery voltage at the inverter connection point. SMA Sunny Island guidance compares the
    measured value against 39 V to separate deep discharge from other causes.
  cite:
  - src: src:sma-kb-f213-on-sunny-island
    loc: sec=h1
    h: b6251367dbc7
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=27.r3
    h: 06c38a9cbc87
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r3
    h: 06c38a9cbc87
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r3
    h: 06c38a9cbc87
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=53.r7
    h: 5c7c8b953a25
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:deep-discharge-event-message
  note: Sunny Island F213 with battery voltage below 39 V means the battery is deeply discharged.
  cite:
  - src: src:sma-kb-f213-on-sunny-island
    loc: sec=h1
    h: b6251367dbc7
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:battery-soc-reading-low
  note: A low state of charge goes along with undervoltage. Rarely cycled batteries in winter can drift
    into undervoltage.
  cite:
  - src: src:sma-kb-vermeidung-der-unterspannung-der-batterie-mit-sunny-boy-smart-energy
    loc: sec=h1
    h: 6009fa209cb8
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=53.r7
    h: 5c7c8b953a25
  review: drafted
  review_note: 'support check: partial - Rarely cycled batteries in winter leading to undervoltage is
    stated, but the claim that low SOC goes along with undervoltage as a reading is only loosely implied
    (SOC too low triggers recharge).; review: partial - The passages back winter under-cycling leading
    to undervoltage, and both mention low SOC next to undervoltage (recharge when SOC is too low, shed
    loads at low SOC), but neither says a low SOC reading is how undervoltage is observed.'
- claim_id: c4
  rel: observed_as
  target: meas:battery-module-red-led-flashing
  note: 'SMA Home Storage cell undervoltage fault: the red LED flashes quickly on the battery module.'
  cite:
  - src: src:sma-kb-ereignis-9312-mit-sma-home-storage
    loc: sec=h1
    h: 00bed37d0ec3
  review: drafted
- claim_id: c5
  rel: observed_as
  target: meas:bms-error-message
  note: Sunny Island reports battery undervoltage from external battery management via SiCom as error
    F922 or warning W938.
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r4
    h: 7de1e6cb5839
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r5
    h: a1d54c6223cc
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155
    h: 9ec13aab83bd
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156
    h: c6b09b8dcebc
  review: drafted
---
Battery undervoltage means the battery voltage seen by a battery inverter or hybrid inverter has fallen too low, and the device raises an error or warning. On Sunny Island it shows as F213, or as F922 and W938 when the battery management reports it over SiCom. Hybrid inverters may show a battery undervoltage message. Measure the battery voltage at the inverter connection point first, and check that it is within the battery's specified range. On Sunny Island, a reading below 39 V means the battery is deeply discharged. Recharge it straight away with emergency charge mode or an external charger, then give it a manual equalization charge. If the voltage is above 39 V but the Sunny Island will not restart, the inverter itself should be replaced. If it does restart, review the battery protection settings so the battery is not drained that far again. Use a load-shedding contactor to drop DC loads when the state of charge is low, which helps prevent repeat events. On SMA Home Storage, a cell undervoltage fault makes the red LED on the battery module flash quickly. Low PV generation in winter can leave the battery rarely cycled and lead to undervoltage, so newer firmware recharges the battery from the grid. If a cell undervoltage fault persists after restarting the battery and inverter, contact the battery manufacturer or service.

<!-- review notes
- sentence 2: support check: partial - F922 and W938 via SiCom and a generic undervoltage message are supported, but the F213 row is labeled 'Warning low battery voltage' and the hybrid inverter statement is vague; mapping of F213 is supported loosely.
- sentence 6: support check: partial - Load-shedding contactor for DC loads at low SOC is stated, but the 'prevents repeat events' purpose is not explicitly stated.
- sentence 1: review: partial - Battery voltage too low raising an error or message is supported by the F213 and Solis rows, but no passage text says the Solis device is a 'hybrid inverter'.
-->
