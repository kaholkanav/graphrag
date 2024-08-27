CREATE TABLE Payment_Instructions (
    PaymentInstructionID INT PRIMARY KEY,
    CustomerID INT,
    AccountID INT,
    PaymentAmount DECIMAL(15, 2),
    PaymentDate DATE,
    PaymentStatus VARCHAR(50), -- e.g., Scheduled, Executed, Cancelled
    PaymentMethod VARCHAR(50), -- e.g., Bank Transfer, Credit Card
    BeneficiaryName VARCHAR(100),
    BeneficiaryAccountNumber VARCHAR(20),
    BeneficiaryBankName VARCHAR(100),
    BeneficiaryBankSWIFT VARCHAR(20),
    ReferenceNumber VARCHAR(50),
    PurposeOfPayment VARCHAR(255),
    PaymentCurrency VARCHAR(3),
    ScheduledPaymentDate DATE,
    RecurrencePattern VARCHAR(50), -- e.g., Monthly, Quarterly
    NextPaymentDate DATE,
    InstructionSource VARCHAR(50), -- e.g., Online, In-branch
    PaymentChannel VARCHAR(50), -- e.g., Mobile, Web
    TransactionID INT,
    RiskAssessmentScore INT,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account_Master(AccountID),
    FOREIGN KEY (TransactionID) REFERENCES Transaction_Master(TransactionID)
);
