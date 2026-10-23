---
id: symptom:backup-ac-overvoltage
type: Symptom
name: Backup output AC overvoltage
aliases:
- AC overvoltage in backup operation
- SPS AC overvoltage
- OV-Vbackup
- Backup overvoltage fault
- Inverting overvoltage
- AC overvoltage backup (fast)
- AC overvoltage backup (slow)
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Shown as SMA event 9202 (AC overvoltage in backup operation or SPS AC overvoltage), SMA 9204/9205
    (AC overvoltage backup, fast or slow), or Solis OV-Vbackup / OV-VBackup.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h776
    h: a0cd72becf14
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h74
    h: 1f9d96aac36d
  - src: src:kb-sma-sbx1xpus41-event-messages
    loc: sec=h69
    h: 9fefbdc798d7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h442
    h: 71693e53938a
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r8
    h: bcf28adc0525
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
---
The inverter reports too much AC voltage on its backup or secure power supply (SPS) output, and it shows this as an event code on the display or in the event log. On SMA SB-US inverters, event 9202 (SPS AC overvoltage) means an outside AC source has been connected to the SPS outlet, so check the SPS connections first and correct them. SMA events 9204 and 9205 point to high voltage in the battery-backup grid or large load steps there; check for newer firmware and update it, and contact Service if none is available. On Solis hybrid inverters, check the wiring at the backup port, then restart the system and see whether the fault comes back. If a Solis backup overvoltage fault keeps coming back after a restart, the inverter may have to go back to the factory for repair.

<!-- review notes
- sentence 2: support check: partial - Passages say 9202 SPS AC overvoltage means an AC source is connected to the SPS outlet and to check/correct the SPS connections, but nothing specifies SB-US models or 'outside' source (the 'Contact Service' version also appears).
- sentence 4: support check: partial - Passages give the OV-Vbackup steps (check backup port wiring, restart, confirm whether fault continues) but don't specify Solis hybrid inverters beyond the message name.
-->
