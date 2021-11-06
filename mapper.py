sales_draft_tcr0_map = [
    [2, 'Transaction Code'],
    [1, 'Transaction Code Qualifier'],
    [1, 'Transaction Component Sequence Number'],
    [16, 'Account Number'],
    [3, 'Account Number Extension'],
    [1, 'Floor Limit Indicator'],
    [1, 'CRB/Exception File Indicator'],
    [1, 'Reserved'],
    [23, 'Acquirer Reference Number'],
    [8, 'Acquirers Business ID'],
    [4, 'Purchase Date(MMDD)'],
    [12, 'Destination Amount'],
    [3, 'Destination Currency Code'],
    [12, 'Source Amount'],
    [3, 'Source Currency Code'],
    [25, 'Merchant Name'],
    [13, 'Merchant City'],
    [3, 'Merchant Country Code'],
    [4, 'Merchant Category Code'],
    [5, 'Merchant ZIP Code'],
    [3, 'Merchant State/Province Code'],
    [1, 'Requested Payment Service'],
    [1, 'Number of Payment Forms'],
    [1, 'Usage Code'],
    [2, 'Reason Code'],
    [1, 'Settlement Flag'],
    [1, 'Authorization Characteristics Indicator'],
    [6, 'Authorization Code'],
    [1, 'POS Terminal Capability'],
    [1, 'Reserved'],
    [1, 'Cardholder ID Method'],
    [1, 'Collection-Only Flag'],
    [2, 'POS Entry Mode'],
    [4, 'Central Processing Date(YDDD)'],
    [1, 'Reimbursement Attribute']
]
sales_draft_tcr1_map = [
    [2, 'Transaction Code'],
    [1, 'Transaction Code Qualifier'],
    [1, 'Transaction Component Sequence Number'],
    [1, 'Business Format Code'],
    [2, 'Token Assurance Level'],
    [5, 'Rate Table ID'],
    [3, 'Reserved'],
    [6, 'Reserved'],
    [1, 'Documentation Indicator'],
    [50, 'Member Message Text'],
    [2, 'Special Condition Indicators'],
    [3, 'Fee Program Indicator'],
    [1, 'Issuer Charge'],
    [1, 'Persistent FX Applied Indicator'],
    [15, 'Card Acceptor ID'],
    [8, 'Terminal ID'],
    [12, 'National Reimbursement Fee'],
    [1, 'Mail/Phone/Electronic Commerce and Payment Indicator'],
    [1, 'Special Chargeback Indicator'],
    [4, 'Conversion Date'],
    [2, 'Reserved'],
    [1, 'Acceptance Terminal Indicator'],
    [1, 'Prepaid Card Indicator'],
    [1, 'Service Development Field'],
    [1, 'AVS Response Code'],
    [1, 'Authorization Source Code'],
    [1, 'Purchase Identifier Format'],
    [1, 'Account Selection'],
    [2, 'Installment Payment Count'],
    [25, 'Purchase Identifier'],
    [9, 'Cashback'],
    [1, 'Chip Condition Code'],
    [1, 'POS Environment']
]
sales_draft_tcr2_ar_map = [
    [2, 'Transaction Code'],
    [1, 'Transaction Code Qualifier'],
    [1, 'Transaction Component Sequence Number'],
    [12, 'Installment Payment Total Amount'],
    [3, 'Country Code (AR^)'],
    [2, 'Installment Payment Indicator'],
    [2, 'Number of Installment Payments'],
    [2, 'Installment Payment Number'],
    [12, 'Installment Payment Interest Amount'],
    [10, 'VAT for Installment Payment Interest Amount'],
    [10, 'Installment Payment Risk Fee Amount'],
    [10, 'VAT for Installment Payment Risk Fee Amount'],
    [1, 'Installment Payment Interest National Net Impact in IRF Calculation - IRF Indicator'],
    [1, 'Installment Payment Interest National Net Impact - Settlement Indicator'],
    [6, 'Deferred Cardholder Billing Date'],
    [6, 'Deferred Settlement Date'],
    [12, 'Tip Amount'],
    [10, 'Interchange Reimbursement Fee (IRF)'],
    [10, 'VAT National Reimbursement Fee'],
    [20, 'Promotion Data'],
    [6, 'Deferred Settlement Date of the Original'],
    [29, 'Reserved']
]
sales_draft_tcr2_br_map = [
    [2, 'Transaction Code'],
    [1, 'Transaction Code Qualifier'],
    [1, 'Transaction Component Sequence Number'],
    [12, 'Reserved'],
    [3, 'Country Code (BR^)'],
    [3, 'Reserved'],
    [3, 'Settlement Type'],
    [10, 'National Reimbursement Fee'],
    [4, 'National Net CPD of Original (YDDD)'],
    [2, 'Installment Payment Count'],
    [5, 'Special Merchant Identifier'],
    [1, 'Special Purchase Identifier'],
    [15, 'Merchant Tax ID Number'],
    [106, 'Reserved']
]
sales_draft_tcr5_map = [
    [2, 'Transaction Code'],
    [1, 'Transaction Code Qualifier'],
    [1, 'Transaction Component Sequence Number'],
    [15, 'Transaction Identifier'],
    [12, 'Authorized Amount'],
    [3, 'Authorization Currency Code'],
    [2, 'Authorization Response Code'],
    [4, 'Validation Code'],
    [1, 'Excluded Transaction Identifier Reason'],
    [1, 'Reserved'],
    [2, 'Reserved'],
    [2, 'Multiple Clearing Sequence Number'],
    [2, 'Multiple Clearing Sequence Count'],
    [1, 'Market-Specific Authorization Data Indicator'],
    [12, 'Total Authorized Amount'],
    [1, 'Information Indicator'],
    [14, 'Merchant Telephone Number'],
    [1, 'Additional Data Indicator'],
    [2, 'Merchant Volume Indicator'],
    [2, 'Electronic Commerce Goods Indicator'],
    [10, 'Merchant Verification Value'],
    [15, 'Interchange Fee Amount'],
    [1, 'Interchange Fee Sign'],
    [8, 'Source Currency to Base Currency Exchange Rate'],
    [8, 'Base Currency to Destination Currency Exchange Rate'],
    [12, 'Optional Issuer ISA Amount'],
    [2, 'Product ID'],
    [6, 'Program ID'],
    [1, 'Dynamic Currency Conversion (DCC) Indicator'],
    [4, 'Account Type Identification'],
    [1, 'Spend Qualified Indicator'],
    [16, 'PAN Token'],
    [2, 'Reserved'],
    [1, 'CVV2 Result Code']
]
sales_draft_tcr7_map = [
    [2, 'Transaction Code'],
    [1, 'Transaction Code Qualifier'],
    [1, 'Transaction Component Sequence Number'],
    [2, 'Transaction Type'],
    [3, 'Card Sequence Number'],
    [6, 'Terminal Transaction Date'],
    [6, 'Terminal Capability Profile'],
    [3, 'Terminal Country Code'],
    [8, 'Terminal Serial Number'],
    [8, 'Unpredictable Number'],
    [4, 'Application Transaction Counter'],
    [4, 'Application Interchange Profile'],
    [16, 'Cryptogram'],
    [2, 'Issuer Application Data, Byte 2'],
    [2, 'Issuer Application Data, Byte 3'],
    [10, 'Terminal Verification Results'],
    [8, 'Issuer Application Data, Byte 4-7'],
    [12, 'Cryptogram Amount'],
    [2, 'Issuer Application Data, Byte 8'],
    [16, 'Issuer Application Data, Byte 9-16'],
    [2, 'Issuer Application Data, Byte 1'],
    [2, 'Issuer Application Data, Byte 17'],
    [30, 'Issuer Application Data, Byte 18-32'],
    [8, 'Form Factor Indicator'],
    [10, 'Issuer Script 1 Results']
]

rules = {}
rules['sales draft0'] = sales_draft_tcr0_map
rules['sales draft1'] = sales_draft_tcr1_map
rules['sales draft2AR'] = sales_draft_tcr2_ar_map
rules['sales draft2BR'] = sales_draft_tcr2_br_map
rules['sales draft5'] = sales_draft_tcr5_map
rules['sales draft7'] = sales_draft_tcr7_map

tc2trxType = {}
tc2trxType['01'] = "sales draft"
tc2trxType['02'] = "sales draft"
tc2trxType['05'] = "sales draft"
tc2trxType['06'] = "sales draft"
tc2trxType['07'] = "sales draft"
tc2trxType['15'] = "sales draft"
tc2trxType['16'] = "sales draft"
tc2trxType['17'] = "sales draft"
tc2trxType['25'] = "sales draft"
tc2trxType['26'] = "sales draft"
tc2trxType['27'] = "sales draft"
tc2trxType['35'] = "sales draft"
tc2trxType['36'] = "sales draft"
tc2trxType['37'] = "sales draft"


def exist_rules(tc, tcr):
    if tc in tc2trxType.keys() and tc2trxType[tc]+tcr in rules.keys():
        return True
    return False


def get_rules(tc, tcr):
    if tc in tc2trxType.keys() and tc2trxType[tc]+tcr in rules.keys():
        return rules[tc2trxType[tc] + tcr]


def is_sales_draft(tc):
    if tc in tc2trxType.keys() and tc2trxType[tc] == "sales draft":
        return True
    return False
