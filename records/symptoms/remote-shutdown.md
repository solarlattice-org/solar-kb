---
id: symptom:remote-shutdown
type: Symptom
name: Remote shutdown
claims:
- claim_id: c1
  rel: observed_as
  target: meas:remote-shutdown-status-point
  note: In Tesla controls manuals this is a status point (Modbus/DNP3 binary input, DNP3 index StartIndex
    + (X-1)*30 + 9). It shows that the customer's external I/O is commanding a remote shutdown.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=79.r2
    h: 2cbd821733c1
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=88.r9
    h: 2cbd821733c1
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=95.r9
    h: 2cbd821733c1
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=175.r9
    h: 9bf10f260c7c
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=196.r9
    h: f359fef01762
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=261.r9
    h: f359fef01762
  review: drafted
  review_note: 'support check: partial - Point label, description and DNP3 index are stated, but the passages
    don''t say AC power falls to zero (though shutdown opening the breaker implies it) and don''t mention
    the model_103.W signal explicitly.'
---
Remote shutdown is a status point that turns on when the customer's external I/O is commanding the system to shut down. The command comes from a pair of remote shutdown terminals in the customer I/O area of the Customer Interface Bay. When it is active, the inverter stops operating, the AC bus is isolated from the battery DC source, and the AC circuit breaker opens, so output goes to zero. This is usually a deliberate action, for example when the unit is put into storage or when a customer E-Stop button wired to these terminals puts the system into standby. Remote shutdown is a software function and may not meet emergency stop rules everywhere, so check local codes and the AHJ before using it as an E-Stop.
