---
id: meas:performance-ratio-decline
type: Measurement
name: Declining performance ratio
aliases:
- PR
- Ref_PR
signals:
- point: model_103.W
  unit: unit:W
  pattern: irradiance-normalized output gradually falls during dry periods and recovers after rain or
    cleaning
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: reference irradiance for the normalization
- point: model_307.Rain
  unit: unit:MilliM
  pattern: rain events that line up with recovery steps
---
The performance ratio divides the specific (final) yield by the reference yield. That means AC energy is normalised to the plant's peak DC power and to the measured plane-of-array insolation. Because PR combines all plant losses (modules, inverters, transformers, cabling and downtime), a falling PR shows that the plant converts the available sunlight less well. It does not show which part is at fault. Tracking PR over a long period lets the operator check output and see seasonal swings and long-term degradation. Losses that can lower PR include soiling, module mismatch, cabling, MPPT, transformer and inverter losses, grid unavailability, and module degradation through ageing. Before blaming the plant, check the measurement itself. A shaded or soiled irradiance sensor, a misoriented sensor, spectral mismatch between the reference cell and the modules, module temperature, and the recording period all affect the PR value. Weather-corrected PR uses module temperature as well as irradiation, so it gives a more accurate result and helps detect faults or low efficiency early. PR can be stated as an instantaneous or an average value, for the whole system or for the array, either as a fraction or as a percentage.

<!-- review notes
- sentence 2: support check: partial - The passage says PR captures the combined effect of all losses, but it doesn't say a falling PR fails to show which part is at fault.
-->
