---
id: prog:masscec-pts
type: Program
name: MassCEC Production Tracking System
aliases:
- PTS
- MassCEC PTS
- Mass CEC PTS
- Massachusetts CEC PTS
- MA CEC PTS
- CEC PTS
category: REC registry
program_kind: incentive
claims:
- claim_id: c1
  rel: issued_by
  target: org:masscec
  note: Production data reported to PTS is used by the Massachusetts CEC to award renewable energy certificates.
  cite:
  - src: src:alsoenergy-kb-ma-cec-pts-reporting-setup-guide
    loc: sec=front
    h: 68c8060227a5
  - src: src:alsoenergy-kb-notifications
    loc: sec=front
    h: 2545de89ed0d
  review: drafted
  review_note: 'support check: partial - The passages say the CEC uses PTS data to award RECs, but they
    don''t state that MassCEC PTS is issued by Massachusetts Clean Energy Center. They only imply it by
    calling it the ''Massachusetts CEC PTS program''.'
- claim_id: c2
  rel: applies_to
  target: region:us-ma
  note: Production tracking for PV systems registered in the Massachusetts CEC SREC incentive program.
  cite:
  - src: src:alsoenergy-kb-ma-cec-pts-reporting-setup-guide
    loc: sec=front
    h: 68c8060227a5
  review: drafted
---
The MassCEC Production Tracking System (PTS) collects production data for PV systems in the Massachusetts CEC SREC incentive program. The CEC uses that data to award renewable energy certificates to the account holder. To start reporting, first register the PV system with the Massachusetts CEC SREC program. Then name a reporting party, such as a monitoring provider, as the System Representative in the PTS portal. Each system gets a PTS ID as its tracking number. The ID is printed on the CEC final approval notice, and SREC aggregators can also find it on a report. The date in service given to the reporting party must match the date in service registered with PTS. That date is when the utility approved the system to operate. The reporter submits a lifetime meter reading as of the last day of each month, and PTS works out the monthly values from it. Generation is submitted between the 1st and 5th of the following month. If the monitoring meter is offline for a long time, Mass CEC accepts inverter lifetime energy readings for SREC minting. Send a photo of the inverter display or a portal screenshot. If a reading is rejected as too high or too low, check that the system capacity and the initial meter reading in the Mass CEC portal match what is actually on site. Generation is minted quarterly, so a short PTS reporting outage does not have to mean lost RECs. For example, October 2019 generation was minted with Q4 2019 in April 2020.

<!-- review notes
- sentence 2: support check: partial - The passages give the order: register with the Massachusetts CEC SREC program, then designate the reporter as System Representative, which is checked in the PTS portal. They describe this only for Locus, and they say to designate it at registration, not afterward in the portal.
- sentence 8: support check: partial - The notice says October 2019 generation mints in April 2020 with Q4 2019, so RECs weren't missed. It does not say generation is minted quarterly in general, and the example is presented in the notice as being about that specific disruption.
-->
