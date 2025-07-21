"""
Unit tests for Distributed AI Training Platform
"""

import unittest
import asyncio
from unittest.mock import Mock, patch
from src.main import Distributed AI Training Platform
from src.models import Task, ProcessingStatus, DataProcessor
from src.utils import generate_id, current_timestamp, PerformanceMonitor
from src.config import config

class TestDistributed AI Training Platform(unittest.TestCase):
    def setUp(self):
        self.system = Distributed AI Training Platform()
    
    def test_initialization(self):
        """Test system initialization"""
        self.assertIsNotNone(self.system.config)
        self.assertEqual(self.system.performance_metrics['operations_count'], 0)
    
    def test_config_loading(self):
        """Test configuration loading"""
        self.assertIsInstance(self.system.config, dict)
        self.assertIn('version', self.system.config)
    
    async def test_process_data(self):
        """Test data processing functionality"""
        test_data = [{'id': 1, 'value': 'test'}]
        result = await self.system.process(test_data)
        
        self.assertIsInstance(result, dict)
        self.assertIn('processed_items', result)
        self.assertEqual(result['processed_items'], len(test_data))

class TestModels(unittest.TestCase):
    def test_task_creation(self):
        """Test task model creation"""
        task = Task(id=generate_id(), name="test_task")
        self.assertEqual(task.status, ProcessingStatus.PENDING)
        self.assertIsNotNone(task.created_at)
    
    def test_task_status_update(self):
        """Test task status updates"""
        task = Task(id=generate_id(), name="test_task")
        original_time = task.updated_at
        
        task.update_status(ProcessingStatus.COMPLETED)
        self.assertEqual(task.status, ProcessingStatus.COMPLETED)
        self.assertGreater(task.updated_at, original_time)
    
    def test_data_processor(self):
        """Test data processor functionality"""
        processor = DataProcessor()
        task = Task(id=generate_id(), name="test_task")
        
        processor.add_task(task)
        self.assertEqual(len(processor.tasks), 1)
        
        retrieved_task = processor.get_task_by_id(task.id)
        self.assertEqual(retrieved_task, task)

class TestUtils(unittest.TestCase):
    def test_generate_id(self):
        """Test ID generation"""
        id1 = generate_id()
        id2 = generate_id()
        
        self.assertNotEqual(id1, id2)
        self.assertEqual(len(id1), 12)
    
    def test_timestamp_generation(self):
        """Test timestamp generation"""
        timestamp = current_timestamp()
        self.assertIsInstance(timestamp, str)
        self.assertIn('T', timestamp)
    
    def test_performance_monitor(self):
        """Test performance monitoring"""
        monitor = PerformanceMonitor()
        monitor.start_timer('test')
        
        import time
        time.sleep(0.1)
        
        duration = monitor.end_timer('test')
        self.assertGreater(duration, 0.05)

class TestConfig(unittest.TestCase):
    def test_config_access(self):
        """Test configuration access"""
        self.assertIsNotNone(config.get('debug'))
        self.assertIsNotNone(config.get('api_version'))
    
    def test_config_update(self):
        """Test configuration updates"""
        original_debug = config.get('debug')
        config.update({'debug': not original_debug})
        
        self.assertNotEqual(config.get('debug'), original_debug)

if __name__ == '__main__':
    # Run async tests
    loop = asyncio.get_event_loop()
    
    # Run regular unittest
    unittest.main(verbosity=2)
