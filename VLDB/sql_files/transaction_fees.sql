CREATE TABLE Transaction_Fees (
    FeeID INT PRIMARY KEY,
    TransactionID INT,
    FeeType VARCHAR(50), -- e.g., Processing Fee, Service Fee
    FeeAmount DECIMAL(10, 2),
    FeeCurrency VARCHAR(3),
    FeeDate DATE,
    FeeStatus VARCHAR(50), -- e.g., Charged, Waived, Refunded
    TaxAmount DECIMAL(10, 2),
    TaxRate DECIMAL(5, 2),
    TotalFeeAmount DECIMAL(15, 2),
    FeeDescription VARCHAR(255),
    WaiverReason VARCHAR(255),
    RegulatoryCompliance VARCHAR(50),
    AppliedBy VARCHAR(100),
    SettlementID INT,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID),
    FOREIGN KEY (SettlementID) REFERENCES Settlement_Data(SettlementID)
);
