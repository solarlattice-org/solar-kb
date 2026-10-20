---
id: comp:pv-array
type: Component
name: PV array
---
A PV array is an assembly of PV modules wired together electrically, either directly or as strings or sub-arrays. IEC 62548 sets the design requirements for PV arrays, covering DC array wiring, protection devices, switching and earthing, and it refers to IEC 62446 for operation and maintenance. IEC 62446 covers commissioning and periodic checks of the array, including a PV array test report and insulation resistance tests, both dry and wet. IEC 61829 describes how to measure I-V curves of the array on site and correct them to standard test conditions, which is useful for commissioning and troubleshooting. Some inverters can plot an I-V curve of the array for each MPP tracker, which helps catch array problems early. Module temperature that is unusually high compared with irradiance can mean the array is poorly ventilated or has local hot spots, but a detached temperature sensor can also cause readings like this. Some inverters offer anti-PID and PID repair functions that shift the potential of the array's positive pole relative to ground to suppress or reverse potential induced degradation.

<!-- review notes
- sentence 3: support check: partial - The passages show IEC 62446 covers commissioning tests and a PV array test report with initial and periodic verification, and an array insulation resistance test and a wet one appear in headings; however, they don't say a dry test is covered or that IEC 62446 is the source of those tests.
- sentence 7: support check: partial - The passage describes anti-PID and PID repair functions that lower the positive-pole potential for N-type panels, but it says nothing about 'some inverters' or other panel types, and the repair function drives the potential to -500Vdc rather than just shifting it.
-->
