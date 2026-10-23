---
id: symptom:license-expiring
type: Symptom
name: Feature license expiring
aliases:
- License Expired
claims:
- claim_id: c1
  rel: observed_as
  target: meas:license-status-reading
  note: The license management screen (Function Menu > Maintenance > License management) shows the license
    status as Normal, Deregistered or No license.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=h161
    h: a02978d674fe
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=h163
    h: 6f4f56ea47ed
  review: drafted
  review_note: 'support check: partial - Passages list statuses Normal, Deregistered, No license on that
    screen, but don''t say an expiring feature license is observed as this reading (expiry isn''t a listed
    status).'
---
The inverter raises a warning-level alarm saying the license has expired. This happens when the privilege certificate has entered its grace period and a licensed feature will soon stop working. It is a licensing and configuration matter, not a hardware or PV array fault, and the manual lists no production effect for it. Check the license status in the app under Function Menu, Maintenance, License management. The status will read Normal, Deregistered or No license. To clear it, apply for a new certificate and load it into the inverter from the license management screen. If the inverter is being replaced, revoke the current license first. This generates a revocation code, which is needed to apply for a license for the new device. Monitoring portals can have their own licenses as well. For example, when a portal license expires, a notice appears at sign-in and directs the user to renew it.

<!-- review notes
- sentence 2: support check: partial - The row lists no production effect and is a license matter, but the 'not a hardware or PV array fault' characterization is an inference not stated.
- sentence 4: support check: partial - Measures say apply for and load a new certificate; the license management screen has a load function for No license status, but loading the certificate from that screen for this alarm is not explicitly stated.
- sentence 6: support check: partial - The passage says a notification appears at sign-in and redirects to SolrenPay to renew the RAP license, but 'monitoring portals can have their own licenses' generally is only exemplified by one portal; the core is stated.
-->
