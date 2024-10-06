import pandas as pd

# Define test cases
test_cases = [
    {
        "Test Case ID": "TC001",
        "Test Case Description": "Verify that a new asset can be added successfully.",
        "Preconditions": "User is logged in and on the 'Add Asset' page.",
        "Test Steps": "1. Enter asset details (name, type, value, acquisition date).\n2. Click the 'Save' button.",
        "Expected Result": "The asset is added to the system and a confirmation message is displayed.",
        "Actual Result": "",
        "Status": "",
        "Remarks": ""
    },
    {
        "Test Case ID": "TC002",
        "Test Case Description": "Verify that an existing asset can be edited successfully.",
        "Preconditions": "User is logged in and on the 'Asset List' page.",
        "Test Steps": "1. Select an asset from the list.\n2. Click the 'Edit' button.\n3. Modify asset details.\n4. Click the 'Save' button.",
        "Expected Result": "The asset details are updated and a confirmation message is displayed.",
        "Actual Result": "",
        "Status": "",
        "Remarks": ""
    },
    {
        "Test Case ID": "TC003",
        "Test Case Description": "Verify that an asset can be deleted successfully.",
        "Preconditions": "User is logged in and on the 'Asset List' page.",
        "Test Steps": "1. Select an asset from the list.\n2. Click the 'Delete' button.\n3. Confirm the deletion.",
        "Expected Result": "The asset is removed from the system and a confirmation message is displayed.",
        "Actual Result": "",
        "Status": "",
        "Remarks": ""
    },
    {
        "Test Case ID": "TC004",
        "Test Case Description": "Verify that asset details can be viewed.",
        "Preconditions": "User is logged in and on the 'Asset List' page.",
        "Test Steps": "1. Select an asset from the list.\n2. Click the 'View' button.",
        "Expected Result": "The asset details are displayed correctly.",
        "Actual Result": "",
        "Status": "",
        "Remarks": ""
    },
    {
        "Test Case ID": "TC005",
        "Test Case Description": "Verify that assets can be searched based on various criteria.",
        "Preconditions": "User is logged in and on the 'Asset List' page.",
        "Test Steps": "1. Enter search criteria (e.g., name, type).\n2. Click the 'Search' button.",
        "Expected Result": "The assets matching the search criteria are displayed.",
        "Actual Result": "",
        "Status": "",
        "Remarks": ""
    },
    {
        "Test Case ID": "TC006",
        "Test Case Description": "Verify that reports of assets can be generated.",
        "Preconditions": "User is logged in and on the 'Reports' page.",
        "Test Steps": "1. Select report criteria (e.g., date range, asset type).\n2. Click the 'Generate Report' button.",
        "Expected Result": "The report is generated and displayed.",
        "Actual Result": "",
        "Status": "",
        "Remarks": ""
    }
]

# Create a DataFrame
df = pd.DataFrame(test_cases)

# Save to Excel
df.to_excel("test_cases.xlsx", index=False)

print("Excel file 'test_cases.xlsx' has been generated.")