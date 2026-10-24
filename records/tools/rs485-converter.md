---
id: tool:rs485-converter
type: Tool
name: RS-485 to USB converter
aliases:
- USB-RS485 adapter
- serial converter
- RS485 to USB adapter
- USB-485 converter
- USB to RS485 interface converter
- signal converter
category: Instruments
tool_kind: instrument
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:rs485
  note: Converts signals between an RS-485 device such as an inverter or sensor and a computer's USB port.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: sec=h152
    h: 3dbfcac9d6bd
  - src: src:imt-solar-si-instruction-digital-2017-e
    loc: sec=h11
    h: 99d7c334850f
  - src: src:abb-fimer-trio-20-0-27-6-tl-outd-product-manual-revg
    loc: sec=h159
    h: b39ae62d2bb7
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: sec=h147
    h: 6e5f987b1f59
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
An RS-485 to USB converter connects a computer's USB port to an RS-485 serial line. It converts signals between the field device, such as a PV inverter, and the computer. The Conext CL125 EasyConfig tool lists an RS485 to USB adapter, part TCSMCNAM3M002P or equivalent, as its serial port requirement. For the CL125 inverter, Schneider Electric also points to third-party converters such as the Moxa UPort 1130I. On FIMER TRIO inverters, a PC can collect operating data from the RS-485 line through the PVI-USB-RS485_232 signal converter. IMT Solar Si irradiance sensors are configured with the Si Modbus Configurator software. This needs a computer, a voltage supply and a USB to RS485 converter, for example an ICPCON I-7561 or a DIGITUS DA-70157. For BACnet troubleshooting, a USB-485 converter can capture bus traffic for a tool such as BACspy or Hyperterminal. Use shielded, grounded twisted-pair cable for the RS-485 run. Set each inverter's termination resistor switch according to its position on the bus. Once the converter is connected, confirm that the devices are communicating, then set the communication parameters, for example in the eConfigure CL125 app.

<!-- review notes
- sentence 2: support check: partial - The TCSMCNAM3M002P requirement is in u1 and the Moxa UPort 1130I in u12, but the passages don't say the requirement is in the 'Conext CL125 EasyConfig tool' specifically, and u1 doesn't name the product.
- sentence 4: support check: partial - u14 states the software, requirements and converters, but it doesn't say the sensors are IMT Solar Si irradiance sensors.
- sentence 7: support check: partial - u12 says to confirm communication and set parameters in the eConfigure CL125 app, but it doesn't tie this to 'once the converter is connected'; the step concerns connecting devices.
- sentence 4: review: partial - The passage supports the Si Modbus Configurator requirements (computer, voltage supply, USB to RS485 converter, ICPCON I-7561 or DIGITUS DA-70157), but the quoted text never calls the devices IMT Solar Si irradiance sensors.
-->
