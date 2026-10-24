---
id: arch:dc-optimized-system
type: Architecture
name: DC-optimized system
aliases:
- power optimizer system
- DC optimized architecture
- optimizers with string inverter
- DC-optimized inverters
category: System topology
claims:
- claim_id: c1
  rel: subclass_of
  target: arch:module-level-power-electronics
  note: Module optimizers are given as an example of module-level power electronics (MLPE).
  cite:
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h7
    h: 38424fe4bca1
  review: drafted
  review_note: 'support check: partial - The passage says module optimizers are an example of MLPE, but
    it doesn''t say a DC-optimized system is a kind of MLPE.; review: partial - The passage names module
    optimizers as an example of MLPE, which supports the note, but it never mentions a DC-optimized system
    or classifies one as a kind of MLPE.'
---
A DC-optimized system places a power optimizer on each PV module and feeds the optimized strings to an inverter, combining elements of the string and microinverter topologies. Each optimizer sits next to or is attached to its module and runs its own MPPT loop and DC-to-DC conversion, so the module's voltage and current are decoupled from the optimizer output. Because each panel works independently, one shaded or dirty panel does not pull the whole string down to its level, as happens in a plain string system. The optimizers also provide module-level monitoring and safety functions; when shut down, each optimizer puts out only about 1 V, so the string wiring to the inverter is de-energized. Module-level data with mapped module locations often allows remote troubleshooting comparable to on-site I-V sweeps. If the measured string voltage is above zero but lower than the number of optimizers in the string, one or more optimizers are not connected.

<!-- review notes
- sentence 6: support check: partial - The passages give 'optimizer(s) not connected in the string' as a possible cause, not a definite conclusion, so the statement is stronger than the evidence.
-->
