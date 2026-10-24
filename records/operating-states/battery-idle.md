---
id: state:battery-idle
type: OperatingState
name: Battery idle
aliases:
- battery standby
- battery sleep
category: Storage
---
On an Enphase IQ Battery, idle means the battery is neither charging nor discharging. In this state the IQ Battery LED is solid blue or green, and the colour shifts from blue toward green as the charge level rises. When a Sunny Island system is stopped, the unit drops from operation into standby, and its own standby consumption slowly drains the battery; for long shutdowns the Sunny Island should be switched off instead. In grid-connected Sunny Island systems, silent mode puts the unit in standby once the float charge time has run out, and the grid alone supplies the loads. The Sunny Island leaves silent mode at a set interval or when battery voltage per cell drops by 0.14 V, which keeps the battery fully charged. On a Generac PWRcell running in island mode, the battery goes to sleep once its state of charge reaches the Min Absolute setpoint; the inverter then powers down and protected loads lose power. While asleep during an islanded outage, the Generac system wakes every hour for four minutes to search for power, and it charges again as soon as power is available on REbus.
