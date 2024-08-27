CREATE TABLE Employee_Details (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    EmployeeRole VARCHAR(50), -- e.g., Teller, Manager, Loan Officer
    BranchID INT,
    DateOfJoining DATE,
    EmploymentStatus VARCHAR(50), -- e.g., Active, On Leave, Resigned
    Salary DECIMAL(15, 2),
    ContactNumber VARCHAR(20),
    Email VARCHAR(100),
    EmployeeAddress VARCHAR(255),
    NationalID VARCHAR(50),
    TaxID VARCHAR(50),
    PerformanceRating DECIMAL(5, 2),
    LastPromotionDate DATE,
    ReportingManager VARCHAR(100),
    Department VARCHAR(50),
    ComplianceTrainingStatus VARCHAR(50),
    RiskAssessmentScore INT,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (BranchID) REFERENCES Branch_Details(BranchID)
);
