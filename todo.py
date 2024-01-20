import streamlit as st
from PIL import Image
from datetime import datetime, timedelta

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def get_todo():
    return Todo()

class Todo:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, content, due_date):
        self.tasks.append({"content": content, "due_date": due_date})

    def delete_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]

    def mark_completed(self, index):
        if index < len(self.tasks):
            completed_task = self.tasks.pop(index)
            self.completed_tasks.append(completed_task)

    def display_tasks(self):
        if not self.tasks:
            st.write("No tasks to display.")
        else:
            st.write("---- Tasks ----")
            for i, task in enumerate(self.tasks):
                st.write(f"{i + 1}. {task['content']} - Due: {task['due_date'].strftime('%Y-%m-%d')}")

        if not self.completed_tasks:
            st.write("No completed tasks to display.")
        else:
            st.write("---- Completed Tasks ----")
            for i, completed_task in enumerate(self.completed_tasks):
                st.write(f"{i + 1}. {completed_task['content']} - Completed on: {completed_task['completed_date'].strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    st.title("📆 Scheduled To-Do List App")
    st.sidebar.image(Image.open("to-do.jpeg"), use_column_width=True)

    todo = get_todo()

    # Input for adding a task with due date
    new_task = st.text_area("Add a new task:")
    due_date = st.date_input("Due Date", datetime.today() + timedelta(days=1))
    
    if st.button("Add Task"):
        todo.add_task(new_task, due_date)

    # Display current tasks
    st.header("Tasks:")
    todo.display_tasks()

    # Delete and mark as completed buttons
    if todo.tasks:
        selected_task_index = st.radio("Select a task:", list(range(1, len(todo.tasks) + 1))) - 1
        if st.button("Delete"):
            todo.delete_task(selected_task_index)
        if st.button("Mark as Completed"):
            todo.mark_completed(selected_task_index)

            # Display completed tasks in a separate table
            st.table(todo.completed_tasks)

if __name__ == "__main__":
    main()
