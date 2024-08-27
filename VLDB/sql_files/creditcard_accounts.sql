CREATE TABLE Credit_Card_Accounts (
    CreditCardID INT PRIMARY KEY,
    CustomerID INT,
    AccountNumber VARCHAR(20) UNIQUE,
    CreditLimit DECIMAL(15, 2),
    AvailableCredit DECIMAL(15, 2),
    InterestRate DECIMAL(5, 2),
    AnnualFee DECIMAL(10, 2),
    DueDate DATE,
    MinimumPayment DECIMAL(15, 2),
    LateFee DECIMAL(10, 2),
    CardStatus VARCHAR(50), -- e.g., Active, Suspended, Closed
    CardType VARCHAR(50), -- e.g., Visa, MasterCard
    ExpiryDate DATE,
    RiskAssessmentScore INT,
    LastPaymentDate DATE,
    LastPaymentAmount DECIMAL(15, 2),
    BillingCycle VARCHAR(50),
    CreditCardIssuer VARCHAR(100),
    CreditCardOfficerID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
