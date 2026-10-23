---
id: mit:ntp-configuration-check
type: Mitigation
name: Time server configuration check
---
This check is the corrective action for SMA event 10110, Time synchronization failed, which is raised when the inverter cannot get time information from the NTP server it has been set to use. Start by confirming that the NTP server is set up correctly in the inverter configuration. Next, make sure the inverter is connected to a local network that has Internet access. On networks without a DHCP server, every device has to be given a valid IP address from the free address pool when the system is commissioned. Some sites cannot keep permanent access to a public NTP server, for example sites reached through a jump server. These sites need an NTP server on the local network. Behind a firewall, pointing the device at a local NTP server is usually easier than routing time traffic through the firewall. NTP uses UDP port 123. How accurate SNTP time is depends on the server and the network. Fewer switches and routers between the server and the device give better synchronization.
