---
id: meas:inaccurate-timestamps
type: Measurement
name: Inaccurate event timestamps
aliases:
- Time stamps inaccurate
- Inaccurate time
- Invalid date
---
The device logs events with time stamps that do not match the real time. On Fronius inverters, status code 758 (Galvo, Primo) or 753 (Symo) means the real-time clock module is in emergency mode, so the time is inaccurate and may be lost. Grid feed-in carries on normally while this clock fault is active, so it points to a real-time clock failure and not to a power fault. On an Eaton surge protector, wrong time stamps come from a clock that is not synced, or from a supercap that drained during a long power outage. SMA devices can report an invalid system time (event 10117) or a failed time synchronization (event 10110). When the clock is corrected, SMA logs a pair of events showing the old time and the new time (10108 and 10109). To fix it, set the date and time on the device, and use the SNTP feature where it exists so the time stays accurate.

<!-- review notes
- sentence 3: support check: partial - Grid feed operation normal is stated, but the inference that it points to an RTC failure rather than a power fault is not stated explicitly.
-->
