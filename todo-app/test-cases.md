## Test Cases Overview

# 1 - Add Task

Description
User should be able to add task using add button on the top-left of the screen.
After clicking and filling up the modal, Task should be visible and possible to edit on the main screen.

Prerequisites:
-Application opened in the browser

Steps:
-Click on the "Add Task" button on the top-left
-Fill the Task title in "Title" input field
-Leave status on default value
-Click "Add Task"

Validation Critieria:
-Task should be visible on the page
-Its status should be the same as defined in add form


# 2 Update Task

Description
User should be able to edit Task on the board. Validation should work correctly 
and status should be possible to change using the dropdown.

Prerequisites:
-Previously created Task on the board

Steps:
-Click on the Pencil Icon on the right of the Task row
-Delete Task Title
-Click "Update Task"
-Fill different Title than original one
-Click on Status dropdown and change the Status on the list
-Click "Update Task"

Validation Critieria:
-Validation should fire up after saving with empty Title field
-Changes should be correctly saved after saving with all fields filled in.
-Data should be displayed properly after Update modal close.

# 3 Delete Task

Description
User should be able to delete Task from the board.

Prerequisites:
-Previously created Task on the board

Steps:
-Click on the Trash icon on the right of Task row

Validation Critieria
-Task should be successfully deleted from the board
-Confirmation window should roll-up on the bottom-right of the screen

# 4 Change Task Status

Description
User should be able to change Task Status by clicking on the checkbox on the left of the Task

Prerequisites:
-Previously created Task on the board

Steps:
a
-Click on the checkbox on the left of the Task Title
-Click on the pencil Icon on the right of the Task row
b
-Click on the checkbox on the left of the Task Title once again
-Click on the pencil Icon on the right of the Task row

Validation Critieria:
a
-Task Title should be crossed out
-Task status should be changed to "Completed"
b
-Task Title should be displayed normally
-Task status should be changed to "Incomplete"

# 5 Filter Tasks

Description
User should be able to filter Tasks by their status.

Prerequisites:
-At least two Tasks with different statuses

Steps:
a
-Click on drop-down list on the top-right of the board
-Click "Incomplete" option
b
-Click on drop-down list on the top-right of the board
-Click "Completed" option

Validation Critieria:
a
-Only "Incomplete" status Tasks should be visible on the board
b
-Only "Completed" status Tasks should be visible on the board