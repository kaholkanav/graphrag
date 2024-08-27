CREATE TABLE Loan_Applications (
    ApplicationID INT PRIMARY KEY,
    CustomerID INT,
    LoanType VARCHAR(50), -- e.g., Personal, Home, Auto
    LoanAmount DECIMAL(15, 2),
    ApplicationDate DATE,
    ApplicationStatus VARCHAR(50), -- e.g., Pending, Approved, Rejected
    ApprovedAmount DECIMAL(15, 2),
    ApprovedDate DATE,
    RejectionReason VARCHAR(255),
    LoanTermInMonths INT,
    InterestRate DECIMAL(5, 2),
    RepaymentSchedule VARCHAR(50), -- e.g., Monthly, Quarterly
    CollateralRequired BOOLEAN,
    CollateralDetails TEXT,
    CreditScore INT,
    ProcessingFee DECIMAL(10, 2),
    DisbursementDate DATE,
    DisbursedBy VARCHAR(100),
    LoanPurpose VARCHAR(255),
    RiskGrade VARCHAR(50),
    LoanOfficerID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
