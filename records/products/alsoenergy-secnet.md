---
id: prod:alsoenergy-secnet
type: Product
name: AlsoEnergy SecNet
aliases:
- SecNet
- AlsoEnergy Private Network
category: Monitoring and communications
make: alsoenergy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:alsoenergy
  note: SecNet is described as the AlsoEnergy private network.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-secnet-getting-started-r2
    loc: sec=h1
    h: d1069f002d32
  - src: src:eq-equip-das-alsoenergy-alsoenergy-secnet-getting-started
    loc: sec=h1
    h: 0b2ff82b76a7
  - src: src:eq-equip-das-alsoenergy-alsoenergy-secnet-getting-started-r2
    loc: sec=h2
    h: da489ce9e84b
  review: drafted
  review_note: 'support check: partial - Passages call SecNet the AlsoEnergy private network and use alsoenergy.com
    domain, but never explicitly state AlsoEnergy makes it.'
- claim_id: c2
  rel: requires
  target: tool:vpn-client
  note: Access uses the AnyConnect VPN client. It installs automatically from the SecNet web page or can
    be downloaded by hand. The endpoint is secnet.alsoenergy.com.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-secnet-getting-started
    loc: sec=h1
    h: 0b2ff82b76a7
  - src: src:eq-equip-das-alsoenergy-alsoenergy-secnet-getting-started-r2
    loc: sec=h2
    h: da489ce9e84b
  review: drafted
- claim_id: c3
  rel: implements
  target: func:remote-maintenance
  note: Once users have credentials, the private network gives them remote access to their site devices
    over VPN.
  cite:
  - src: src:eq-equip-das-alsoenergy-alsoenergy-secnet-getting-started
    loc: sec=h1
    h: 0b2ff82b76a7
  - src: src:eq-equip-das-alsoenergy-alsoenergy-secnet-getting-started-r2
    loc: sec=h2
    h: da489ce9e84b
  review: drafted
---
AlsoEnergy SecNet is the AlsoEnergy private network. Users with credentials connect to it over a VPN to reach their site devices. VPN credentials arrive as a one-time access link and password by email. The username is an email address and is case sensitive, so enter it exactly as shown. To connect, log in at the SecNet web page. The AnyConnect VPN client then installs automatically, or you can download and install it from the link on the page. The web page may show a certificate warning, which the guide says to accept as an exception. In the AnyConnect settings (gear icon), uncheck the option that blocks connections to untrusted servers. Then enter the SecNet address as the endpoint and connect with the VPN credentials.
