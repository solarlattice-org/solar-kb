---
id: mit:optimizer-pairing
type: Mitigation
name: Power optimizer re-pairing
aliases:
- Remote pairing
- Pair optimizers
- Choose Operation > Pair
- Logical Layout > Replace
- Re-pair
- Pairing
---
Pairing logically links each power optimizer to its inverter. Optimizers do not start producing power until this has been done. Pairing runs on its own the first time the inverter is commissioned. It has to be repeated when an optimizer is replaced or the string length is changed. If pairing fails because the optimizers were shaded, you can retry it remotely from the monitoring platform in sunlight. Leave the inverter ON/OFF switch ON and check that S_OK shows on the status screen. To pair remotely, open the layout in the portal, right-click the inverter, and choose Operation, then Pair. The installer account must have the right permissions. Optimizers need power to pair, so only pair in good light and allow for snow cover in winter. If a battery is installed, turn it off before pairing on a Home Hub. Pairing usually takes about 15 to 20 minutes. Wait for the next reporting period and confirm that every optimizer shows production. After swapping an optimizer, replace its serial number under Admin, Logical Layout, Replace. If the portal was never updated after an earlier replacement, it can look like the optimizer is not reporting. Remote pairing may bring a string that is down back online, but keep monitoring it. If a wiring fault changes the resistance, the optimizers ignore the command to produce and the string will likely go down again.
