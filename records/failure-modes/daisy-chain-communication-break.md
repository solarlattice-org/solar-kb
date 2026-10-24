---
id: fm:daisy-chain-communication-break
type: FailureMode
name: Daisy-chain communication break
aliases:
- daisy-chain communication issues
- line break after last communicating device
- bad port in the SWDM
- mixed inverter generations in one chain
claims:
- claim_id: c1
  rel: presents_as
  target: symptom:communication-loss
  note: One or more inverters on the daisy chain stop reporting to the cluster controller or Sunny Explorer,
    while possibly still producing.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:communication-module
  note: A bad port in the Speedwire-Webconnect Data Module (SWDM) is named as the typical cause of a chain
    interruption.
  quote: One of the other two inverters may be interrupting the daisy-chain, which is typically caused
    by a bad port in the SWDM.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:network-cable
  note: Faulty Ethernet cabling or poor RJ45 crimps between inverters can break the chain.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:internal-communication-cable
  note: Ribbon cables to the display are part of the communication path and must be fully seated and undamaged.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  rel: affects
  target: comp:inverter-display
  note: On STP-US-10 the display is blank but still part of the communication pathway.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c6
  rel: caused_by
  target: fm:internal-connector-unseated
  note: Ribbon cables not fully seated, kinked or damaged can stop communication through the display.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c7
  rel: caused_by
  target: stressor:improper-crimping
  note: Questionable RJ45 crimps or cable strain on the crimp degrade conductivity.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:signal-cable-emi
  note: Signal cables run near AC power cables, and noise that increases with each inverter added to an
    RS-485 chain, compromise communication.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  - src: src:yaskawa-commercial-inverters-communication-manual
    loc: sec=4.1
    h: b4a6cb97bc31
  - src: src:yaskawa-commercial-inverters-communication-manual
    loc: sec=h33
    h: 46bce2516544
  review: drafted
- claim_id: c9
  rel: caused_by
  target: stressor:installation-error
  note: Star or T connection schemes cause signal reflections; plugging into the middle of a chain during
    commissioning disconnects inverters from the cluster.
  cite:
  - src: src:yaskawa-commercial-inverters-communication-manual
    loc: sec=h33
    h: 46bce2516544
  - src: src:yaskawa-xgi-1500-1mw-iom-docr-071091-h
    loc: sec=h144
    h: c078ef130aec
  - src: src:yaskawa-solectria-xgi-1500-manual-rev-i-21-sep-2021
    loc: sec=h119
    h: c078ef130aec
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:known-good-swap-test
  note: Swap the suspect SWDM and display into inverters further down the chain to see which component
    follows the fault.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:communication-test
  note: Isolate the suspect inverter and connect a laptop with Sunny Explorer directly to its SWDM port
    to check whether the inverter itself communicates.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:inverter-restart
  note: Do a power cycle with both AC and DC off before further troubleshooting; extend to the whole chain
    or site if the issue persists.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  rel: mitigated_by
  target: mit:communication-cable-check
  note: Disconnect, inspect and reconnect Ethernet cables at both SWDM ports; try a known-good cable or
    re-crimp RJ45 jacks.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:proper-cable-routing
  note: Keep signal cables away from AC cables and out of power conduits; use twisted, shielded cable
    away from noise sources.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  - src: src:yaskawa-commercial-inverters-communication-manual
    loc: sec=h33
    h: 46bce2516544
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:communication-bus-termination
  note: Use point-to-point daisy chaining with matching polarity, avoid star or T topologies, terminate
    cable ends where needed and keep the chain short.
  cite:
  - src: src:yaskawa-commercial-inverters-communication-manual
    loc: sec=h33
    h: 46bce2516544
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:rs485-isolated-repeater
  note: Repeaters isolate noise and boost RS-485 signals on chains with multiple inverters.
  cite:
  - src: src:yaskawa-commercial-inverters-communication-manual
    loc: sec=4.1
    h: b4a6cb97bc31
  - src: src:yaskawa-commercial-inverters-communication-manual
    loc: sec=h33
    h: 46bce2516544
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:in-line-coupler-bypass
  note: Temporarily join both sides of the chain with an in-line coupler to jump over a faulty inverter.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Report the faulty SWDM, display or inverter to the manufacturer service line if the steps do not
    resolve the issue.
  cite:
  - src: src:sma-kb-stp-us-10-swdm-display-swap-troubleshooting-guidance-for-inverters-reporting-to-a-c
    loc: sec=h1
    h: d46a4d414b21
  review: drafted
---
A daisy-chain communication break happens when one link in a chain of networked inverters fails. Inverters downstream of that link, or the faulty unit itself, then stop reporting to the cluster controller. Common culprits are Ethernet cables or RJ45 crimps, unseated or kinked ribbon cables, the data module (often a bad port), the display, or the inverter's communication board. On RS-485 chains, noise builds up as more inverters are added, and star or T wiring causes signal reflections that disrupt communication. Start with a full power cycle with AC and DC both off. Then reseat the ribbon cables and check or replace the Ethernet cables, keeping signal cables away from AC wiring. To find the faulty part, swap the suspect data module and display into known-good inverters further down the chain, or isolate the inverter and connect a laptop to it directly. An in-line coupler can bridge around a faulty inverter so the rest of the chain keeps working. During commissioning, connect only at an open port at the end of the chain. On long RS-485 chains, use isolated repeaters and shielded twisted cable.

<!-- review notes
- sentence 1: support check: partial - The passages cover inverters not reporting and a bad link interrupting the chain, but do not define it as a single failed link causing downstream inverters to stop reporting; that framing is a generalization.
- sentence 7: support check: partial - Isolated repeaters and shielded twisted cable are suggested, but the passages do not tie them specifically to 'long' chains; they relate to multiple inverters and noise, with only a length limit stated.
- sentence 1: review: partial - The passages cover inverters not reporting to the cluster controller and one unit interrupting the chain, but do not say outright that a single failed link makes the downstream inverters stop reporting.
- sentence 7: review: partial - Isolated repeaters and well-twisted shielded cable are both recommended, but the passages tie repeaters to daisy-chaining multiple inverters and noise, not specifically to long chains (length is only covered by a 1000 ft limit).
-->
