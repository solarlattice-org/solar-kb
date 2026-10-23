---
id: mit:insulation-monitor-check
type: Mitigation
name: Insulation monitoring check
---
An insulation monitoring check means inspecting the inverter's insulation monitoring function, including the monitoring device and its cabling, after the inverter reports a problem with that function. On the SMA Sunny Central CP XT, error 6448 means the insulation monitoring is returning values that are not permitted, and the inverter logs it as a warning. Error 6461 on the same inverter means the insulation monitoring device has not accepted its threshold, and the corrective step is to check the device and the cabling to it. Inverters monitor the insulation of the DC input to ground, and each model has its own minimum insulation resistance. The check relates to loss of electrical insulation and ground faults, which can affect modules, cables and interconnectors. If a real ground fault is suspected, first measure the voltages in the PV system, and only if that does not succeed, carry out an insulation resistance measurement. As a preventive measure, ground faults should be detected by the inverter or other devices at all times, so a monitoring function that is not working properly should be fixed promptly. The plant operator decides how the insulation test of the whole plant is carried out.

<!-- review notes
- sentence 1: support check: partial - Passages say 'Check insulation monitoring' and 'check the device and cabling' as corrective measures, but don't define the term as stated; the combined definition is a reasonable paraphrase though slightly synthesized.
- sentence 2: support check: partial - Explanation matches and S1/S2 'W' suggests warning, but the passage doesn't name the SMA Sunny Central CP XT or define W explicitly.
- sentence 3: support check: partial - Explanation and corrective action match, but the model (same inverter) isn't stated in the passage; also behavior (15 min) not mentioned though not required.
- sentence 7: support check: partial - Ground fault detection by inverter or other devices at all times is stated, but fixing a non-working monitoring function promptly is not stated.
-->
