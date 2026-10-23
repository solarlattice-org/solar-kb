---
id: symptom:generator-locked-error
type: Symptom
name: Generator management locked
aliases:
- Fail-Lock
- FailLock
---
On SMA Sunny Island inverters, display message W402 is a level 1 warning that generator management has entered its locked error status, called Fail-Lock. To confirm it, read the generator state parameter: FailLock (12) means locked after an error, which is a different value from Lock (10). The neighbouring warning W401 is reverse power protection for the generator, so check which of the two codes is actually shown. When generator management detects a generator failure on the master phase, it disconnects the generator at once, sends it a stop signal and enters a minimum stop time. A start can also be aborted if the warm-up time is set too short, because some generators only put voltage on their output after their own internal warm-up has finished. The manual sets the abort limit at double the warm-up time plus 2 minutes, so check the warm-up setting against how the generator actually behaves. Also check the generator interface setting (for example the SMA generator management box) and the current and voltage thresholds for generator connection in the generator management menu.

<!-- review notes
- sentence 7: support check: partial - Generator interface (GenMan, SMA generator management box) and current/voltage thresholds sections exist, but nothing in the passages ties them as checks for this W402 problem, and the thresholds being in the generator management menu is only implied by section 7.8.
-->
