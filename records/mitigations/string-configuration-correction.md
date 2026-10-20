---
id: mit:string-configuration-correction
type: Mitigation
name: String configuration correction
aliases:
- PV module configuration
- system configuration
- DC configuration
---
String configuration correction means fixing how PV modules are wired into strings, such as the number of modules in a string or the string polarity, after the inverter reports a string fault. For a string current reflux fault, check whether the affected string has fewer modules than the other strings and change the module layout if it does. Also check for shading and for modules facing an abnormal direction. A reverse-DC alarm can mean a string is connected backwards or that strings on the inputs have different module counts. Correct the polarity first, then make sure every string has the same number of modules. For string or MPPT reverse connection alarms and faults, check the polarity of the named string and correct it. Only open the DC switch and rework a string when irradiance is low and the string current is below 0.5 A, for example at night. To check the work, use a meter on each string to measure open-circuit voltage and polarity. A negative reading means the string is reversed, and a voltage close to the inverter maximum means the string length needs checking, because cold weather raises string voltage. If the inverter reports high DC voltage, measure DC at the inverter test points with the DC switch off. If the voltage really is high, check the string configuration; if not, the inverter's measurement circuit may be faulty. If the fault continues after these causes are ruled out, contact the manufacturer. Mixing module models or orientations in one MPPT circuit or string does not damage the inverter but lowers performance.

<!-- review notes
- sentence 5: support check: partial - Low irradiance and below 0.5 A are stated, with night as an example, but 'only' applies to reverse and reflux rework, and it is stated as a general rule beyond what the rows say; the reflux row doesn't mention low irradiance.
- sentence 6: support check: partial - Meter measurement, negative reading meaning reverse polarity, and near-max voltage prompting string length check with cold raising voltage are stated, but 'meter on each string' is fine; however the passage says low ambient temperatures, not 'cold weather' explanation differences are minor, and the check is described as verifying VOC generally.
- sentence 7: support check: partial - The row says test with DC switch off, check string config if voltage is high, and with switch on check LCD reading for a bad measurement circuit; the statement's 'if not high, measurement circuit faulty' is roughly implied but the LCD check with switch on is omitted.
-->
