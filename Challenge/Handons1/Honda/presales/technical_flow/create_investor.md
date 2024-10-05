title Face to face investor registration
participant RM
    participant UI
    participant Backend
    participant Database

    RM->>UI: Open Registration Form
    UI->>RM: Display Form
    RM->>UI: Fill Form and Submit
    UI->>Backend: Send Form Data (/registerInvestor)
    Backend->>Backend: Validate Data
    Backend->>Database: Check for Existing Investor
    Database-->>Backend: Investor Not Found
    Backend->>Database: Save New Investor Data
    Database-->>Backend: Save Success
    Backend-->>UI: Return Success Message
    UI-->>RM: Display Success Message