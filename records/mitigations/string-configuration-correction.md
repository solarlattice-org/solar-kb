---
id: mit:string-configuration-correction
type: Mitigation
name: String configuration correction
---
String configuration correction means changing how a PV string is built or wired. That can mean changing the number of modules in the string or fixing a faulty string connection. It applies when the inverter reports PV input overvoltage or MPPT voltage high, or a reverse injection fault on one or more PV inputs. For an overvoltage alarm, measure the voltage at the DC terminals in the wiring box and compare it with the inverter's measurement reading. If the two agree within 2%, adjust the number of panels in the string. If they do not agree, the inverter is replaced instead. On these inverters, the open-circuit PV voltage must stay below 1000 V. For a reverse injection fault, first watch for about 5 minutes to see if the alarm clears by itself. If it keeps coming back, switch the DC off and open the fuse holders to isolate the strings. Then use a meter to find the abnormal string and correct its connection. When resizing a string, the maximum number of modules can be found by applying the NEC 690.7 temperature correction factor to the module open-circuit voltage. Fuse ratings should be checked against the new string configuration with fuse sizing calculations. If the alarm still occurs after the adjustment, contact the manufacturer's after-sales service.

<!-- review notes
- sentence 5: support check: partial - Steps are present, but the passage says to turn DC off and isolate strings if the alarm still occurs after the 5-minute observation, not specifically 'keeps coming back'; roughly consistent.
- sentence 6: support check: partial - NEC 690.7 correction for max modules and fuse sizing calculations are stated, but the example uses 1500V and the passages don't link them as part of resizing a string beyond general advice.
-->
