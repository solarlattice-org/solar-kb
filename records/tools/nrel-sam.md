---
id: tool:nrel-sam
type: Tool
name: System Advisor Model
aliases:
- SAM
- NREL SAM
- NREL System Advisor Model
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:nrel
  note: The model is provided by NREL, which the Alliance for Sustainable Energy operates for the U.S.
    Department of Energy.
  cite:
  - src: src:man-nrel-ssc-guide
    loc: sec=9
    h: 0964e7477d01
  - src: src:man-nrel-ssc-guide
    loc: sec=h1
    h: af3c08013584
  review: drafted
---
The System Advisor Model is free NREL software that models both the performance and the economics of renewable energy projects, including grid-connected solar. Its performance model estimates a system's energy output hour by hour, and some technologies can also run sub-hourly. Its financial model works out annual project cash flows, levelized cost of energy and the effect of incentives. SAM supports parametric studies, sensitivity analysis, optimization and statistical analysis, and its spreadsheet interface can exchange data with Excel models. In O&M work, SAM is one example of a performance model you can use to calculate expected output for performance ratio evaluations. It can simulate effects such as inverter clipping. A model result is only as good as its inputs. For example, a dirty irradiance sensor will exaggerate the performance ratio, so keep your field instruments maintained. The desktop application is a front end for the SAM Simulation Core library. Developers can call that library through an API with wrappers for languages such as Python and MATLAB. NREL provides the model as is, with no warranty, and offers no support or training for using it.

<!-- review notes
- sentence 1: support check: partial - Performance and economic modeling of grid-connected solar is stated, but nothing in the passages says SAM is free software.
- sentence 5: support check: partial - Dirt on a pyranometer exaggerates PR and instrument maintenance is very important, but the 'only as good as its inputs' generalization is not stated.
-->
