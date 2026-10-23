---
id: meas:incorrect-login-rights-event
type: Measurement
name: Incorrect login rights event
aliases:
- Event 7349
---
This signature is an inverter event log entry saying that the login rights are incorrect for a configuration file. SMA lists it as event number 7349. It is logged when someone tries to import a configuration while signed in under a user group that does not have the rights needed for an import. It points to insufficient user rights. It does not point to a hardware or PV array fault. To clear it, log in with the Installer user group and import the configuration file again. Do not confuse it with the separate login-lock event. That event is logged after several wrong login attempts and blocks login for a limited time.

<!-- review notes
- sentence 4: support check: partial - Insufficient user rights is stated, but nothing in the passages says it is not a hardware or PV array fault (only implied).
- sentence 4: review: partial - The passages state that the logged-in user group lacks the rights to import, but they never say it does not point to a hardware or PV array fault.
-->
