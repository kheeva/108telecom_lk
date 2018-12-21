from django.db import models


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


class Users108(models.Model):
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
