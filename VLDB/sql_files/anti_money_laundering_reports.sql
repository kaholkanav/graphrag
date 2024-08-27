CREATE TABLE Anti_Money_Laundering_Reports (
    AMLReportID INT PRIMARY KEY,
    CustomerID INT,
    TransactionID INT,
    ReportDate DATE,
    SuspiciousActivity VARCHAR(255),
    ReportStatus VARCHAR(50), -- e.g., Open, Investigating, Closed
    InvestigationStartDate DATE,
    InvestigationEndDate DATE,
    RiskScore INT,
    ReportingOfficer VARCHAR(100),
    RegulatoryComplianceStatus VARCHAR(50),
    EscalationStatus VARCHAR(50),
    ReportingDetails TEXT,
    InvestigativeFindings TEXT,
    ResolutionDate DATE,
    ResolutionDetails TEXT,
    ReportNotes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID)
);
