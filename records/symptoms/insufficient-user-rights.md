---
id: symptom:insufficient-user-rights
type: Symptom
name: Insufficient user rights
aliases:
- Incorrect login rights
claims:
- claim_id: c1
  rel: observed_as
  target: meas:incorrect-login-rights-event
  note: SMA event 7349 is logged when the user group that is logged in tries to import a configuration
    file without the rights to do so. The fix is to log in as Installer and import the file again.
  quote: Incorrect login rights for configuration file
  cite:
  - src: src:kb-sma-shpxxxus21-event-messages
    loc: sec=h26
    h: 479d42d580b7
  - src: src:sma-doc-259761
    loc: tbl=67.r5
    h: 9d90d13712cb
  - src: src:sma-doc-278742
    loc: tbl=72.r5
    h: 9d90d13712cb
  review: drafted
---
This symptom shows up as SMA event 7349. It appears when someone tries to import a configuration file while logged in to a user group that does not have the rights to import one. The fix is to log in as Installer and then import the configuration file again. Guest and Standard user roles cannot import data. The Installer and System administrator roles can. The user rights decide which functions a user can reach in a system. A function the user is not allowed to use may simply not be shown, so a missing menu item can point to the same cause. In Sunny Portal, the account that registered the system gets administrator rights. Only the administrator can view user management and set user rights. Even with Installer rights, changing SMA Grid Guard parameters also needs the SMA Grid Guard code. So check which role you are logged in with, and whether a code is needed, before suspecting a device fault.

<!-- review notes
- sentence 4: support check: partial - Passage says user rights determine available functions and functions may not be shown due to missing authorization; the 'missing menu item can point to the same cause' link to the earlier issue is inference but the core is stated.
- sentence 5: support check: partial - Registering account getting administrator rights is stated, and View user management is admin-only, but 'only the administrator can set user rights' is only partly shown (configuring user rights ✓ for administrator, '-' for others, which isn't explicit prohibition).
- sentence 6: support check: partial - Installer changing Grid Guard parameters only with the Grid Guard code is stated, but the advice to check role/code before suspecting a device fault is not in the passage.
-->
