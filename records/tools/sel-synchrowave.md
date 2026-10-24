---
id: tool:sel-synchrowave
type: Tool
name: SEL SynchroWAVe software
aliases:
- SynchroWAVe
- SYNCHROWAVE Event
- SEL-5601-2 SYNCHROWAVE Event
- SEL SynchroWAVe Event
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sel
  note: Sold as SEL-5601-2 and downloaded from the SEL website.
  cite:
  - src: src:sel-synchrowave-instruction-manual
    loc: sec=h2
    h: bfd797a7158d
  - src: src:sel-synchrowave-instruction-manual
    loc: sec=h11
    h: fc96b019e2bd
  - src: src:sel-synchrowave-instruction-manual
    loc: sec=h90
    h: 07fab266c2df
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passages show SEL-5601-2 SYNCHROWAVE Event, downloaded from the
    SEL website, but never name Schweitzer Engineering Laboratories; the sold-as claim is only implied
    by the purchased license.'
---
SYNCHROWAVE Event (SEL-5601-2) is SEL software for viewing and analyzing relay and meter event reports, with analog and digital charts, phasor diagrams and complex charts. It is installed as the default event viewer in ACSELERATOR QuickSet and supports disturbance analysis of protection system operations. It imports COMTRADE, SEL ASCII and Compressed ASCII event reports, sequential events recorder files, CSV and other SEL formats, and exports COMTRADE and CSV. The basic version needs no added license and includes harmonic and spectral analysis, symmetrical components and ABC or ACB phase rotation support. The advanced version adds custom calculations, mho and differential alpha plane analysis, Bewley lattice traveling-wave analysis and multi-event time alignment, with a 60-day trial after installation and a purchased license after that. SEL application guides use its custom calculations and templates to plot differential characteristics, 32Q and 32V directional elements and compensator distance characteristics, and to support testing of power elements. License activation can be done over the internet or manually, and you can check license details under Help, About, Manage License. A Host Mismatch error during licensing means the company name on the license does not match other SEL software on the same computer; send a screenshot to SEL Support.

<!-- review notes
- sentence 1: support check: partial - Charts, phasor diagrams and event report viewing are stated, but 'relay and meter event reports' is only partly stated (COMTRADE/SEL ASCII event reports; meter data in formats).
- sentence 3: support check: partial - Import formats and export of COMTRADE and CSV are listed, but 'other SEL formats' is loose; broadly matches.
- sentence 6: support check: partial - Differential characteristic, 32Q/32V, compensator distance and custom calculations for power element testing are covered, but templates for differential and the power element testing support are only loosely tied (power element guide uses a spreadsheet and custom calculations in appendix).
- sentence 1: review: partial - SEL-5601-2, the analog and digital charts, phasor diagrams, complex charts and event report viewing are all stated, but the passages never describe the reports as relay and meter event reports.
-->
