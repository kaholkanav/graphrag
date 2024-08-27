CREATE TABLE Customer_KYC_Details (
    KYCID INT PRIMARY KEY,
    CustomerID INT,
    KYCStatus VARCHAR(50),
    KYCExpiryDate DATE,
    KYCVerificationDate DATE,
    IDProofType VARCHAR(50),
    IDProofNumber VARCHAR(50),
    AddressProofType VARCHAR(50),
    AddressProofNumber VARCHAR(50),
    RiskCategory VARCHAR(50),
    PoliticallyExposedPerson BOOLEAN,
    SourceOfWealth VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
