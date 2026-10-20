---
id: symptom:unauthorized-access-attempt
type: Symptom
name: Unauthorized network access attempt
aliases:
- Unauthorized Network Access
claims:
- claim_id: c1
  rel: observed_as
  target: meas:unauthorized-access-event-code
  note: Inverter fault table entry 30 reports that someone tried to get into the inverter network without
    authorization; the listed action is to check for malicious access attempts.
  cite:
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22.r4
    h: 30fada4483b8
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: tbl=22
    h: 616f2ad5807a
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:login-lockout-event
  note: After repeated wrong login attempts, the inverter blocks login for a set time. The user login
    and the Grid Guard login have different lockout periods.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=24
    h: 471c133abf5f
  review: drafted
- claim_id: c3
  rel: observed_as
  target: meas:failed-login-alarm-bit
  note: On a revenue meter, a device alarm bit pulses briefly when a login fails, a password or the settings
    change, or the access level is raised. All settings changes are logged in the event log, which can
    show unauthorized changes.
  cite:
  - src: src:sel-735-im-20250228
    loc: sec=h1252
    h: df534e8fdb65
  review: drafted
---
Some inverters raise a dedicated event when someone tries to get into the inverter network without authorization. Repeated failed logins can also appear as a login lockout message, which blocks login for a limited time. On connected meters, a device alarm bit pulses when a login fails or the settings change, and the settings-change log shows whether any unauthorized changes were made. First, check whether there were malicious attempts to access the inverter network, and review the device logs for settings or password changes. Devices exposed to the internet are at risk of their data being accessed and changed, so keep them on a trusted network behind a firewall. Close unused ports and protocols, avoid port forwarding, use a VPN only if remote access is truly needed, and keep system components on a separate network segment. Replace default passwords with private ones at installation, because leaving the defaults in place can allow unauthorized access.

<!-- review notes
- sentence 4: support check: partial - Checking for malicious access attempts is stated, but the passages say to analyze the SER log for settings changes, not to review logs for password changes; the SALARM bit, not the log, indicates password changes, and the first/ordering is not stated.
-->
