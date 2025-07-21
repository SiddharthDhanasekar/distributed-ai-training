"""
Configuration settings for Distributed AI Training Platform
"""

import os
from typing import Dict, Any

class Config:
    def __init__(self):
        self.settings = {
            'debug': os.getenv('DEBUG', 'false').lower() == 'true',
            'log_level': os.getenv('LOG_LEVEL', 'INFO'),
            'max_workers': int(os.getenv('MAX_WORKERS', '4')),
            'timeout': int(os.getenv('TIMEOUT', '30')),
            'api_version': '1.0.0',
            'features': {
                'async_processing': True,
                'caching': True,
                'monitoring': True,
                'auto_scaling': True
            }
        }
    
    def get(self, key: str, default=None) -> Any:
        return self.settings.get(key, default)
    
    def update(self, updates: Dict[str, Any]):
        self.settings.update(updates)

# Global configuration instance
config = Config()
