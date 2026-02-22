import json 



def load_tasks():
	with open("tasks.json", "r") as file:
		return json.load(file)

def save_tasks(tasks):
	with open("tasks.json", "w") as file:
		json.dump(tasks, file, indent=4)

def add_task():
	tasks = load_tasks()
	title = input("Enter task: ")

	task = {
		"title": title,
		"completed": False
	}

	tasks.append(task)
	save_tasks(tasks)
	print("Task added!")

def view_tasks():
	tasks = load_tasks()

	if not tasks: 
		print("No tasks found.")
		return

	for i, task in enumerate(tasks):
		status = "✓" if task["completed"] else "✗"
		print(f"{i + 1}. [{status}] {task['title']}")


def complete_task():
	tasks = load_tasks()
	view_tasks()
	
	index = int(input("Enter task number to complete: ")) - 1

	if 0 <= index < len(tasks):
		tasks[index]["completed"] = True
		save_tasks(tasks)
		print("Task marked complete!")
	else:
		print("Invalid task number.")

def main():
	while True:
		print("\nTask Manager")
		print("1. Add Task")
		print("2. View Tasks")
		print("3. Complete Task")
		print("4. Delete Task")
		print("5. Exit")
		
		choice = input("Choose an option: ")

		if choice == "1":
			add_task()
		elif choice == "2":
			view_tasks()
		elif choice == "3":
			complete_task() 
		elif choice == "4":
			delete_task()
		elif choice == "5":
			break
		else: 
			print("Invalid choice. ")
if __name__ == "__main__":
	main()
