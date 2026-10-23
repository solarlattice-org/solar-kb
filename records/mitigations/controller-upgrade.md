---
id: mit:controller-upgrade
type: Mitigation
name: Controller hardware upgrade
aliases:
- PWRcell ATS Controller Upgrade Kit
- Modified PWRcell ATS Controller
---
This action fits a newer controller into the PWRcell automatic transfer switch (ATS) so that the inverter can work with an AC generator. Use it when the inverter shows configuration error 0X7707. That code means the inverter is set up for AC Generator Integration but the installed ATS units do not have the right controller. The upgrade kit is model G0080060 and contains the PWRcell ATS Controller, part number A0002532225. Follow the PWRcell ATS Installation Manual for the kit installation and the generator integration requirements. The upgraded controller also works in every other configuration that needs a PWRcell ATS. Generator integration also needs inverter firmware version 13794 or newer and an ATS that supports generator integration, so the controller upgrade alone may not be enough. A controller version that does not suit the application can make the PWRcell system behave in unexpected and incorrect ways, so check the equipment against the chosen configuration before installing.
