---
id: mit:ntp-configuration-check
type: Mitigation
name: Time server configuration check
---
Use this check when the SMA Sunny Tripower CORE1-US inverter logs event 10110, which means time synchronization failed because the inverter could not get time information from its configured NTP server. First, confirm that the NTP server address is set up correctly in the inverter. Next, confirm that the inverter is connected to a local network that has Internet access. Correct time matters because site controllers need an external time source to put correct timestamps on logged data. If the site cannot give permanent access to a public NTP server, for example where remote access goes through a jump server, put an NTP server on the local network instead. If the devices sit behind a firewall, the simplest approach is usually to point them at a local NTP server rather than routing time traffic through the firewall. NTP uses UDP port 123. The check has limits: sync accuracy depends on the accuracy of the time server and on the network, and it improves when there are fewer switches and routers between the server and the device.

<!-- review notes
- sentence 4: support check: partial - The passage says the Tesla System Controller needs an external time source to timestamp logged data correctly; it does not state this for site controllers in general.
- sentence 4: review: partial - The passage says the Tesla System Controller needs an external time source to timestamp logged data correctly, not site controllers in general.
-->
