---
id: tool:sma-energy-app
type: Tool
name: SMA Energy App
category: Apps
tool_kind: app
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sma
  cite:
  - src: src:sma-kb-sunny-portal-app
    loc: sec=h1
    h: ec8aa85c43ff
  - src: src:sma-kb-wie-erstelle-ich-ein-pv-erzeugungs-widget-f-r-die-sma-energy-app
    loc: sec=h1
    h: 0b38159e2b91
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passages show SMA Energy App is an SMA-service product (SMA support
    site, SMA Smart Home), but never explicitly say SMA makes/publishes it; implied only.'
---
The SMA Energy App is SMA's smartphone app for monitoring a system's energy. On the Sunny Boy Smart Energy US, you commission the system with the SMA 360° app first, then use the SMA Energy App to monitor energy. It replaces the Sunny Portal App, which is no longer supported. It keeps all of the old app's functions except the Sunny Portal logbook and adds features such as a PV forecast. Users log in with their existing username and password, and historical data is moved over automatically. SMA is working toward one SMA ID that works across its platforms, including this app. The app can be used to view and control the SMA eCharger 22. It can also put PV generation widgets on the phone home screen, starting with iOS 15 or Android 12. If the forecast is missing, log in to Sunny Portal as installer or administrator, open the PV system properties, run Find geo data and save. If data stops updating, update the app, refresh the screen, log out and back in, and check the local network. If the values still show in Sunny Portal, reinstall the app. If the problem continues, restart the inverter, check network speed and topology, and use LAN instead of Wi-Fi if the inverter is on Wi-Fi.

<!-- review notes
- sentence 1: support check: partial - Commissioning via SMA 360° then SMA Energy App for energy monitoring is stated, but the passage doesn't name the Sunny Boy Smart Energy US or explicitly say it is a smartphone app.
- sentence 4: support check: partial - Widgets on iOS 15/Android 12 are supported, and the eCharger 22 lists SMA Energy App under visualisation & control; but 'view and control' is only loosely supported by the combined 'Visualisierung & Steuerung' row.
- sentence 7: support check: partial - Restart inverter, check network speed and topology, and use LAN instead of Wi-Fi are stated, but the passage ties these to system errors after the earlier steps fail, and the exact trigger 'if problem continues' is loosely matched.
- sentence 1: review: partial - The passage states that you commission with the SMA 360° app first and then use the SMA Energy App for energy monitoring, but the quoted text never names the Sunny Boy Smart Energy US or calls the app a smartphone…
-->
