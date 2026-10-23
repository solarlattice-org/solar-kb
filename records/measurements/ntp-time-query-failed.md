---
id: meas:ntp-time-query-failed
type: Measurement
name: NTP time query failure
aliases:
- Time synchronization failed
---
The inverter logs an event saying time synchronization failed because it could not get time information from the configured NTP server. On SMA inverters this shows up as event 10110, and some documents list the same NTP explanation under event 10114. The manufacturer's corrective steps are to check that the NTP server is configured correctly and that the inverter sits on a local network with Internet access. Because of these steps, a wrong NTP server setting or a missing network or Internet connection are the likely causes to check first. On meters that use SNTP, the internal clock syncs to an NTP server, and SNTP serves as a secondary time source. In unicast mode, the meter queries a primary or backup NTP server at a set rate and switches to the other server if no reply arrives within the timeout. A successful sync sets a status bit for the primary or the backup server, so if neither bit is set, the meter is not synchronized.

<!-- review notes
- sentence 4: support check: partial - The corrective measures imply these checks, but passages do not state they are the likely causes or to check first; this is inference.
- sentence 7: support check: partial - Bits TSNTPP/TSNTPB assert on successful sync, but the passage does not state that neither bit set means the meter is unsynchronized.
- sentence 4: review: partial - The passages give the corrective measures, but calling a wrong NTP setting or missing network/Internet the likely causes to check first is an inference they do not state.
- sentence 7: review: partial - The passage says TSNTPP or TSNTPB asserts on a successful sync, but it does not say that neither bit being set means the meter is unsynchronized.
-->
