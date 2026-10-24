---
id: comp:power-optimizer
type: Component
name: DC power optimizer
aliases:
- Power Optimizer
- module-level power electronics
- module-level optimizer
- DC optimizer
- MLPE optimizer
- Power Optimiser
- Optimizer
- Module add-on Power Optimizer
---
A DC power optimizer is a DC-DC converter attached to a PV module that runs its own maximum power point tracking for that module, so shading or soiling on one module does not pull down the rest of the string. Optimizers hold the string voltage constant whatever the string length or conditions, so strings can be uneven in length or mix module orientations. They come as add-on units wired to one or more modules, or built into smart modules. A safety function drops each optimizer's output to a touch-safe voltage during faults, when the optimizer is disconnected from the inverter, when the inverter switch or AC breaker is off, or when rapid shutdown is triggered. Each optimizer sends module-level data such as voltage, current, power and energy to the inverter over the DC power line for monitoring. To troubleshoot a power optimizer failure, disconnect the string, measure each optimizer's output to find the one without safety voltage, check its connections, polarity and module, and replace it. Field inspection covers the optimizer-to-module connections, visible damage and the serial number. In confined spaces such as BIPV, ventilation may be needed to keep optimizers within their rated temperature.
