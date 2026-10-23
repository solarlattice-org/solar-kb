---
id: symptom:switch-cycle-limit
type: Symptom
name: Switching cycle limit reached
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Sunny Central CP XT the condition is reported as event 7709 (90% of DC switchgear switch cycles
    used), 7710 (100% used) or 7714 (GFDI switch cycle maximum reached).
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r19
    h: 6a42c84c3a64
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r20
    h: 9fe28a733d7b
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r1
    h: bdaed900d26c
  review: drafted
  review_note: 'support check: partial - Events 7709, 7710 and 7714 are in the passages, but they don''t
    mention the Sunny Central CP XT model or the inverter fault code display channel.'
---
This symptom is a wear warning: the inverter counts how often a switching device has operated and raises an event when the count nears or reaches its rated limit. On a Sunny Central CP XT, event 7709 means the DC switchgear has used 90% of its switch cycles, and event 7710 means it has used all of them. Event 7714 is a separate event: the GFDI has reached its maximum number of switch cycles. The manual lists an inverter behavior time of 10 s for 7709 and 30 s for 7710 and 7714. For the DC switchgear events, the corrective action is to contact the SMA Service Line. For the GFDI event, the GFDI should be replaced. First, read the event number in the inverter's event log to find out which device is worn: the DC switchgear or the GFDI. As a comparison, SMA rates the switch in some string inverters for a minimum electrical endurance of 100000 switching cycles, as long as its maximum switching voltage and current are not exceeded.

<!-- review notes
- sentence 2: support check: partial - The passages give the 90% and 100% meanings of 7709 and 7710, but they don't name the Sunny Central CP XT.
- sentence 6: support check: partial - The event numbers do distinguish the DC switchgear (7709, 7710) from the GFDI (7714), but the passages don't say to read the event number in the event log as a first step.
-->
