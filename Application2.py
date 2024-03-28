def rekap_barang():
  # Initialize a dictionary to store cosmetics along with purchase price, selling price, supplier price, and stock
  cosmetics = {
      'Lipstick': {'purchase_price': 100000, 'selling_price': 110000, 'supplier_price': 80000, 'stock': 50},
      'Mascara': {'purchase_price': 80000, 'selling_price': 88000, 'supplier_price': 60000, 'stock': 100},
      'Foundation': {'purchase_price': 150000, 'selling_price': 165000, 'supplier_price': 100000, 'stock': 30},
      'Eyeliner': {'purchase_price': 70000, 'selling_price': 77000, 'supplier_price': 50000, 'stock': 80},
      'Blush': {'purchase_price': 90000, 'selling_price': 99000, 'supplier_price': 65000, 'stock': 60},
      'Eyeshadow': {'purchase_price': 120000, 'selling_price': 132000, 'supplier_price': 85000, 'stock': 40},
      'Highlighter': {'purchase_price': 110000, 'selling_price': 121000, 'supplier_price': 75000, 'stock': 70},
      'Concealer': {'purchase_price': 130000, 'selling_price': 143000, 'supplier_price': 90000, 'stock': 20}
  }

  # Function to display the list of cosmetics and their stock
  def display_cosmetics():
      print("===========================================================================================")
      print("| {:<15} | {:<15} | {:<15} | {:<15} | {:<10} |".format("Cosmetic", "Supplier Price", "Purchase Price", "Selling Price", "Stock"))
      print("===========================================================================================")
      for cosmetic, info in cosmetics.items():
          print("| {:<15} | {:<15} | {:<15} | {:<15} | {:<10} |".format(cosmetic, info['supplier_price'], info['purchase_price'], info['selling_price'], info['stock']))
      print("===========================================================================================")
      print()

  # Function to make transactions
  def transaction():
      total_transaction = 0
      total_profit = 0

      while True:
          display_cosmetics()
          cosmetic = input("Enter the cosmetic to purchase: ")

          # Check if the cosmetic is available
          if cosmetic in cosmetics:
              # Check cosmetic stock
              if cosmetics[cosmetic]['stock'] > 0:
                  purchase_price = cosmetics[cosmetic]['purchase_price']
                  selling_price = cosmetics[cosmetic]['selling_price']
                  profit = selling_price - cosmetics[cosmetic]['supplier_price']  # Profit calculation
                  print("Selling Price:", "Rp", selling_price)
                  print("Profit per Unit:", "Rp", profit)

                  # Update stock and total transaction
                  cosmetics[cosmetic]['stock'] -= 1
                  total_transaction += selling_price
                  total_profit += profit

                  print("The", cosmetic, "has been purchased.")
                  print("Total Temporary Transaction:", "Rp", total_transaction)
                  print()
              else:
                  print("Sorry, the stock for", cosmetic, "is empty.")
          else:
              print("The", cosmetic, "is not available.")

          more_transactions = input("Are there more transactions? (y/n): ")
          if more_transactions.lower() != 'y':
              break

      print("===========================================================================================")
      print("Total Transaction:", "Rp", total_transaction)
      print("Total Profit:", "Rp", total_profit)
      print("===========================================================================================")

  # Call the transaction function
  transaction()

# Call the rekap_barang function
rekap_barang()