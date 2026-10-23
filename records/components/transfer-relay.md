---
id: comp:transfer-relay
type: Component
name: Transfer relay
aliases:
- Internal transfer relay
---
The transfer relay is a relay built into SMA Sunny Island battery inverters, and the event log reports whether it is open or closed. In multi-unit clusters, each slave unit has its own transfer relay with separate open and closed event messages for slave 1, slave 2 and slave 3. These open and closed events are status messages. They are not faults on their own. The main failure mode is a transfer relay that will not open. On the master unit this is reported as a level 4 fault (F605). If a slave unit's transfer relay will not open, the unit logs a level 1 warning (W606, W607 or W608, one for each slave). The transfer relay is a different part from the Sunny Island multifunction relays, which have their own activation events and functions, such as requesting PV arrays.

<!-- review notes
- sentence 1: support check: partial - Passages show event messages for the internal transfer relay being open or closed, but nothing says it is built into SMA Sunny Island inverters, though that is implied by context.
- sentence 3: support check: partial - The passages list the open/closed events as E-number event messages, but none of them says they are status messages or not faults.
- sentence 4: support check: partial - F605 is level 4 'Transfer relay does not open', but the passages don't say it is the main failure mode or that it applies to the master unit.
-->
