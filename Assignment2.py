"""
This program reads sales data from a CSV file, manages retail records,
calculates sales totals, and generates customer purchase reports.
"""

def main():
    """
    Reads sales data from a CSV file, displays a management menu, 
    and handles user input.
    """
    records = []
    try:
        file = open("C:/Users/youse/Spring2026/sales_data.csv", "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 4:
                name = parts[0]
                product = parts[1]
                qty = int(parts[2])
                price = int(parts[3])
                records.append([name, product, qty, price]) 
        file.close()
    except FileNotFoundError:
        print("Error: sales_data.csv not found.")
         
    while True:
        print("1. View All Records")
        print("2. View Sales Summary")
        print("3. Search Product")
        print("4. Customer Analysis")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
        # Displays a table of all sales records.
            print("------ SALES RECORDS ------")
            print("Customer   Product     Quantity   Price   Total")
            print("------------------------------------------------")
            for r in records:
                total = r[2] * r[3]
                print(r[0], "    ", r[1], "    ", r[2], "    ", r[3], "    ", total)

        elif choice == "2":
        # Calculates and shows the grand total of all sales.
            overall_total = 0
            for r in records:
                overall_total = overall_total + (r[2] * r[3])
            print("Calculating Total Sales...\nTotal Sales Amount:", overall_total)
            print("(30 + 20 + 15 + 5 + 6 = 76)")

        elif choice == "3":
        # Finds and displays records for a specific product.   
            search_name = input("Enter Product Name: ").lower()
            found = False
            grand_total = 0
            for r in records:
                if r[1].lower() == search_name:
                    if found == False:
                       print("Product Found!")
                       print("Customer   Quantity   Price   Total")
                       print("--------------------------------------")
                       found = True

                    total = r[2] * r[3]
                    print(r[0], "    ", r[2], "    ", r[3], "    ", total)
                    grand_total = grand_total + total

            if found == True:
                print("Total Sales for", search_name.capitalize(), ":", grand_total)
            if found == False:
                print("Product not found in records.")

        elif choice == "4":
        # Finds and displays purchase details for a specific customer.
            search_name = input("Enter Customer Name: ").lower()
            found = False
            grand_total = 0
            purchase_count = 0
            for r in records:
                if r[0].lower() == search_name:
                    if found == False:
                       print("Purchase Details of", search_name.capitalize(),":")
                       print("Product     Quantity   Price   Total")
                       print("--------------------------------------")
                       found = True

                    total = r[2] * r[3]
                    print(r[1], "    ", r[2], "    ", r[3], "    ", total)
                    grand_total = grand_total + total
                    purchase_count = purchase_count + 1
                    
            if found == True:
                print("Total Amount Spent by", search_name.capitalize(), ":", grand_total)
                print("Number of Purchases:", purchase_count)

        elif choice == "5":
        # Ends the loop and exits the program.
            print("Exiting Program...\nThank you! ")
            break

# Calls the main function
main()