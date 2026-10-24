---
id: metric:array-capture-loss
type: Metric
name: Array capture loss
aliases:
- Lc
- Capture losses
- Instantaneous array capture losses
category: Performance
---
Array capture loss is a performance quantity from the IEA PVPS analytical monitoring framework. Its symbol is LC, and lC for the instantaneous form. It is reported in hours. The instantaneous form has no unit. It is listed with array yield, system yield, system losses and performance ratio, and each of these has an instantaneous form. Capture loss comes from comparing array yield with reference yield. That comparison shows how well the PV array converts the available sunlight. You need the measured DC power of the array to calculate it. If both AC and DC power are measured accurately and at short intervals, the total losses can be split into capture losses and system losses. Only power that is physically lost inside the inverter counts as a system loss. Problems the inverter causes elsewhere, such as poor MPP tracking or output power limiting, are not counted as system losses.

<!-- review notes
- sentence 1: support check: partial - Symbols lC and LC are given, but the passages don't say it comes from the IEA PVPS framework (that attribution isn't visible) beyond the parameter table.
- sentence 4: support check: partial - Array yield vs reference yield is said to represent PV array conversion efficiency, and capture losses are mentioned, but the passage doesn't explicitly say capture loss is derived from that comparison; it is derived by comparing both relationships.
- sentence 5: support check: partial - The passage says array yield requires measuring PV array output power and PDC is measured DC power, but it doesn't explicitly state capture loss calculation needs it, though this is implied.
- sentence 4: review: partial - The passage says array yield versus reference yield shows the PV array's conversion efficiency, but it says capture and system losses are separated by comparing both relationships, not that capture loss comes from the array-versus-reference comparison alone.
-->
