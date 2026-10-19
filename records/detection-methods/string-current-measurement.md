---
id: method:string-current-measurement
type: DetectionMethod
name: String current measurement
aliases:
- string current comparison
- PV string current measurement
---
String current measurement checks the current of each PV string to confirm that the system operates correctly and that the array wiring has no major faults; it is not a measure of module or array performance. It can be done as a short circuit test, which is preferred because it excludes the inverter, or as an operational test with a clip-on ammeter around the string cable while the inverter tracks maximum power. Measured currents are compared with the expected value and, for identical strings in stable irradiance, with each other; they should be close to the average string current. When irradiance is unstable, delay the test, use a reference string meter, correct with an irradiance reading, or run an I-V curve test instead. String current comparison is used to detect cable defects and connector defects, and to confirm module hotspots from cell damage after an infrared scan and to retest after repair. Making and breaking string short circuit currents is hazardous: isolate all strings first, use instruments and switches rated above the short circuit current and open circuit voltage, and confirm the current is zero before changing connections. Monitored string currents can also be used to calculate string losses, and these work best when strings share the same orientation and shading and each combiner input has few strings.
