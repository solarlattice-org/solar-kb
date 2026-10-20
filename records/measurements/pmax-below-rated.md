---
id: meas:pmax-below-rated
type: Measurement
name: Pmax below rated value
aliases:
- PMPP
- Maximum power
---
The signature is a measured maximum power that falls short of the module's rated nameplate value. For a brand new module, this means the STC output is below the specified tolerance limit. It is mainly detected with IV measurements, and monitoring data can sometimes show it too. An IV curve tracer sweeps the voltage from zero to open-circuit voltage under a known irradiance and records the current. This gives the maximum power point, the short-circuit current and the open-circuit voltage of a module or string. To check whether a new module meets its rating, compare its stabilized lab STC Pmax with the minimum nameplate power. Allow for the lab's measurement uncertainty and the manufacturer's lower production tolerance. A shortfall in a new module can come from product variability, manufacturing quality, the labelling policy or measurement uncertainty. Cell quality, such as susceptibility to light induced degradation, and the binning method also play a part. In the field, Pmax drops with a short-circuited or inverted bypass diode, where Voc is also affected. It also drops with heterogeneous loss of transparency, where Isc is also affected. A string IV curve can be compared with the sum of its module curves. A difference in power or fill factor points to the problem, which you can then trace to individual modules or to shading. A rating shortfall is not a degradation or safety failure. It does lower lifetime energy yield and makes yield predictions wrong.

<!-- review notes
- sentence 2: support check: partial - Detection lists IV with MON in parentheses, but 'mainly' and 'sometimes' are interpretive; the parenthesis is not explained.
-->
