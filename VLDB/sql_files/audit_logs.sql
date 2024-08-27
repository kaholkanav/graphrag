CREATE TABLE Audit_Logs (
    AuditLogID INT PRIMARY KEY,
    AuditDate DATE,
    AuditType VARCHAR(50), -- e.g., Internal, External, Regulatory
    AuditedEntity VARCHAR(100), -- e.g., Account, Customer, Transaction
    CustomerID INT,
    AccountID INT,
    TransactionID INT,
    Auditor VARCHAR(100),
    AuditStatus VARCHAR(50), -- e.g., Completed, Pending, Escalated
    Findings TEXT,
    ComplianceCheckStatus VARCHAR(50),
    CorrectiveActions TEXT,
    EscalationStatus VARCHAR(50),
    FinalReportDate DATE,
    FinalReportDetails TEXT,
    ResolutionStatus VARCHAR(50),
    ResolutionDate DATE,
    ResolutionDetails TEXT,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID)
);
