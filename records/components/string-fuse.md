---
id: comp:string-fuse
type: Component
name: String protection fuse
aliases:
- String fuses
- DC string fuses
- PV string fuse
- String overcurrent protective device
- DC fuses
---
A string fuse is an overcurrent device fitted on each PV string inside the inverter or its wiring box. It gives the solar modules extra protection. You size it from three values on the module data sheet: the module short circuit current Isc, the maximum backfeed current, and the maximum string fuse rating. Fronius recommends a fuse nominal current above 1.5 x Isc and a nominal voltage at least equal to the maximum open circuit voltage of the array. The fuse body should be 10 x 38 mm. Following these criteria prevents the fuse from tripping early in normal operation. Size overcurrent protection according to NEC Article 690. The fuse rating must never exceed the module manufacturer's maximum series fuse rating. Under the 2017 NEC, a single protective device in either the positive or the negative polarity is enough. The main failure mode is string fuse failure, meaning a damaged or open fuse. On FIMER inverters with monitored string fuses, it raises warning W017 String Err. To diagnose it, check each fuse on the fuse boards with a multimeter. After replacing an open fuse, confirm that the string input current does not exceed the fuse rating, especially where strings are paralleled outside the inverter. If no fuse is damaged but the alarm persists, check the inverter settings for which input strings are present. You may need to replace fuses because a fuse is damaged or because the fuse value has to match the PV panels used. Open the AC and DC disconnect switches first, but DC input voltage is still present on the fuse board afterwards. Wear proper PPE and wait at least 30 minutes for stored energy to discharge.

<!-- review notes
- sentence 1: support check: partial - Passages support string fuses as extra module protection and the three decisive values (Isc, backfeed current IR, max string fuse value), but not 'overcurrent device on each string' or the 'size it from' framing; u3 mentions only Isc.
- sentence 2: support check: partial - Criteria IN>1.5×ISC, VN>=max open circuit voltage, 10x38 mm and premature tripping prevention are stated, but attribution to 'Fronius' isn't in the passages (and 'at least equal' fits >=).
- sentence 4: support check: partial - W017 String Err for damaged fuses on models with monitored string fuses and the multimeter check are stated, but 'main failure mode' and 'FIMER' are not in the passages.
-->
