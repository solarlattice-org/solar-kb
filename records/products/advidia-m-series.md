---
id: prod:advidia-m-series
type: Product
name: Advidia M-series (i-PRO) network cameras
aliases:
- M-200-P
- i-PRO cameras
- iPro Cameras
- Outdoor Network PTZ Dome Camera
category: Security
make: advidia
product_level: family
claims:
- claim_id: c1
  rel: requires
  target: tool:vpn-client
  note: A VPN client connection is needed for remote access to the cameras; Advidia Guard reaches the
    camera through port 80.
  cite:
  - src: src:eq-equip-cameras-advidia-ipro-cameras-advidia-guard-setup
    loc: sec=h1
    h: 41e684fe062b
  - src: src:eq-equip-cameras-advidia-ipro-cameras-advidia-guard-setup
    loc: sec=h3
    h: 8ba4706522cc
  review: drafted
- claim_id: c2
  rel: implements
  target: func:ptz-control
  note: The M-200-P is an outdoor network PTZ dome camera, and Advidia Guard keeps the ability to move
    the camera.
  cite:
  - src: src:eq-equip-cameras-advidia-ipro-cameras-advidia-guard-setup
    loc: sec=h1
    h: 41e684fe062b
  - src: src:eq-equip-cameras-advidia-m-200-p-quickguide-v1-00-en-031622-0
    loc: sec=h2
    h: 980cd64abebd
  - src: src:eq-equip-cameras-advidia-ipro-cameras-advidia-guard-setup
    loc: sec=h3
    h: 8ba4706522cc
  review: drafted
  review_note: 'support check: partial - Passages say Advidia Guard keeps camera-move functionality, PTZ
    control is described, and the M-200-P is a PTZ dome, but the support relation for the M-series generally
    is implied, not explicit.'
---
The Advidia M-series are i-PRO network cameras. The M-200-P is an outdoor network PTZ dome camera, sold as a 2MP 33x Lighthunter model. Its listed network protocols include TCP, UDP, DHCP, NTP, FTP, HTTP, HTTPS, SMTP, SNMP, IGMP and RTSP. Remote access needs a VPN client connection. Opening the camera's web interface needs a plugin and a deprecated browser, or Microsoft Edge in IE mode. The Advidia Guard software can view and move several cameras at once, but it cannot change the cameras' communication settings. By default, Advidia Guard plays HD video and can use a lot of cellular data. Set the stream type to Third and playback to SD to lower data use.

<!-- review notes
- sentence 1: support check: partial - M-200-P as outdoor PTZ dome and 2MP 33x Lighthunter PTZ dome are stated, but the passages don't explicitly say the M-200-P is the 2MP 33x model or that M-series are i-PRO cameras beyond context.
- sentence 3: support check: partial - Passages state VPN is needed, a plugin is needed, and a web browser is deprecated/Edge setup is needed, but the 'IE mode' detail and explicit plugin+deprecated browser pairing are only loosely stated.
- sentence 1: review: partial - The passages support the M-200-P as an outdoor network PTZ dome and give the 2MP 33x Lighthunter title from its cut sheet, but no passage says the Advidia M-series are i-PRO cameras; they only say Advidia Guard accesses i-PRO cameras.
-->
