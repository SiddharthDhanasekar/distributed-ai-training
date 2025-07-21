"""
Utility functions for Distributed AI Training Platform
"""

import time
import hashlib
import json
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone

def generate_id() -> str:
    """Generate a unique identifier"""
    timestamp = str(int(time.time() * 1000000))
    return hashlib.md5(timestamp.encode()).hexdigest()[:12]

def current_timestamp() -> str:
    """Get current UTC timestamp in ISO format"""
    return datetime.now(timezone.utc).isoformat()

def safe_json_loads(data: str, default=None) -> Any:
    """Safely load JSON data with error handling"""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default

def batch_process(items: List[Any], batch_size: int = 100):
    """Process items in batches"""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

def retry_operation(func, max_retries: int = 3, delay: float = 1.0):
    """Retry operation with exponential backoff"""
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(delay * (2 ** attempt))

class PerformanceMonitor:
    def __init__(self):
        self.metrics = {}
    
    def start_timer(self, name: str):
        self.metrics[name] = {'start': time.time()}
    
    def end_timer(self, name: str) -> float:
        if name in self.metrics:
            duration = time.time() - self.metrics[name]['start']
            self.metrics[name]['duration'] = duration
            return duration
        return 0.0
    
    def get_metrics(self) -> Dict[str, Any]:
        return self.metrics.copy()
