# main.py

import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

class TaskManager:
    """
    A simple task management system that demonstrates basic Python functionality.
    Features:
    - Task creation and management
    - Data persistence using JSON
    - Error handling
    - Logging
    """

    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description, priority="medium"):
        """Add a new task to the task list."""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed": False
        }
        
        self.tasks.append(task)
        logging.info(f"Task created: {title}")
        self.save_tasks()
        return task

    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                logging.info(f"Task completed: {task['title']}")
                self.save_tasks()
                return True
        logging.warning(f"Task not found: {task_id}")
        return False

    def list_tasks(self, show_completed=False):
        """List all tasks, optionally including completed ones."""
        return [task for task in self.tasks if show_completed or not task["completed"]]

    def save_tasks(self):
        """Save tasks to a JSON file."""
        try:
            with open('tasks.json', 'w') as f:
                json.dump(self.tasks, f, indent=2)
            logging.info("Tasks saved successfully")
        except Exception as e:
            logging.error(f"Error saving tasks: {str(e)}")

    def load_tasks(self):
        """Load tasks from a JSON file."""
        try:
            with open('tasks.json', 'r') as f:
                self.tasks = json.load(f)
            logging.info("Tasks loaded successfully")
        except FileNotFoundError:
            logging.info("No existing tasks file found")
        except Exception as e:
            logging.error(f"Error loading tasks: {str(e)}")

def main():
    """Main function to demonstrate TaskManager usage."""
    # Create an instance of TaskManager
    manager = TaskManager()

    # Add some sample tasks
    manager.add_task(
        "Create GitHub Repository",
        "Initialize a new repository for the project",
        "high"
    )
    manager.add_task(
        "Write Documentation",
        "Create README.md and add project documentation",
        "medium"
    )
    manager.add_task(
        "Implement Unit Tests",
        "Add unit tests for all major functions",
        "high"
    )

    # List all uncompleted tasks
    print("\nCurrent Tasks:")
    for task in manager.list_tasks():
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Priority: {task['priority']}")
        print(f"Created: {task['created_at']}")
        print("-" * 30)

    # Complete a task
    manager.complete_task(1)

    # List all tasks including completed
    print("\nAll Tasks (including completed):")
    for task in manager.list_tasks(show_completed=True):
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['title']} (Priority: {task['priority']})")

if __name__ == "__main__":
    main()
