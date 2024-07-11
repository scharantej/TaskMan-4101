**React Todo App Design Using Python Flask and Bootstrap**

## HTML Files

### index.html
- The main page of the application, containing the todo list.
- It uses Bootstrap for styling and may include:
    - An input field for adding new todos
    - A list of existing todos, each with a checkbox for completion
    - A button to remove completed todos

## Routes

### /
- The route for the index page, serving the `index.html` file.

### /add_todo
- A POST route to add a new todo to the list.
- It takes the todo text from the request and adds it to the database.
- Redirects back to the index page.

### /remove_completed
- A POST route to remove all completed todos from the list.
- Redirects back to the index page.