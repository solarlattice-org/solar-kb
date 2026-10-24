---
id: arch:grounded-pv-array
type: Architecture
name: Grounded PV array
aliases:
- negatively grounded array
- positively grounded array
- solidly grounded
- Earth PV System
- positively grounded
category: Earthing
---
In a grounded PV array, one of the current-carrying DC conductors is intentionally bonded to earth, so some planned earth leakage current is part of the design. In most legacy systems installed before 2011, one DC pole is solidly bonded to ground inside the inverter. Modern non-isolated string inverters are usually functionally grounded, with neither pole solidly bonded. The bond between the grounded conductor and the grounding electrode system normally runs through the ground-fault protection device. If fault current is detected in that path, the circuit opens and the inverter shows a ground-fault alarm. A ground fault on the normally ungrounded terminal sends residual current back to the grounded terminal through the ground-fault monitoring, such as a GFDI, which then trips. When retrofitting, check whether the modules must be negatively or positively grounded. Moving them to a functionally grounded modern inverter can cause potential induced degradation and a fast loss of production, so consult the module manufacturer first. Some module-level electronics cannot be used with this topology. The Generac PV Link requires modules that do not need positive or negative grounding, because grounding would interfere with its power line communication. Commissioning guides give separate insulation resistance test procedures for source circuits and combiner sub-arrays in grounded arrays and in ungrounded arrays.

<!-- review notes
- sentence 2: support check: partial - Passage says 'most legacy' solidly grounded and modern generally functionally grounded non-isolated; 'usually' fine, but 'inside the inverter' ok; minor wording differences, though the claim matches closely—'most' legacy systems is stated, so only small qualifiers differ.
- sentence 4: support check: partial - Passage says residual current flows via ground-fault monitoring (e.g., GFDI) and triggers it, but does not explicitly say it trips.
- sentence 6: support check: partial - PV Link requirement of modules not needing grounding due to PLC interference is stated, but the claim that module-level electronics generally cannot be used with this topology is a generalization not stated.
- sentence 7: support check: partial - Passages list separate procedures for source circuits and sub-arrays in grounded and ungrounded arrays, but are in a typical commercial PV system meg testing section, not explicitly 'commissioning guides' generally.
-->
