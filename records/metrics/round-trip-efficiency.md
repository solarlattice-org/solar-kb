---
id: metric:round-trip-efficiency
type: Metric
name: Round-trip efficiency
aliases:
- RTE
- roundtrip efficiency
- round-trip system efficiency
category: Storage
---
Round-trip efficiency compares the energy charged into a battery system with the energy you get back when it discharges. It is given as a percentage and covers all losses along the way, including self-discharge and other electrical losses. It can be stated DC-to-DC for the battery alone or AC-to-AC for the whole system. Manufacturers often quote the DC figure, but utilities care more about the AC figure measured at the point of interconnection. Because the point of measurement changes the result, one product table lists a battery DC round-trip efficiency of 0.93 to 0.95, depending on storage duration, and separate lower system values at the point of measurement for AC-coupled and DC-coupled layouts. Coupling matters because each power conversion adds loss: one vendor compares a DC-coupled design with one conversion at 93.3 percent against an AC-coupled design with three conversions at 89 percent. Spec sheets may give a maximum value and say what it includes, for example a maximum round-trip efficiency of 92.4 percent including the battery.

<!-- review notes
- sentence 3: support check: partial - DC-DC vs AC-AC, manufacturer DC preference and utility AC preference at interconnection are stated, but 'DC for battery alone, AC for whole system' is only loosely implied.
-->
