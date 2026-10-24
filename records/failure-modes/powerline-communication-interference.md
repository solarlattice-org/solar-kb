---
id: fm:powerline-communication-interference
type: FailureMode
name: Power line communication interference
aliases:
- PLC communication impaired
- AC cables laid in parallel
- communication error rate
- Communication impaired
- Communication disrupted
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:signal-cable-emi
  note: AC cables in operation create an electromagnetic field that can induce leading or lagging interference
    in network cables while data is being sent.
  cite:
  - src: src:sma-doc-275752
    loc: sec=h161
    h: bde2494ef9c1
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-doc-275752
    loc: sec=h161
    h: bde2494ef9c1
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  note: For PLC, the AC cables both carry the signal and can be the source of interference, so how they
    are laid matters.
  cite:
  - src: src:sma-doc-275752
    loc: sec=h161
    h: bde2494ef9c1
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: sec=h178
    h: 593b544afb5c
  review: drafted
  review_note: 'support check: partial - AC cable routing is covered, but the claim that AC cables carry
    the PLC signal is not stated in the passages.'
- claim_id: c4
  rel: affects
  target: comp:microinverter
  note: The microinverters communicate over power line communication, so detection problems are handled
    as PLC troubleshooting.
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h81
    h: 45e34b20bb80
  - src: src:enphase-enphase-iq8-series-mc4-microinverter-installation-and-operation-manual-na
    loc: tbl=35.r1
    h: 76326e99f670
  review: drafted
  review_note: 'support check: partial - Microinverters use PLC and detection issues are PLC troubleshooting,
    but the link to interference affecting microinverters is only implied.'
- claim_id: c5
  rel: presents_as
  target: symptom:communication-loss
  note: Reported as communication impaired or disrupted, with no valid signal on the network line.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h892
    h: 396e8cc792b8
  - src: src:sma-doc-278742
    loc: sec=h942
    h: b98fbac47ec5
  - src: src:sma-doc-259761
    loc: sec=h818
    h: c02dfb4d0c55
  review: drafted
  review_note: 'support check: partial - Communication impaired/disrupted with no valid signal is stated,
    but not as a symptom of PLC interference specifically.'
- claim_id: c6
  rel: presents_as
  target: symptom:mlpe-detection-failure
  note: The gateway fails to detect microinverters, and this is troubleshot as a power line communication
    issue.
  cite:
  - src: src:enphase-enphase-envoy-s-installation-and-operation-manual
    loc: sec=h81
    h: 45e34b20bb80
  review: drafted
  review_note: 'support check: partial - Detection issues are troubleshot as PLC issues, but the passage
    does not say the gateway fails to detect microinverters due to interference.'
- claim_id: c7
  rel: mitigated_by
  target: mit:proper-cable-routing
  note: Keep network cables well away from AC cables. For PLC, keep low-voltage AC cables away from medium-voltage
    AC cables when they run in parallel, cross them at 60 to 120 degrees, and keep cable trays from different
    box-type transformers apart.
  cite:
  - src: src:sma-doc-275752
    loc: sec=h161
    h: bde2494ef9c1
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: sec=h178
    h: 593b544afb5c
  - src: src:sma-doc-278879
    loc: sec=h33
    h: 67be443ec394
  review: drafted
  review_note: 'support check: partial - Routing guidance is stated, but 50 m network clearance and the
    PLC LV/MV spacing are not explicitly tied as mitigation of PLC interference; also the grounding passage
    mentions routing generally.'
- claim_id: c8
  rel: mitigated_by
  target: mit:system-grounding
  note: Grounding the communication device properly and routing cables correctly limits emitted interference
    and susceptibility to it.
  cite:
  - src: src:sma-doc-278879
    loc: sec=h33
    h: 67be443ec394
  review: drafted
---
Power line communication interference happens when the data signal between devices is disturbed by electromagnetic fields from nearby energized AC cables. In the field it usually shows up as an impaired or disrupted communication alarm, with no valid signal on the network line. On microinverter systems that use power line communication, a gateway that cannot detect the microinverters should be treated as a PLC problem. Check how the cables are laid: network cables need plenty of clearance from AC cables. For PLC links, keep low-voltage AC cables apart from medium-voltage AC cables when they run in parallel, and cross them at close to a right angle. Only put AC cables fed from the same box-type transformer in a shared trench, and keep cable trays from different transformers apart. Grounding the communication device properly and routing its cables correctly reduces interference and improves communication quality.

<!-- review notes
- sentence 1: support check: partial - Passage covers EMF from AC cables interfering with network cable data, not specifically PLC signals between devices.
- sentence 2: support check: partial - The no-valid-signal communication messages are present, but not linked to PLC interference or being 'usual'.
- sentence 6: support check: partial - Same-transformer trench rule is stated, but trays from different transformers require 0.5 m horizontal distance, which is consistent with 'apart'; 'fed from' wording is minor.
-->
