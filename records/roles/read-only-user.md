---
id: role:read-only-user
type: Role
name: Read-only user
aliases:
- guest user
- read-only access
- Guest
- Read-Only users
- Viewer
- Account Watcher
category: Access levels
role_kind: access-level
---
A read-only user can see monitoring and device data but cannot change settings or configuration. In AlsoEnergy PowerTrack, the Guest role can view portfolios, sites, hardware, folders and files. It cannot modify settings or add notes. For alerts, read-only users can see the acknowledgement state and the alert history. They cannot change an acknowledgement or add comments. In the SolarEdge Monitoring Platform, the Account Watcher role has read-only access to every feature, including the Admin tab of sites. The Account Sites Viewer role sees only the dashboard, layout, site details and account details, without the Admin tab. On the SolarEdge platform, the Account Admin assigns or changes a user's role from the Users tab of the account. This is the only role that can add, remove or update users. In SMA user management, a Guest can view pages and view or change their own user information. A Guest cannot view user management, read out device properties or import data. On SMA devices, the User group can read displayed values and parameter settings but cannot change settings that affect how the device works. Changing those settings needs the Installer group. On Eaton SPD devices, the Viewer and Operator roles can read the IP address and Modbus timeout but cannot write them. Factory reset, reboot and user/password changes are reserved for the Admin role.

<!-- review notes
- sentence 5: support check: partial - Account Admin being the only role that can add/remove/update users is stated, and the Users tab is the location, but the passage doesn't explicitly say the Admin assigns roles there, though it is implied.
- sentence 8: support check: partial - The table shows Viewer and Operator are read-only on IP and Modbus timeout, and only Admin has User/Pass, Factory Reset and Reboot, but nothing in the passage mentions 'SPD' devices specifically.
-->
