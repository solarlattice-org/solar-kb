---
id: concept:grid-following-inverter
type: Concept
name: Grid-following inverter
aliases:
- grid-following
- current source mode
- grid-tied mode
- grid-tied
- grid-interactive
- utility-interactive
- Interactive Mode
- on-grid
- Grid-Following mode
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:grid-forming-inverter
  note: 'Grid-forming is the alternative mode: the system acts as a standalone voltage-frequency source
    instead of needing an external one.'
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: sec=2.4.2
    h: 46138d6d5564
  review: drafted
- claim_id: c2
  rel: related_to
  target: arch:grid-tied-pv
  note: In a grid-tied PV system the inverter turns PV DC into AC matching the grid's frequency and phase,
    serves local loads and exports any surplus.
  cite:
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=1.1
    h: f9e7a43d5f54
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: sec=2.1
    h: e07a4b96b306
  - src: src:eq-equip-inverters-chint-100-125-kw-inverter-cps-sch100-125ktl-do-us-600-480-manual-aug-2021-1
    loc: sec=2.1
    h: ce68a960151d
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:mppt
  note: While feeding the grid, grid-tied PV inverters keep the array at its maximum power point.
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h194
    h: 8888040dfeec
  - src: src:eq-equip-inverters-yaskawa-pvi-50-60tl-installation-operation-manual
    loc: sec=5.4
    h: 0ff98e7345a2
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=5.4
    h: 13dbd37919ff
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c4
  rel: related_to
  target: func:dynamic-voltage-support
  scope:
    products:
    - prod:tesla-megapack-2-xl
  note: In grid-following mode the inverters do not support voltage on their own. Reactive current injection
    at the inverter can be turned on for low-voltage events if interconnection rules require it.
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: sec=2.1.1
    h: 88ff51d41440
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:transformer-winding-configuration
  scope:
    products:
    - prod:tesla-megapack-2-xl
    - prod:tesla-megapack-2
  note: For on-grid grid-following use, the transformer side facing Megapack must be wye-grounded. The
    other side may be delta or wye, and the utility transformer may provide the solidly grounded circuit.
  cite:
  - src: src:tesla-megapack-2-xl-design-and-installation-manual
    loc: sec=2.4.4
    h: 00cff5dab44a
  - src: src:tesla-tesla-mp2-design-and-installation-manual-v3-0
    loc: sec=2.4.3
    h: e6d480a0f54a
  review: drafted
  review_note: 'support check: partial - Wye-grounded Megapack side, delta or wye other side, and utility-provided
    grounding are stated, but the passages do not name Megapack 2 vs 2 XL explicitly (only Megapack).'
- claim_id: c6
  rel: related_to
  target: state:standby
  note: If PV power in low light is too weak to keep grid-tied generation going, the inverter drops to
    standby. It tries again once array voltage is stable and above the start value.
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h194
    h: 8888040dfeec
  - src: src:eq-equip-inverters-yaskawa-pvi-50-60tl-installation-operation-manual
    loc: sec=5.4
    h: 0ff98e7345a2
  - src: src:yaskawa-solectria-pvi-36tl
    loc: sec=5.4
    h: 13dbd37919ff
  review: drafted
---
A grid-following inverter needs an external voltage source, normally the utility grid, before it can run and produce power. It follows the grid voltage and frequency it measures and changes its output current waveform and amplitude to deliver the real and reactive power it is asked for. A typical grid-tied PV inverter turns DC from the modules into AC at the grid's frequency and phase, supplies local loads and exports the surplus. It keeps checking the grid and the PV array, and it enters its protection routine as soon as the grid becomes abnormal. When the external voltage is lost, a grid-following battery system trips or goes into a faulted state on its own. In this mode the inverters give no independent voltage or frequency support. A plant controller can calculate power commands from metered voltage and frequency, and reactive current injection for low-voltage events can be turned on if required. The NEC calls this an interactive inverter: it runs in parallel with the utility and can deliver power to it. It is also called grid-tied, grid-interactive or utility-interactive. The opposite approach is the grid-forming inverter, which acts as a standalone voltage and frequency source.

<!-- review notes
- sentence 1: support check: partial - Requirement of an external voltage source is stated, but 'normally the utility grid' is not stated in the passages.
- sentence 7: support check: partial - Definition from NEC with the alternative names is given, but the term is 'Interactive Mode' inverter; the wording matches mostly, though equating it to grid-following is implied rather than stated.
- sentence 1: review: partial - The Tesla passages say grid-following mode needs an external voltage source to operate and produce power, but 'normally the utility grid' is not stated and the passages describe a battery system rather than inverters in general.
-->
