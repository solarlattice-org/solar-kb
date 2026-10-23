---
id: comp:internal-communication-cable
type: Component
name: Internal communication cable
aliases:
- Internal communication wires
- Internal communication cabling
- Data cable
---
The internal communication cable carries data between devices or boards so they can coordinate operation. In a Sunny Island cluster, for example, the inverters talk to each other over a dedicated data cable. In a Sunny Island cluster the cable is daisy-chained between the ComSync Out and ComSync In terminals, running from the master to slave 1 and then to slave 2. The last device in the chain is connected to only one neighbour, and its terminator stays plugged in. Poor contact at the terminal block connectors of the internal communication wires is listed as a possible cause of communication errors.

<!-- review notes
- sentence 1: review: partial - The passages show Sunny Island cluster inverters communicating over a data cable, but the general claim that it carries data 'between devices or boards' so they can coordinate operation is not stated.
-->
