---
id: arch:microinverter-system
type: Architecture
name: Microinverter system
aliases:
- microinverter architecture
- microinverters
- IQ Microinverter system
- Enphase microinverter system
category: System topology
---
A microinverter system puts a small inverter at each PV module. Each unit mounts under its module and the AC output runs on a trunk cable such as the IQ Cable. A typical layout runs from the IQ Cable to a rooftop AC junction box, then along the AC branch circuits to a load center or IQ Combiner that holds the dedicated microinverter breakers, and on to the point of common coupling. Voltage rise is checked separately for each wire section. Enphase tables list the maximum conductor lengths that keep each section within a 1% voltage rise. With IQ8 microinverters the system can be built as grid-tied, grid-agnostic, PV plus storage, PV plus generator, or PV plus storage plus generator, using IQ Batteries and an IQ System Controller. An IQ Gateway is required to collect performance data and send it to the cloud. The IQ Combiner includes the gateway. Enphase says the distributed design of the microinverter system is the basis for several features that give it high reliability. Each microinverter works only with a standard, compatible PV module. Smart modules, fuel cells, turbines, DC generators and non-Enphase batteries are not supported, and the module's open-circuit voltage must not exceed the microinverter's maximum DC input voltage. Some microinverter generations can be mixed: IQ8MC, IQ8AC and IQ8HC units can share a branch and an IQ Gateway with IQ8, IQ8+, IQ8M, IQ8A and IQ8H units.

<!-- review notes
- sentence 1: support check: partial - Passages say install under the PV module and mention IQ Cable with microinverter connectors, but not that a small inverter is at each module or that AC output runs on a trunk cable as a general definition.
- sentence 5: support check: partial - Gateway required and included in the Combiner are stated, and it collects and transmits data to the cloud, but 'required to collect data' is slightly reframed; essentially supported though.
- sentence 1: review: partial - The passages support mounting under the PV module and the IQ Cable carrying microinverter connections, but they never say there is one small inverter at each module or call the IQ Cable an AC trunk cable.
-->
