---
id: proto:bluetooth
type: Protocol
name: Bluetooth
aliases:
- Bluetooth Low Energy
- BLE
- BLE4.2
- Bluetooth 4.0
- Bluetooth Wireless Technology
- Bluetooth Class 1
category: Communication
protocol_kind: transport
---
Bluetooth is a wireless link for exchanging data between devices. It uses the public 2.4 GHz band, so no cables are needed and end users do not have to register it. It uses adaptive frequency hopping across 79 channels and skips frequencies that are disturbed or already in use, for example by WLAN routers. Because of this it rarely suffers interference or causes it. Bluetooth Class 1 reaches up to 100 m in open air with a maximum transmit power of 100 mW, and the power drops automatically once the connection is good. A computer can be given Bluetooth with a USB stick. The Schneider Electric Conext CL125 is commissioned and configured from a smart device using the eConfigure CL125 app over Bluetooth 4.0. The phone or tablet needs iOS 10 or Android 5 or later. On the Sungrow SG200HX-US, local display and setup is done through Bluetooth and an app. The LED blinks fast while Bluetooth data is flowing and blinks red if a system fault is present during the connection. The Solis S1-W4G-ST Wi-Fi and cellular data logger uses BLE4.2 for near-end communication, and the CPS FlexOM Gateway also has a Bluetooth interface. On SMA systems, inverters with Bluetooth are configured using Sunny Explorer or the Sunny WebBox with Bluetooth. The Sunny Boy Storage and Sunny Boy Smart Energy have no Bluetooth and use Speedwire or WLAN instead.

<!-- review notes
- sentence 5: support check: partial - Bluetooth+App display, fast blink with data communication, and red blink with fault are stated, but 'fast blink' is defined for no system fault and 'local setup' isn't stated.
- sentence 6: support check: partial - BLE4.2 for S1-W4G-ST near-end is stated and a Bluetooth interface is listed, but the passage doesn't say it's the CPS FlexOM Gateway's or the Solis logger is Wi-Fi and cellular.
- sentence 7: support check: partial - Bluetooth config tools and Sunny Boy Storage (Speedwire/WLAN) are supported, but Smart Energy only has Speedwire, not WLAN.
-->
