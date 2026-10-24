---
id: proto:semp
type: Protocol
name: SEMP
aliases:
- Simple Energy Management Protocol
category: Communication
protocol_kind: application
---
SEMP is an application-level communication protocol that SMA uses to bring household loads into its Smart Home energy management with the Sunny Home Manager 2.0. SMA groups SEMP with EEBus as a communication protocol, separate from communication standards such as Wi-Fi and ZigBee that carry the data. The list names Stiebel and Tecalor heat pumps, the AC ELWA-E, AC ELWA 2, AC•Thor and AC•Thor 9s heating devices, and Mennekes AMTRON wallboxes. Some AMTRON models need a minimum firmware version, such as 5.22 or 1.3.45. Miele appliances in Miele@home do not use SEMP. The Sunny Home Manager talks to them over Miele's own Homebus protocol instead. SMA does not expect to add more SEMP devices, because EEBus, which covers the same functions, is becoming the industry standard. The SEMP protocol description is available to integrators on the SMA Developer page, under on-site integration.

<!-- review notes
- sentence 1: support check: partial - Passages show SEMP is a protocol for integrating devices into SMA Smart Home/Sunny Home Manager 2.0 energy management, but don't say it is 'application-level' or specifically about household loads in those words (loads are implied by related titles).
- sentence 2: support check: partial - Only a related-article title is shown, which contrasts communication standards (Wi-Fi, ZigBee, radio) with protocols (EEBus, SEMP, Mo…), but it is truncated and doesn't say the standards 'carry the data'.
-->
