---
id: mit:string-isolation
type: Mitigation
name: String isolation
aliases:
- safety isolation
---
String isolation means taking the affected string out of service before further diagnosis or repair work on a suspect module. It is the first step of the corrective action for a module hotspot from cell damage. After isolating the string, the thermal signature is checked under load, the module is replaced if cell damage is confirmed, and the string current is retested after the repair. For junction box failure, safety isolation should be the priority when there is evidence of arcing or burning. This priority matters because bad wiring or poor solder contacts in a junction box can cause internal arcing or heating that may start a fire. One thermal anomaly does not prove the module is permanently damaged, so confirm the electrical impact and that the anomaly repeats before approving a replacement. Raise the priority when the anomaly stays stable across inspections or when several modules in the same string show related signatures.

<!-- review notes
- sentence 1: support check: partial - The passages list 'Isolate the string' as a mitigation step but never define it as taking the string out of service before further diagnosis or repair (verification under load follows isolation).
-->
