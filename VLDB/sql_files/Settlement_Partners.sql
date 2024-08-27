CREATE TABLE Settlement_Partners (
    PartnerID INT PRIMARY KEY,
    PartnerName VARCHAR(100),
    PartnerType VARCHAR(50), -- e.g., Bank, Financial Institution, Clearing House
    ContactPerson VARCHAR(100),
    ContactNumber VARCHAR(20),
    ContactEmail VARCHAR(100),
    PartnerSWIFTCode VARCHAR(20),
    PartnerAddress VARCHAR(255),
    PartnershipStartDate DATE,
    PartnershipStatus VARCHAR(50), -- e.g., Active, Inactive
    RegulatoryComplianceStatus VARCHAR(50),
    AMLCheckStatus VARCHAR(50),
    RiskAssessmentScore INT,
    SettlementFrequency VARCHAR(50), -- e.g., Daily, Weekly, Monthly
    SettlementLimit DECIMAL(15, 2),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
