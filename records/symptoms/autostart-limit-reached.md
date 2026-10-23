---
id: symptom:autostart-limit-reached
type: Symptom
name: Automatic restart limit reached
aliases:
- Autostart meter elapsed
- Autostart meter slave 1 elapsed
- Autostart meter slave 3 elapsed
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: On Sunny Island devices this shows as warning W724, W725 or W726 (one per line or slave, L1/L2/L3),
    or as event 6133 or F710. Each means the maximum number of autostarts has been reached.
  cite:
  - src: src:sma-kb-event-number-6133-f710-w724-w725-w726
    loc: sec=h1
    h: 1156b85654cf
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r17
    h: ff936afd3095
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: tbl=151.r15
    h: 62d098a4cc54
  review: drafted
---
On a Sunny Island, warnings W724, W725 or W726, or event 6133 or F710, mean the unit has hit its maximum number of autostarts. In other words, it has restarted several times in a row on L1, L2 or L3. Autostart restarts the unit automatically after a malfunction. If one attempt fails, the next one starts right away, but the total number of attempts is limited. Once the limit is reached, the Sunny Island waits ten minutes, resets the autostart counter and tries again. It repeats this cycle each time the limit is reached. This warning is a result of another fault, not the root cause. Read the pending and logged warnings and faults, for example in Sunny Portal, and fix the fault that keeps causing the restarts. The generator has its own restart-attempt setting, GnAutoStr. It can also be set from 0 to 10 and defaults to 3. If the cause is not clear, the owner should contact the installer for further investigation.

<!-- review notes
- sentence 4: support check: partial - The passage says to read the pending and logged warnings and faults (e.g. Sunny Portal) and search for the corresponding message, but it does not explicitly say the warning is a consequence rather than the root cause.
- sentence 6: support check: partial - The article tells the owner to contact the installer for further investigation, but it does not condition this on the cause being unclear.
-->
