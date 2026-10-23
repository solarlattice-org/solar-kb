---
id: comp:mv-transformer
type: Component
name: Medium voltage transformer
aliases:
- MV transformer
- Transformer
---
The medium voltage transformer steps up the low voltage AC output of the inverter units to medium voltage AC for the grid connection. Inverter manuals set requirements for the transformer, and system designers must select a suitable one; for some smaller inverters it may not be strictly required, depending on local standards and connection conditions. For the Conext CL125, the transformer secondary must be rated 600 VAC line-to-line, with an allowed range of 480 to 690 VAC, and the primary voltage must match the grid connection point. On the Sunny Central CP XT, error 6440 reports that the transformer is no longer hermetically sealed, and the corrective action is to check the transformer. Service manuals give procedures for disconnecting and reconnecting the transformer during maintenance. Distribution transformers are factory tested to ANSI C57.12.00 and C57.12.90. These tests include polarity, ratio, losses, impedance, impulse, dielectric and mechanical leak tests. ANSI C57.12.00 also gives guidance on operating these transformers under different service conditions.

<!-- review notes
- sentence 2: support check: partial - Passages say a suitable transformer is needed, designers choose it, and the SHP 100-21 may not need one; they don't say inverter manuals generally set requirements, and 'some smaller inverters' is broader than the one model named.
- sentence 7: support check: partial - Passage refers to 'ANSI C57.12.00.4' for detailed information on operation in different service conditions, which is not exactly C57.12.00, so the attribution is only loosely supported.
- sentence 7: review: partial - The passage points to 'ANSI C57.12.00.4' for operation in different service conditions, so pinning the guidance on C57.12.00 is only loosely supported.
-->
