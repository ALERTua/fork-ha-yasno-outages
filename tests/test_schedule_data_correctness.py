"""Regression tests for schedule/data-correctness defects."""

import time as time_module
from datetime import date, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock

import pytest

from custom_components.svitlo_yeah.api.dtek.json import _parse_update_dt
from custom_components.svitlo_yeah.api.e_svitlo import ESvitloClient
from custom_components.svitlo_yeah.api.yasno import YasnoApi
from custom_components.svitlo_yeah.const import TZ_UA
from custom_components.svitlo_yeah.coordinator.dtek.json import DtekCoordinatorJson
from custom_components.svitlo_yeah.models import (
    PlannedOutageEvent,
    PlannedOutageEventType,
)


class TestStaleConsentPropagation:
    """The stale-data consent given during config flow must survive into polling."""

    @pytest.mark.asyncio
    async def test_coordinator_polls_with_stale_consent(self):
        """A consented entry must poll with allow_stale_data=True."""
        coordinator = object.__new__(DtekCoordinatorJson)
        coordinator.config_entry = MagicMock()
        coordinator.config_entry.options = {}
        coordinator.config_entry.data = {"allow_stale_data": True}
        coordinator.api = MagicMock()
        coordinator.api.fetch_data = AsyncMock()
        coordinator.api.get_events = MagicMock(return_value=[])
        coordinator.async_fetch_translations = AsyncMock()
        coordinator.check_outage_data_changed = MagicMock()

        await coordinator._async_update_data()

        coordinator.api.fetch_data.assert_called_once_with(allow_stale_data=True)

    @pytest.mark.asyncio
    async def test_coordinator_defaults_to_fresh_only(self):
        """Without consent the coordinator must not adopt stale data."""
        coordinator = object.__new__(DtekCoordinatorJson)
        coordinator.config_entry = MagicMock()
        coordinator.config_entry.options = {}
        coordinator.config_entry.data = {}
        coordinator.api = MagicMock()
        coordinator.api.fetch_data = AsyncMock()
        coordinator.api.get_events = MagicMock(return_value=[])
        coordinator.async_fetch_translations = AsyncMock()
        coordinator.check_outage_data_changed = MagicMock()

        await coordinator._async_update_data()

        coordinator.api.fetch_data.assert_called_once_with(allow_stale_data=False)


class TestOvernightPeriodMonthRollover:
    """Overnight periods on the last day of a month must roll into the next month."""

    def test_parse_period_month_boundary(self):
        """23:00-04:00 on Oct 31 must end on Nov 1, not raise ValueError."""
        client = object.__new__(ESvitloClient)
        period = {"start_time": "23:00", "end_time": "04:00"}

        event = client._parse_period(period, date(2026, 10, 31))

        assert event is not None
        assert event.start == datetime(2026, 10, 31, 23, 0, tzinfo=TZ_UA)
        assert event.end == datetime(2026, 11, 1, 4, 0, tzinfo=TZ_UA)


class TestMultiDayAllDayCurrentEvent:
    """A merged multi-day all-day event stays 'current' on its later days."""

    def test_get_current_event_second_day(self):
        """Day 2 of a merged 2-day emergency must still report the event."""
        api = YasnoApi(region_id=1, provider_id=1)
        day1 = date(2026, 7, 1)
        merged = PlannedOutageEvent(
            start=day1,
            end=day1 + timedelta(days=2),
            all_day=True,
            event_type=PlannedOutageEventType.EMERGENCY,
        )
        api.get_events = MagicMock(return_value=[merged])

        at_day2 = datetime(2026, 7, 2, 12, 0, tzinfo=TZ_UA)
        assert api.get_current_event(at_day2) is merged


class TestUpdateTimestampTimezone:
    """The DTEK 'update' stamp is Kyiv wall-clock time, not host-local time."""

    def test_parse_update_dt_uses_kyiv_tz(self, monkeypatch):
        """Parsing must not depend on the host timezone."""
        monkeypatch.setenv("TZ", "America/New_York")
        time_module.tzset()
        try:
            parsed = _parse_update_dt("01.07.2026 12:00")
            assert parsed == datetime(2026, 7, 1, 12, 0, tzinfo=TZ_UA)
        finally:
            monkeypatch.undo()
            time_module.tzset()
