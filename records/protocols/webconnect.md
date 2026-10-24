---
id: proto:webconnect
type: Protocol
name: SMA Webconnect
aliases:
- Webconnect
- Speedwire/Webconnect
- Webconnect function
- SMA Webconnect function
- Webconnect 1.0
- Webconnect 1.5
category: Communication
protocol_kind: application
---
SMA Webconnect is an application-level function that sends data straight from SMA inverters to the Sunny Portal, and in some manuals Sunny Places, through a router with internet access. No separate communication device is needed. One Sunny Portal system can hold up to four Webconnect devices, and only one of them may be a Sunny Boy Smart Energy. Larger plants need extra Sunny Portal systems or a data logger such as the SMA Cluster Controller or SMA Data Manager. Webconnect 1.0 uses SIP to set up, run and end encrypted sessions between authenticated nodes. Webconnect 1.5 talks TCP/IP to a cloud server, which converts the traffic to SIP for Sunny Portal. For Webconnect 1.0, the network must pass SIP and STUN traffic and must not filter SIP packets. Switches between SMA devices must support IGMP v3 multicast, IGMP snooping should be turned off, and outgoing UDP ports above 1024 must be open. For Webconnect 1.5 on a company network, allow outgoing TCP traffic to wco.sunnyportal.com on port 9524. Webconnect comes built in on products such as the Sunny Boy Storage, the Sunny Tripower CORE1 and the SB 240 with Sunny Multigate. Older inverters can be retrofitted with a Speedwire/Webconnect data module or piggy-back. To register a device in Sunny Portal, you enter its PIC and RID in the Plant Setup Assistant.

<!-- review notes
- sentence 6: support check: partial - Sunny Boy Storage standard Webconnect and retrofit via SWDM/piggyback are supported, and SB 240 with Multigate is listed, but Sunny Tripower CORE1 isn't mentioned and SB 240 isn't stated as built-in.
- sentence 1: review: partial - The passages support direct data transmission to Sunny Portal (and Sunny Places in some manuals) through a router with internet access and without an extra communication device, but they never call Webconnect an 'application-level' function.
-->
