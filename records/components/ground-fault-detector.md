---
id: comp:ground-fault-detector
type: Component
name: Ground fault detection circuit
aliases:
- GFCI
- residual current detection
- Ground Fault Detector
- Ground Fault Current Sensor
- GFCI sensor
- residual-current monitoring unit
- comp:residual-current-monitor
- Residual current monitoring unit
---
The ground fault detection circuit is the part of the inverter that provides DC ground fault protection. It uses residual current detection, as UL 1741 requires. If the PV array has a ground fault, the circuit senses the leakage current and raises an alarm, and the inverter stops operating. Some manuals state that the inverter shuts down when the leakage current goes above 500 mA. Other manuals point to static and dynamic trip thresholds that are set during commissioning or in the app. A ground fault is an unintended connection, or a loss of insulation, between the PV system and ground. A common cause is damaged conductor insulation, and electrical codes require devices that detect and interrupt ground faults. The detector itself can fail (Ground fault detector failure). In that case the inverter reports a ground fault current sensor or leakage current sensor fault code, such as Protect0310 or Protect0100. To clear a sensor fault, cycle both the AC and DC switches off and on, waiting one minute between off and on. If the fault does not clear, contact service or replace the inverter. Inverters also monitor DC insulation to ground, but this monitoring may not show where the fault is. To locate it, technicians measure the voltage from each pole to ground or test the insulation resistance.

<!-- review notes
- sentence 3: support check: partial - The 500 mA shutdown (u3, u36) and the references to static/dynamic trip thresholds are stated, but the passages say only to see the Commissioning, Chapter 5/6 or App Interface sections, not that the thresholds are set during commissioning or in the app.
- sentence 5: support check: partial - Protect0310 (GFCI sensor abnormal) and Protect0100 (leakage current sensor fault) are in the passages, but none of them uses the name 'Ground fault detector failure' or says the detector itself failing is the cause.
-->
