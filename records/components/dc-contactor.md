---
id: comp:dc-contactor
type: Component
name: DC contactor
---
This DC contactor event is written to the inverter event log. The main failure mode the sources report is a contactor that stays closed when the inverter tells it to open. For this fault, the manual says an authorized service provider may need to inspect and service the inverter. In battery storage commissioning, each contactor is tested on its own: open the DC disconnect, close one stack at a time, and check that the contactor reports closed. In the same test, the other stacks should show the DC bus voltage within plus or minus 10 V.

<!-- review notes
- sentence 2: support check: partial - The description says the contactor failed to open properly, which fits a stuck-closed contactor, but the passage doesn't say it stays closed or call it the main failure mode across sources.
- sentence 4: support check: partial - Passage states DC disconnect open, closing each stack individually and checking the contactor reports closed, but 'one at a time' is implied and the other-stack voltage check is omitted; the 'battery storage commissioning' context is only implied by the section.
-->
