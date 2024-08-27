CREATE TABLE IF NOT EXISTS Clearing_Houses (
    ClearingHouseID INT PRIMARY KEY,
    ClearingHouseName VARCHAR(100),
    ClearingHouseCode VARCHAR(50),
    ContactPerson VARCHAR(100),
    ContactNumber VARCHAR(20),
    ContactEmail VARCHAR(100),
    ClearingHouseSWIFTCode VARCHAR(20),
    ClearingHouseAddress VARCHAR(255),
    OperatingHours VARCHAR(50),
    SettlementFrequency VARCHAR(50), -- e.g., Hourly, Daily
    ComplianceCheckStatus VARCHAR(50),
    AMLCheckStatus VARCHAR(50),
    RiskAssessmentScore INT,
    RegulatoryApprovalStatus VARCHAR(50),
    SettlementInstructions TEXT,
    OperationalNotes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
