
Online Filing -- > Capital Subsidy  --> Form --> Retruns Application Subsidy
Utilities --> Gudelines, Check Subsidy Eligibility (Service/Manufacturing)
Application Status --> NEEDS (Application Number)

Users : Department Login (MSME Facilitation Desk )

UAM Filing (UAM Registeration to register his business)
=======================================================
- Non-exisiting user (Registeration to MSME DB)
- Exisitng user in MSME DB (Validate and Reject)


Only for exisiting user in MSME(NEEDS) DB
Online Filing - Claim Subsidy
=========================================
Page-1
•	Udyog number    - 12 digit
•	Name of the entrepreneur
Page-2
    subsidy for 1.manufacturing 2.services
•	Upload Bank statements (PDF/Image)

---> should return application view after uploading
---> should retrun subsidy application number


DB - MSME Table
====================================
•	Sno                             (should be there)
•	Pan no                          (should be there)
•	Entrepreneur name(***)          (should be there)
•	Udyog aadhar number(***)        (should be there)
•	Enterprise name                 (should be there)
•	Account number                  (should be there)
•	Bank                            (should be there)
•	Branch (ifsc code)              (should be there)
•	Partnership(members amount)     (should be there)
•	Civil investment(in rs)         (should be there)
•	Subsidy provided(yes/no)already
•	approval date
•	sector                          (services, manufacturing)

DB - SUBSIDY Table
====================================
•	subsidy application number
•	sector
•	name
•	udyog aadhar
•	acc number of bank
•	amount of interest
•	term loan(year/month/days)
•	pan no
•	amount of loan (provided by bank)
•	subsidy amount
•	subsidy claimed
•	approval date


MSME - OFFCIE

Now the final report is generated in web page is viewed by msme
===============================================================
•	The web page contains the details of
1. S.no
2. Subsidy Application Number
3. Status

search/click with udyog aadhar number:

•	Subsidy Application No
•	Time /date/month/year
•	Pan no
•	Udyog aadhar
•	Name of entrepreneur
•	Sector
•	Name of enterprise
•	Amount of interest(percent 15%)
•	Sanctioned amount(in rs)    --subsidy amount
•	Subsidy claimed(yes/no)
•	Case pending/approved/dismissed
