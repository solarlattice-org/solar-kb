---
id: proto:fronius-solar-net
type: Protocol
name: Fronius Solar Net
aliases:
- Solar Net
- Fronius Solar API
category: Communication
protocol_kind: application
---
Fronius Solar Net is a Fronius data network that links one or more inverters to system add-ons such as a datalogger or sensor box. It is a bus with a ring topology, and one suitable cable is enough to connect the inverters on the net to an add-on. On the inverter, the data communication area has two RS 422 ports, one IN and one OUT, and they connect through RJ45 plugs. When several DATCOM components are networked, fit a termination plug in every unused IN or OUT socket. Inverters supplied with a Fronius Datamanager card come with two of these plugs. Give every inverter on the net its own number in the SETUP menu. Add-ons are recognized automatically, but identical add-ons each need a unique number too. The Fronius Datamanager acts as the datalogger, so each Solar Net ring may have only one. Remove any extra Datamanager cards or use light inverter versions that have no card. On inverters such as the Fronius Symo, Primo and Galvo, the Protocol Type setting chooses between Fronius Solar Net (factory default) and Interface. Interface only works once the Datamanager card has been removed. A Solar Net LED on the inverter shows whether the Solar Net power supply is available.

<!-- review notes
- sentence 7: support check: partial - Protocol Type options, factory default and Interface requiring card removal are stated, but the passages do not name Symo, Primo or Galvo models.
- sentence 1: review: partial - The passages say Solar Net is a Fronius data network linking several inverters to system add-ons, but they never give a datalogger or sensor box as examples.
-->
