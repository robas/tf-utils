
from mappings import *

rules = {}
rules['sales draft0'] = sales_draft_tcr0_map
rules['sales draft1'] = sales_draft_tcr1_map
rules['sales draft2AR'] = sales_draft_tcr2_ar_map
rules['sales draft2BR'] = sales_draft_tcr2_br_map
rules['sales draft5'] = sales_draft_tcr5_map
rules['sales draft7'] = sales_draft_tcr7_map
rules['fee collection0'] = tc10_tcr0_map
rules['fee collection1'] = tc10_tcr1_map
rules['funds disbursement0'] = tc20_tcr0_map

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
tc2trxType['10'] = "fee collection"
tc2trxType['20'] = "funds disbursement"


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
