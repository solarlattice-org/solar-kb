---
id: mit:reverse-voltage-sweep
type: Mitigation
name: Dark reverse voltage sweep
aliases:
- BPD test
---
A dark reverse voltage sweep drives reverse current through a module or string with no light on it. It checks that the bypass diodes are connected and that the contacts in the junction box have low resistance. It targets junction box failure caused by cold or unreliable solder joints, which can lead to arcing, burnt junction boxes and fire. The sweep shows diodes with no current flowing through them and exposes high contact resistance, provided a maximum allowed resistance is set for the bypass diode IV curve. In the field, sweep each module string at night by applying 3% to 5% of rated Isc and recording the reverse bias voltage reached. An unusually high voltage points to an open or high-resistance bypass diode (failure mode A). To find the affected modules in a suspect string, do a night infrared inspection while the reverse current is applied and look for substrings that are a few kelvin warmer. The sweep can miss contacts that are not fully working but still have low resistance at test time. An automated visual inspection after soldering is recommended to catch these, and thermal inspection is still needed for failure modes B and C. If even one failure is found, test all modules because the fire risk is high.

<!-- review notes
- sentence 4: support check: partial - 3-5% Isc, night, string-wise reverse voltage and high voltage indicating mode A/open BPD are stated, but 'high-resistance' diode is from the system-level sentence and 'unusually high voltage points to' is slightly stronger; also Statement says 'sweep' while passage describes applying a current.
-->
