---
id: meas:battery-overtemperature-message
type: Measurement
name: Battery overtemperature message
aliases:
- Battery overtemperature
- BatTmpHi
- BatTmpHiWarn
- Battery temperature too high
- Battery temperature high
- XA04DcHiTmp
- XA06DcHiTmpC
- Overtemperature fault in battery
---
Battery management continuously tracks battery temperature, and this message appears in the event list or on the display when that temperature is too high. It comes in two levels: a level 1 warning such as W212, and a level 3 fault such as F206, when the battery is too hot. The warning is issued when the battery comes within 5°C of its maximum permissible temperature. If that maximum is exceeded, the Sunny Island switches off and starts again once the battery has cooled down. A status of 'Battery temperature high' means the temperature is in a critical range and the battery may not work properly. A status of 'too high' means the battery has been shut down. An external battery management system can also report battery overtemperature over SiCom, either in general or specifically during charging. In that case, find and fix the cause in the external system using the battery manufacturer's documentation. Let the battery cool down first. If the message keeps coming back, measure the battery temperature sensor: at 20°C to 25°C it should read about 2000 ohms. A large deviation points to a faulty sensor that needs replacing. Keeping the battery below 25°C helps prevent early battery aging. On some devices, the service team must find the cause, and you should contact the battery manufacturer.

<!-- review notes
- sentence 1: support check: partial - Continuous monitoring and F206 'Battery overtemperature' on display are stated, but the passages don't say the message appears in the event list, and the statement is vague about which message.
- sentence 6: support check: partial - Cooling and the ~2000 Ω at 20–25°C sensor check with replacement on large deviation are stated, but 'if the message keeps coming back' is not in the passages.
- sentence 8: support check: partial - Event 9313 says Service must determine the cause and to contact the battery manufacturer, but 'on some devices' is not stated.
- sentence 1: review: partial - Continuous temperature monitoring and the F206 'Battery overtemperature' display entry are stated, but no passage says the message appears in the event list.
-->
