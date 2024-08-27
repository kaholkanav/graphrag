CREATE TABLE Settlement_Reconciliation (
    ReconciliationID INT PRIMARY KEY,
    SettlementID INT,
    ReconciliationDate DATE,
    ReconciliationStatus VARCHAR(50), -- e.g., Completed, Pending, Discrepancy
    DiscrepancyAmount DECIMAL(15, 2),
    DiscrepancyReason VARCHAR(255),
    AdjustedAmount DECIMAL(15, 2),
    AdjustmentDetails TEXT,
    ClearingHouse VARCHAR(100),
    ReconciliationMethod VARCHAR(50), -- e.g., Automated, Manual
    ReconciledBy VARCHAR(100),
    ReconciliationTime TIMESTAMP,
    ReconciliationNotes TEXT,
    ResolutionDate DATE,
    ResolutionStatus VARCHAR(50), -- e.g., Resolved, Escalated
    ComplianceCheckStatus VARCHAR(50),
    AMLCheckStatus VARCHAR(50),
    FraudCheckStatus VARCHAR(50),
    AuditStatus VARCHAR(50),
    RegulatoryApprovalStatus VARCHAR(50),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (SettlementID) REFERENCES Settlement_Data(SettlementID)
);
