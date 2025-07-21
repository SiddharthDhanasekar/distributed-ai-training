"""
Data models and classes for Distributed AI Training Platform
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime
from enum import Enum

class ProcessingStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    id: str
    name: str
    status: ProcessingStatus = ProcessingStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    priority: int = 0
    
    def update_status(self, status: ProcessingStatus):
        self.status = status
        self.updated_at = datetime.now()

@dataclass
class ProcessingResult:
    task_id: str
    success: bool
    data: Any = None
    error: Optional[str] = None
    execution_time: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class SystemMetrics:
    total_tasks: int = 0
    completed_tasks: int = 0
    failed_tasks: int = 0
    avg_processing_time: float = 0.0
    system_load: float = 0.0
    memory_usage: float = 0.0
    uptime: float = 0.0
    
    @property
    def success_rate(self) -> float:
        if self.total_tasks == 0:
            return 0.0
        return (self.completed_tasks / self.total_tasks) * 100

class DataProcessor:
    def __init__(self):
        self.tasks: List[Task] = []
        self.results: List[ProcessingResult] = []
    
    def add_task(self, task: Task):
        self.tasks.append(task)
    
    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)
    
    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.tasks if task.status == ProcessingStatus.PENDING]
    
    def get_metrics(self) -> SystemMetrics:
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.status == ProcessingStatus.COMPLETED])
        failed = len([t for t in self.tasks if t.status == ProcessingStatus.FAILED])
        
        avg_time = 0.0
        if self.results:
            avg_time = sum(r.execution_time for r in self.results) / len(self.results)
        
        return SystemMetrics(
            total_tasks=total,
            completed_tasks=completed,
            failed_tasks=failed,
            avg_processing_time=avg_time
        )
