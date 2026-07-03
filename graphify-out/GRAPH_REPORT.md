# Graph Report - ha-svitlo-yeah  (2026-07-03)

## Corpus Check
- 41 files · ~169,236 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 890 nodes · 1167 edges · 102 communities (49 shown, 53 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 179 edges (avg confidence: 0.63)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `05f9c9bf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 70|Community 70]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]
- [[_COMMUNITY_Community 77|Community 77]]
- [[_COMMUNITY_Community 78|Community 78]]
- [[_COMMUNITY_Community 79|Community 79]]
- [[_COMMUNITY_Community 80|Community 80]]
- [[_COMMUNITY_Community 81|Community 81]]
- [[_COMMUNITY_Community 82|Community 82]]
- [[_COMMUNITY_Community 83|Community 83]]
- [[_COMMUNITY_Community 84|Community 84]]
- [[_COMMUNITY_Community 85|Community 85]]
- [[_COMMUNITY_Community 86|Community 86]]
- [[_COMMUNITY_Community 87|Community 87]]
- [[_COMMUNITY_Community 88|Community 88]]
- [[_COMMUNITY_Community 89|Community 89]]
- [[_COMMUNITY_Community 90|Community 90]]
- [[_COMMUNITY_Community 91|Community 91]]
- [[_COMMUNITY_Community 92|Community 92]]
- [[_COMMUNITY_Community 93|Community 93]]
- [[_COMMUNITY_Community 94|Community 94]]
- [[_COMMUNITY_Community 95|Community 95]]
- [[_COMMUNITY_Community 96|Community 96]]
- [[_COMMUNITY_Community 97|Community 97]]
- [[_COMMUNITY_Community 98|Community 98]]
- [[_COMMUNITY_Community 99|Community 99]]
- [[_COMMUNITY_Community 100|Community 100]]

## God Nodes (most connected - your core abstractions)
1. `IntegrationCoordinator` - 34 edges
2. `YasnoApi` - 33 edges
3. `DtekAPIJson` - 31 edges
4. `PlannedOutageEvent` - 27 edges
5. `ESvitloClient` - 24 edges
6. `IntegrationSensor` - 21 edges
7. `IntegrationConfigFlow` - 20 edges
8. `YasnoCoordinator` - 17 edges
9. `TestESvitloClientDisconnections` - 16 edges
10. `PlannedOutagesCalendar` - 15 edges

## Surprising Connections (you probably didn't know these)
- `_provider()` --calls--> `ESvitloProvider`  [INFERRED]
  tests/test_api_e_svitlo.py → custom_components/svitlo_yeah/models/providers.py
- `mock_provider()` --calls--> `ESvitloProvider`  [INFERRED]
  tests/test_coordinator_e_svitlo.py → custom_components/svitlo_yeah/models/providers.py
- `test_fetch_data_real_endpoints()` --calls--> `DtekAPIJson`  [INFERRED]
  tests/test_dtek_json_api.py → custom_components/svitlo_yeah/api/dtek/json.py
- `_api()` --calls--> `DtekAPIJson`  [INFERRED]
  tests/test_dtek_base.py → custom_components/svitlo_yeah/api/dtek/json.py
- `TestDtekAPIBaseGroups` --uses--> `DtekAPIJson`  [INFERRED]
  tests/test_dtek_base.py → custom_components/svitlo_yeah/api/dtek/json.py

## Communities (102 total, 53 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (27): Common tools for API clients., Yasno API client for Svitlo Yeah integration., Base coordinator for Svitlo Yeah integration., E-Svitlo coordinator for Svitlo Yeah integration., provider_name(), Coordinator for Svitlo Yeah integration., Simplify provider names for cleaner display in device names., _simplify_provider_name() (+19 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (33): ABC, ConfigFlow, provider(), BaseProvider, DTEKJsonProvider, Providers module for Svitlo Yeah., Base class for provider models., DTEK provider for DTEK JSON API. (+25 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (32): _is_data_sufficiently_fresh(), _parse_update_dt(), Parse the ``update`` field into an aware UTC datetime, or None., Check if update_dt is within DTEK_FRESH_DATA_DAYS days., Fetch from JSON sources with freshness checking.          Returns a :class:`Fetc, create_sample_json_data(), _make_response(), _patch_session() (+24 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (25): SensorEntity, IntegrationSensor, Initialize the sensor., Implementation of sensor entity., _coordinator(), MockCoordinator, next_scheduled_outage(), Tests for sensor functionality. (+17 more)

### Community 4 - "Community 4"
Cohesion: 0.07
Nodes (23): _debug_data(), _main(), Class to interact with Yasno API., Initialize the Yasno API., Fetch data from the given URL., Fetch regions and providers data., Fetch outage data for the configured region and provider., Get region data by name. (+15 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (21): _client(), _mock_session_post(), _provider(), Tests for E-Svitlo API., Test automatic re-login when session expired., Test get accounts relogin failure., Test fetching user info when user_id is missing., Test login failure inside get_accounts. (+13 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (21): current_state(), IntegrationCoordinator, next_connectivity(), next_event(), next_planned_outage(), next_scheduled_outage(), Get the next event of a specific type., Get the event at the present time. (+13 more)

### Community 7 - "Community 7"
Cohesion: 0.07
Nodes (29): Adding a New DTEK Region, Code Style, code:bash (git clone https://github.com/ALERTua/ha-svitlo-yeah.git), code:bash (uv sync), code:bash (uv run pre-commit install), code:bash (uv run pytest), code:bash (uv run pytest), code:bash (uv run pre-commit run --all-files) (+21 more)

### Community 8 - "Community 8"
Cohesion: 0.1
Nodes (15): ESvitloClient, Get list of available accounts., Get user information from E-Svitlo API., Get user disconnections from E-Svitlo API., Check and ensure connection is authenticated., Check if the response indicates a logged out state., Parse disconnections data into PlannedOutageEvent objects., Parse disconnection periods for a single day. (+7 more)

### Community 9 - "Community 9"
Cohesion: 0.07
Nodes (14): Tests for disconnection parsing., Test parsing of disconnections., Test get_events and get_current_event using cached data., Test ensuring connection calls login if needed., Test login failure in get_disconnections., Test get_disconnections HTTP error., Test get_disconnections exception., Test parsing day data with date error. (+6 more)

### Community 10 - "Community 10"
Cohesion: 0.08
Nodes (13): Tests for Svitlo Yeah models., Test YasnoPlannedOutageEventType enum., Test NOT_PLANNED type., Test YasnoPlannedOutageDayStatus enum., Test STATUS_SCHEDULE_APPLIES., Test STATUS_EMERGENCY_SHUTDOWNS., Test STATUS_WAITING_FOR_SCHEDULE., Test ConnectivityState enum. (+5 more)

### Community 11 - "Community 11"
Cohesion: 0.09
Nodes (22): Button, Calendar, Calendar View, Caveats, code:yaml (event_type: svitlo_yeah_data_changed), code:yaml (event_type: svitlo_yeah_data_changed), Contributing, Entity Usage Examples (+14 more)

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (13): parse_timestamp(), Parse a timestamp string into a datetime object.      Supports multiple formats:, Get the updated on timestamp for the configured group., Get the updated on timestamp., Tests for common_tools module., Test parse_timestamp function., Test parsing invalid timestamp strings., Test parsing empty string. (+5 more)

### Community 13 - "Community 13"
Cohesion: 0.14
Nodes (11): _merge_adjacent_events(), Merge adjacent events of the same type., Test event merging functionality., Test merging adjacent datetime events of same type., Test merging adjacent all-day events of same type., Test that events of different types are not merged., Test that non-adjacent events are not merged., Test merging empty event list. (+3 more)

### Community 14 - "Community 14"
Cohesion: 0.15
Nodes (11): CalendarEntity, async_setup_entry(), PlannedOutagesCalendar, Calendar platform for Svitlo Yeah integration., Set up the Svitlo Yeah calendar platform., Implementation of the Planned Outages Calendar entity., Return calendar events within a datetime range., Test PlannedOutagesCalendar entity. (+3 more)

### Community 15 - "Community 15"
Cohesion: 0.15
Nodes (8): DtekAPIBase, Base class for DTEK API implementations., Initialize the DTEK API base., Fetch outage data. To be implemented by subclasses., Get the list of available groups (with GPV prefix stripped).          {, Get the current event at a specific time., Get all events within the date range., Get scheduled events within the date range from preset data.

### Community 16 - "Community 16"
Cohesion: 0.14
Nodes (8): Test getting next event with a future datetime event., Test getting next event skips past datetime events., Test filtering events by type., Test getting next event when no events exist., Test _get_next_event_of_type method., Test getting next event with a future all-day event., Test getting next event skips past all-day events., TestCoordinatorGetNextEventOfType

### Community 17 - "Community 17"
Cohesion: 0.15
Nodes (13): _parse_group_hours(), Parse group hours data into a list of outage time ranges.      'GPV1.1': {, _api(), Tests for DTEK base API functionality., Test _parse_group_hours method., Create a DTEK API instance for testing base functionality., Sample parsed schedule data., Test _parse_group_hours method for preset data (same function as for real data). (+5 more)

### Community 18 - "Community 18"
Cohesion: 0.15
Nodes (10): coordinator(), mock_provider(), Tests for E-Svitlo Coordinator., Create coordinator with mocked client., Test data update failure., Test provider_name returns address., Test provider_name fallback., test_provider_name_fallback() (+2 more)

### Community 19 - "Community 19"
Cohesion: 0.15
Nodes (7): Test event retrieval methods., Test getting updated timestamp., Test getting updated timestamp without data., Test getting emergency events., Test getting current event., Test getting current event when none active., TestYasnoApiEvents

### Community 20 - "Community 20"
Cohesion: 0.18
Nodes (10): DtekAPIJson, DTEK API for JSON sources (GitHub raw files, etc.)., Initialize the JSON DTEK API., DtekAPIBase, _api(), Create a JSON DTEK API instance., Test JsonDtekAPI initialization., Test initialization with group and URLs. (+2 more)

### Community 21 - "Community 21"
Cohesion: 0.17
Nodes (7): Test event merging functionality in DTEK base API., Test that adjacent events are merged in get_events method., Test merging multiple adjacent events., Test that non-adjacent events are not merged., Test merging events with half-hour precision (second/first)., Test that events across midnight are not merged (DTEK doesn't span days)., TestDtekAPIBaseEventMerging

### Community 22 - "Community 22"
Cohesion: 0.17
Nodes (7): Test get_scheduled_events method., Test getting scheduled events with valid preset data., Test getting scheduled events without preset data., Test getting scheduled events without group set., Test getting scheduled events with empty preset data., Test that events are properly filtered by date range., TestDtekAPIBaseScheduledEvents

### Community 23 - "Community 23"
Cohesion: 0.17
Nodes (7): Test get_scheduled_events method., Test getting scheduled events with ScheduleApplies status - now ignored., Test getting scheduled events with WaitingForSchedule status., Test getting scheduled events with EmergencyShutdowns status - now ignored., Test getting scheduled events without data., Test that scheduled events are filtered by date range., TestYasnoApiScheduledEvents

### Community 24 - "Community 24"
Cohesion: 0.29
Nodes (10): ConnectivityState, PlannedOutageEventType, Models for Svitlo Yeah., YasnoPlannedOutageDayStatus, YasnoRegion, ESvitloProvider, E-Svitlo provider model., Yasno provider model. (+2 more)

### Community 25 - "Community 25"
Cohesion: 0.21
Nodes (8): PlannedOutageEvent, Represents an outage event., Test check_outage_data_changed method., Test that first call initializes outage data tracking and returns False., Test that calling with same data returns False and no event fired., Test that calling with changed data returns True and fires event., Test that events are sorted before comparison., TestCheckOutageDataChanged

### Community 26 - "Community 26"
Cohesion: 0.17
Nodes (7): Test getting groups with missing data key., Test getting groups with empty data., Empty schedules arrive as a list ("data": []) — must not crash., Test group-related methods., Test getting groups list., Test getting groups without data., TestDtekAPIBaseGroups

### Community 27 - "Community 27"
Cohesion: 0.23
Nodes (7): IntegrationEntity, Run at exact event start/end., Common logic for Svitlo Yeah entity., Initialize the integration entity., When entity is added, schedule first boundary update., Recalculate active state from events., Schedule callback exactly at next event boundary.

### Community 28 - "Community 28"
Cohesion: 0.18
Nodes (9): ButtonEntity, IntegrationEntity, async_setup_entry(), IntegrationRefreshButton, Button platform for Svitlo Yeah integration., Set up the button platform., Button that forces a coordinator refresh regardless of the timer., Initialize the button. (+1 more)

### Community 29 - "Community 29"
Cohesion: 0.2
Nodes (6): Test data fetching methods., Test successful regions fetch., Test regions fetch with error., Test successful planned outage fetch., Test planned outage fetch without region/provider., TestYasnoApiFetchData

### Community 30 - "Community 30"
Cohesion: 0.2
Nodes (6): Test scheduled events functionality., Test getting scheduled events between dates., Test getting scheduled events when none exist., Test both _get_calendar_event and _get_scheduled_calendar_event methods., Test _get_calendar_event with None event., TestCoordinatorScheduledEvents

### Community 31 - "Community 31"
Cohesion: 0.2
Nodes (6): DtekCoordinatorBase, Get scheduled outage events., Map event to connectivity state., Class to manage fetching DTEK outages data., Initialize the coordinator., Fetch data from DTEK API.

### Community 32 - "Community 32"
Cohesion: 0.24
Nodes (7): Return calendar events within a datetime range., Implementation of the Scheduled Outages Calendar entity., ScheduledOutagesCalendar, Test ScheduledOutagesCalendar entity., Test scheduled calendar entity initialization., Test scheduled calendar event property returns None., TestScheduledOutagesCalendar

### Community 33 - "Community 33"
Cohesion: 0.22
Nodes (7): _api(), emergency_outage_data(), planned_outage_data(), Tests for Svitlo Yeah API., Create an API instance., Sample planned outage data., Sample emergency outage data.

### Community 34 - "Community 34"
Cohesion: 0.22
Nodes (6): ESvitloCoordinator, Map event to connectivity state., Coordinator for E-Svitlo API integration., Initialize the E-Svitlo coordinator., Fetch data from E-Svitlo API., IntegrationCoordinator

### Community 35 - "Community 35"
Cohesion: 0.29
Nodes (6): _minutes_to_time(), Convert minutes from start of day to datetime., Test time conversion methods., Test converting minutes to time., Test converting 24:00 to time., TestYasnoApiTimeConversion

### Community 36 - "Community 36"
Cohesion: 0.25
Nodes (5): Test that event is frozen., Test YasnoPlannedOutageEvent dataclass., Test creating event with datetime., Test creating event with date., TestYasnoPlannedOutageEvent

### Community 37 - "Community 37"
Cohesion: 0.29
Nodes (5): _parse_day_schedule(), Get data for the configured group.          {           'today': {             ', Get all events within the date range., Parse schedule for a single day.      {       "3.1": {         "today": {, Get scheduled events (includes WaitingForSchedule status).

### Community 38 - "Community 38"
Cohesion: 0.25
Nodes (5): _coordinator(), Tests for coordinator functionality., Create a mock coordinator for testing base functionality., Test _event_to_state method for all coordinators., TestCoordinatorEventToState

### Community 39 - "Community 39"
Cohesion: 0.25
Nodes (5): Test timestamp-related methods., Test getting updated timestamp., Test getting updated timestamp without data., Test getting updated timestamp with missing update field., TestDtekAPIBaseTimestamps

### Community 40 - "Community 40"
Cohesion: 0.25
Nodes (5): Test event-related methods., Test getting current event during an outage., Test getting current event when there's no outage., Test getting current event without data., TestDtekAPIBaseEvents

### Community 41 - "Community 41"
Cohesion: 0.25
Nodes (5): Tests for DTEK API factory function and region selection., Test the create_dtek_api factory function., Test creating JSON API when region is specified., Test factory can create JSON APIs for all regions., TestCreateDtekApi

### Community 42 - "Community 42"
Cohesion: 0.25
Nodes (6): _coordinator(), Tests for calendar functionality., Test calendar setup functionality., Create a mock coordinator for testing., test_async_get_events(), TestCalendarSetup

### Community 43 - "Community 43"
Cohesion: 0.33
Nodes (5): Pytest configuration and fixtures., Create an API instance., Create an API instance., _today(), _tomorrow()

### Community 44 - "Community 44"
Cohesion: 0.33
Nodes (4): Test schedule parsing methods., Test parsing day schedule., Test parsing emergency shutdown., TestYasnoApiScheduleParsing

### Community 45 - "Community 45"
Cohesion: 0.33
Nodes (4): Test group-related methods., Test getting groups list., Test getting groups when none loaded., TestYasnoApiGroups

### Community 46 - "Community 46"
Cohesion: 0.33
Nodes (4): Regression: upstream feed serializes an empty schedule as "data": []., get_events must return [] instead of raising AttributeError., get_current_event must return None on list-shaped data., TestDtekAPIBaseEventsListShapedData

### Community 47 - "Community 47"
Cohesion: 0.4
Nodes (4): DtekCoordinatorJson, Class to manage fetching DTEK outage data., Initialize the DtekCoordinatorBase class., DtekCoordinatorBase

## Knowledge Gaps
- **431 isolated node(s):** `Pytest configuration and fixtures.`, `Create an API instance.`, `Create an API instance.`, `Tests for sensor functionality.`, `Create a mock coordinator for testing.` (+426 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **53 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DtekAPIJson` connect `Community 20` to `Community 0`, `Community 1`, `Community 2`, `Community 39`, `Community 40`, `Community 41`, `Community 46`, `Community 47`, `Community 15`, `Community 17`, `Community 21`, `Community 22`, `Community 26`?**
  _High betweenness centrality (0.227) - this node is a cross-community bridge._
- **Why does `IntegrationCoordinator` connect `Community 6` to `Community 0`, `Community 32`, `Community 34`, `Community 3`, `Community 4`, `Community 1`, `Community 38`, `Community 14`, `Community 15`, `Community 16`, `Community 25`, `Community 27`, `Community 28`, `Community 30`, `Community 31`?**
  _High betweenness centrality (0.208) - this node is a cross-community bridge._
- **Why does `YasnoApi` connect `Community 4` to `Community 0`, `Community 1`, `Community 33`, `Community 35`, `Community 37`, `Community 6`, `Community 12`, `Community 45`, `Community 44`, `Community 13`, `Community 19`, `Community 23`, `Community 29`?**
  _High betweenness centrality (0.197) - this node is a cross-community bridge._
- **Are the 16 inferred relationships involving `IntegrationCoordinator` (e.g. with `TestCoordinatorGetNextEventOfType` and `TestCheckOutageDataChanged`) actually correct?**
  _`IntegrationCoordinator` has 16 INFERRED edges - model-reasoned connections that need verification._
- **Are the 14 inferred relationships involving `YasnoApi` (e.g. with `TestYasnoApiInit` and `TestYasnoApiFetchData`) actually correct?**
  _`YasnoApi` has 14 INFERRED edges - model-reasoned connections that need verification._
- **Are the 24 inferred relationships involving `DtekAPIJson` (e.g. with `TestDtekAPIBaseGroups` and `TestDtekAPIBaseParseGroupHours`) actually correct?**
  _`DtekAPIJson` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Are the 25 inferred relationships involving `PlannedOutageEvent` (e.g. with `ESvitloProvider` and `YasnoProvider`) actually correct?**
  _`PlannedOutageEvent` has 25 INFERRED edges - model-reasoned connections that need verification._