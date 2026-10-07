def main():
    #INPUT
    client_name = input("Client name: ")
    estimated_work_hours = float(input("Estimated work hours: "))
    hourly_rate = float(input("Hourly rate: "))
    direct_expenses = float(input("Direct expenses: "))
    client_name = client_format(client_name)
    labor_costs = get_labor_costs(estimated_work_hours, hourly_rate)
    total_estimate = get_total_estimate(labor_costs, direct_expenses)
    output_project_estimate(client_name, labor_costs, direct_expenses, total_estimate)
    #PROCESSING
"""
What is the client asking of us? They want us to (1) properly format our name so unnecessary white space isn't an issue &
(2) the capitalization is correct for proper nouns. 
"""
def client_format(client_name):
    formatted_client_name = client_name.strip().title()
    return formatted_client_name
    
"""
We need to get the product for labor costs. If the original example utilizes multiplication from 7.5 * 40 = 300, then we have to
go with the same approach and just multiply, then return the variable into the system for later usage in the main function.
"""
def get_labor_costs(estimated_work_hours, hourly_rate):
    labor_costs = estimated_work_hours * hourly_rate
    return labor_costs

"""
This is essentially the same as last approach but just replace the variables with labor costs and direct expenses, getting the sum with
addition (+) to get the total estimate. Again, we return because without it, we cannot place it into the main function to utilize later.
"""
def get_total_estimate(labor_costs, direct_expenses):
    total_estimate = labor_costs + direct_expenses
    return total_estimate


    #OUTPUT
"""
For the frontend of the project, we need to make the code as readable as possible. Going with the example, we just copy the code and
add a \n to add a new line for user readability and making it look nice. overall, we use .2f for decimal places when needed and f to 
format the .2f properly with the string.
"""
def output_project_estimate(client_name, labor_costs, direct_expenses, total_estimate):
    print("\nPROJECT ESTIMATE")
    print(f"Client: {client_name}")
    print(f"Labor cost: ${labor_costs:.2f}")
    print(f"Direct expenses: ${direct_expenses:.2f}")
    print(f"Total estimate: ${total_estimate:.2f}")

main()
#We call the main to gather input from the user and then run all the other functions in order.