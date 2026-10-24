---
id: concept:series-and-parallel-arcs
type: Concept
name: Series and parallel arc faults
aliases:
- series arc
- parallel arc
- series arc-fault
- parallel arc-faults
- series arc faults
category: Safety
concept_kind: electrical
claims:
- claim_id: c1
  rel: explains
  target: fm:arc-fault
  note: Separates arcs that form along one conductor path (series) from arcs between conductors or between
    parallel strings (parallel).
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  - src: src:test-ground-fault-nrel-field-guide-to-pv-ground-falt-testing
    loc: sec=6
    h: f9609f5bf2cf
  - src: src:kb-sma-sma-america-kb-pv-arc-fault-circuit-interrupter
    loc: sec=h4
    h: 675522b8fd06
  review: drafted
- claim_id: c2
  rel: explains
  target: hazard:fire
  note: DC arcs usually cause destructive fires. Arc faults and ground faults are reported as the two
    most common causes of PV array fires.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  - src: src:test-ground-fault-nrel-field-guide-to-pv-ground-falt-testing
    loc: sec=6
    h: f9609f5bf2cf
  - src: src:test-ground-fault-nrel-field-guide-to-pv-ground-falt-testing
    loc: sec=h10
    h: 709d473ec789
  review: drafted
- claim_id: c3
  rel: related_to
  target: hazard:dc-arc-flash
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  review: drafted
  review_note: 'support check: partial - u1 describes DC arc faults, but no passage mentions DC arc flash
    as a hazard or relates it to them.'
- claim_id: c4
  rel: related_to
  target: func:dc-arc-fault-protection
  note: The inverter arc fault function detects and interrupts DC series arcs.
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=6.r7
    h: 0a2c4c8b596a
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h15
    h: d574c58e979c
  review: drafted
- claim_id: c5
  rel: related_to
  target: mit:arc-fault-circuit-interrupter
  note: Arc fault circuit interrupters installed on individual strings protect against arc faults.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  review: drafted
- claim_id: c6
  rel: related_to
  target: comp:arc-fault-detector
  cite:
  - src: src:test-ground-fault-nrel-field-guide-to-pv-ground-falt-testing
    loc: sec=h10
    h: 709d473ec789
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h15
    h: d574c58e979c
  review: drafted
- claim_id: c7
  rel: related_to
  target: method:waveform-spectrum-analysis
  note: Arcs are found by spectrum analysis of current and voltage waveforms, or by detecting the electrical
    noise that comes with a series arc.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.9
    h: 6199cd73a1f7
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h15
    h: d574c58e979c
  review: drafted
- claim_id: c8
  rel: related_to
  target: std:ul-1699b
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h15
    h: d574c58e979c
  review: drafted
  review_note: 'support check: partial - u21 says the inverter''s arc fault detection complies with UL
    1699B and relates it to series arcs, but the link is via a specific product.'
- claim_id: c9
  rel: related_to
  target: stressor:poor-connector-contact
  note: Loose, separated, damaged or badly mated connections are a common cause of series arcs.
  cite:
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: sec=h13
    h: 48f3c580120e
  - src: src:test-ground-fault-nrel-field-guide-to-pv-ground-falt-testing
    loc: sec=6
    h: f9609f5bf2cf
  - src: src:kb-sma-sma-america-kb-pv-arc-fault-circuit-interrupter
    loc: sec=h5
    h: a958fac316ce
  review: drafted
- claim_id: c10
  rel: related_to
  target: comp:dc-connector
  cite:
  - src: src:sma-doc-core1-us-afci-handling-ti-en-11
    loc: sec=h13
    h: 48f3c580120e
  - src: src:test-ground-fault-nrel-field-guide-to-pv-ground-falt-testing
    loc: sec=6
    h: f9609f5bf2cf
  review: drafted
- claim_id: c11
  rel: related_to
  target: stressor:solder-bond-defect
  note: Separated, cracked or corroded solder joints in modules can start a series arc.
  cite:
  - src: src:test-ground-fault-nrel-field-guide-to-pv-ground-falt-testing
    loc: sec=6
    h: f9609f5bf2cf
  - src: src:kb-sma-sma-america-kb-pv-arc-fault-circuit-interrupter
    loc: sec=h5
    h: a958fac316ce
  review: drafted
- claim_id: c12
  rel: related_to
  target: fm:insulation-loss
  note: Parallel arc faults come from an insulation failure between two conductors.
  cite:
  - src: src:kb-sma-sma-america-kb-pv-arc-fault-circuit-interrupter
    loc: sec=h3
    h: 05678f48e57a
  review: drafted
---
A DC arc fault is a sudden high-power discharge between conductors. In a PV system it can occur in series along neighboring conductors in a string, or in parallel between parallel strings. A series arc forms when a conductor or connection opens while current is flowing. The spark ionizes the air into plasma, and if the current is high enough the plasma keeps the current flowing across the gap as a visible arc. Once a series arc starts, it can last for seconds, minutes or longer. Typical causes are a loose module connector, a loose combiner box terminal, or a solder joint that separates inside a module. Other common causes are damaged or badly mated PV connectors, pinched or abraded conductors, and damage to modules. A parallel arc fault is different: it comes from an insulation failure between two conductors. The NEC 690.11 arc fault requirement covers only series arcs. DC arcs are severely damaging and usually cause destructive fires. Field experience puts arc faults and ground faults as the two most common causes of PV array fires. Arcs are transient, which makes them hard to detect. Inverter arc fault detection looks for the electrical noise of a series arc and shuts down the inverter, and string-level arc fault circuit interrupters add further protection.
