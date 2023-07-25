from prettytable import PrettyTable

table = PrettyTable()

for numeric in range(27, 30+1):
    table.field_names = [f"Multiply with {numeric}", "Result"]

    for multiper in range(1, 12+1):
        table.add_row([f"{numeric} x {multiper}", numeric * multiper])

    print(table)
    table.clear()
