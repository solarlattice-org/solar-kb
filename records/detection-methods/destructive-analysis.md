---
id: method:destructive-analysis
type: DetectionMethod
name: Destructive analysis
---
Destructive analysis of the junction box is the only way to tell a failing bypass diode apart from failure mode A, an unreliable cold solder joint inside the box. Such weak joints are more common in newer half-cell modules: the diode boxes are small, the leads are soldered rather than clamped, and the boxes are filled with a filler material that can shrink or change chemically and loosen a weak connection. Infrared thermography cannot detect failure mode A, and the fault goes unnoticed while the module is not shaded. Before taking anything apart, suspect modules can be found with a string-wise bypass diode test at night: apply 3% to 5% of rated Isc in reverse and look for a string with unusually high reverse voltage. Then use night infrared to find the slightly warmed substring. If the fleet shows a mixture of failure modes A and B, a cold solder joint is the likely cause, and the problem usually affects a share of modules from the same production batch. Safety: a shaded module with this fault can heat up within seconds and char or burn. If even one failure is found, all modules should be tested because of the high fire risk.

<!-- review notes
- sentence 1: support check: partial - The passage says a failing BPD cannot be differentiated from mode A without destructive analysis of the junction box, but it does not say this is the only way, and it describes tests (reverse-bias test plus IRT) that find mode A or an open BPD without distinguishing them.
-->
