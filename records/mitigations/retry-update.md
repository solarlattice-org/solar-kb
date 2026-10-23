---
id: mit:retry-update
type: Mitigation
name: Update retry
aliases:
- Repeat the update process
- Retry update
- Perform an upgrade again
- Upgrade again
- Restart update
---
Retrying the update means running a failed firmware or software update on the inverter a second time. Use it when the inverter reports an update error or an upgrade-failed alarm. On Fronius inverters, status code 743 shows a warning on the display. The fix is to repeat the update and check the USB drive that holds the update. If Fronius code 746 cancels the update, wait 2 minutes before you start it again. On Huawei SUN2000 units, the alarm appears as Upgrade Failed (2065) or Firmware Upgrade Failed (505). To run the upgrade again, open Function Menu > Inverter Update and follow the operation guide. SMA inverters also say to retry after a failed update, including bootloader and time zone database updates. Make sure the update file you selected is the right one for that inverter. While the update runs, the inverter restarts and may not work at times. This takes several minutes and cannot be canceled. A retry only fixes a one-off interruption. If the error comes back or the upgrade fails several times, contact a trained service technician, the dealer or the manufacturer's Service.

<!-- review notes
- sentence 7: support check: partial - Contact service when error persists/recurs is stated, but the claim that a retry only fixes one-off interruption is an unstated inference, and the manufacturer's Service/dealer/trained technician are covered separately.
-->
