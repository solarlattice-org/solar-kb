---
id: symptom:generator-overload
type: Symptom
name: Backup generator overload
aliases:
- Generator overload
- generator connects only briefly
- generator current limitation
claims:
- claim_id: c1
  rel: observed_as
  target: meas:brief-generator-connection
  note: The battery inverter connects to the running generator only for a short time. Overload is one
    possible cause; voltage or frequency thresholds that are too strict and exceeded reverse-power time
    are others.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h992
    h: 2d3702134b5f
  - src: src:sma-doc-259761
    loc: sec=h855
    h: 7bfd72b92a8c
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:generator-frequency-sag
  note: The battery inverter watches the generator frequency against its nominal value and reduces the
    generator load when the frequency drops below it.
  cite:
  - src: src:sma-doc-sigen-13fe0914
    loc: sec=h20
    h: f8f3cc00a432
  - src: src:sma-doc-278742
    loc: sec=h769
    h: 955e6bbcb046
  review: drafted
---
A typical sign is a battery inverter that connects to the running backup generator but drops it again after only a short time. The generator may be overloaded. In that case, set the rated generator current parameter to 75% of the generator's rated current and reduce the load power if possible. Other causes give the same short-connection behavior: generator voltage or frequency limits set too strictly, or the allowed reverse-power time being exceeded. Check the event log for a reverse power warning before blaming overload. The inverter detects overload by watching the generator frequency. When the frequency falls below the nominal value, it reduces the generator load by cutting battery charging, up to switching to discharge. When adjusting the frequency thresholds, watch and evaluate the measured frequency at the external grid connection during operation. Staggering load use over time also relieves the generator. With parallel inverters, only the total generator current is limited. The current can therefore be shared unevenly, and if one unit fails, more current flows through the others. If the generator current setting is too low for the loads, enhanced generator management draws extra current from the battery to cover the difference.

<!-- review notes
- sentence 3: support check: partial - Other causes and the reverse-power event check are stated, but 'before blaming overload' ordering is not stated in the passages.
-->
