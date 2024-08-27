CREATE TABLE Account_Holders (
    HolderID INT PRIMARY KEY,
    AccountID INT,
    CustomerID INT,
    HolderType VARCHAR(20), -- e.g., Primary, Secondary
    HolderStatus VARCHAR(20),
    RelationshipWithPrimary VARCHAR(50),
    SignatureFilePath VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
