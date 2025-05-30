"""Constants for the Continuously Casting Dashboards integration."""

DOMAIN = "continuously_casting_dashboards"
CONF_SWITCH_ENTITY = "switch_entity_id"
CONF_SWITCH_ENTITY_STATE = "switch_entity_state"
PLATFORMS = ["sensor"]  # Add sensor platform here!

# Default configuration values
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_CAST_DELAY = 60
DEFAULT_START_TIME = "07:00"
DEFAULT_END_TIME = "01:00"
DEFAULT_VOLUME = 5
DEFAULT_MAX_RETRIES = 5
DEFAULT_RETRY_DELAY = 10
DEFAULT_VERIFICATION_WAIT_TIME = 15
DEFAULT_CASTING_TIMEOUT = 60
DEFAULT_LOGGING_LEVEL = "warning"

# Logging levels
LOGGING_LEVELS = ["debug", "info", "warning", "error", "critical"]

# File paths
CONFIG_DIR = "/config/continuously_casting_dashboards"
STATUS_FILE = f"{CONFIG_DIR}/status.json"
HEALTH_STATS_FILE = f"{CONFIG_DIR}/health_stats.json"

# Device status types
STATUS_CONNECTED = "connected"
STATUS_DISCONNECTED = "disconnected"  
STATUS_MEDIA_PLAYING = "media_playing"
STATUS_OTHER_CONTENT = "other_content"
STATUS_UNKNOWN = "unknown"
STATUS_STOPPED = "stopped"
STATUS_SPEAKER_GROUP_ACTIVE = "speaker_group_active"
STATUS_CASTING_IN_PROGRESS = "casting_in_progress"

# Health stats event types
EVENT_CONNECTION_ATTEMPT = "connection_attempt"
EVENT_CONNECTION_SUCCESS = "connection_success"
EVENT_DISCONNECTED = "disconnected"
EVENT_RECONNECT_ATTEMPT = "reconnect_attempt"
EVENT_RECONNECT_SUCCESS = "reconnect_success"
EVENT_RECONNECT_FAILED = "reconnect_failed"

# Configuration keys
CONF_LOGGING_LEVEL = "logging_level"
CONF_CAST_DELAY = "cast_delay"
CONF_START_TIME = "start_time"
CONF_END_TIME = "end_time"
CONF_SWITCH_ENTITY_ID = "switch_entity_id"
CONF_SWITCH_ENTITY_STATE = "switch_entity_state"
CONF_DASHBOARD_URL = "dashboard_url"
CONF_VOLUME = "volume"
CONF_SPEAKER_GROUPS = "speaker_groups"

# Translation strings
ERR_DEVICE_ALREADY_EXISTS = "device_already_exists"