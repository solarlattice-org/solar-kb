---
id: fm:plc-signal-crosstalk
type: FailureMode
name: Rapid shutdown PLC signal crosstalk
aliases:
- PLC crosstalk
- signal crosstalk on PV conductors
- multiple transmitter interference
- Crosstalk
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:multiple-plc-transmitters
  note: Several rapid shutdown transmitters, for example ones built into parallel string inverters, operating
    on one roof or site.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h1
    h: b48d859b0cfc
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h2
    h: 3cace183879e
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h4
    h: 13c712581d66
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:dc-conductor-proximity
  note: DC conductors tied to different transmitters are bundled or run close together. The signal couples
    more easily between conductors of the same polarity, even through insulation or separate metallic
    tubing.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h2
    h: 3cace183879e
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h4
    h: 13c712581d66
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:rapid-shutdown-device
  note: Module-level receivers malfunction, shut down unexpectedly and can overheat.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h1
    h: b48d859b0cfc
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h2
    h: 3cace183879e
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:rapid-shutdown-transmitter
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h1
    h: b48d859b0cfc
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h3
    h: ce804f1b360e
  review: drafted
  review_note: 'support check: partial - Transmitters can be damaged by crosstalk (u3), but the passages
    mainly describe the transmitter as the source; damage is only mentioned loosely as a cost-avoidance
    consequence.'
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  note: The PLC signal travels on the PV array DC conductors.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h4
    h: 13c712581d66
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h3
    h: ce804f1b360e
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:rapid-shutdown
  note: Receivers shut down even though the transmitter was never turned off.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h2
    h: 3cace183879e
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:low-output-despite-irradiance
  note: Loss of PV system output or low production.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h2
    h: 3cace183879e
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:arc-fault-detected
  note: Repeated arc-fault alarms at the inverter.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
  review_note: 'support check: partial - Ongoing arc-fault alarms at the inverter are mentioned as costs
    of crosstalk, but only indirectly and without stating they are caused by it; ''repeated'' is implied
    by ''ongoing''.'
- claim_id: c9
  rel: presents_as
  target: symptom:inverter-shutdown
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
  review_note: 'support check: partial - Inverter shutdowns are listed among problems to be avoided, but
    it is not clearly stated as a crosstalk symptom.'
- claim_id: c10
  rel: leads_to
  target: fm:rapid-shutdown-device-failure
  note: Severe crosstalk can overheat receivers and damage both transmitters and receivers.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
  review_note: 'support check: partial - Overheating of receivers under severe crosstalk is stated, and
    damage to transmitters and receivers is mentioned, though the damage is not explicitly tied to severe
    crosstalk.'
- claim_id: c11
  rel: detected_by
  target: method:rapid-shutdown-function-test
  note: Required at commissioning on sites with several transmitters whose DC wiring runs close together.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:performance-monitoring
  note: Watch inverter performance for several days after installation.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:plc-transmitter-consolidation
  note: Disable the transmitters built into the inverters and use one external transmitter, or split the
    array into separated blocks that each have their own transmitter, for example along fire access pathways.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h6
    h: f0f3257eb884
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:proper-cable-routing
  note: Keep the bundles, conduit and tray of different transmitters apart. Keep PLC loops short. Keep
    shared runs as short as possible.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h8
    h: 39f90f1eae3d
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h4
    h: 13c712581d66
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h7
    h: 0de98e74a54c
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:homerun-conductor-pairing
  note: Run the positive and negative conductors of a homerun together and twist them lightly.
  cite:
  - src: src:solis-plc-transmitter-crosstalk-application-note-ginlong-solis-us-v5-0
    loc: sec=h7
    h: 0de98e74a54c
  review: drafted
---
Crosstalk happens when a power line communication signal from one rapid shutdown transmitter is induced onto DC conductors that belong to another transmitter. It shows up on sites with several transmitters, often built into parallel inverters, where DC conductors from different transmitters are bundled or run close together. Module-level receivers then shut down even though no shutdown was commanded. This causes lost output, low production, inverter shutdowns and repeated arc-fault alarms. If the crosstalk is severe, receivers can overheat, and both transmitters and receivers can be damaged. On sites with several transmitters, test the rapid shutdown system during commissioning and watch inverter performance for several days afterward. The best fix is a single transmitter for the whole site. Otherwise, split the array into separated blocks, each with its own inverters, DC wiring and transmitter. Keep wiring for different transmitters well apart, keep shared runs short, and route each homerun's positive and negative conductors together with a light twist.

<!-- review notes
- sentence 3: support check: partial - Unintended receiver shutdown and lost output/low production are stated; inverter shutdowns and arc-fault alarms are listed as costs but not explicitly as crosstalk effects.
- sentence 4: support check: partial - Severe crosstalk can overheat receivers is stated; damage to transmitters and receivers is mentioned but not explicitly conditioned on severity.
-->
