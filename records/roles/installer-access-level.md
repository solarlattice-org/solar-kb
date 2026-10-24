---
id: role:installer-access-level
type: Role
name: Installer access level
aliases:
- installer password
- installer login
- installer user group
- Installer level
- user group Installer
category: Access levels
role_kind: access-level
---
On SMA devices the Installer access level is unlocked by logging in with the installer password, and on some central inverters it drops back after 15 minutes. To log in on the web interface, choose Installer in the User group list, type the password and select Login; the Sunny Tripower CORE2 ships with a standard installer password of pw1111. Both the Installer and User passwords are set the first time the user interface is opened, and when the inverter is registered in a system manager such as the SMA Data Manager, the system password serves as the installer password. Use one installer password on all SMA devices in a system so that registration in the Data Manager or Sunny Portal succeeds; the installer password itself can only be changed from within the Installer group. On the Sunny Island off-grid inverter, parameters that affect operating safety are locked behind the installer level, only trained electrically qualified persons should change them, and the password is the digit sum of the operating hours entered in menu 280# Password Setting. The fallback behaviour for an external active power setpoint can be read and written at Installer level, while the superordinate fallback in the LCS-Tool also needs the SMA Grid Guard code under the Installer group. On the SMA Data Manager M, the Installer group, like the Administrator group, may activate service access, but the User group may not. Parameters for the power-generating unit protection test on Sunny Central UP units require the installer password, which is changed at first installation and can be obtained from the PV system operator.

<!-- review notes
- sentence 1: support check: partial - Installer password activates the level and it resets after 15 minutes, but the passage doesn't say 'on some central inverters' or restrict it to SMA devices generally.
- sentence 8: support check: partial - The passage covers the installer password being needed, changed at initial installation and obtainable from the operator, but doesn't mention Sunny Central UP specifically.
- sentence 1: review: partial - The passage says the installer password activates the Installer level and that the level resets after 15 minutes, but it does not limit the reset to 'some central inverters' or extend the statement to SMA devices in general.
-->
