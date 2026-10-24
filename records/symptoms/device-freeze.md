---
id: symptom:device-freeze
type: Symptom
name: Device freeze or boot loop
aliases:
- Device freezes periodically
- Boot loop
- Repeated startup screens
- User interface cannot be called up
- Behaving erratically
- Startup loop
claims:
- claim_id: c1
  rel: observed_as
  target: meas:zero-ac-output
  note: Unit keeps restarting and never feeds the grid, even though DC voltage is present.
  cite:
  - src: src:sma-kb-sb-us-4x-inverter-boot-loop-after-rma-part-installation-kp-or-pu
    loc: sec=h1
    h: 532fa585b052
  - src: src:se-academy-advanced-monitoring-platform-na-technical-02-remote-troubleshooting-inverters-using-the-monitoring
    loc: sec=h10
    h: 9f04da0ed3e5
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: observed_as
  target: meas:repeated-startup-sequence
  note: Display or LEDs cycle through startup screens, or monitoring shows the inverter continually in
    Starting status without progressing to normal operation.
  cite:
  - src: src:sma-kb-sb-us-4x-inverter-boot-loop-after-rma-part-installation-kp-or-pu
    loc: sec=h1
    h: 532fa585b052
  - src: src:se-academy-advanced-monitoring-platform-na-technical-02-remote-troubleshooting-inverters-using-the-monitoring
    loc: sec=h10
    h: 9f04da0ed3e5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
In a boot loop the inverter keeps cycling through its startup screens or LED patterns and never reaches normal operation. It does not feed into the grid and its user interface cannot be reached. In monitoring, the inverter stays in Starting status with DC voltage present but no AC production. A startup loop like this points to an inverter error, so check the errors tab first. A boot loop that starts right after a replacement communication board or power unit is installed usually means the new part is still synchronizing with the rest of the inverter. In that case, disconnect WiFi and Ethernet and leave the unit powered with AC and DC connected. Make sure the DC input voltage is within the operating range, then wait for synchronization (typically about 30 minutes, in rare cases up to 2 hours) before commissioning through the Web UI. If a monitoring device's user interface cannot be called up after a firmware update, reset the device to default settings. If there was no update, check that the device can reach an internet time server. If no data shows after a long period without power, the real-time clock's buffer capacitor may have run down. If the device reports that the boot loader update failed, contact the manufacturer's service.
