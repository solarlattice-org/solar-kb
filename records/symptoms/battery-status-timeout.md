---
id: symptom:battery-status-timeout
type: Symptom
name: Battery state change timeout
aliases:
- Timeout for battery status change
- Event 9350
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: SMA event 9350 appears as the message 'Timeout for battery status change' when the battery did
    not complete a requested state change in the allowed time.
  cite:
  - src: src:kb-sma-sbsexx-us-50-event-messages
    loc: sec=h79
    h: 1d8b6de8d3e4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h801
    h: 92f63d932262
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h57
    h: 1d8b6de8d3e4
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h65
    h: 062b28756a01
  - src: src:sma-kb-ereignis-9350
    loc: sec=h1
    h: 0876eb4676f8
  review: drafted
---
The inverter logs event 9350 when it asks the battery to change state and the battery does not do so within the set time. The event appears in the inverter event log as the message Timeout for battery status change. First make sure the battery is switched on and is not in a fault state. Next, check that the battery communication cable is assembled correctly and firmly connected. Compare the battery's actual state with the state you expect. If they differ, check that the battery's ambient temperature meets the manufacturer's limits and review the battery management settings. Do not confuse this with event 9308, which means the external battery management cannot be reached at all. For 9308, check the battery communication parameters, such as the IP address. If you cannot find the cause, maintain the battery to the manufacturer's specifications and contact Service.

<!-- review notes
- sentence 6: support check: partial - Event 9308 meaning and the check of battery communication parameters (e.g., IP address) are stated, but the 'do not confuse' with 9350 comparison is not in the passages.
- sentence 7: review: partial - Both actions are in the passages, but battery maintenance is a general procedure step, not something done only when the cause cannot be found; only contacting Service carries that condition.
-->
