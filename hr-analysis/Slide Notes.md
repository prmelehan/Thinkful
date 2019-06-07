# Notes

- Roughly ~2% of rows contain 1 or more null values. Those have been dropped. 109 rows with 1+ null values in columns.

- The original shape is (4410, 28), and the subsequent shape after dropping nulls is (4300, 28). After dummifying our variables (removing the first column) our shape is (4300, 69)

- Our original distribution of Attrition had roughly 16% of the values in the Leaving class. In other words, the dominant class was the group of employees who did not leave the company.
