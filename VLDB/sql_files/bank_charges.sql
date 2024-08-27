CREATE TABLE Bank_Charges (
    ChargeID INT PRIMARY KEY,
    ChargeType VARCHAR(50), -- e.g., Account Maintenance, Late Payment
    ChargeDescription VARCHAR(255),
    Amount DECIMAL(15, 2),
    ApplicableTo VARCHAR(50), -- e.g., Savings Account, Fixed Deposit
    Frequency VARCHAR(50), -- e.g., Monthly, Annually
    ChargeDate DATE,
    ChargeStatus VARCHAR(50), -- e.g., Applied, Waived
    TaxAmount DECIMAL(10, 2),
    TotalChargeAmount DECIMAL(15, 2),
    RegulatoryComplianceStatus VARCHAR(50),
    ApprovedBy VARCHAR(100),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
