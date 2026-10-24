---
id: func:monitor-key-data
type: Function
name: Monitor key DER data
aliases:
- monitor key data
- DER monitoring
- Monitoring information
category: Monitoring
function_kind: monitoring
---
This function makes the present operating conditions of a DER readable through a local communication interface at the reference point of applicability. Each reported value must be the latest one measured within the required response time. The required data set includes the DER's operational state, with on and off as the minimum supported states, and its power-connected status. The SMA Cluster Controller reads out and manages PV system data from SMA devices with Speedwire or Webconnect interfaces. It reports total active power, sends e-mail alarms and forwards system data to an FTP server or to Sunny Portal. The Enphase IQ Combiner 6C has a built-in IQ Gateway that shows PV production, battery use and system performance in real time in the Enphase App. An IQ Gateway or IQ Combiner can monitor up to 300 IQ9N microinverters. The Huawei SmartLogger connects to SUN2000 inverters over RS485 and can push its data by FTP to PowerTrack. Pick file Format 2 or higher so the SmartLogger data and cumulative energy values are included.

<!-- review notes
- sentence 3: support check: partial - Reading out system data, total active power feedback, e-mail alarms, and sending data to FTP/Sunny Portal are stated; but e-mail alarms are 'in the event of critical system statuses', and 'reports total active power' is only loosely 'feedback'; the Cluster Controller also does more (minor), core is supported though qualifier on alarms is missing.
- sentence 4: support check: partial - Integrated IQ Gateway and real-time monitoring are stated (also via Enlighten portal), and up to 300 IQ9N microinverters is stated, but the 'IQ9N' passages say IQ9N-HPB/IQ9N; the Enphase App claim is fine; minor omission of Enlighten web portal option.
-->
