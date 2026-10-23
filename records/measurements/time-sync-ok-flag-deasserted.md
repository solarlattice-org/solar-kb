---
id: meas:time-sync-ok-flag-deasserted
type: Measurement
name: Time sync OK flag cleared
aliases:
- TSOK
- Time Synchronization OK
---
TSOK is a device word bit on the SEL-735 meter. It is set only while the meter takes its time from an IRIG-B source that is accurate enough for synchrophasor measurement. When TSOK is cleared, the meter clock is either not using IRIG-B or the IRIG-B source is not accurate enough for synchrophasor use. Read TSOK together with the IRIGOK bit, which is set whenever meter time comes from IRIG-B. If IRIGOK is set but TSOK is cleared, the source is there but not accurate enough. The related PMDOK bit shows whether the meter can produce synchrophasor data. It can take a few seconds to set after power-up, after a settings change, or when an IRIG-B signal is first connected. On SMA inverters, a time synchronization failure shows up as event 10110 instead. It means no time information could be retrieved from the configured NTP server. For that SMA event, check that the NTP server is configured correctly and that the inverter is on a local network with an Internet connection.
