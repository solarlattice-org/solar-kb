---
id: mit:battery-module-balancing
type: Mitigation
name: Battery module balancing
aliases:
- module balancing
- bypass mode
- balancing firmware
- Battery Balancing
- Forced Balancing
- Passive Balancing
---
Battery module balancing brings every module in a storage system to roughly the same state of charge. This helps the battery's efficiency, service life and safety. It is needed when module SOC values drift apart. The portal and inverter show only the average SOC, so this can block charging: one module may already be full while the average still looks low. On SMA Home Storage, balancing starts automatically when a module's SOC differs from the others by more than 7%, or when a module can no longer take charging current. That module is put in bypass and its green LED flashes every 2 seconds until the other modules catch up. Automatic balancing arrived with battery firmware 1.1.20.R or later. Older systems that lack it can be updated so manual balancing is no longer needed. Automatic updates must be enabled for the update to reach the battery. In large Megapack systems, the battery group balances units passively by adjusting each unit's power command while a real power command is active. If a unit's state of energy strays more than 10% from the average, the group force-balances by charging and discharging units into each other. During commissioning, balancing is tested in both the charge and discharge directions after a full discharge at rated power. Do not move the test plan forward until these tests pass. If the inverter reports a battery imbalance fault, the cause must be found by service and the battery manufacturer should be contacted.

<!-- review notes
- sentence 4: support check: partial - Firmware ≥1.1.20.R and the update that removes manual balancing are stated, and automatic updates must be enabled; but the article ties the update to recommissioning (1.1.3x.B), and 'older systems lacking it' is only loosely implied.
- sentence 5: support check: partial - Passive balancing adjusting commands under a Real Command and forced balancing at a 10% default deadband are supported, but 'large Megapack systems' is not stated, passive balancing 'while a real power command is active' is fine, and 10% is only a default; forced balancing also needs State Request ON.
-->
