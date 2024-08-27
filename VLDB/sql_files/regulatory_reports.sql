CREATE TABLE Regulatory_Reports (
    ReportID INT PRIMARY KEY,
    ReportType VARCHAR(50), -- e.g., AML Report, KYC Report, Tax Report
    ReportingPeriodStartDate DATE,
    ReportingPeriodEndDate DATE,
    SubmissionDate DATE,
    ReportStatus VARCHAR(50), -- e.g., Submitted, Pending, Rejected
    RegulatoryBody VARCHAR(100),
    ReportedBy VARCHAR(100),
    ComplianceStatus VARCHAR(50),
    RiskAssessmentScore INT,
    ReportDetails TEXT,
    CorrectiveActions TEXT,
    ApprovalStatus VARCHAR(50),
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
