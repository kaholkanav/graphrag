CREATE TABLE Settlement_Disputes (
    DisputeID INT PRIMARY KEY,
    SettlementID INT,
    DisputeDate DATE,
    DisputeStatus VARCHAR(50), -- e.g., Open, Resolved, Escalated
    DisputeReason VARCHAR(255),
    DisputedAmount DECIMAL(15, 2),
    ResolutionDate DATE,
    ResolutionDetails TEXT,
    ResponsibleParty VARCHAR(100),
    ComplianceCheckStatus VARCHAR(50),
    RegulatoryApprovalStatus VARCHAR(50),
    SettlementCorrectionAmount DECIMAL(15, 2),
    SettlementCorrectionDetails TEXT,
    DisputeNotes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (SettlementID) REFERENCES Settlement_Data(SettlementID)
);
