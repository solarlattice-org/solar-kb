---
id: mit:bess-charging-strategy
type: Mitigation
name: Battery charging strategy tuning
---
Battery charging strategy tuning means adjusting how a co-located battery charges so that it captures PV energy that would otherwise be curtailed. It applies to grid curtailment yield losses at PV-plus-storage sites, and only where a battery is present. Curtailed energy can be partly recovered through DC-coupled or AC-coupled battery charging. This works only if the battery has spare capacity and power headroom, its controls allow charging, and its operating objective gives value to the charge. Before tuning, rebuild available power from irradiance and plant data, then sort each constrained interval by cause, including battery charging limits. At storage sites, track whether curtailed PV energy was charged, clipped or abandoned, so you can see what the charging strategy recovers. Charging strategy tuning does not remove the curtailment itself, so it should go together with tracking curtailment separately and using curtailment-aware performance metrics.

<!-- review notes
- sentence 5: support check: partial - The workflow reconstructs available power and classifies constrained intervals including BESS charging limit, but it doesn't say this is done 'before tuning'.
- sentence 6: support check: partial - u7 says to track whether curtailed PV was charged, clipped, or abandoned at storage sites, but doesn't state the purpose of seeing what the charging strategy recovers.
- sentence 7: support check: partial - The mitigation lists tracking curtailment separately and using curtailment-aware metrics alongside tuning, but the passages don't say tuning fails to remove curtailment or that they must go together.
-->
