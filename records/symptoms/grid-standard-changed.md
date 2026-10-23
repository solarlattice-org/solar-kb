---
id: symptom:grid-standard-changed
type: Symptom
name: Grid standard changed
aliases:
- Variation of the grid standard
- Global-Settings Event
- Set country standard
- country data set
- Grid connection rule
---
This event is logged when someone changes the inverter's grid standard. On FIMER inverters the change can be made through the internal webserver. The manufacturer says the change is made by the customer or installer and is not an error. It is only recorded in the inverter's event history, and no LED lights up. The selected standard sets the grid connection and protection limits. These include the undervoltage and overvoltage limits and the reactive power capability, so a change can alter when the inverter trips or connects. If the new country data set or parameter does not match local requirements, the inverter may fail to connect to the grid. Check the selected standard against the site's interconnection requirements. If thresholds are set outside the range allowed by the national standard, an external interface protection is required. On some FIMER models the grid standard can only be changed within a limited operating window. After that the setting is locked. First check the event history and the current grid standard setting. Confirm that the change was intended and that it matches the standard the installation requires.

<!-- review notes
- sentence 3: support check: partial - Passages say the country standard can change U</U> values, grid connection thresholds and P-Q capability, but the explicit claim that a change alters when the inverter trips or connects is only loosely implied.
- sentence 7: support check: partial - Passages support the event being a non-error record and checking the country standard against local requirements, but they don't state a procedure to check the event history first and confirm the change was intended.
-->
