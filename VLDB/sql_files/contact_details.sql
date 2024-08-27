CREATE TABLE Customer_Contact_Details (
    ContactID INT PRIMARY KEY,
    CustomerID INT,
    ContactType VARCHAR(50),
    ContactDetail VARCHAR(255),
    IsPrimaryContact BOOLEAN,
    ValidFrom DATE,
    ValidTo DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
