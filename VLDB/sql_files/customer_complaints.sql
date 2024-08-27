CREATE TABLE Customer_Complaints (
    ComplaintID INT PRIMARY KEY,
    CustomerID INT,
    ComplaintDate DATE,
    ComplaintCategory VARCHAR(50),
    ComplaintDetails TEXT,
    ComplaintStatus VARCHAR(20),
    ResolutionDetails TEXT,
    ResolutionDate DATE,
    AssignedTo INT,
    PriorityLevel VARCHAR(20),
    EscalationLevel VARCHAR(20),
    ResponseDueDate DATE,
    ClosureDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customer_Master(CustomerID)
);
