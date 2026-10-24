---
id: func:pv-only-backup
type: Function
name: PV-only backup outlet
aliases:
- Secure Power Supply
- SPS
- Sunlight Backup
- opportunity power
- Secure power supply operation
- SMA Backup Secure
- Backup Secure
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  rel: subclass_of
  target: func:backup-power
  note: During a grid outage, loads are supplied from PV alone, without a battery.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h70
    h: 7bfa99f0bd27
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=4.1.1
    h: a53d792004a6
  review: drafted
- claim_id: c2
  rel: requires
  target: prod:sma-backup-start
  scope:
    products:
    - prod:sma-sbse-us-50
  note: SMA Backup Secure works only when SMA Backup Start is installed in the inverter.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=4.4.12
    h: a3c8380440e0
  review: drafted
  review_note: 'support check: partial - Passage says Backup Secure requires Backup Start, but it does
    not mention the SBSE-US-50 scope, and it says Backup Secure can use battery or PV.'
- claim_id: c3
  attr: reconnect_delay
  value:
    nominal: 20
    unit: unit:SEC
  scope:
    products:
    - prod:sma-sb-us-41
  conditions: Automatic attempt to restore the outlet voltage after a brief interruption caused by overload,
    underload or insufficient irradiation
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=4.8.1
    h: 6a5797090f65
  review: drafted
- claim_id: c4
  attr: reconnect_delay
  value:
    nominal: 20
    unit: unit:SEC
  scope:
    products:
    - prod:sma-sb-us-40
  conditions: Automatic attempt to restore the outlet voltage after a brief interruption caused by overload,
    underload or insufficient irradiation
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=4.8.1
    h: 625b0b2226b5
  review: drafted
- claim_id: c5
  attr: trip_time
  value:
    min: 5
    unit: unit:SEC
  scope:
    products:
    - prod:sma-sb-us-40
  conditions: The 'Short circuit in the SPS power outlet' event is raised when the starting current stays
    above the permitted load current of the SPS connection for more than this time
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h260
    h: a672af75e661
  review: drafted
  review_note: 'support check: partial - The passage gives more than 5 s for the overshoot, but it does
    not state the ''at least'' framing or the trip-time classification beyond the event text.'
- claim_id: c6
  attr: reconnect_delay
  value:
    nominal: 30
    unit: unit:SEC
  scope:
    products:
    - prod:solis-s6-eh3p-75-150k-us
  conditions: Recovery after the first overload fault while backing up loads from PV only
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=4.1.1
    h: a53d792004a6
  review: drafted
- claim_id: c7
  attr: reconnect_delay
  value:
    nominal: 3
    unit: unit:MIN
  scope:
    products:
    - prod:solis-s6-eh3p-75-150k-us
  conditions: Recovery after the second overload fault while backing up loads from PV only
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=4.1.1
    h: a53d792004a6
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: reconnect_delay
  value:
    nominal: 10
    unit: unit:MIN
  scope:
    products:
    - prod:solis-s6-eh3p-75-150k-us
  conditions: Recovery after the third, fourth and fifth overload faults while backing up loads from PV
    only; after the sixth fault a hard reset is needed
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=4.1.1
    h: a53d792004a6
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions)
---
PV-only backup lets a grid-tied inverter power a dedicated outlet from the PV array during a grid outage. While it does this, the inverter is disconnected from the grid and does not export. The power available follows the irradiation. If there is an overload, an underload or too little sun, the outlet drops out and the inverter retries 20 seconds later, so loads that need a stable supply must not be connected. On the Sunny Boy Smart Energy, SMA Backup Secure needs SMA Backup Start in the inverter. To set it up, set Configuration of the backup type to Emergency Power Mode and set Backup Voltage to 120V. Enphase calls this function Sunlight Backup. These sites must be set to Load with Solar production, and installers need IQ Battery certification to commission them.

<!-- review notes
- sentence 3: support check: partial - Backup Start requirement and the Emergency Power Mode and 120V settings are supported, but the SMA article concerns an array without rapid shutdown modules, which the statement omits.
- sentence 4: support check: partial - Load with Solar production and installer certification are stated, but the passages do not say Enphase calls the PV-only backup function Sunlight Backup, and certification is not applicable to PV-only systems.
-->
