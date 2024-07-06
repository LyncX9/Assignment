products = []

def list_products():
    print("List of Products:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product}")

def add_product():
    product_name = input("Enter product name: ")
    products.append(product_name)
    print(f"Product '{product_name}' added successfully!")

def delete_product():
    product_name = input("Enter product name to delete: ")
    if product_name in products:
        products.remove(product_name)
        print(f"Product '{product_name}' deleted successfully!")
    else:
        print(f"Product '{product_name}' not found!")

def delete_by_id():
    try:
        id = int(input("Enter product ID to delete: "))
        if id > 0 and id <= len(products):
            del products[id - 1]
            print(f"Product at ID {id} deleted successfully!")
        else:
            print("Invalid ID!")
    except ValueError:
        print("Invalid input! Please enter a valid ID.")

def main():
    while True:
        print("\nMenu:")
        print("1. List Products")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Delete by ID")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            delete_by_id()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()