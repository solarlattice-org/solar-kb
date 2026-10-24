---
id: state:pv-search
type: OperatingState
name: PV search
aliases:
- searching for PV
- PV Search Mode
category: Storage
make: generac
product: prod:generac-pwrcell-2
---
PV Search Mode brings the system out of Sleep Mode. The battery turns on and the storage system powers the Smart Disconnect Switch and the backup loads, so the AC-coupled PV can reconnect and start charging the battery. The system enters PV Search Mode in one of three ways: when morning comes or an automatic black start occurs, after a reset at the battery cabinet (battery disconnect switch OFF, ON, OFF, ON), or when someone enables it in PWRview. While this mode is active, the inverter status LED and the Smart Disconnect Switch status LED both flash orange at a one-second interval. When the system finds PV power, it switches to backup mode and starts charging the battery. Keep loads low while it charges. The system keeps searching until it finds PV power or the battery drops to the Sleep Mode reserve threshold. If the reserve runs out, the battery goes into Deep Sleep Mode and needs grid or generator power to recharge. Before you enable this mode, cut house loads as far as you can. Do not enable it when there is no sunlight, because that can drain the battery reserve.

<!-- review notes
- sentence 2: support check: partial - The passage lists these as methods to enable PV Search Mode, but 'waiting for morning or automatic black start' and the other two are phrased as ways to enable it; 'enters in one of three ways' is close but the reset/morning framing is a paraphrase; acceptable core, though 'only three' is stronger.
- sentence 6: support check: partial - Reducing house loads is stated, and a note warns that enabling without sunlight may drain reserve below threshold, but 'do not enable' is not an explicit prohibition.
-->
