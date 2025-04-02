# Smart TaskBot

Smart TaskBot is an intelligent personal productivity assistant designed to help users organize their schedules, track tasks, and provide timely reminders. By leveraging the capabilities of Large Language Models (LLMs), Smart TaskBot interprets natural language inputs to manage tasks effectively.

## Features

- **Natural Language Task Input:** Add tasks using natural language commands, such as "Remind me to call John on Friday at 6 PM."
- **Task Management:** View, delete, and manage your tasks seamlessly.
- **Autonomous Scheduling:** Automatically schedules tasks based on user input and existing commitments.
- **Integration with External Calendars:** (Planned) Sync tasks with external calendar systems for comprehensive schedule management.

## Project Structure

- `main.py`: The main entry point for the application, handling user interactions.
- `agent.py`: Contains functions that utilize LLMs to interpret user inputs and generate task details.
- `task_manager.py`: Manages task storage, retrieval, and scheduling logic.
- `tasks.json`: A JSON file used to persist tasks between sessions.
