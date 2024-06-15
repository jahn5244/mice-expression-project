import pandas as pd
import heapq

class Node:
    def __init__(self, mouse_id, protein_expression):
        self.mouse_id = mouse_id
        self.protein_expression = protein_expression
        self.next = None

def insert_into_linked_list(head, mouse_id, protein_expression):
    new_node = Node(mouse_id, protein_expression)
    
    if head is None or protein_expression > head.protein_expression:
        new_node.next = head
        return new_node
    
    current = head
    while current.next is not None and protein_expression > current.next.protein_expression:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

def retrieve_top5_from_linked_list(head):
    top5 = []
    current = head
    while current is not None and len(top5) < 5:
        top5.append(current.mouse_id)
        current = current.next
    return top5

def calculate_median(min_heap, max_heap):
    if len(min_heap) == len(max_heap):
        return (min_heap[0] - max_heap[0]) / 2
    elif len(min_heap) > len(max_heap):
        return min_heap[0]
    else:
        return -max_heap[0]


def process_dataset(dataset, column_index):
    num_proteins = len(dataset.columns) - 1  # Assuming the first column is MouseID
    max_heap = []
    min_heap = []
    top5_linked_list = None
    bottom5_linked_list = None

    for index, row in dataset.iterrows():
        mouse_id = row[0]
        try:
            protein_value = float(row[column_index])
        except ValueError:
            print(f"Invalid value at column {column_index} for mouse ID {mouse_id}. Skipping.")
            continue

        # Process heaps
        heapq.heappush(max_heap, -protein_value)
        heapq.heappush(min_heap, protein_value)

        # Process linked lists
        top5_linked_list = insert_into_linked_list(top5_linked_list, mouse_id, protein_value)
        bottom5_linked_list = insert_into_linked_list(bottom5_linked_list, mouse_id, -protein_value)

    # Retrieve max and min values
    max_value = -heapq.heappop(max_heap)
    min_value = heapq.heappop(min_heap)

    # Retrieve top and bottom 5 Mouse IDs
    top5_mouse_ids = retrieve_top5_from_linked_list(top5_linked_list)
    bottom5_mouse_ids = retrieve_top5_from_linked_list(bottom5_linked_list)

    median_value = calculate_median(min_heap, max_heap)


    return max_value, min_value, top5_mouse_ids, bottom5_mouse_ids, median_value


def main():
    # Use Pandas to read the csv file of the dataset.
    mydata1 = pd.read_csv("/Users/johnahnline/Downloads/Data_Cortex_Nuclear.csv", header=None)
    # Remove the variables that are not necessary for the analysis.
    mydata1 = mydata1.drop(78, axis='columns')
    mydata1 = mydata1.drop(79, axis='columns')
    mydata1 = mydata1.drop(80, axis='columns')
    mydata1 = mydata1.drop(81, axis='columns')

    # For the input function, use the ValueError to check if the input value is correct
    while True:
        try:
            column_index = int(input("Enter the column index: "))
            if 0 <= column_index <= 77:
                break  # Break the loop if the input is a valid integer within the specified range
            else:
                print("Please enter an integer between 0 and 77 (inclusive).")
        except ValueError:
            print("This is not an integer. Please input again.")
        
    
    # Process the dataset
    max_val, min_val, top5_ids, bottom5_ids, median_val= process_dataset(mydata1, column_index)

    # Print or use the results as needed
    print(f"Max Value at Column Index {column_index}:", max_val)
    print(f"Min Value at Column Index {column_index}:", min_val)
    print(f"Top 5 Mouse IDs for Column Index {column_index}:", top5_ids)
    print(f"Bottom 5 Mouse IDs for Column Index {column_index}:", bottom5_ids)
    print(f"Median Value for Column Index {column_index}:", median_val)    


if __name__ == "__main__":
    main()
