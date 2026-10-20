"""Config flow for OpenStick.

Manual entry for now. Later: zeroconf discovery of _openstick._tcp and
on-screen pairing (the TV shows a code, the user types it here).
"""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST, CONF_PORT

from .const import CONF_TOKEN, DEFAULT_PORT, DOMAIN

STEP_USER_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
        vol.Required(CONF_TOKEN): str,
    }
)


class OpenStickConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for OpenStick."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle manual setup."""
        if user_input is not None:
            await self.async_set_unique_id(f"{user_input[CONF_HOST]}:{user_input[CONF_PORT]}")
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=user_input[CONF_HOST], data=user_input)
        return self.async_show_form(step_id="user", data_schema=STEP_USER_SCHEMA)
