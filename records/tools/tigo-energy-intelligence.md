---
id: tool:tigo-energy-intelligence
type: Tool
name: Tigo Energy Intelligence
aliases:
- Tigo EI
- Tigo platform
category: Platforms
tool_kind: platform
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:tigo
  note: The Solis manual calls Tigo Energy Intelligence Tigo's own platform for module-level monitoring.
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: sec=5.8.4
    h: ee2d3504a624
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - The passage names Tigo Energy Intelligence as Tigo''s platform,
    but it doesn''t say Tigo Energy (org:tigo) makes it. That is only implied by ''Tigo''s platform''.'
---
Tigo Energy Intelligence is Tigo's cloud monitoring platform. You need it to see module-level data from Tigo optimizers. On a Solis hybrid inverter with a Tigo CCA, the inverter and the CCA do not talk to each other. Tigo and Solis monitoring can run side by side, but Solis data does not show up in Tigo Energy Intelligence, and Tigo data does not show up in SolisCloud on its own. SolisCloud can show Tigo optimizer data by pulling it from the Tigo platform through an API. To do this, the plant must already exist on both platforms. You need a Tigo Premium account for the SolisCloud link, because only premium users get API access. To link them, go to Optimizer Access in SolisCloud and enter your Tigo account username and password. Then pick the plant you created on the Tigo platform so the right optimizers are imported. Finally, assign each optimizer to its PV module in the physical layout. Solis does not support Tigo optimizers, so take optimizer problems to Tigo directly.

<!-- review notes
- sentence 1: support check: partial - The passage says module-level monitoring needs Tigo's platform, which is Tigo Energy Intelligence. It doesn't say 'cloud' explicitly, and it doesn't say this applies to data from Tigo optimizers generally.
- sentence 1: review: partial - Passage says Tigo's platform (Tigo Energy Intelligence) must be used for module-level monitoring, but does not explicitly describe it as a cloud platform.
-->
