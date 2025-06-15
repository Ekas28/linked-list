class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return

        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index must be a positive integer (1-based).")

        if n == 1:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted node with value: {deleted_value}")
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        prev.next = current.next
        print(f"Deleted node with value: {current.data}")

if __name__ == "__main__":
    ll = LinkedList()

    print("Creating linked list with values: 10, 20, 30, 40")
    for value in [10, 20, 30, 40]:
        ll.add_node(value)

    while True:
        ll.print_list()

        if not ll.head:
            print("The list is now empty. No more deletions possible.")
            break

        try:
            pos = int(input("Enter the position of the node to delete: "))
            ll.delete_nth_node(pos)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue
        except Exception as e:
            print("Error:", e)
            continue

        choice = input("Do you want to delete another node? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Stopping deletions. Final list:")
            ll.print_list()
            break

