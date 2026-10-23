---
id: symptom:internal-communication-failure
type: Symptom
name: Internal communication failure
aliases:
- CommErr
- Communication failure
- Internal Communication 1 Failure
- Internal Communication 2 Failure
---
This symptom is an inverter alarm saying that communication inside the inverter has failed. It is shown on the inverter display or in the event log. On CPS SCA inverters it appears as the CommErr alarm. The listed cause is poor contact at the terminal block connectors of the internal communication wires. On SMA STP-US inverters, event 6702 points to an error in the communication processor. The inverter keeps feeding in power, so production data may look normal. On CPS units, first wait 5 minutes to see if the alarm clears by itself. If it does not, switch the external AC disconnect off and back on to reboot. If the alarm stays, or comes back often, contact the manufacturer's service team, because they must find the cause.

<!-- review notes
- sentence 1: support check: partial - Passages show internal communication failure alarms/critical events, but 'shown on the inverter display or in the event log' is only loosely implied (Display Message appears in u2/u3, event log not stated).
- sentence 3: support check: partial - Event 6702 communication processor error and continued feed-in are stated, but 'production data may look normal' is an inference not in the passage.
-->
