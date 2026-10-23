---
id: symptom:battery-disconnected
type: Symptom
name: Battery disconnected
aliases:
- Battery separated externally
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA inverters report event 9395 with the message 'Battery separated externally' when the DC power
    link to the battery is lost.
  quote: Battery separated externally
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h81
    h: 3ee924ad3710
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h65
    h: 3ee924ad3710
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h73
    h: 3ee924ad3710
  review: drafted
---
This symptom appears as event 9395 on SMA battery-capable inverters, logged with the message Battery separated externally. The event means the DC power connection between the inverter and the battery has been broken. The same event number and meaning appear in the documentation for several SMA inverter families, so read it the same way across them. Keep it separate from event 9308, which reports a communication error in the battery system, not a lost DC power connection.

<!-- review notes
- sentence 1: support check: partial - Event 9395 and message are stated, but 'battery-capable inverters' and 'logged' are not specified in the passages.
- sentence 3: support check: partial - The same event text appears in several sources (u1-u3), but the passages don't name different inverter families or state it should be read the same across them.
-->
