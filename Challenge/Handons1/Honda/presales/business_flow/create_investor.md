flowchart TD
    A[Investor Initiation] -->|Choose Face-to-Face| B[Face-to-Face Process]
    A -->|Choose Remote| C[Remote Process]
    
    subgraph Face-to-Face Process
        B1[Meet with Representative]
        B2[Collect Required Documents]
        B3[Enter Investor Details into System]
    end
    
    subgraph Remote Process
        C1[Fill Out Online Registration Form]
        C2[Upload Required Documents]
        C3[Perform KYC Verification]
        C4[Enter Investor Details into System]
    end
    
    B3 --> D[Common Steps]
    C4 --> D
    
    subgraph Common Steps
        D1[Validate Investor Details]
        D2[Save Investor Details to Database]
    end
    
    D --> E[Completion]
    
    subgraph Completion
        E1[Send Confirmation to Investor]
        E2[Investor Receives Confirmation]
    end