---
id: meas:datetime-change-event-log
type: Measurement
name: Date/time change event log entry
aliases:
- DateSet
- date, time changed
- Time adjusted / new time
- Time or date change
- Time Changed by
---
Some devices record a dedicated event when someone changes the date or time. SMA Sunny Island inverters log code E706, also named DateSet, with the text that the date or time has been changed. Other SMA devices log event 10109, time adjusted or new time. They log event 10117, invalid date, when the system time is not valid, and the fix is to set the date and device time in the installation assistant. Time shifts larger than the TIME_CHG setting are recorded. Any shift over 10000 seconds is shown as 10,000.0 s, so the real size of a large jump is lost. The meter's audit log is kept apart from the event log. It stores the date, the time, the source of each logged change (IP address, port or HMI) and the action taken, and you can filter it by date range or by entry count. Clock settings on WAGO controllers can be checked and set from the web management page under the clock menu.
