---
id: prod:sungrow-logger1000
type: Product
name: Sungrow Logger1000
aliases:
- Logger1000
category: Monitoring and communications
make: sungrow
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sungrow
  cite:
  - src: src:kb-sungrow-how-to-log-in-logger1000-web-interface
    loc: sec=front
    h: 8410925d63aa
  - src: src:kb-sungrow-how-to-enable-the-remote-maintenance-function
    loc: sec=front
    h: 275985bf923d
  review: drafted
  review_note: 'support check: partial - Passages show a SunGrow-sourced FAQ about Logger1000 but never
    explicitly state Sungrow makes it; only implied by the make metadata and website.'
- claim_id: c2
  rel: implements
  target: func:remote-maintenance
  note: Turned on from the local Logger1000 Web interface under System > Remote maintenance. This creates
    a remote access link that O&M users can use to reach the Web UI.
  cite:
  - src: src:kb-sungrow-how-to-enable-the-remote-maintenance-function
    loc: sec=front
    h: 275985bf923d
  review: drafted
---
The Logger1000 is a Sungrow monitoring and communications logger, and technicians set it up through a local Web interface. To log in locally for maintenance, use the default maintenance account and password given in Sungrow's FAQ. The logger has a remote maintenance function. You switch it on in the System menu, save, and confirm with the login password. Turning it on creates a remote access link. You can copy the access details locally or email them, so O&M users can reach the Web UI remotely.

<!-- review notes
- sentence 1: support check: partial - A local Web interface for Logger1000 is evident, but nothing describes it as a monitoring and communications logger or that technicians set it up there.
- sentence 2: support check: partial - FAQ gives default account maintain/pw1111 for logging into the local Web interface, but doesn't state it's for local maintenance login generally; mostly supported.
- sentence 1: review: partial - The passages show that Logger1000 is a Sungrow device with a local Web interface, but they never call it a monitoring and communications logger or say that technicians set it up there.
-->
