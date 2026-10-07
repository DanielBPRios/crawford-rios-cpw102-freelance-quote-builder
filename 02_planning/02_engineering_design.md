# Engineering Design

**Team members: Daniel Rios & Zachary Crawford**

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

*List each input and its Python data type.*
input str client_name
input str estimated_work_hours
input str hourly_rate
input str direct_expenses

## Processing

```text
*What calculations, text clean up, numberic converstions, ext will the program perform on the inputs?*
process client's name, removeing leading and trailing whitespace. Convert our other 3 numerical inputs to floats. Calculate Labor Cost, then Total Estimate.
```

## Output

*What will the program display? How will you format it?* Our program will display four separate lines, first being client name, second being labor costs, then third being direct expenses, and finally the total estimates, with the last three having their costs labeled with $ and two decimal places for cents.

## Functions

*Describe `main()` and at least one calculation function. For each, give its name, purpose, parameters, and returned result (or none).*

main() should take inputs from the user and print at the end after calculations. get_labor_costs function calculates hourly rate multiplied by estimated work hours. get_labor_costs's parameters are hourly_rate and estimated_work_hours. The returned result should return a float value to main. 
