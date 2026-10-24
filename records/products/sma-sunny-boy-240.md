---
id: prod:sma-sunny-boy-240
type: Product
name: Sunny Boy 240 and Sunny Multigate
aliases:
- SB240-10
- Sunny Multigate
- SB 240
- SB240-US-10
- SB 240-US-10
- Sunny Boy 240-US
- SB 240-10
- module inverter
- micro inverter
- SB240
category: Inverters
make: sma
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-doc-259463
    loc: sec=h98
    h: 233a351a05ab
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:microinverter
  cite:
  - src: src:sma-kb-event-8104-with-sb240-10-and-sunny-multigate
    loc: sec=h1
    h: cb41fd4e6a20
  - src: src:sma-kb-event-6402-with-sb240-10-and-sunny-multigate
    loc: sec=h1
    h: 5f30c61ad11f
  review: drafted
  review_note: 'support check: partial - Passages call the SB240-10 a micro inverter/module inverter,
    but the Multigate is a gateway, so ''Sunny Boy 240 and Sunny Multigate'' as a microinverter instance
    is only partly supported.'
- claim_id: c3
  attr: max_input_voltage
  value:
    max: 45
    unit: unit:V
  conditions: Maximum allowed DC input voltage of the SB240-10 module inverter; higher voltage triggers
    event 3401 (DC overvoltage)
  cite:
  - src: src:sma-kb-sb240-10-sunny-multigate-event-number-3401
    loc: sec=h1
    h: 9cfe1dfd8be7
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:power-line-communication
  note: Micro inverters communicate with the Sunny Multigate over PLC; inverter and Multigate PLC protocol
    versions must match.
  cite:
  - src: src:sma-kb-sb240-10-sunny-multigate-event-number-10259
    loc: sec=h1
    h: b0deaff55d8a
  - src: src:sma-kb-event-10265-with-sb240-10-and-sunny-multigate
    loc: sec=h1
    h: 36c2fdacb2c4
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:webconnect
  note: Sunny Multigate is added to Sunny Portal as a Webconnect device.
  cite:
  - src: src:sma-kb-sunny-portal-webconnect-adding-and-replacing-the-sunny-multigate
    loc: sec=h1
    h: 04224190f629
  review: drafted
- claim_id: c6
  rel: requires
  target: tool:sma-sunny-explorer
  note: Needed to delete an old micro inverter allocation after moving it to another Multigate.
  cite:
  - src: src:sma-doc-279088
    loc: sec=h132
    h: 24329d46be87
  review: drafted
- claim_id: c7
  rel: requires
  target: role:grid-guard-code-holder
  note: An SMA Grid Guard Code is needed to change specific monitored grid operating limits.
  cite:
  - src: src:sma-kb-sb240-10-sunny-multigate-event-number-2-202
    loc: sec=h1
    h: bd9b63da6b8b
  review: drafted
  review_note: 'support check: partial - Passage says a Grid Guard Code is required to change specific
    parameters (monitored operating limits), but doesn''t state it as a requirement role of the product
    in general.'
---
The Sunny Boy 240 (SB240-10, with a US version SB240-US-10) is an SMA module-level micro inverter that works with the Sunny Multigate, which gathers the micro inverters and links them to the grid and network. The DC input voltage limit is 45 V; module open-circuit voltage at or above that, taking temperature into account, causes event 3401 and the module is not suitable. The micro inverters talk to the Multigate over power line communication, so long AC runs, many switching points, or parallel AC cables less than 10 cm apart can disrupt communication; the line from the Multigate to the last micro inverter should be at most 30 m. Inverters and Multigates are monitored through Sunny Portal or Sunny Explorer, and one Sunny Portal plant can hold up to four Multigates. SMA does not support using the product in Sunny Home Manager systems. Many events, such as 1001, 8104, 10259 and 6305, are fixed by installing the combined firmware package for the module inverter and the Multigate, and a PLC protocol version mismatch after replacing an inverter needs a Multigate firmware update. Event 9014 means an invalid device combination, such as a US unit mixed with a rest-of-world unit or the wrong country data set. If one inverter stops communicating, replace that micro inverter; if all of them stop, replace the Multigate. Event 6402 means the micro inverter is above 75°C and it restarts by itself once it cools.

<!-- review notes
- sentence 1: support check: partial - Passages support SB240-10/SB240-US-10 micro inverter with Multigate, but not that the Multigate gathers the micro inverters and links them to the grid and network explicitly.
- sentence 3: support check: partial - PLC impairment, 30 m line, switching points and 10 cm clearance are stated, but the passage also says 10 m for AC lines and does not explicitly say micro inverters use power line communication generally; the statement omits the conflicting 10 m.
- sentence 5: support check: partial - Passage says not intended for Sunny Home Manager systems and use is not recommended, with no liability, rather than explicitly that SMA doesn't support it (title says no support).
- sentence 6: support check: partial - Firmware install is a step in events 1001, 8104, 6305 and fixes 10259, but for 1001, 8104 and 6305 it is one step among others, not a definitive fix.
-->
