---
id: state:mpp-operation
type: OperatingState
name: MPP operation
aliases:
- MPP
- MPP tracking
- feed-in operation
- normal operation
- grid-connected operation
- MPP search
- MPP-Such
- Run
category: Inverters
---
In MPP operation the inverter is connected to the grid, feeds power into it, and automatically tracks the maximum power point of the PV array. This is the normal operating mode once the inverter is energized; Sungrow shows it as the Run state, and SMA reports it as the Mpp substatus of the Run operating status. The tracker adjusts the power drawn so the array stays as close as possible to its MPP, which changes during the day with irradiance, clouds and module temperature. On SMA inverters MPP is the standard display in normal irradiance, while MPP-Such means the inverter is still adjusting to the best operating point. Yaskawa SGI units show MPP Tracking on the display, and Solectria PVI units show a steady green LED with the text Normal operation. If an SMA inverter's DC voltage control type is set to constant voltage, the DC voltage is held fixed and no MPP tracking takes place; Fronius inverters likewise offer MPP AUTO, MPP USER or FIX tracking modes. This is a normal state and no corrective action is needed.

<!-- review notes
- sentence 5: support check: partial - The passages give the MPP Tracking text and the Normal operation text with a green LED, but they do not name Yaskawa SGI or Solectria PVI, and the LED is described as green/ON rather than explicitly steady.
-->
