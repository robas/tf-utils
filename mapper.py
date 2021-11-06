tc05tcr0_map = [
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
tc05tcr1_map = [
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

rules = {}
rules['sales draft0'] = tc05tcr0_map
rules['sales draft1'] = tc05tcr1_map

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
