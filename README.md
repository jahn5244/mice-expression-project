Mice Protein Expression Analysis
This project analyzes protein expression data from mice, focusing on specific columns of interest. It retrieves the maximum and minimum values, the top and bottom 5 mouse IDs based on protein expression, and the median value for a selected column.

Table of Contents
Installation
Usage
Functions
insert_into_linked_list
retrieve_top5_from_linked_list
calculate_median
process_dataset
Running Tests
License
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/jahn5244/miceexpressionproject.git
Navigate to the project directory:

sh
Copy code
cd miceexpressionproject
Install the required dependencies:

sh
Copy code
pip install pandas
Usage
Ensure you have the dataset Data_Cortex_Nuclear.csv in the appropriate directory.

Run the script:

sh
Copy code
python main.py
You will be prompted to enter a column index (between 0 and 77) for analysis.

Functions
insert_into_linked_list
Inserts a new node into a linked list maintaining the order based on protein expression values.

Parameters:

head: The head node of the linked list.
mouse_id: The mouse ID to be inserted.
protein_expression: The protein expression value to be inserted.
Returns:

The head node of the modified linked list.
retrieve_top5_from_linked_list
Retrieves the top 5 mouse IDs from the linked list based on protein expression values.

Parameters:

head: The head node of the linked list.
Returns:

A list of top 5 mouse IDs.
calculate_median
Calculates the median value from two heaps (min-heap and max-heap).

Parameters:

min_heap: The min-heap containing protein expression values.
max_heap: The max-heap containing protein expression values.
Returns:

The median value.
process_dataset
Processes the dataset to retrieve the max, min, top 5, bottom 5 mouse IDs, and the median value for a specified column index.

Parameters:

dataset: The dataset to be processed.
column_index: The index of the column to analyze.
Returns:

A tuple containing max value, min value, top 5 mouse IDs, bottom 5 mouse IDs, and the median value.
Running Tests
To run the tests, use the following command:

sh
Copy code
python -m unittest discover
The tests validate the functionality of the process_dataset function using predefined datasets.

License
This project is licensed under the MIT License. See the LICENSE file for details.
