CREATE TABLE Transaction_Charges (
    ChargeID INT PRIMARY KEY,
    TransactionID INT,
    ChargeType VARCHAR(50), -- e.g., Service Fee, Convenience Fee
    ChargeAmount DECIMAL(10, 2),
    ChargeCurrency VARCHAR(3),
    ChargeDate DATE,
    ChargeStatus VARCHAR(50), -- e.g., Applied, Waived, Refunded
    TaxAmount DECIMAL(10, 2),
    TaxRate DECIMAL(5, 2),
    TotalChargeAmount DECIMAL(15, 2),
    ChargeDescription VARCHAR(255),
    WaiverReason VARCHAR(255),
    AppliedBy VARCHAR(100),
    SettlementID INT,
    RegulatoryCompliance VARCHAR(50),
    ChargeApprovalStatus VARCHAR(50),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID),
    FOREIGN KEY (SettlementID) REFERENCES Settlement_Data(SettlementID)
);
