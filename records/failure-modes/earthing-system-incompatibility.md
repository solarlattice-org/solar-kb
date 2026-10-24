---
id: fm:earthing-system-incompatibility
type: FailureMode
name: Grid earthing system incompatibility
aliases:
- TN-C connection
- IT grid
- IT network not supported
- Delta IT utility grid
- improper PE connection
- TT grid
- touch voltage on enclosure
- grid configuration
- TN-C system
- IT not supported
- delta IT networks
- earthing system compatibility
- corner grounded Delta
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  note: Each inverter model supports only certain grid earthing systems or grid configurations; for example
    some hybrid models do not support IT grids, and TN-C is not recommended for them.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: tbl=1
    h: 24362010cc2f
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h11
    h: 638e47cbf091
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: sec=h87
    h: 1a9a178d6ef0
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:enclosure-touch-voltage
  note: On TN-C systems, a large load imbalance can put a touch voltage on the inverter enclosure under
    some operating conditions.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h11
    h: 638e47cbf091
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:installation-error
  note: Connecting the inverter to a grid topology or earthing system the model does not support. On one
    product line, delta grids other than the supported one may damage the inverter and void the warranty.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h14
    h: a99e703fbd5d
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: sec=h87
    h: 1a9a178d6ef0
  review: drafted
  review_note: 'support check: partial - The delta-grid damage and warranty caution is stated, but nothing
    explicitly names installation error as the cause. Only best practices that imply it are given.'
- claim_id: c4
  rel: caused_by
  target: stressor:line-to-ground-fault
  note: On a 480 V delta service, co-located loads that cause recurring line-to-ground faults effectively
    turn it into a corner-grounded delta grid, which exposes the inverters to excessive line-to-ground
    voltage.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h110
    h: 347cabe51550
  review: drafted
  review_note: 'support check: partial - u25 describes recurring line-to-ground faults on 480 V delta
    giving an effective corner-grounded delta and excessive line-to-ground voltage. It does not say this
    is an earthing incompatibility, and it prescribes isolating the PV system from the fault source.'
- claim_id: c5
  rel: mitigated_by
  target: mit:earthing-system-verification
  note: Check the site earthing system and confirm it is compatible with the inverter model before installing.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h14
    h: a99e703fbd5d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:tn-c-s-conversion
  note: Where possible, convert a TN-C installation to TN-C-S before connecting the inverter.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h11
    h: 638e47cbf091
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-settings-review
  note: If a TN-C connection cannot be avoided, the unbalanced output function must stay disabled.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h11
    h: 638e47cbf091
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:phase-load-balancing
  note: On three-phase systems, balance loads across all phases. If there is no neutral conductor, do
    not connect loads to a neutral terminal.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h13
    h: 10802b4ec3ae
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact the manufacturer when the site topology or transformer configuration is outside the supported
    standard configurations.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h14
    h: a99e703fbd5d
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=h37
    h: a2433cb3d772
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: sec=h29
    h: 853ef8d607e3
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:utility-consultation
  note: Get the exact connection specifications from the electric utility; local regulations and distribution
    system operator requirements take priority.
  cite:
  - src: src:sma-doc-243910
    loc: sec=h35
    h: 14372b068de8
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h2
    h: bf11df3c0f94
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:proper-installation
  note: A qualified electrician should do the work, following local regulations and the model-specific
    installation manual. Earthing arrangements should never be changed without approval.
  cite:
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h14
    h: a99e703fbd5d
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h2
    h: bf11df3c0f94
  - src: src:kb-solis-44002860963-solis-inverters-and-grid-earthing-systems-general-connection-guidance
    loc: sec=h11
    h: 638e47cbf091
  review: drafted
---
This failure happens when an inverter is connected to a grid earthing system or grid configuration that the model does not support, such as an IT grid on a model without IT support, or a delta grid other than the one specified. Support depends on the model. Some hybrid models do not support IT networks and are not recommended for TN-C, while some commercial and utility models support all major earthing systems. On a TN-C system with a large load imbalance, a touch voltage can appear on the inverter enclosure. Connecting to an unsupported delta grid can damage the inverter. Before installing, verify the site earthing system and confirm it is compatible with the inverter model, using the manufacturer compatibility table and the installation manual. If TN-C cannot be avoided, keep the unbalanced output function disabled. Where possible, convert the installation to TN-C-S before connecting the inverter. Balance loads across the phases, and do not use a neutral terminal for loads when there is no neutral conductor. For non-standard topologies, contact the manufacturer and the utility. Never change earthing arrangements without approval from the electrical authority or a qualified engineer.

<!-- review notes
- sentence 7: support check: partial - The passages support contacting the manufacturer for non-standard topologies and never changing earthing without approval. Contacting the utility is only for exact connection specifications, not specifically for non-standard topologies.
-->
