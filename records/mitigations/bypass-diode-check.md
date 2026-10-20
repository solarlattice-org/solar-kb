---
id: mit:bypass-diode-check
type: Mitigation
name: Bypass diode functional check
aliases:
- Bypass diode testing
- BYT
- bypass diode check
---
A bypass diode functional check tests whether the diodes in a module junction box still work, so that open or shorted diodes can be found as part of Bypass Diode Failure. If hotspots or burn marks are found, check the bypass diodes to confirm they still activate, which helps prevent more severe degradation. The most reliable test is to measure the diode directly with a multimeter in diode or ohmmeter mode, which shows whether it is short-circuited or open-circuited. Open-circuit voltage measurements and IV curves can also show a shorted diode, because the module's Voc comes out lower than expected. Infrared thermography can show diode activations or hotspots, since an active cell group runs hotter than the neighbouring cells that are still producing current. Open-circuit diodes are harder to find, because they cause no visible effect unless the module is in a strong mismatch condition, and they often go undetected. A failed diode can technically be replaced, but in practice the whole module is usually replaced, and modules that are left in place should be closely monitored. After a repair, verify string behaviour, and fix upstream mismatch or shading so the replacement diodes last longer.

<!-- review notes
- sentence 8: support check: partial - Mitigation says correct mismatch/shading drivers and verify string behaviour after repair, and avoiding shading extends bypass lifetime, but the 'replacement diodes last longer' link for mismatch is not explicit.
-->
