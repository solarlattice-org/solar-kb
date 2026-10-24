---
id: arch:high-leg-delta-240v
type: Architecture
name: 240 V high-leg delta service
aliases:
- high-leg delta
- stinger leg
- 240/120 V delta
- Hi-Leg Delta
- Delta Hi Leg
- Stinger leg AC Grid
- Three phase high leg delta
- 240V High-leg Delta
category: Grid service
---
High-leg delta is an older service type, found mainly in rural areas. It was a cheap way to deliver 240 V three-phase plus 240 V or 120 V single-phase from one pole-mounted transformer. On the Solis S6-GC-30K-LV-US, the high side goes on the L2 or B phase. That phase is shown with the larger conductor at the AC input. The Solis S6-GC-30K-LV-US can connect to a 240 V high-leg delta service. First update it to HMI software C701 and DSP software 5906, then select the UL-240L grid standard. The Fronius Symo and Symo Advanced 10.0-3 and 12.0-3 208-240 models have a Hi-Leg Delta setup (HI1). A neutral conductor is required. Enphase IQ commercial microinverters cannot connect directly to a 240 V high-leg delta service. They need a transformer with a 208/120 V wye secondary, chosen by the installer according to the NEC and local code. Eaton makes 120/240 V high-leg delta surge protective devices with their own wiring diagram. Their protection modes include high leg to neutral, high leg to ground and high leg to line.

<!-- review notes
- sentence 5: support check: partial - Passage gives 208/120 V wye secondary and installer-selected transformer per NEC/local code, but does not explicitly say direct connection is impossible or name IQ commercial microinverters.
-->
