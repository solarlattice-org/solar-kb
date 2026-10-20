---
id: symptom:configuration-error
type: Symptom
name: Configuration error
aliases:
- CONF REV MISMA
- Configuration Revision mismatch
claims:
- claim_id: c1
  rel: observed_as
  target: meas:no-dhcp-message
  note: SolarEdge commercial three-phase inverter shows 'No DHCP' for an IP settings issue; check the
    router and configuration with network IT.
  cite:
  - src: src:solaredge-se-commercial-3ph-inverter-w-synergy-tech-installation-guide-pn-sexxk
    loc: tbl=10.r2
    h: b92c8f7c38c1
  review: drafted
  review_note: 'support check: partial - The passage gives ''No DHCP'' as an IP settings issue with check
    router/configuration and consult network IT, but doesn''t say it''s a SolarEdge commercial three-phase
    inverter or classify it as a configuration error.'
---
A configuration error appears as a status or error message on the device or in the monitoring platform. It is not a physical defect of the PV array. Some meter data includes a counter that starts at zero and goes up each time the configuration changes, so you can use it to check whether the setup was changed. On a SolarEdge commercial inverter, a 'No DHCP' message points to a problem with the IP settings. Check the router and the network configuration, and talk to the site's network IT staff. In the PowerTrack monitoring platform, the Rule Tool has a configuration check. It confirms that the site generates alerts and that at least one person is set up to receive alert notifications. Be careful when editing device driver settings at a live site: changing the data name of a register makes the archived data for that address get lost.

<!-- review notes
- sentence 1: support check: partial - Passages show configuration messages/errors on devices or platforms, but nothing states that they are not physical defects of the PV array or describes this general characterization.
- sentence 3: support check: partial - The IP settings issue, router/configuration check and network IT advice are stated, but the passage doesn't name SolarEdge commercial inverter.
- sentence 4: support check: partial - The Rule Tool configuration/Alert Recipients check is stated, but the passage doesn't name PowerTrack and says to make sure rather than that it confirms automatically.
-->
