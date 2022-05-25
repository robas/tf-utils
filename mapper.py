
from mappings import *

rules = {}

rules['returned items0'] = returned_items_tcr0_map
rules['returned items1'] = returned_items_tcr1_map
rules['returned items2'] = returned_items_tcr2_map
rules['returned items3'] = returned_items_tcr3_map
rules['returned items4'] = returned_items_tcr4_map
rules['returned items5'] = returned_items_tcr5_map
rules['returned items6'] = returned_items_tcr6_map
rules['returned items7'] = returned_items_tcr7_map
rules['returned items8'] = returned_items_tcr8_map
rules['returned itemsD'] = returned_items_tcrD_map
rules['returned items9'] = returned_items_tcr9_map
rules['reclassification advice0'] = reclassification_advice_tcr0_map
rules['reclassification advice9'] = reclassification_advice_tcr9_map
rules['sales draft0'] = sales_draft_tcr0_map
rules['sales draft1'] = sales_draft_tcr1_map
rules['sales draft2AR'] = sales_draft_tcr2_ar_map
rules['sales draft2BR'] = sales_draft_tcr2_br_map
rules['sales draft5'] = sales_draft_tcr5_map
rules['sales draft7'] = sales_draft_tcr7_map
rules['fee collection0'] = tc10_tcr0_map
rules['fee collection1'] = tc10_tcr1_map
rules['fee collection2AR'] = tc10_tcr2_ar_map
rules['fee collection2BR'] = tc10_tcr2_br_map
rules['fee collection4'] = tc10_tcr4_map
rules['funds disbursement0'] = tc20_tcr0_map
rules['funds disbursement4'] = tc20_tcr4_map
rules['multipurposeCAS0'] = tc33_cas_tcr0_map
rules['multipurposeCAS1'] = tc33_cas_tcr1_map
rules['multipurposeVCR0'] = tc33_cas_vcr0_map
rules['multipurposeVCR1'] = tc33_cas_vcr1_map
rules['fraud advice0'] = tc40_tcr0_map
rules['fraud advice1'] = tc40_tcr1_map
rules['fraud advice2'] = tc40_tcr2_map
rules['fraud advice3'] = tc40_tcr3_map
rules['fraud advice4'] = tc40_tcr4_map
rules['fraud advice5'] = tc40_tcr5_map
rules['fraud advice6'] = tc40_tcr6_map
rules['fraud advice7'] = tc40_tcr7_map
rules['batch ack0A'] = tc44_tcr0_a_map
rules['batch ack0R'] = tc44_tcr0_r_map
rules['batch ack0X'] = tc44_tcr0_x_map
rules['batch ack1'] = tc44_tcr1_map
rules['batch ack2'] = tc44_tcr2_map
rules['batch ack3'] = tc44_tcr3_map
rules['batch ack4'] = tc44_tcr4_map
rules['batch ack5'] = tc44_tcr5_map
rules['batch ack6'] = tc44_tcr6_map
rules['batch ack7'] = tc44_tcr7_map
rules['batch ack8'] = tc44_tcr8_map
rules['table update0'] = tc54_tcr0_map
rules['currency conversion0'] = tc56_tcr0_map
rules['currency conversion1'] = tc56_tcr1_map
rules['batch trailer'] = tc91_tcr0_map
rules['file trailer'] = tc92_tcr0_map
rules['incoming header'] = tc90_tcr0_map

tc2trxType = {}
tc2trxType['01'] = "returned items"
tc2trxType['02'] = "returned items"
tc2trxType['03'] = "returned items"
tc2trxType['04'] = "reclassification advice"
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
tc2trxType['33'] = "multipurpose"
tc2trxType['33CAS'] = "multipurposeCAS"
tc2trxType['33VCR'] = "multipurposeVCR"
tc2trxType['40'] = "fraud advice"
tc2trxType['44'] = "batch ack"
tc2trxType['54'] = "table update"
tc2trxType['56'] = "currency conversion"
tc2trxType['90'] = "incoming header"
tc2trxType['91'] = "batch trailer"
tc2trxType['92'] = "file trailer"


def exist_rules(tc, tcr):
    if tc in tc2trxType.keys() and tc2trxType[tc]+tcr in rules.keys():
        return True
    return False


def get_rules(tc, tcr):
    if tc in tc2trxType.keys() and tc2trxType[tc]+tcr in rules.keys():
        return rules[tc2trxType[tc] + tcr]


def is_tc_of_type(tc, type):
    if tc in tc2trxType.keys() and tc2trxType[tc] == type:
        return True
    return False
