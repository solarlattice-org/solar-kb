---
id: comp:ac-connector
type: Component
name: AC connector
aliases:
- AC Bulkhead Connector
- AC pair plug terminal
---
On the Huawei SUN2000-25KTL-US and 30KTL-US, the AC connection is a waterproof cable connector with an OT terminal. The Modbus map lists the connector over-temperature fault as a trip-level fault. For the warning and the temperature sensor alarm, check that the AC bulkhead connectors are connected properly. For the abnormal-connector alarm, restart the inverter by switching both the AC and DC switches off and on, waiting 1 minute between OFF and ON. For the over-temperature fault, watch for 5 minutes to see if the alarm clears by itself. If any of these alarms keeps coming back, contact after-sales service. On Solis inverters, a loose contact in the AC connector is one thing to check when troubleshooting AC backfeed errors. Measure grid voltage at the connector, and if you suspect a loose contact, disconnect the cable and reconnect it properly.

<!-- review notes
- sentence 2: support check: partial - The register row shows Level Trip Fault 6 for AC pair plug terminal over temperature (Fault6010), but doesn't use 'connector' wording exactly; essentially supported, though 'Modbus map' naming is implied; minor wording difference.
-->
