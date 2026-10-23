---
id: symptom:short-circuit
type: Symptom
name: Short circuit
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Sunny Island US units the short circuit shows as display code F930 (level 3 error via SiCom)
    or W946 (level 1 warning via SiCom).
  cite:
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=155.r12
    h: 5de9c9959559
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=156.r13
    h: 3d6fcdd239fb
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:ac-terminal-voltage-low
  note: A load-side short circuit pulls the Sunny Island supply voltage on the affected line conductor
    down until it can no longer be held. The Multicluster-Box contactor Q10/Q110 then loses its supply
    and the event log reports 'Cluster incomplete' (event 8616).
  cite:
  - src: src:sma-doc-259761
    loc: tbl=71.r2
    h: 7387db824fd2
  - src: src:sma-doc-278742
    loc: tbl=75.r2
    h: 7387db824fd2
  review: drafted
  review_note: 'support check: partial - Event 8616 supports the supply voltage dropping on the line conductor,
    the Q10/Q110 supply failing and ''Cluster incomplete''. The passages do not mention a phase voltage
    signal or an ''event log'' as such.'
---
On SMA Sunny Island US systems, the communication bus reports a short circuit either as error F930 or as the lower-level warning W946. If the short circuit is on the load side, the Sunny Island cannot hold the voltage on the affected line conductor. The supply to the Multicluster-Box contactor Q10/Q110 then fails and the cluster is reported as incomplete. Look for the short circuit in the loads and in the stand-alone grid wiring first, and also check that connection AC2 is not shorted. Clear the short circuit before restarting. On the DC side, insulation failures come from short circuits. These usually happen when humidity meets damaged or aged DC cables or connectors. Inside a module, a bypass diode can fail shorted. This happens when the diode is physically shorted in the junction box, mounted the wrong way round, or hit by lightning or static discharge. Shorted diodes are reported more often than open ones. Short-circuit currents in a battery can cause heating and electric arcs. Remove metal jewellery and use insulated tools and gloves when working on the battery.

<!-- review notes
- sentence 1: support check: partial - F930 and W946 are the short-circuit codes, but the passages say they are SiCom messages, not that the 'communication bus' reports either code, and they do not mention US units.
- sentence 3: support check: partial - Eliminating the short circuit and checking AC2 are in the passages, but the AC2 check appears in an overload context. The instruction to look in the loads and wiring first and to clear the fault before restarting is not clearly stated.
-->
