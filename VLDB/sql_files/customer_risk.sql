CREATE TABLE Customer_Risk_Profile (
    RiskProfileID INT PRIMARY KEY,
    CustomerID INT,
    RiskCategory VARCHAR(50),
    RiskScore INT,
    RiskAssessmentDate DATE,
    ReviewDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
