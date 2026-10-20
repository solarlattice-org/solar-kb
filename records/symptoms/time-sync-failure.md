---
id: symptom:time-sync-failure
type: Symptom
name: Time synchronization failure
aliases:
- Time synchronization failed
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ntp-time-query-failed
  note: 'SMA inverters log event 10110 when they cannot get time information from the configured NTP server.
    Suggested checks: confirm the NTP server configuration and confirm the inverter is on a local network
    with Internet access.'
  quote: No time information could be called up from the set NTP server.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r8
    h: f12fd6a968ec
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r8
    h: f12fd6a968ec
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23
    h: f5135afff656
  review: drafted
  review_note: 'support check: partial - SMA event 10110 and both checks are stated, but the SEL-735 TSOK/IRIGOK
    note is not in the cited passages for the NTP measurement, and the statement mixes the two.'
- claim_id: c2
  rel: observed_as
  target: meas:time-sync-ok-flag-deasserted
  note: On SEL-735 meters, the TSOK bit is set only while meter time comes from an IRIG-B source accurate
    enough for synchrophasor measurement. IRIGOK is set while meter time comes from IRIG-B at all. If
    these bits are cleared, the meter is not synchronized to that source.
  cite:
  - src: src:sel-735-im-20250228
    loc: tbl=436.r2
    h: 2586fc064cd2
  - src: src:sel-735-im-20250228
    loc: tbl=436
    h: 29064759d4e1
  review: drafted
  review_note: 'support check: partial - TSOK and IRIGOK assert definitions are given, but the passages
    don''t state that cleared bits mean the meter is unsynchronized or that time-sync failure is observed
    that way.'
---
On SMA STP-US inverters, this symptom shows up in the event log as event 10110, which means the inverter could not get time information from its configured NTP server. Check the NTP server settings in the inverter first. Next, make sure the inverter is connected to a local network that has Internet access. In the same event log, events 10108 and 10109 record the old and new time when the clock is adjusted, which helps show when synchronization last worked. On SEL-735 revenue meters, check the IRIGOK and TSOK bits: these are set only while meter time comes from an IRIG-B source, and TSOK also requires enough accuracy for synchrophasor measurement. Where SNTP is used, accuracy depends on the server and the network, and it is best with few switches and routers between the server and the meter.

<!-- review notes
- sentence 2: support check: partial - Checking NTP server configuration is a listed corrective measure, but the passages don't say to do it first (it is listed first).
- sentence 3: support check: partial - Network with Internet connection is a listed corrective measure, but the passages don't state an order (next/second), though it is listed second.
- sentence 4: support check: partial - Events 10108/10109 are listed as time adjusted old/new time, but the passages don't say they help show when synchronization last worked.
-->
