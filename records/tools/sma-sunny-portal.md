---
id: tool:sma-sunny-portal
type: Tool
name: SMA Sunny Portal
aliases:
- Sunny Portal
- Sunny Portal Classic
- Sunny Portal powered by ennexOS
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  note: Referred to as the SMA Sunny Portal, through which SMA Smart Connected monitoring is provided.
  cite:
  - src: src:sma-doc-sunnyportalennexos-ba-en-16
    loc: sec=h32
    h: 076ca61687cd
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h85
    h: a7a5051716e8
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Sunny Portal is SMA's internet portal for monitoring and configuring PV systems and for visualizing and presenting system data. It only works with an SMA product that records system data and sends it to the portal, and the functions you get depend on that product. There are two versions with different features: Sunny Portal Classic works with the SMA Cluster Controller and Sunny Home Manager 2.0, while Sunny Portal powered by ennexOS works with the SMA Data Manager M. Sunny Portal is the user interface for configuring the Sunny Home Manager and its loads, and you can check the Home Manager firmware version under Configuration > Device Overview. You must log in as an installer to set up forecast-based battery charging in the portal, and the setup needs the system location, string configuration, tariffs and active power limitation entered correctly. If Tigo optimizers are integrated into the Sunny Portal system over communication, forecast-based charging cannot be used. SMA Smart Connected is switched on during registration and sends automatic event notices to the operator and the qualified person, but only if the product stays connected to the portal and the inverters support the feature. The portal can also watch Cluster Controller communication and send an e-mail alert when the expected signal does not arrive.

<!-- review notes
- sentence 2: support check: partial - Passages say you need an SMA product that sends data and functions depend on the product, but 'only works with' is stated as a requirement, roughly fine; some nuance (e.g. Cluster Controller example) is omitted, though core holds.
-->
