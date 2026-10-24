---
id: concept:open-circuit-voltage
type: Concept
name: Open-circuit voltage
aliases:
- Voc
category: Modules
concept_kind: electrical
claims:
- claim_id: c1
  rel: related_to
  target: method:voc-measurement
  note: Voc of each PV source circuit is measured before the array DC disconnects are closed, to confirm
    correct installation and polarity.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=5.3.1
    h: 5dce7dfc896d
  - src: src:iec-62446-1
    loc: tbl=2.r3
    h: 4a9dff1fba77
  - src: src:test-testing-tools-seaward-pv200-seaward-pv200-manual
    loc: sec=7.1
    h: 8d8044e267c7
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:temperature-coefficient
  note: If cell temperature is also measured, a voltage-temperature coefficient can translate Voc readings
    to a reference temperature.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=5.3.1
    h: 5dce7dfc896d
  review: drafted
- claim_id: c3
  rel: related_to
  target: meas:low-voc
  note: Voc below expectation can point to improper array wiring, failed modules or shorted bypass diodes.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=5.3.1
    h: 5dce7dfc896d
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:crystalline-silicon
  note: The guide gives a standard voltage-temperature coefficient for crystalline silicon modules.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=5.3.1
    h: 5dce7dfc896d
  review: drafted
- claim_id: c5
  rel: related_to
  target: func:rapid-shutdown
  note: The expected string Voc changes when SunSpec rapid shutdown devices are installed.
  cite:
  - src: src:eq-equip-inverters-sma-stp-core1-us-rss-ti-en-11
    loc: fig=3
    h: 7b9f7a9f1da3
  review: drafted
  review_note: 'support check: partial - u15 only shows a figure of expected Voc for a string with SunSpec
    rapid shutdown devices; it implies but doesn''t explicitly state that expected Voc changes.'
---
Open-circuit voltage, abbreviated Voc, is the voltage across a PV module or string's terminals when no current flows. Module datasheets and design guides list Voc as a key electrical rating. During commissioning, the Voc of each source circuit is measured before the DC disconnects are closed. The reading is compared with the expected value, and the same test confirms polarity. Identical strings measured under the same conditions should read about the same Voc, usually within 5% of each other. A reading lower than expected can mean wiring errors, failed modules or shorted bypass diodes. Voc goes down as module temperature goes up. With measured cell temperature and the temperature coefficient, readings can be corrected to a reference temperature. String Voc must stay inside the DC voltage limits of the inverter, charge controller or other DC equipment. Module-level rapid shutdown devices change the expected string Voc, so check the manufacturer's guidance when testing these systems.

<!-- review notes
- sentence 1: support check: partial - Passages give the abbreviation Voc and name open circuit voltage, but none state the definition of voltage across terminals when no current flows.
- sentence 2: support check: partial - u2 and u13 show Voc listed in a module datasheet/spec, but 'design guides' and 'key rating' are not clearly stated.
- sentence 8: support check: partial - u15 only shows expected Voc figure with SunSpec rapid shutdown devices; the advice to check manufacturer guidance is not stated.
-->
