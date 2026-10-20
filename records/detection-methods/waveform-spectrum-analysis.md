---
id: method:waveform-spectrum-analysis
type: DetectionMethod
name: Waveform spectrum analysis
---
Waveform spectrum analysis looks at the frequency content of a PV system's current and voltage waveforms. It is one of the current ways to identify DC arc faults. A DC arc fault is a sudden high-power discharge between two conductors. It can occur in series between neighbouring conductors in a string, or in parallel between strings, and it often causes destructive fires. Arcs are transient by nature, so they are hard to catch. Analysing the waveforms is one way to find them. Power quality meters with an oscilloscope-like tool can capture voltage and current waveforms. They show both the time trace and the frequency spectrum, in magnitude, percent or dB. On one such tool, you sample at 128 or 512 samples per cycle and record for 2 to 60 cycles. You need at least 12 cycles to get 5 Hz bin resolution. Captured waveforms can be exported to CSV and imported again later for review. A signal that points to a fault under some conditions can be normal under others, such as clouds instead of full sun. Compare a suspect signature with past behaviour under similar conditions. Detection alone does not protect the system. Arc fault circuit interrupters installed on individual strings provide the protection against arc faults.

<!-- review notes
- sentence 2: support check: partial - Sudden high-power discharge, series/parallel occurrence and destructive fires are stated, but 'usually causing' fires is fair while 'between strings' and 'neighbouring conductors' match; minor softening is fine, though 'often' vs 'usually' is the only drift, so core is supported yet slightly weaker.
- sentence 3: support check: partial - Transient nature and difficult detection are stated, and waveform spectrum analysis is listed as a method, but 'analysing the waveforms' is a looser paraphrase of spectrum analysis.
- sentence 8: support check: partial - Passage says AFCIs on individual strings can protect against arc faults, but does not say detection alone is insufficient or that AFCIs are the protection.
-->
