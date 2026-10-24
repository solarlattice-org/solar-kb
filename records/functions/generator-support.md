---
id: func:generator-support
type: Function
name: Generator support
aliases:
- generator port
- generator integration
- generator start
- load-dependent generator start
- Load-Dependent Start
- Power-dependent generator start
- load-dependent generator request
- Generator Management
- Automatic generator start
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  rel: requires
  target: prod:enphase-iq-system-controller
  note: Enphase says every system configuration that has an IQ System Controller or IQ System Controller
    2 allows generator integration.
  cite:
  - src: src:kb-enphase-which-configurations-of-the-enphase-energy-system-support-generator-integration
    loc: sec=h1
    h: b4b224e1c5c2
  review: drafted
---
Generator support lets a storage or off-grid system connect a generator and use it. The system can start and stop the generator automatically, or the generator can be run manually. In the Enphase Energy System, generator support works in any configuration that has an IQ System Controller or IQ System Controller 2. Systems with M215 or M250 microinverters also need an extra contactor or relay to control the PV. Among third-generation Enphase controllers, the generator goes on the third DER port of the IQ System Controller 3G. The IQ System Controller 3 uses that port for extra PV and IQ Battery 5P instead, and has a No generator support sticker inside its door. On an IQ System Controller 2 with IQ8 microinverters, the generator circuit breaker must go in the generator slot on the controller busbar. On SMA Sunny Island inverters, load-dependent start asks for the generator when the average load is high. It is switched on with parameter 235.09 GnPwrEna, which only works if 235.01 GnAutoEna is also on. The start and stop limits are set with 235.10 GnPwrStr and 235.11 GnPwrStp, and the averaging time with 235.12 GnPwrAvgTm. After a load-triggered start, the Sunny Island still applies its warm-up time, minimum run time and power-down time. This feature protects the battery from deep discharge and adds the generator's power to the inverter's power for supplying loads. For SolarEdge Home Hub systems, generator support was planned for generators up to 15,000 watts with a 2-wire dry-contact start/stop, and it needs a firmware update. Many Solis S6 hybrid inverters support generators and prevent unintended backfeed into them. A generator larger than 30 kW must connect on the grid port, and it needs a dry contact for automatic start and stop based on battery state of charge.

<!-- review notes
- sentence 8: support check: partial - Solis generator support and backfeed prevention are stated, but the >30 kW grid-port and dry-contact details come from a passage that isn't about Solis S6 (it doesn't name Solis).
-->
