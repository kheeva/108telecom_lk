# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountInvoice(models.Model):
    is_printed = models.IntegerField()
    invc_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_invoice'


class AccountTariffLink(models.Model):
    account_id = models.IntegerField()
    tariff_id = models.IntegerField()
    next_tariff_id = models.IntegerField()
    discount_period_id = models.IntegerField()
    is_deleted = models.IntegerField()
    link_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account_tariff_link'


class Accounts(models.Model):
    balance = models.FloatField()
    account_name = models.CharField(max_length=255)
    credit = models.FloatField()
    flags = models.IntegerField()
    is_blocked = models.IntegerField()
    vat_rate = models.FloatField()
    sale_tax_rate = models.FloatField()
    int_status = models.IntegerField()
    unlimited = models.IntegerField()
    is_deleted = models.IntegerField()
    external_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'accounts'


class Acts(models.Model):
    act_id = models.IntegerField()
    invc_id = models.IntegerField()
    gen_date = models.IntegerField()
    act_text = models.TextField(blank=True, null=True)
    is_sign = models.IntegerField()
    sign_date = models.IntegerField()
    doc_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acts'


class ActsTemplates(models.Model):
    act_id = models.IntegerField()
    is_old = models.IntegerField()
    gen_date = models.IntegerField()
    act_name = models.CharField(max_length=255)
    act_text = models.TextField(blank=True, null=True)
    doc_type = models.IntegerField()
    def_field = models.IntegerField(db_column='def')  # Field renamed because it was a Python reserved word.
    landscape = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acts_templates'


class AdditionalIpZones2Houses(models.Model):
    house_key = models.IntegerField()
    ip_zone_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'additional_ip_zones2houses'


class Archives(models.Model):
    archive_id = models.IntegerField()
    table_type = models.IntegerField()
    table_name = models.CharField(max_length=255)
    start_date = models.IntegerField()
    end_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'archives'


class BalanceHistory(models.Model):
    account_id = models.IntegerField()
    accounting_period_id = models.IntegerField()
    out_balance = models.FloatField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'balance_history'


class Banks(models.Model):
    bic = models.CharField(max_length=255)
    name = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255)
    kschet = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'banks'


class BlocksInfo(models.Model):
    account_id = models.IntegerField()
    block_type = models.IntegerField()
    start_date = models.IntegerField()
    expire_date = models.IntegerField(blank=True, null=True)
    is_planning = models.IntegerField()
    is_deleted = models.IntegerField()
    unabon = models.IntegerField()
    unprepay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blocks_info'


class CardInfo(models.Model):
    pool_id = models.IntegerField()
    secret = models.CharField(max_length=255)
    balance = models.FloatField()
    currency = models.IntegerField()
    expiration = models.IntegerField(blank=True, null=True)
    is_used = models.IntegerField()
    service_id = models.IntegerField()
    days = models.IntegerField()
    is_blocked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_info'


class CardInfoExpired(models.Model):
    card_id = models.IntegerField()
    pool_id = models.IntegerField()
    secret = models.CharField(max_length=255)
    balance = models.FloatField()
    currency = models.IntegerField()
    expiration = models.IntegerField()
    is_used = models.IntegerField()
    service_id = models.IntegerField()
    days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_info_expired'


class CardPoolInfo(models.Model):
    pool_id = models.IntegerField(primary_key=True)
    cards = models.IntegerField()
    cards_used = models.IntegerField()
    last_update = models.IntegerField()
    first_update = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_pool_info'


class CardPoolOwners(models.Model):
    pool_id = models.IntegerField()
    user_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card_pool_owners'


class Contracts(models.Model):
    contract_number = models.CharField(max_length=255)
    date = models.IntegerField()
    contract_text = models.TextField(blank=True, null=True)
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contracts'


class ContractsTemplates(models.Model):
    contract_number = models.CharField(max_length=255)
    date = models.IntegerField()
    contract_text = models.TextField(blank=True, null=True)
    template_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'contracts_templates'


class Credits(models.Model):
    payment_trans_id = models.IntegerField()
    expire_date = models.IntegerField()
    start_date = models.IntegerField()
    account_id = models.IntegerField()
    value = models.FloatField()
    status = models.IntegerField()
    is_passed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'credits'


class CrmAdminNotifications(models.Model):
    admin_id = models.SmallIntegerField(blank=True, null=True)
    ticket_id = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    viewed = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_admin_notifications'


class CrmDealers(models.Model):
    dealer_id = models.IntegerField(blank=True, null=True)
    object_type = models.CharField(max_length=6, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    is_deleted = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_dealers'


class CrmOpLog(models.Model):
    op_id = models.IntegerField()
    action = models.CharField(max_length=7)
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'crm_op_log'


class CrmTickets(models.Model):
    pin = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    type = models.SmallIntegerField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    author = models.SmallIntegerField(blank=True, null=True)
    owner = models.SmallIntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    admin_comment = models.TextField(blank=True, null=True)
    admin_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tickets'


class CrmTicketsReply(models.Model):
    ticket_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    author = models.SmallIntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    internal_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tickets_reply'


class CurrencyList(models.Model):
    currency_brief_name = models.CharField(max_length=255)
    currency_full_name = models.CharField(max_length=255)
    percent = models.FloatField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'currency_list'


class CurrencyRates(models.Model):
    currency_id = models.IntegerField()
    date = models.IntegerField()
    currency_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'currency_rates'


class CustomServices(models.Model):
    account_id = models.IntegerField()
    mark = models.CharField(max_length=255)
    service_key = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    trans_id = models.IntegerField()
    burn_trans_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_services'


class DealerAccessList(models.Model):
    dealer_id = models.IntegerField()
    entity_type = models.IntegerField()
    entity_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dealer_access_list'


class DealerDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255)
    act_address = models.CharField(max_length=255)
    passport = models.CharField(max_length=255)
    work_tel = models.CharField(max_length=255)
    home_tel = models.CharField(max_length=255)
    mob_tel = models.CharField(max_length=255)
    web_page = models.CharField(max_length=255)
    icq_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    who_create = models.IntegerField()
    who_change = models.IntegerField()
    create_date = models.IntegerField()
    change_date = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dealer_details'


class DealerLog(models.Model):
    dealer_id = models.IntegerField()
    action = models.IntegerField()
    action_date = models.IntegerField()
    comments = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dealer_log'


class DhsAccessLog(models.Model):
    recv_date = models.IntegerField()
    user_name = models.CharField(db_column='User_Name', max_length=255)  # Field name made lowercase.
    service_type = models.IntegerField(db_column='Service_Type')  # Field name made lowercase.
    framed_protocol = models.IntegerField(db_column='Framed_Protocol')  # Field name made lowercase.
    nas_ip_address = models.IntegerField(db_column='NAS_IP_Address')  # Field name made lowercase.
    nas_id = models.CharField(db_column='NAS_Id', max_length=255)  # Field name made lowercase.
    is_success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dhs_access_log'


class DhsAccessLogAttrs(models.Model):
    access_id = models.IntegerField()
    vendor = models.IntegerField()
    attr = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    status_type = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dhs_access_log_attrs'


class DhsSessionsDetail(models.Model):
    dhs_sess_id = models.IntegerField()
    trange_id = models.IntegerField()
    recv_date = models.IntegerField()
    account_id = models.IntegerField()
    disc_per_id = models.IntegerField()
    slink_id = models.IntegerField()
    duration = models.BigIntegerField()
    base_cost = models.FloatField()
    sum_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dhs_sessions_detail'


class DhsSessionsLog(models.Model):
    account_id = models.IntegerField()
    slink_id = models.IntegerField()
    recv_date = models.IntegerField()
    last_update_date = models.IntegerField()
    framed_ip_address = models.IntegerField(db_column='Framed_IP_Address')  # Field name made lowercase.
    nas_port = models.IntegerField(db_column='NAS_Port')  # Field name made lowercase.
    acct_delay_time = models.IntegerField(db_column='Acct_Delay_Time')  # Field name made lowercase.
    acct_session_id = models.CharField(db_column='Acct_Session_Id', max_length=255)  # Field name made lowercase.
    nas_port_type = models.IntegerField(db_column='NAS_Port_Type')  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=255)  # Field name made lowercase.
    service_type = models.IntegerField(db_column='Service_Type')  # Field name made lowercase.
    framed_protocol = models.IntegerField(db_column='Framed_Protocol')  # Field name made lowercase.
    nas_ip_address = models.IntegerField(db_column='NAS_IP_Address')  # Field name made lowercase.
    nas_id = models.CharField(db_column='NAS_Id', max_length=255)  # Field name made lowercase.
    acct_status_type = models.IntegerField(db_column='Acct_Status_Type')  # Field name made lowercase.
    acct_input_packets = models.BigIntegerField(db_column='Acct_Input_Packets')  # Field name made lowercase.
    acct_input_octets = models.BigIntegerField(db_column='Acct_Input_Octets')  # Field name made lowercase.
    acct_input_gigawords = models.BigIntegerField(db_column='Acct_Input_Gigawords')  # Field name made lowercase.
    acct_output_packets = models.BigIntegerField(db_column='Acct_Output_Packets')  # Field name made lowercase.
    acct_output_octets = models.BigIntegerField(db_column='Acct_Output_Octets')  # Field name made lowercase.
    acct_output_gigawords = models.BigIntegerField(db_column='Acct_Output_Gigawords')  # Field name made lowercase.
    acct_session_time = models.BigIntegerField(db_column='Acct_Session_Time')  # Field name made lowercase.
    acct_terminate_cause = models.IntegerField(db_column='Acct_Terminate_Cause')  # Field name made lowercase.
    called_station_id = models.CharField(db_column='Called_Station_Id', max_length=255)  # Field name made lowercase.
    calling_station_id = models.CharField(db_column='Calling_Station_Id', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dhs_sessions_log'


class DhsSessionsLogAttrs(models.Model):
    session_id = models.IntegerField()
    vendor = models.IntegerField()
    attr = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    status_type = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dhs_sessions_log_attrs'


class DialupCostInfo(models.Model):
    dialup_cost_info_id = models.IntegerField()
    timerange_id = models.IntegerField()
    cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dialup_cost_info'


class DialupServiceLinks(models.Model):
    time_in_curr_disc_period = models.IntegerField()
    old_time = models.IntegerField()
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    allowed_cid = models.CharField(max_length=255)
    allowed_csid = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    callback_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dialup_service_links'


class DialupServicesData(models.Model):
    dialup_cost_info_id = models.IntegerField()
    pool_name = models.CharField(max_length=255)
    max_timeout = models.IntegerField()
    login_prefix = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dialup_services_data'


class DirZones(models.Model):
    zone_id = models.IntegerField()
    dir_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dir_zones'


class DiscountPeriods(models.Model):
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    periodic_type = models.IntegerField()
    next_discount_period_id = models.IntegerField()
    discount_interval = models.IntegerField()
    canonical_len = models.IntegerField()
    is_expired = models.IntegerField()
    custom_duration = models.IntegerField()
    static_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'discount_periods'


class DiscountTransactionsAll(models.Model):
    account_id = models.IntegerField()
    incoming_rest = models.FloatField()
    outgoing_rest = models.FloatField()
    discount = models.FloatField()
    discount_with_tax = models.FloatField()
    service_id = models.IntegerField()
    service_type = models.IntegerField()
    discount_period_id = models.IntegerField()
    slink_id = models.IntegerField()
    discount_date = models.IntegerField()
    charge_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'discount_transactions_all'


class DiscountTransactionsIptrafficAll(models.Model):
    id = models.IntegerField(primary_key=True)
    account_id = models.IntegerField()
    discount = models.FloatField()
    discount_with_tax = models.FloatField()
    service_id = models.IntegerField()
    discount_period_id = models.IntegerField()
    slink_id = models.IntegerField()
    discount_date = models.IntegerField()
    discount_date_hour = models.IntegerField()
    discount_date_day = models.IntegerField()
    discount_date_month = models.IntegerField()
    t_class = models.IntegerField()
    base_cost = models.FloatField()
    ipid = models.IntegerField()
    bytes = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'discount_transactions_iptraffic_all'


class Downloaded(models.Model):
    downloaded_id = models.IntegerField()
    tclass_id = models.IntegerField()
    qnt = models.BigIntegerField()
    old_prepay = models.BigIntegerField()
    custom_prepay = models.BigIntegerField()
    downed_as_prepaid = models.BigIntegerField()
    discounted = models.FloatField()
    traffic_quota = models.BigIntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'downloaded'


class DtaggCust(models.Model):
    account_id = models.IntegerField()
    discounted = models.FloatField()
    discounted_without_tax = models.FloatField()
    exp_date = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtagg_cust'


class DtaggHotspot(models.Model):
    slink_id = models.IntegerField()
    is_closed = models.IntegerField()
    base_cost = models.FloatField()
    discounted = models.FloatField()
    discounted_without_tax = models.FloatField()
    session_time = models.IntegerField()
    recv_bytes = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dtagg_hotspot'


class DtaggIptraffic(models.Model):
    slink_id = models.IntegerField()
    is_closed = models.IntegerField()
    base_cost = models.FloatField()
    tclass = models.IntegerField()
    ipid = models.IntegerField()
    discounted = models.FloatField()
    discounted_without_tax = models.FloatField()
    bytes = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'dtagg_iptraffic'


class DtaggOnce(models.Model):
    account_id = models.IntegerField()
    is_closed = models.IntegerField()
    discounted = models.FloatField()
    discounted_without_tax = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dtagg_once'


class DtaggPeriodic(models.Model):
    slink_id = models.IntegerField()
    is_closed = models.IntegerField()
    discounted = models.FloatField()
    discounted_without_tax = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dtagg_periodic'


class DtaggTelephony(models.Model):
    slink_id = models.IntegerField()
    is_closed = models.IntegerField()
    base_cost = models.FloatField()
    zone_id = models.IntegerField()
    discounted = models.FloatField()
    discounted_without_tax = models.FloatField()
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtagg_telephony'


class DynashapeBorders(models.Model):
    dyna_id = models.IntegerField()
    border = models.BigIntegerField()
    timerange = models.IntegerField()
    lim = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynashape_borders'


class DynashapeData(models.Model):
    slink_id = models.IntegerField()
    direction = models.IntegerField()
    curr_limit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynashape_data'


class DynashapeRadiusAttrs(models.Model):
    service_id = models.IntegerField()
    vendor_id = models.IntegerField()
    attr_id = models.IntegerField()
    attr_type = models.IntegerField()
    value = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynashape_radius_attrs'


class DynashapeServices(models.Model):
    service_id = models.IntegerField()
    direction = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynashape_services'


class DynashapeSettings(models.Model):
    flags = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynashape_settings'


class DynashapeTclasses(models.Model):
    dyna_id = models.IntegerField()
    tclass_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dynashape_tclasses'


class FirewallRules(models.Model):
    is_for_all = models.IntegerField()
    uid = models.IntegerField()
    group_id = models.IntegerField()
    tariff_id = models.IntegerField()
    rule_on = models.CharField(max_length=255)
    rule_off = models.CharField(max_length=255)
    rule_block = models.CharField(max_length=255)
    router_id = models.IntegerField()
    and_logic = models.IntegerField()
    add_user = models.IntegerField()
    edit_user = models.IntegerField()
    del_user = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'firewall_rules'


class FirewallRulesNew(models.Model):
    flags = models.IntegerField()
    events = models.IntegerField()
    router_id = models.IntegerField()
    tariff_id = models.IntegerField()
    group_id = models.IntegerField()
    user_id = models.IntegerField()
    rule = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'firewall_rules_new'


class FundsFlowSettings(models.Model):
    group_id = models.IntegerField()
    priority = models.IntegerField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'funds_flow_settings'


class FundsFlowTransactions(models.Model):
    uid = models.IntegerField()
    account_id_from = models.IntegerField()
    account_id_to = models.IntegerField()
    amount = models.IntegerField()
    flow_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'funds_flow_transactions'


class Groups(models.Model):
    group_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'groups'


class HotspotAllowedNet(models.Model):
    hotspot_service_id = models.IntegerField()
    ip = models.IntegerField()
    mask = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hotspot_allowed_net'


class HotspotCostInfo(models.Model):
    hotspot_cost_info_id = models.IntegerField()
    timerange_id = models.IntegerField()
    cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'hotspot_cost_info'


class HotspotNetworkList(models.Model):
    service_id = models.IntegerField()
    ip = models.IntegerField()
    mask = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hotspot_network_list'


class HotspotServiceLinks(models.Model):
    time_in_curr_disc_period = models.IntegerField()
    old_time = models.IntegerField()
    recv_bytes = models.BigIntegerField()
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hotspot_service_links'


class HotspotServicesData(models.Model):
    hotspot_cost_info_id = models.IntegerField()
    recv_cost = models.FloatField()
    rate_limit = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hotspot_services_data'


class Houses(models.Model):
    post_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    connect_date = models.IntegerField()
    ip_zone_id = models.IntegerField()
    additional_ip_zones_key = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'houses'


class IcIntegration(models.Model):
    user_id = models.IntegerField()
    max_invoice_id = models.IntegerField()
    max_payment_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ic_integration'


class IcSettings(models.Model):
    send_users = models.IntegerField()
    send_inv = models.IntegerField()
    send_payments = models.IntegerField()
    recv_payments = models.IntegerField()
    sync_card = models.IntegerField()
    sync_empty_name = models.IntegerField()
    sync_empty_inn = models.IntegerField()
    sync_empty_kpp = models.IntegerField()
    sync_users_since = models.IntegerField()
    sync_users_till = models.IntegerField()
    sync_inv_since = models.IntegerField()
    sync_inv_till = models.IntegerField()
    sync_payments_since = models.IntegerField()
    sync_payments_till = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ic_settings'


class InvoiceEntry(models.Model):
    name = models.CharField(max_length=255)
    invoice_id = models.IntegerField()
    slink_id = models.IntegerField()
    service_type = models.IntegerField()
    discount_period_id = models.IntegerField()
    qnt = models.FloatField()
    base_cost = models.FloatField()
    sum_cost = models.FloatField()
    tax_amount = models.FloatField()
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_entry'


class InvoiceEntryDetails(models.Model):
    entry_id = models.IntegerField()
    type = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_entry_details'


class Invoices(models.Model):
    ext_num = models.CharField(max_length=255)
    invoice_date = models.IntegerField()
    payment_transaction_id = models.IntegerField()
    expire_date = models.IntegerField()
    is_payed = models.IntegerField()
    is_printed = models.IntegerField()
    is_mailed = models.IntegerField()
    uid = models.IntegerField()
    account_id = models.IntegerField()
    arrearage = models.FloatField()
    period_start = models.IntegerField()
    period_end = models.IntegerField()
    balance_on_set = models.FloatField()
    version = models.IntegerField()
    ic_status = models.IntegerField()
    ic_id = models.CharField(max_length=255)
    last_sync_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoices'


class IpGroups(models.Model):
    ip_group_id = models.IntegerField()
    ip = models.IntegerField()
    mask = models.IntegerField()
    uname = models.CharField(max_length=255)
    upass = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    allowed_cid = models.CharField(max_length=255)
    ip_type = models.IntegerField()
    router_id = models.IntegerField()
    create_date = models.IntegerField()
    delete_date = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ip_groups'


class IpZones(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ip_zones'


class IpZonesDetail(models.Model):
    ip_zone_id = models.IntegerField()
    net = models.IntegerField()
    mask = models.IntegerField()
    gateway = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ip_zones_detail'


class IptrafficBorders(models.Model):
    borders_id = models.IntegerField()
    border = models.BigIntegerField()
    cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'iptraffic_borders'


class IptrafficServiceLinks(models.Model):
    ip_group_id = models.IntegerField()
    downloaded_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iptraffic_service_links'


class IptrafficServicesData(models.Model):
    tst_id = models.IntegerField()
    null_service_prepaid = models.IntegerField()
    aggregation_interval = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iptraffic_services_data'


class LicenseData(models.Model):
    hash1 = models.CharField(max_length=255)
    hash2 = models.CharField(max_length=255)
    date = models.IntegerField()
    lic_type = models.IntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license_data'


class Messages(models.Model):
    sender_id = models.IntegerField()
    group_id = models.IntegerField()
    is_for_all = models.IntegerField()
    receiver_type = models.IntegerField()
    receiver_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    mime = models.CharField(max_length=255)
    send_date = models.IntegerField()
    recv_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messages'


class MessagesStatus(models.Model):
    message_id = models.IntegerField()
    user_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'messages_status'


class NasInfo(models.Model):
    nas_id = models.CharField(max_length=255, blank=True, null=True)
    auth_secret = models.CharField(max_length=255, blank=True, null=True)
    acct_secret = models.CharField(max_length=255, blank=True, null=True)
    nas_type = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nas_info'


class OnceServiceData(models.Model):
    cost = models.FloatField()
    drop_from_group = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'once_service_data'


class OnceServiceLinks(models.Model):
    discount_date = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'once_service_links'


class Option82Log(models.Model):
    account_id = models.IntegerField(blank=True, null=True)
    mac = models.CharField(max_length=20, blank=True, null=True)
    switch = models.CharField(max_length=15, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    vlan = models.IntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option82_log'


class PaymentMethods(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'payment_methods'


class PaymentTransactions(models.Model):
    account_id = models.IntegerField()
    payment_incurrency = models.FloatField()
    currency_id = models.IntegerField()
    currency_rate = models.FloatField()
    payment_absolute = models.FloatField()
    actual_date = models.IntegerField()
    payment_enter_date = models.IntegerField()
    payment_ext_number = models.CharField(max_length=255, blank=True, null=True)
    method = models.IntegerField()
    who_receive = models.IntegerField()
    comments_for_user = models.CharField(max_length=255, blank=True, null=True)
    comments_for_admins = models.CharField(max_length=255, blank=True, null=True)
    burn_time = models.IntegerField()
    is_canceled = models.IntegerField()
    cancel_id = models.IntegerField()
    hash = models.CharField(max_length=255)
    charge_id = models.IntegerField()
    ic_status = models.IntegerField()
    ic_id = models.CharField(max_length=255)
    last_sync_date = models.IntegerField()
    is_sms_notificated = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'payment_transactions'


class PaymentsTimed(models.Model):
    payment_trans_id = models.IntegerField()
    expire_date = models.IntegerField()
    pay_date = models.IntegerField()
    last_pay_date = models.IntegerField()
    account_id = models.IntegerField()
    payment_value = models.FloatField()
    custagg_id = models.IntegerField()
    is_passed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payments_timed'


class PeriodicServiceLinks(models.Model):
    is_blocked = models.IntegerField()
    discount_period_id = models.IntegerField()
    discounted_in_curr_period = models.FloatField()
    repaid_in_curr_period = models.FloatField()
    start_date = models.IntegerField()
    is_planned = models.IntegerField()
    expire_date = models.IntegerField(blank=True, null=True)
    need_del = models.IntegerField()
    unabon_period = models.IntegerField()
    unprepay_period = models.IntegerField()
    start_block_unabon = models.IntegerField()
    start_block_unprepay = models.IntegerField()
    is_invoice_set = models.IntegerField()
    is_deleted = models.IntegerField()
    recalc_type = models.IntegerField()
    next_recalc_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'periodic_service_links'


class PeriodicServicesData(models.Model):
    cost = models.FloatField()
    discount_method = models.IntegerField()
    start_date = models.IntegerField()
    expire_date = models.IntegerField()
    radius_sessions_limit = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'periodic_services_data'


class PromisedPaymentData(models.Model):
    account_id = models.IntegerField()
    last_payment_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promised_payment_data'


class PromisedPaymentSettings(models.Model):
    group_id = models.IntegerField()
    priority = models.IntegerField()
    is_enabled = models.IntegerField()
    max_duration = models.IntegerField()
    max_value = models.FloatField()
    interval_duration = models.IntegerField()
    min_balance = models.FloatField()
    use_min_balance = models.IntegerField()
    free_balance = models.FloatField()
    use_free_balance = models.IntegerField()
    service_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promised_payment_settings'


class RadiusData(models.Model):
    owner_id = models.IntegerField()
    owner_type = models.IntegerField()
    vendor = models.IntegerField()
    attr = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    attr_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radius_data'


class RadiusPoolInfo(models.Model):
    name = models.CharField(max_length=255)
    ip = models.IntegerField()
    mask = models.IntegerField()
    create_date = models.IntegerField()
    delete_date = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radius_pool_info'


class RoutersInfo(models.Model):
    router_type = models.IntegerField()
    router_ip = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    router_comments = models.CharField(max_length=255)
    router_bin_ip = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'routers_info'


class ServiceLinks(models.Model):
    user_id = models.IntegerField()
    account_id = models.IntegerField()
    service_id = models.IntegerField()
    tariff_link_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_links'


class ServicesData(models.Model):
    service_type = models.IntegerField()
    service_name = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)
    is_deleted = models.IntegerField()
    tariff_id = models.IntegerField()
    parent_service_id = models.IntegerField()
    link_by_default = models.IntegerField()
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services_data'


class SlinkTechParam(models.Model):
    type_id = models.IntegerField()
    param = models.CharField(max_length=255)
    reg_date = models.IntegerField()
    slink_id = models.IntegerField()
    passwd = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'slink_tech_param'


class SlinkTechParamType(models.Model):
    name = models.CharField(max_length=255)
    descr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'slink_tech_param_type'


class SupplierInfo(models.Model):
    name = models.CharField(max_length=255)
    ur_adress = models.CharField(max_length=255)
    act_adress = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    kpp = models.CharField(max_length=255)
    bank_id = models.IntegerField()
    account = models.CharField(max_length=255)
    fio_headman = models.CharField(max_length=255)
    fio_bookeeper = models.CharField(max_length=255)
    fio_headman_sh = models.CharField(max_length=255)
    fio_bookeeper_sh = models.CharField(max_length=255)
    name_sh = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'supplier_info'


class SwitchTariffData(models.Model):
    group_id = models.IntegerField()
    tariff_id = models.IntegerField()
    min_balance = models.FloatField()
    use_min_balance = models.IntegerField()
    free_balance = models.FloatField()
    use_free_balance = models.IntegerField()
    service_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'switch_tariff_data'


class SwitchTariffSettings(models.Model):
    group_id = models.IntegerField()
    priority = models.IntegerField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'switch_tariff_settings'


class SystemAccounts(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    ip = models.IntegerField()
    mask = models.IntegerField()
    is_dealer = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system_accounts'


class SystemGroupInfo(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'system_group_info'


class SystemGroups(models.Model):
    group_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system_groups'


class SystemRights(models.Model):
    group_id = models.IntegerField()
    fid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'system_rights'


class TClass(models.Model):
    t_class_name = models.CharField(max_length=255)
    graph_color = models.IntegerField()
    is_display = models.IntegerField()
    is_fill = models.IntegerField()
    time_range_id = models.IntegerField()
    dont_save = models.IntegerField()
    local_traf_policy = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_class'


class TClassDetail(models.Model):
    t_class_id = models.IntegerField()
    saddr = models.IntegerField()
    saddr_mask = models.IntegerField()
    daddr = models.IntegerField()
    daddr_mask = models.IntegerField()
    sport = models.IntegerField()
    dport = models.IntegerField()
    input = models.IntegerField()
    output = models.IntegerField()
    src_as = models.IntegerField()
    dst_as = models.IntegerField()
    nexthop = models.IntegerField()
    tcp_flags = models.IntegerField()
    proto = models.IntegerField()
    tos = models.IntegerField()
    use_sport = models.IntegerField()
    use_dport = models.IntegerField()
    use_input = models.IntegerField()
    use_output = models.IntegerField()
    use_src_as = models.IntegerField()
    use_dst_as = models.IntegerField()
    use_nexthop = models.IntegerField()
    use_tcp_flags = models.IntegerField()
    use_proto = models.IntegerField()
    use_tos = models.IntegerField()
    skip = models.IntegerField()
    ip_from = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_class_detail'


class Tariffs(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.IntegerField()
    change_date = models.IntegerField()
    who_change = models.IntegerField()
    who_create = models.IntegerField()
    expire_date = models.IntegerField()
    balance_rollover = models.IntegerField()
    is_deleted = models.IntegerField()
    comments = models.CharField(max_length=255)
    min_payment = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'tariffs'


class TariffsHistory(models.Model):
    account_id = models.IntegerField()
    tariff_id = models.IntegerField()
    link_date = models.IntegerField()
    unlink_date = models.IntegerField()
    tariff_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tariffs_history'


class TariffsServicesLink(models.Model):
    tariff_id = models.IntegerField()
    service_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tariffs_services_link'


class TelDirections(models.Model):
    prefix = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    create_date = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_directions'


class TelNumbers(models.Model):
    slink_id = models.IntegerField()
    tel_number = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    allowed_cid = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_numbers'


class TelServiceLinks(models.Model):
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_service_links'


class TelServiceLinksDownloaded(models.Model):
    slink_id = models.IntegerField()
    direction_id = models.IntegerField()
    downloaded = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_service_links_downloaded'


class TelServiceLinksPrepaid(models.Model):
    slink_id = models.IntegerField()
    tarif_key = models.IntegerField()
    downed_as_prepaid = models.IntegerField()
    old_prepaid = models.IntegerField()
    custom_prepaid = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_service_links_prepaid'


class TelServicesBorders(models.Model):
    tel_service_id = models.IntegerField()
    tarif_key = models.IntegerField()
    border = models.BigIntegerField()
    cost = models.FloatField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_services_borders'


class TelServicesData(models.Model):
    t_s_step = models.IntegerField()
    t_s_free = models.IntegerField()
    max_timeout = models.IntegerField()
    first_interval = models.BigIntegerField()
    incremental_interval = models.BigIntegerField()
    first_interval_around = models.BigIntegerField()
    free_time = models.BigIntegerField()
    fixed_call_cost = models.FloatField()
    unit_size = models.BigIntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_services_data'


class TelServicesPrepaid(models.Model):
    tel_service_id = models.IntegerField()
    tarif_key = models.IntegerField()
    prepaid = models.BigIntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_services_prepaid'


class TelServicesTrMult(models.Model):
    tel_service_id = models.IntegerField()
    tarif_key = models.IntegerField()
    time_range_id = models.IntegerField()
    mult = models.FloatField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_services_tr_mult'


class TelSessionsDetail(models.Model):
    dhs_sess_id = models.IntegerField()
    recv_date = models.IntegerField()
    trange_id = models.IntegerField()
    account_id = models.IntegerField()
    disc_per_id = models.IntegerField()
    slink_id = models.IntegerField()
    duration = models.BigIntegerField()
    base_cost = models.FloatField()
    sum_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tel_sessions_detail'


class TelSessionsLog(models.Model):
    account_id = models.IntegerField()
    slink_id = models.IntegerField()
    recv_date = models.IntegerField()
    last_update_date = models.IntegerField()
    zone_id = models.IntegerField()
    did = models.IntegerField()
    nas_port = models.IntegerField(db_column='NAS_Port')  # Field name made lowercase.
    acct_delay_time = models.IntegerField(db_column='Acct_Delay_Time')  # Field name made lowercase.
    acct_session_id = models.CharField(db_column='Acct_Session_Id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nas_port_type = models.IntegerField(db_column='NAS_Port_Type')  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=255)  # Field name made lowercase.
    service_type = models.IntegerField(db_column='Service_Type')  # Field name made lowercase.
    framed_protocol = models.IntegerField(db_column='Framed_Protocol')  # Field name made lowercase.
    nas_ip_address = models.IntegerField(db_column='NAS_IP_Address')  # Field name made lowercase.
    nas_id = models.CharField(db_column='NAS_Id', max_length=255)  # Field name made lowercase.
    acct_status_type = models.IntegerField(db_column='Acct_Status_Type')  # Field name made lowercase.
    acct_input_packets = models.BigIntegerField(db_column='Acct_Input_Packets')  # Field name made lowercase.
    acct_input_octets = models.BigIntegerField(db_column='Acct_Input_Octets')  # Field name made lowercase.
    acct_output_packets = models.BigIntegerField(db_column='Acct_Output_Packets')  # Field name made lowercase.
    acct_output_octets = models.BigIntegerField(db_column='Acct_Output_Octets')  # Field name made lowercase.
    acct_session_time = models.BigIntegerField(db_column='Acct_Session_Time')  # Field name made lowercase.
    called_station_id = models.CharField(db_column='Called_Station_Id', max_length=255)  # Field name made lowercase.
    calling_station_id = models.CharField(db_column='Calling_Station_Id', max_length=255)  # Field name made lowercase.
    h323_remote_address = models.CharField(max_length=255)
    h323_conf_id = models.CharField(max_length=255)
    h323_setup_time = models.CharField(max_length=255)
    h323_call_origin = models.CharField(max_length=255)
    h323_call_type = models.CharField(max_length=255)
    h323_connect_time = models.CharField(max_length=255)
    h323_disconnect_time = models.CharField(max_length=255)
    h323_disconnect_cause = models.CharField(max_length=255)
    h323_gw_id = models.CharField(max_length=255)
    session_start_date = models.IntegerField()
    session_end_date = models.IntegerField()
    acct_input_gigawords = models.BigIntegerField(db_column='Acct_Input_Gigawords')  # Field name made lowercase.
    acct_output_gigawords = models.BigIntegerField(db_column='Acct_Output_Gigawords')  # Field name made lowercase.
    acct_terminate_cause = models.IntegerField(db_column='Acct_Terminate_Cause')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tel_sessions_log'


class TelSessionsLogAttrs(models.Model):
    session_id = models.IntegerField()
    vendor = models.IntegerField()
    attr = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    status_type = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_sessions_log_attrs'


class TelZones(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tel_zones'


class TempIp(models.Model):
    ip = models.IntegerField()
    mac = models.CharField(max_length=255)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'temp_ip'


class TemplateType(models.Model):
    type_id = models.IntegerField()
    type_name = models.CharField(max_length=255)
    sys_doc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'template_type'


class TimeRange(models.Model):
    time_range_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'time_range'


class TimeRangeDays(models.Model):
    time_range_id = models.IntegerField()
    mday = models.IntegerField()
    month = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'time_range_days'


class TimeRangeDetail(models.Model):
    time_range_id = models.IntegerField()
    sec_start = models.IntegerField()
    sec_stop = models.IntegerField()
    min_start = models.IntegerField()
    min_stop = models.IntegerField()
    hour_start = models.IntegerField()
    hour_stop = models.IntegerField()
    wday_start = models.IntegerField()
    wday_stop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'time_range_detail'


class TrafServTclasses(models.Model):
    tst_id = models.IntegerField()
    tclass_id = models.IntegerField()
    borders_id = models.IntegerField()
    prepaid_units = models.BigIntegerField()
    prepaid_units_max = models.BigIntegerField()
    group_id = models.IntegerField()
    tariff_formula = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'traf_serv_tclasses'


class TrafficDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_id = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    bytes_in = models.BigIntegerField(blank=True, null=True)
    bytes_out = models.BigIntegerField(blank=True, null=True)
    acct_session_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traffic_detail'


class TurboModeLinks(models.Model):
    slink_id = models.IntegerField()
    tms_id = models.IntegerField()
    turbo_mode_start = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'turbo_mode_links'


class TurboModeSettings(models.Model):
    iptraf_service_id = models.IntegerField()
    once_service_id = models.IntegerField()
    duration = models.IntegerField()
    incoming_rate = models.IntegerField()
    outgoing_rate = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'turbo_mode_settings'


class UaddparamsDesc(models.Model):
    paramid = models.IntegerField()
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'uaddparams_desc'


class UserAdditionalParams(models.Model):
    paramid = models.IntegerField()
    userid = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_additional_params'


class UserContactEm(models.Model):
    name_position = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_contact_em'


class UserContacts(models.Model):
    uid = models.IntegerField()
    person = models.CharField(max_length=255)
    descr = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    email_notice = models.IntegerField()
    person_short = models.CharField(max_length=128)
    bday = models.CharField(max_length=255)
    id_exec_man = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_contacts'


class UserLog(models.Model):
    user_id = models.IntegerField()
    date = models.IntegerField()
    who = models.IntegerField()
    what = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_log'


class Users(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    basic_account = models.IntegerField()
    advance_payment = models.IntegerField()
    create_date = models.IntegerField()
    last_change_date = models.IntegerField()
    who_create = models.IntegerField()
    who_change = models.IntegerField()
    is_juridical = models.IntegerField()
    full_name = models.TextField(blank=True, null=True)
    juridical_address = models.TextField(blank=True, null=True)
    actual_address = models.TextField(blank=True, null=True)
    work_telephone = models.CharField(max_length=255)
    home_telephone = models.CharField(max_length=255)
    mobile_telephone = models.CharField(max_length=255)
    web_page = models.CharField(max_length=255)
    icq_number = models.CharField(max_length=255)
    tax_number = models.CharField(max_length=255)
    kpp_number = models.CharField(max_length=255)
    bank_id = models.IntegerField()
    bank_account = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    house_id = models.IntegerField()
    flat_number = models.CharField(max_length=255)
    entrance = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    passport = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    personal_manager = models.CharField(max_length=255)
    connect_date = models.IntegerField()
    remote_switch_id = models.IntegerField()
    port_number = models.IntegerField()
    binded_currency_code = models.IntegerField()
    is_deleted = models.IntegerField()
    is_send_invoice = models.IntegerField()
    ic_status = models.IntegerField()
    ic_id = models.CharField(max_length=255)
    last_sync_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersAccounts(models.Model):
    uid = models.IntegerField()
    account_id = models.IntegerField()
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_accounts'


class UsersGroupsLink(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_groups_link'


class Utm5CashierSettings(models.Model):
    key_u = models.CharField(max_length=255)
    value_u = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'utm5_cashier_settings'


class Utm5Settings(models.Model):
    variable = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    change_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'utm5_settings'


class Utm5TraySettings(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm5_tray_settings'


class VoluntarySuspensionData(models.Model):
    account_id = models.IntegerField()
    block_date_start = models.IntegerField()
    block_date_end = models.IntegerField()
    block_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'voluntary_suspension_data'


class VoluntarySuspensionSettings(models.Model):
    group_id = models.IntegerField()
    priority = models.IntegerField()
    is_enabled = models.IntegerField()
    min_balance = models.FloatField()
    use_min_balance = models.IntegerField()
    free_balance = models.FloatField()
    use_free_balance = models.IntegerField()
    service_id = models.IntegerField()
    min_duration = models.IntegerField()
    max_duration = models.IntegerField()
    interval_duration = models.IntegerField()
    block_type = models.IntegerField()
    self_unlock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'voluntary_suspension_settings'
