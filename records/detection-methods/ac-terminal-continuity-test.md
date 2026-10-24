---
id: method:ac-terminal-continuity-test
type: DetectionMethod
name: Inverter AC terminal continuity test
aliases:
- continuity between AC phases
- internal short check
- AC breaker trip test
claims:
- claim_id: c1
  rel: produces
  target: meas:ac-phase-continuity
  note: With AC conductors removed and the inverter fully de-energized, a healthy inverter reads open
    (O.O.L or no reading) between phases. Any continuity points to a possible internal short between phases,
    which can explain an onsite AC breaker trip.
  cite:
  - src: src:sma-kb-how-to-determine-if-the-inverter-caused-the-onsite-ac-breaker-to-trip
    loc: sec=h1
    h: a9e16f4f3084
  review: drafted
---
This test checks whether the inverter itself caused an onsite AC breaker to trip. You look for continuity across the inverter's AC terminals, which would reveal an internal short. First switch off both AC and DC to the inverter. Then remove the AC conductors from the inverter terminals and cap each one safely. Before setting the meter to audible continuity, use it to confirm there is zero AC voltage at the terminals. Measure every pair: each phase to each other phase, each phase to neutral and each phase to ground. On a two-phase unit this means L1-L2, L1-N, L2-N, L1-G and L2-G. On a healthy inverter an auto-ranging meter should show out of limits or no reading between phases. Any continuity suggests an internal short, so photograph the reading and contact the manufacturer's service team about a possible replacement. Be aware that a DC voltage can appear on the AC terminals when the PV strings are still connected and the grid side is off. This is normal behaviour and not a fault, but it is another reason to isolate the DC side before testing. Manufacturer procedures also call for confirming that no voltage is present on the AC terminal block, phase to phase, phase to neutral and to ground, before touching it.

<!-- review notes
- sentence 6: support check: partial - Passages say DC on AC terminals with PV connected and AC off is normal, but do not say it is a reason to isolate DC before testing.
-->
