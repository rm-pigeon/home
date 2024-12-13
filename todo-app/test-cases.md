## Test Cases Overview

# 1 - Add Task

**Description**
User should be able to add task using add button on the top-left of the screen.
After clicking and filling up the modal, Task should be visible and possible to edit on the main screen.

**Prerequisites**:

-Application opened in the browser

**Steps**:

1.Click on the "Add Task" button on the top-left

2.Fill the Task title in "Title" input field

3.Leave status on default value

4.Click "Add Task"

**Validation Critieria**:

-Task should be visible on the page

-Its status should be the same as defined in add form


# 2 - Update Task

**Description**
User should be able to edit Task on the board. Validation should work correctly 
and status should be possible to change using the dropdown.

**Prerequisites**:

-Previously created Task on the board

**Steps**:

1.Click on the Pencil Icon on the right of the Task row

2.Delete Task Title

3.Click "Update Task"

4.Fill different Title than original one

5.Click on Status dropdown and change the Status on the list

6.Click "Update Task"

**Validation Critieria**:

-Validation should fire up after saving with empty Title field

-Changes should be correctly saved after saving with all fields filled in.

-Data should be displayed properly after Update modal close.

# 3 - Delete Task

**Description**
User should be able to delete Task from the board.

**Prerequisites**:

-Previously created Task on the board

**Steps**:

1.Click on the Trash icon on the right of Task row

**Validation Critieria**:

-Task should be successfully deleted from the board

-Confirmation window should roll-up on the bottom-right of the screen

# 4 - Change Task Status

**Description**
User should be able to change Task Status by clicking on the checkbox on the left of the Task

**Prerequisites**:

-Previously created Task on the board

**Steps**:

a

1.Click on the checkbox on the left of the Task Title

2.Click on the pencil Icon on the right of the Task row

b

1.Click on the checkbox on the left of the Task Title once again

2.Click on the pencil Icon on the right of the Task row

**Validation Critieria**:

a

-Task Title should be crossed out

-Task status should be changed to "Completed"

b

-Task Title should be displayed normally

-Task status should be changed to "Incomplete"

# 5 - Filter Tasks

**Description**
User should be able to filter Tasks by their status.

**Prerequisites**:

-At least two Tasks with different statuses

**Steps**:

a

1.Click on drop-down list on the top-right of the board

2.Click "Incomplete" option

b

1.Click on drop-down list on the top-right of the board

2.Click "Completed" option

**Validation Critieria**:

a

-Only "Incomplete" status Tasks should be visible on the board

b

-Only "Completed" status Tasks should be visible on the board