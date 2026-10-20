---
id: mit:fleet-wide-testing
type: Mitigation
name: Fleet-wide module testing
---
Fleet-wide module testing means testing every module in a system as soon as one junction box connection failure is found, because these failures carry a high fire risk. It addresses junction box failure caused by unreliable connections such as cold solder joints. These defects usually come from a production problem shared by a whole batch, so a small share of modules from the same batch may also be affected. At system level, run a reverse voltage sweep on each module string to find bypass diodes that are not connected or have high resistance. Use thermal inspection to find open-circuit substrings. A practical way is a night-time bypass diode test per string with 3% to 5% of rated Isc applied. Any string with unusually high reverse voltage is then scanned with night infrared to find the warmed substring and the faulty module. Limits: one connection failure type stays invisible to infrared unless the module is shaded or under the diode test. An open bypass diode cannot be told apart from it without destructive analysis of the junction box. Unstable connections can come and go, so a module may pass one test and fail a later one. Modules that looked normal at the end of production were later found defective at pre-shipment inspection. For module insulation failures, where modules are tested one by one, replace every module that fails the insulation or wet-leakage test. Insulation testing with a mobile test centre before installation is also recommended.

<!-- review notes
- sentence 1: support check: partial - The passage says that after a single failure all modules should be tested because of the high fire risk, but it does not define 'fleet-wide module testing' as a term or say it applies only to junction box failures.
-->
