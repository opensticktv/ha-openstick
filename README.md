# OpenStick for Home Assistant

Home Assistant integration for [OpenStick.tv](https://github.com/opensticktv) devices.

Status: skeleton. Setup stores the connection; entities arrive once the device's local API exists.

## Planned

- Discovery over mDNS (`_openstick._tcp`) and on-screen pairing
- `media_player` entity with apps as sources
- `remote` entity for d-pad keys
- TV power via HDMI-CEC
- `notify` service that shows a message on the TV

OpenStick devices are also DLNA renderers, so Home Assistant's built-in DLNA integration works without this.

## Install (HACS)

Add `https://github.com/opensticktv/ha-openstick` as a custom repository of type Integration, then install **OpenStick**.
