from datetime import timezone as dt_timezone
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

def _get_current_utc_timestamp() -> str:
    """Returns current UTC timestamp in ISO format with Z suffix."""
    return datetime.now(dt_timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

class HealthResponse(BaseModel):
    """Health check response schema."""
    status: str = Field(default='healthy', description='Service health status')
    timestamp: str = Field(default_factory=_get_current_utc_timestamp, description='UTC timestamp')

class ToolItem(BaseModel):
    """Individual tool item definition."""
    name: str = Field(default='', description='Tool identifier name')
    description: str = Field(default='', description='Tool functional description')
    parameters: Dict[str, Any] = Field(default_factory=dict, description='Tool parameter schema')

class ToolsResponse(BaseModel):
    """Response schema listing available agentic tools."""
    tools: List[Dict[str, Any]] = Field(default_factory=list, description='List of registered tools')

class ComputeTechnologyVelocityRequest(BaseModel):
    """Input request schema for compute_technology_velocity."""
    target_identifier: str = Field(default='langgraph', description='Target technology, package, or repository identifier')
    query_parameter: str = Field(default='velocity', description='Specific query or dimension parameter')
    lat: float = Field(default=0.0, ge=-90.0, le=90.0, description='Latitude coordinate for spatial context')
    lon: float = Field(default=0.0, ge=-180.0, le=180.0, description='Longitude coordinate for spatial context')
    window_steps: int = Field(default=12, ge=1, le=1000, description='Temporal step resolution windows')
    lookback_days: int = Field(default=180, ge=1, le=3650, description='Historical lookback window in days')

class ExplainabilityModel(BaseModel):
    """Explainability metrics and weight distribution breakdown."""
    primary_driver: str = Field(default='adoption_acceleration', description='Primary systemic velocity driver')
    weights: Dict[str, float] = Field(default_factory=lambda: {'velocity': 0.35, 'infrastructure': 0.35, 'propagation': 0.15, 'acceleration': 0.15}, description='Component weighting vector')

class ComputeTechnologyVelocityResponse(BaseModel):
    """Output response schema for compute_technology_velocity."""
    timestamp: str = Field(default_factory=_get_current_utc_timestamp, description='UTC timestamp of computation')
    status: str = Field(default='healthy', description='Execution status')
    primary_metric: float = Field(default=91.6, description='Primary velocity metric score (0-100)')
    secondary_score: float = Field(default=0.94, description='Secondary normalization score')
    state_index: float = Field(default=88.1, description='Calculated composite state index')
    classification: str = Field(default='EXPLOSIVE', description='State classification label (STALLED, SLOW, ACTIVE, RAPID, EXPLOSIVE)')
    infrastructure_health: Optional[str] = Field(default='OPTIMAL', description='Infrastructure health state classification')
    agent_readiness: Optional[str] = Field(default='OPTIMAL', description='Agent execution readiness state classification')
    explainability: ExplainabilityModel = Field(default_factory=ExplainabilityModel, description='Explainability and weighting details')

class SpatialH3TensorRequest(BaseModel):
    """Input request schema for get_spatial_h3_tensor."""
    lat: float = Field(default=2.0442, ge=-90.0, le=90.0, description='Latitude coordinate')
    lon: float = Field(default=102.5689, ge=-180.0, le=180.0, description='Longitude coordinate')
    resolution: int = Field(default=8, ge=0, le=15, description='Uber H3 spatial resolution index (0-15)')

class SpatialH3TensorResponse(BaseModel):
    """Output response schema for get_spatial_h3_tensor."""
    h3_index: str = Field(default='886520d81dfffff', description='Uber H3 cell spatial string identifier')
    spatial_cell: str = Field(default='886520d81dfffff', description='Target spatial cell resolution reference')
    density_score: float = Field(default=64.2, description='Computed network and node density score')
    terrain_state_index: float = Field(default=75.1, description='Regional terrain and routing velocity state index')
    status: str = Field(default='ACTIVE', description='Regional spatial operational status')
    timestamp: str = Field(default_factory=_get_current_utc_timestamp, description='UTC computation timestamp')