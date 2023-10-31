# Este é um módulo de modelo Django gerado automaticamente.
# Você terá que fazer o seguinte manualmente para limpar isso:
# * Reorganize a ordem dos modelos
# * Certifique-se de que cada modelo tenha um campo com primary_key=True
# * Certifique-se de que cada ForeignKey tenha `on_delete` definido para o comportamento desejado.
# * Remova as linhas `managed = False` se você deseja permitir que o Django crie, modifique e exclua a tabela
# Fique à vontade para renomear os modelos, mas não renomeie valores db_table ou nomes de campo.
from django.db import models

from users.models import Login


class AccRegNum(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acc_reg_num'
        unique_together = (('account_id', 'key', 'index'),)


class AccRegStr(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'acc_reg_str'
        unique_together = (('account_id', 'key', 'index'),)


class Achievement(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    id = models.BigIntegerField()
    count1 = models.PositiveIntegerField()
    count2 = models.PositiveIntegerField()
    count3 = models.PositiveIntegerField()
    count4 = models.PositiveIntegerField()
    count5 = models.PositiveIntegerField()
    count6 = models.PositiveIntegerField()
    count7 = models.PositiveIntegerField()
    count8 = models.PositiveIntegerField()
    count9 = models.PositiveIntegerField()
    count10 = models.PositiveIntegerField()
    completed = models.DateTimeField(blank=True, null=True)
    rewarded = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'achievement'
        unique_together = (('char_id', 'id'),)


class Auction(models.Model):
    auction_id = models.BigAutoField(primary_key=True)
    seller_id = models.PositiveIntegerField()
    seller_name = models.CharField(max_length=30)
    buyer_id = models.PositiveIntegerField()
    buyer_name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    buynow = models.PositiveIntegerField()
    hours = models.SmallIntegerField()
    timestamp = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    item_name = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auction'


class BonusScript(models.Model):
    char_id = models.PositiveIntegerField()
    script = models.TextField()
    tick = models.BigIntegerField()
    flag = models.PositiveSmallIntegerField()
    type = models.PositiveIntegerField()
    icon = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'bonus_script'


class BuyingstoreItems(models.Model):
    buyingstore_id = models.PositiveIntegerField()
    index = models.PositiveSmallIntegerField()
    item_id = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'buyingstore_items'


class Buyingstores(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    map = models.CharField(max_length=20)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=80)
    limit = models.PositiveIntegerField()
    body_direction = models.CharField(max_length=1)
    head_direction = models.CharField(max_length=1)
    sit = models.CharField(max_length=1)
    autotrade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'buyingstores'


class CartInventory(models.Model):
    char_id = models.IntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.IntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.IntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cart_inventory'


class CharRegNum(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'char_reg_num'
        unique_together = (('char_id', 'key', 'index'),)


class CharRegStr(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'char_reg_str'
        unique_together = (('char_id', 'key', 'index'),)


class Charlog(models.Model):
    time = models.DateTimeField()
    char_msg = models.CharField(max_length=255)
    account_id = models.IntegerField()
    char_num = models.IntegerField()
    name = models.CharField(max_length=23)
    str = models.PositiveIntegerField()
    agi = models.PositiveIntegerField()
    vit = models.PositiveIntegerField()
    int = models.PositiveIntegerField()
    dex = models.PositiveIntegerField()
    luk = models.PositiveIntegerField()
    hair = models.IntegerField()
    hair_color = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'charlog'


class Clan(models.Model):
    clan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    master = models.CharField(max_length=24)
    mapname = models.CharField(max_length=24)
    max_member = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'clan'


class ClanAlliance(models.Model):
    clan_id = models.PositiveIntegerField(primary_key=True)
    opposition = models.PositiveIntegerField()
    alliance_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'clan_alliance'
        unique_together = (('clan_id', 'alliance_id'),)


class DbRoulette(models.Model):
    index = models.IntegerField(primary_key=True)
    level = models.PositiveSmallIntegerField()
    item_id = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()
    flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'db_roulette'


class Elemental(models.Model):
    ele_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')  # Campo renomeado porque era uma palavra reservada do Python.
    mode = models.PositiveIntegerField()
    hp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    max_hp = models.PositiveIntegerField()
    max_sp = models.PositiveIntegerField()
    atk1 = models.PositiveIntegerField()
    atk2 = models.PositiveIntegerField()
    matk = models.PositiveIntegerField()
    aspd = models.PositiveSmallIntegerField()
    def_field = models.PositiveSmallIntegerField(db_column='def')  # Campo renomeado porque era uma palavra reservada do Python.
    mdef = models.PositiveSmallIntegerField()
    flee = models.PositiveSmallIntegerField()
    hit = models.PositiveSmallIntegerField()
    life_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'elemental'


class Friends(models.Model):
    char_id = models.IntegerField()
    friend_account = models.IntegerField()
    friend_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'friends'


class GlobalAccRegNum(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'global_acc_reg_num'
        unique_together = (('account_id', 'key', 'index'),)


class GlobalAccRegStr(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'global_acc_reg_str'
        unique_together = (('account_id', 'key', 'index'),)


class Guild(models.Model):
    guild_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    char_id = models.PositiveIntegerField()
    master = models.CharField(max_length=24)
    guild_lv = models.PositiveIntegerField()
    connect_member = models.PositiveIntegerField()
    max_member = models.PositiveIntegerField()
    average_lv = models.PositiveSmallIntegerField()
    exp = models.BigIntegerField()
    next_exp = models.PositiveIntegerField()
    skill_point = models.PositiveIntegerField()
    mes1 = models.CharField(max_length=60)
    mes2 = models.CharField(max_length=120)
    emblem_len = models.PositiveIntegerField()
    emblem_id = models.PositiveIntegerField()
    emblem_data = models.TextField(blank=True, null=True)
    last_master_change = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guild'
        unique_together = (('guild_id', 'char_id'),)


class GuildAlliance(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    opposition = models.PositiveIntegerField()
    alliance_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_alliance'
        unique_together = (('guild_id', 'alliance_id'),)


class GuildCastle(models.Model):
    castle_id = models.PositiveIntegerField(primary_key=True)
    guild_id = models.PositiveIntegerField()
    economy = models.PositiveIntegerField()
    defense = models.PositiveIntegerField()
    triggere = models.PositiveIntegerField(db_column='triggerE')  # Nome do campo em minúsculas
    triggerd = models.PositiveIntegerField(db_column='triggerD')  # Nome do campo em minúsculas
    nexttime = models.PositiveIntegerField(db_column='nextTime')  # Nome do campo em minúsculas
    paytime = models.PositiveIntegerField(db_column='payTime')  # Nome do campo em minúsculas
    createtime = models.PositiveIntegerField(db_column='createTime')  # Nome do campo em minúsculas
    visiblec = models.PositiveIntegerField(db_column='visibleC')  # Nome do campo em minúsculas
    visibleg0 = models.PositiveIntegerField(db_column='visibleG0')  # Nome do campo em minúsculas
    visibleg1 = models.PositiveIntegerField(db_column='visibleG1')  # Nome do campo em minúsculas
    visibleg2 = models.PositiveIntegerField(db_column='visibleG2')  # Nome do campo em minúsculas
    visibleg3 = models.PositiveIntegerField(db_column='visibleG3')  # Nome do campo em minúsculas
    visibleg4 = models.PositiveIntegerField(db_column='visibleG4')  # Nome do campo em minúsculas
    visibleg5 = models.PositiveIntegerField(db_column='visibleG5')  # Nome do campo em minúsculas
    visibleg6 = models.PositiveIntegerField(db_column='visibleG6')  # Nome do campo em minúsculas
    visibleg7 = models.PositiveIntegerField(db_column='visibleG7')  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'guild_castle'


class GuildExpulsion(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    mes = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'guild_expulsion'
        unique_together = (('guild_id', 'name'),)


class GuildMember(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    hair = models.PositiveIntegerField()
    hair_color = models.PositiveSmallIntegerField()
    gender = models.PositiveIntegerField()
    class_field = models.PositiveSmallIntegerField(db_column='class')  # Campo renomeado porque era uma palavra reservada do Python.
    lv = models.PositiveSmallIntegerField()
    exp = models.BigIntegerField()
    exp_payper = models.PositiveIntegerField()
    online = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'guild_member'
        unique_together = (('guild_id', 'char_id'),)


class GuildPosition(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    position = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    mode = models.PositiveSmallIntegerField()
    exp_mode = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_position'
        unique_together = (('guild_id', 'position'),)


class GuildSkill(models.Model):
    guild_id = models.PositiveIntegerField(primary_key=True)
    id = models.PositiveSmallIntegerField()
    lv = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_skill'
        unique_together = (('guild_id', 'id'),)


class GuildStorage(models.Model):
    guild_id = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.PositiveSmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_storage'


class GuildStorageLog(models.Model):
    guild_id = models.PositiveIntegerField()
    time = models.DateTimeField()
    char_id = models.IntegerField()
    name = models.CharField(max_length=24)
    nameid = models.PositiveSmallIntegerField()
    amount = models.IntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()
    bound = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guild_storage_log'


class Homunculus(models.Model):
    homun_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')  # Campo renomeado porque era uma palavra reservada do Python.
    prev_class = models.IntegerField()
    name = models.CharField(max_length=24)
    level = models.SmallIntegerField()
    exp = models.BigIntegerField()
    intimacy = models.IntegerField()
    hunger = models.SmallIntegerField()
    str = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    luk = models.PositiveSmallIntegerField()
    hp = models.PositiveIntegerField()
    max_hp = models.PositiveIntegerField()
    sp = models.IntegerField()
    max_sp = models.IntegerField()
    skill_point = models.PositiveSmallIntegerField()
    alive = models.IntegerField()
    rename_flag = models.IntegerField()
    vaporize = models.IntegerField()
    autofeed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'homunculus'


class Hotkey(models.Model):
    char_id = models.IntegerField(primary_key=True)
    hotkey = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    itemskill_id = models.PositiveIntegerField()
    skill_lvl = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'hotkey'
        unique_together = (('char_id', 'hotkey'),)


class Interlog(models.Model):
    time = models.DateTimeField()
    log = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'interlog'


class Interreg(models.Model):
    varname = models.CharField(primary_key=True, max_length=11)
    value = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'interreg'


class Inventory(models.Model):
    char_id = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    favorite = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()
    equip_switch = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Ipbanlist(models.Model):
    list = models.CharField(max_length=255)
    btime = models.DateTimeField()
    rtime = models.DateTimeField()
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ipbanlist'


class ItemCashDb(models.Model):
    tab = models.SmallIntegerField(primary_key=True)
    item_id = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'item_cash_db'
        unique_together = (('tab', 'item_id'),)


class ItemCashDb2(models.Model):
    tab = models.SmallIntegerField(primary_key=True)
    item_id = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'item_cash_db2'
        unique_together = (('tab', 'item_id'),)


class ItemDb(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name_english = models.CharField(unique=True, max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    price_buy = models.PositiveIntegerField(blank=True, null=True)
    price_sell = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField(blank=True, null=True)
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.PositiveIntegerField(blank=True, null=True)
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level = models.PositiveIntegerField(blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)
    view = models.PositiveSmallIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db'


class ItemDb2(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name_english = models.CharField(unique=True, max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    price_buy = models.PositiveIntegerField(blank=True, null=True)
    price_sell = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField(blank=True, null=True)
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.PositiveIntegerField(blank=True, null=True)
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level = models.PositiveIntegerField(blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)
    view = models.PositiveSmallIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db2'


class ItemDb2Re(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name_english = models.CharField(unique=True, max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    price_buy = models.PositiveIntegerField(blank=True, null=True)
    price_sell = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    atk_matk = models.CharField(db_column='atk:matk', max_length=11, blank=True, null=True)  # Campo renomeado para remover caracteres inadequados.
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.PositiveIntegerField(blank=True, null=True)
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level = models.CharField(max_length=10, blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)
    view = models.PositiveSmallIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db2_re'


class ItemDbRe(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name_english = models.CharField(unique=True, max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    price_buy = models.PositiveIntegerField(blank=True, null=True)
    price_sell = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField()
    atk_matk = models.CharField(db_column='atk:matk', max_length=11, blank=True, null=True)  # Campo renomeado para remover caracteres inadequados.
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)
    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_upper = models.PositiveIntegerField(blank=True, null=True)
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level = models.CharField(max_length=10, blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)
    view = models.PositiveSmallIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db_re'


class Mail(models.Model):
    id = models.BigAutoField(primary_key=True)
    send_name = models.CharField(max_length=30)
    send_id = models.PositiveIntegerField()
    dest_name = models.CharField(max_length=30)
    dest_id = models.PositiveIntegerField()
    title = models.CharField(max_length=45)
    message = models.CharField(max_length=500)
    time = models.PositiveIntegerField()
    status = models.IntegerField()
    zeny = models.PositiveIntegerField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mail'


class MailAttachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    index = models.PositiveSmallIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    unique_id = models.BigIntegerField()
    bound = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'mail_attachments'
        unique_together = (('id', 'index'),)


class Mapreg(models.Model):
    varname = models.CharField(primary_key=True, max_length=32)
    index = models.PositiveIntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mapreg'
        unique_together = (('varname', 'index'),)


class Market(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    nameid = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    flag = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'market'
        unique_together = (('name', 'nameid'),)


class Memo(models.Model):
    memo_id = models.AutoField(primary_key=True)
    char_id = models.PositiveIntegerField()
    map = models.CharField(max_length=11)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'memo'


class Mercenary(models.Model):
    mer_id = models.AutoField(primary_key=True)
    char_id = models.IntegerField()
    class_field = models.PositiveIntegerField(db_column='class')  # Campo renomeado porque era uma palavra reservada do Python.
    hp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    kill_counter = models.IntegerField()
    life_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mercenary'


class MercenaryOwner(models.Model):
    char_id = models.IntegerField(primary_key=True)
    merc_id = models.IntegerField()
    arch_calls = models.IntegerField()
    arch_faith = models.IntegerField()
    spear_calls = models.IntegerField()
    spear_faith = models.IntegerField()
    sword_calls = models.IntegerField()
    sword_faith = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mercenary_owner'


class MobDb(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Nome do campo em minúsculas
    sprite = models.TextField(db_column='Sprite')  # Nome do campo em minúsculas
    kname = models.TextField(db_column='kName')  # Nome do campo em minúsculas
    iname = models.TextField(db_column='iName')  # Nome do campo em minúsculas
    lv = models.PositiveIntegerField(db_column='LV')  # Nome do campo em minúsculas
    hp = models.PositiveIntegerField(db_column='HP')  # Nome do campo em minúsculas
    sp = models.PositiveIntegerField(db_column='SP')  # Nome do campo em minúsculas
    exp = models.PositiveIntegerField(db_column='EXP')  # Nome do campo em minúsculas
    jexp = models.PositiveIntegerField(db_column='JEXP')  # Nome do campo em minúsculas
    range1 = models.PositiveIntegerField(db_column='Range1')  # Nome do campo em minúsculas
    atk1 = models.PositiveSmallIntegerField(db_column='ATK1')  # Nome do campo em minúsculas
    atk2 = models.PositiveSmallIntegerField(db_column='ATK2')  # Nome do campo em minúsculas
    def_field = models.PositiveSmallIntegerField(db_column='DEF')  # Nome do campo em minúsculas Campo renomeado porque era uma palavra reservada do Python.
    mdef = models.PositiveSmallIntegerField(db_column='MDEF')  # Nome do campo em minúsculas
    str = models.PositiveSmallIntegerField(db_column='STR')  # Nome do campo em minúsculas
    agi = models.PositiveSmallIntegerField(db_column='AGI')  # Nome do campo em minúsculas
    vit = models.PositiveSmallIntegerField(db_column='VIT')  # Nome do campo em minúsculas
    int = models.PositiveSmallIntegerField(db_column='INT')  # Nome do campo em minúsculas
    dex = models.PositiveSmallIntegerField(db_column='DEX')  # Nome do campo em minúsculas
    luk = models.PositiveSmallIntegerField(db_column='LUK')  # Nome do campo em minúsculas
    range2 = models.PositiveIntegerField(db_column='Range2')  # Nome do campo em minúsculas
    range3 = models.PositiveIntegerField(db_column='Range3')  # Nome do campo em minúsculas
    scale = models.PositiveIntegerField(db_column='Scale')  # Nome do campo em minúsculas
    race = models.PositiveIntegerField(db_column='Race')  # Nome do campo em minúsculas
    element = models.PositiveIntegerField(db_column='Element')  # Nome do campo em minúsculas
    mode = models.PositiveIntegerField(db_column='Mode')  # Nome do campo em minúsculas
    speed = models.PositiveSmallIntegerField(db_column='Speed')  # Nome do campo em minúsculas
    adelay = models.PositiveSmallIntegerField(db_column='aDelay')  # Nome do campo em minúsculas
    amotion = models.PositiveSmallIntegerField(db_column='aMotion')  # Nome do campo em minúsculas
    dmotion = models.PositiveSmallIntegerField(db_column='dMotion')  # Nome do campo em minúsculas
    mexp = models.PositiveIntegerField(db_column='MEXP')  # Nome do campo em minúsculas
    mvp1id = models.PositiveSmallIntegerField(db_column='MVP1id')  # Nome do campo em minúsculas
    mvp1per = models.PositiveSmallIntegerField(db_column='MVP1per')  # Nome do campo em minúsculas
    mvp2id = models.PositiveSmallIntegerField(db_column='MVP2id')  # Nome do campo em minúsculas
    mvp2per = models.PositiveSmallIntegerField(db_column='MVP2per')  # Nome do campo em minúsculas
    mvp3id = models.PositiveSmallIntegerField(db_column='MVP3id')  # Nome do campo em minúsculas
    mvp3per = models.PositiveSmallIntegerField(db_column='MVP3per')  # Nome do campo em minúsculas
    drop1id = models.PositiveSmallIntegerField(db_column='Drop1id')  # Nome do campo em minúsculas
    drop1per = models.PositiveSmallIntegerField(db_column='Drop1per')  # Nome do campo em minúsculas
    drop2id = models.PositiveSmallIntegerField(db_column='Drop2id')  # Nome do campo em minúsculas
    drop2per = models.PositiveSmallIntegerField(db_column='Drop2per')  # Nome do campo em minúsculas
    drop3id = models.PositiveSmallIntegerField(db_column='Drop3id')  # Nome do campo em minúsculas
    drop3per = models.PositiveSmallIntegerField(db_column='Drop3per')  # Nome do campo em minúsculas
    drop4id = models.PositiveSmallIntegerField(db_column='Drop4id')  # Nome do campo em minúsculas
    drop4per = models.PositiveSmallIntegerField(db_column='Drop4per')  # Nome do campo em minúsculas
    drop5id = models.PositiveSmallIntegerField(db_column='Drop5id')  # Nome do campo em minúsculas
    drop5per = models.PositiveSmallIntegerField(db_column='Drop5per')  # Nome do campo em minúsculas
    drop6id = models.PositiveSmallIntegerField(db_column='Drop6id')  # Nome do campo em minúsculas
    drop6per = models.PositiveSmallIntegerField(db_column='Drop6per')  # Nome do campo em minúsculas
    drop7id = models.PositiveSmallIntegerField(db_column='Drop7id')  # Nome do campo em minúsculas
    drop7per = models.PositiveSmallIntegerField(db_column='Drop7per')  # Nome do campo em minúsculas
    drop8id = models.PositiveSmallIntegerField(db_column='Drop8id')  # Nome do campo em minúsculas
    drop8per = models.PositiveSmallIntegerField(db_column='Drop8per')  # Nome do campo em minúsculas
    drop9id = models.PositiveSmallIntegerField(db_column='Drop9id')  # Nome do campo em minúsculas
    drop9per = models.PositiveSmallIntegerField(db_column='Drop9per')  # Nome do campo em minúsculas
    dropcardid = models.PositiveSmallIntegerField(db_column='DropCardid')  # Nome do campo em minúsculas
    dropcardper = models.PositiveSmallIntegerField(db_column='DropCardper')  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_db'


class MobDb2(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Nome do campo em minúsculas
    sprite = models.TextField(db_column='Sprite')  # Nome do campo em minúsculas
    kname = models.TextField(db_column='kName')  # Nome do campo em minúsculas
    iname = models.TextField(db_column='iName')  # Nome do campo em minúsculas
    lv = models.PositiveIntegerField(db_column='LV')  # Nome do campo em minúsculas
    hp = models.PositiveIntegerField(db_column='HP')  # Nome do campo em minúsculas
    sp = models.PositiveIntegerField(db_column='SP')  # Nome do campo em minúsculas
    exp = models.PositiveIntegerField(db_column='EXP')  # Nome do campo em minúsculas
    jexp = models.PositiveIntegerField(db_column='JEXP')  # Nome do campo em minúsculas
    range1 = models.PositiveIntegerField(db_column='Range1')  # Nome do campo em minúsculas
    atk1 = models.PositiveSmallIntegerField(db_column='ATK1')  # Nome do campo em minúsculas
    atk2 = models.PositiveSmallIntegerField(db_column='ATK2')  # Nome do campo em minúsculas
    def_field = models.PositiveSmallIntegerField(db_column='DEF')  # Nome do campo em minúsculas Campo renomeado porque era uma palavra reservada do Python.
    mdef = models.PositiveSmallIntegerField(db_column='MDEF')  # Nome do campo em minúsculas
    str = models.PositiveSmallIntegerField(db_column='STR')  # Nome do campo em minúsculas
    agi = models.PositiveSmallIntegerField(db_column='AGI')  # Nome do campo em minúsculas
    vit = models.PositiveSmallIntegerField(db_column='VIT')  # Nome do campo em minúsculas
    int = models.PositiveSmallIntegerField(db_column='INT')  # Nome do campo em minúsculas
    dex = models.PositiveSmallIntegerField(db_column='DEX')  # Nome do campo em minúsculas
    luk = models.PositiveSmallIntegerField(db_column='LUK')  # Nome do campo em minúsculas
    range2 = models.PositiveIntegerField(db_column='Range2')  # Nome do campo em minúsculas
    range3 = models.PositiveIntegerField(db_column='Range3')  # Nome do campo em minúsculas
    scale = models.PositiveIntegerField(db_column='Scale')  # Nome do campo em minúsculas
    race = models.PositiveIntegerField(db_column='Race')  # Nome do campo em minúsculas
    element = models.PositiveIntegerField(db_column='Element')  # Nome do campo em minúsculas
    mode = models.PositiveIntegerField(db_column='Mode')  # Nome do campo em minúsculas
    speed = models.PositiveSmallIntegerField(db_column='Speed')  # Nome do campo em minúsculas
    adelay = models.PositiveSmallIntegerField(db_column='aDelay')  # Nome do campo em minúsculas
    amotion = models.PositiveSmallIntegerField(db_column='aMotion')  # Nome do campo em minúsculas
    dmotion = models.PositiveSmallIntegerField(db_column='dMotion')  # Nome do campo em minúsculas
    mexp = models.PositiveIntegerField(db_column='MEXP')  # Nome do campo em minúsculas
    mvp1id = models.PositiveSmallIntegerField(db_column='MVP1id')  # Nome do campo em minúsculas
    mvp1per = models.PositiveSmallIntegerField(db_column='MVP1per')  # Nome do campo em minúsculas
    mvp2id = models.PositiveSmallIntegerField(db_column='MVP2id')  # Nome do campo em minúsculas
    mvp2per = models.PositiveSmallIntegerField(db_column='MVP2per')  # Nome do campo em minúsculas
    mvp3id = models.PositiveSmallIntegerField(db_column='MVP3id')  # Nome do campo em minúsculas
    mvp3per = models.PositiveSmallIntegerField(db_column='MVP3per')  # Nome do campo em minúsculas
    drop1id = models.PositiveSmallIntegerField(db_column='Drop1id')  # Nome do campo em minúsculas
    drop1per = models.PositiveSmallIntegerField(db_column='Drop1per')  # Nome do campo em minúsculas
    drop2id = models.PositiveSmallIntegerField(db_column='Drop2id')  # Nome do campo em minúsculas
    drop2per = models.PositiveSmallIntegerField(db_column='Drop2per')  # Nome do campo em minúsculas
    drop3id = models.PositiveSmallIntegerField(db_column='Drop3id')  # Nome do campo em minúsculas
    drop3per = models.PositiveSmallIntegerField(db_column='Drop3per')  # Nome do campo em minúsculas
    drop4id = models.PositiveSmallIntegerField(db_column='Drop4id')  # Nome do campo em minúsculas
    drop4per = models.PositiveSmallIntegerField(db_column='Drop4per')  # Nome do campo em minúsculas
    drop5id = models.PositiveSmallIntegerField(db_column='Drop5id')  # Nome do campo em minúsculas
    drop5per = models.PositiveSmallIntegerField(db_column='Drop5per')  # Nome do campo em minúsculas
    drop6id = models.PositiveSmallIntegerField(db_column='Drop6id')  # Nome do campo em minúsculas
    drop6per = models.PositiveSmallIntegerField(db_column='Drop6per')  # Nome do campo em minúsculas
    drop7id = models.PositiveSmallIntegerField(db_column='Drop7id')  # Nome do campo em minúsculas
    drop7per = models.PositiveSmallIntegerField(db_column='Drop7per')  # Nome do campo em minúsculas
    drop8id = models.PositiveSmallIntegerField(db_column='Drop8id')  # Nome do campo em minúsculas
    drop8per = models.PositiveSmallIntegerField(db_column='Drop8per')  # Nome do campo em minúsculas
    drop9id = models.PositiveSmallIntegerField(db_column='Drop9id')  # Nome do campo em minúsculas
    drop9per = models.PositiveSmallIntegerField(db_column='Drop9per')  # Nome do campo em minúsculas
    dropcardid = models.PositiveSmallIntegerField(db_column='DropCardid')  # Nome do campo em minúsculas
    dropcardper = models.PositiveSmallIntegerField(db_column='DropCardper')  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_db2'


class MobDb2Re(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Nome do campo em minúsculas
    sprite = models.TextField(db_column='Sprite')  # Nome do campo em minúsculas
    kname = models.TextField(db_column='kName')  # Nome do campo em minúsculas
    iname = models.TextField(db_column='iName')  # Nome do campo em minúsculas
    lv = models.PositiveIntegerField(db_column='LV')  # Nome do campo em minúsculas
    hp = models.PositiveIntegerField(db_column='HP')  # Nome do campo em minúsculas
    sp = models.PositiveIntegerField(db_column='SP')  # Nome do campo em minúsculas
    exp = models.PositiveIntegerField(db_column='EXP')  # Nome do campo em minúsculas
    jexp = models.PositiveIntegerField(db_column='JEXP')  # Nome do campo em minúsculas
    range1 = models.PositiveIntegerField(db_column='Range1')  # Nome do campo em minúsculas
    atk1 = models.PositiveSmallIntegerField(db_column='ATK1')  # Nome do campo em minúsculas
    atk2 = models.PositiveSmallIntegerField(db_column='ATK2')  # Nome do campo em minúsculas
    def_field = models.PositiveSmallIntegerField(db_column='DEF')  # Nome do campo em minúsculas Campo renomeado porque era uma palavra reservada do Python.
    mdef = models.PositiveSmallIntegerField(db_column='MDEF')  # Nome do campo em minúsculas
    str = models.PositiveSmallIntegerField(db_column='STR')  # Nome do campo em minúsculas
    agi = models.PositiveSmallIntegerField(db_column='AGI')  # Nome do campo em minúsculas
    vit = models.PositiveSmallIntegerField(db_column='VIT')  # Nome do campo em minúsculas
    int = models.PositiveSmallIntegerField(db_column='INT')  # Nome do campo em minúsculas
    dex = models.PositiveSmallIntegerField(db_column='DEX')  # Nome do campo em minúsculas
    luk = models.PositiveSmallIntegerField(db_column='LUK')  # Nome do campo em minúsculas
    range2 = models.PositiveIntegerField(db_column='Range2')  # Nome do campo em minúsculas
    range3 = models.PositiveIntegerField(db_column='Range3')  # Nome do campo em minúsculas
    scale = models.PositiveIntegerField(db_column='Scale')  # Nome do campo em minúsculas
    race = models.PositiveIntegerField(db_column='Race')  # Nome do campo em minúsculas
    element = models.PositiveIntegerField(db_column='Element')  # Nome do campo em minúsculas
    mode = models.PositiveIntegerField(db_column='Mode')  # Nome do campo em minúsculas
    speed = models.PositiveSmallIntegerField(db_column='Speed')  # Nome do campo em minúsculas
    adelay = models.PositiveSmallIntegerField(db_column='aDelay')  # Nome do campo em minúsculas
    amotion = models.PositiveSmallIntegerField(db_column='aMotion')  # Nome do campo em minúsculas
    dmotion = models.PositiveSmallIntegerField(db_column='dMotion')  # Nome do campo em minúsculas
    mexp = models.PositiveIntegerField(db_column='MEXP')  # Nome do campo em minúsculas
    mvp1id = models.PositiveSmallIntegerField(db_column='MVP1id')  # Nome do campo em minúsculas
    mvp1per = models.PositiveSmallIntegerField(db_column='MVP1per')  # Nome do campo em minúsculas
    mvp2id = models.PositiveSmallIntegerField(db_column='MVP2id')  # Nome do campo em minúsculas
    mvp2per = models.PositiveSmallIntegerField(db_column='MVP2per')  # Nome do campo em minúsculas
    mvp3id = models.PositiveSmallIntegerField(db_column='MVP3id')  # Nome do campo em minúsculas
    mvp3per = models.PositiveSmallIntegerField(db_column='MVP3per')  # Nome do campo em minúsculas
    drop1id = models.PositiveSmallIntegerField(db_column='Drop1id')  # Nome do campo em minúsculas
    drop1per = models.PositiveSmallIntegerField(db_column='Drop1per')  # Nome do campo em minúsculas
    drop2id = models.PositiveSmallIntegerField(db_column='Drop2id')  # Nome do campo em minúsculas
    drop2per = models.PositiveSmallIntegerField(db_column='Drop2per')  # Nome do campo em minúsculas
    drop3id = models.PositiveSmallIntegerField(db_column='Drop3id')  # Nome do campo em minúsculas
    drop3per = models.PositiveSmallIntegerField(db_column='Drop3per')  # Nome do campo em minúsculas
    drop4id = models.PositiveSmallIntegerField(db_column='Drop4id')  # Nome do campo em minúsculas
    drop4per = models.PositiveSmallIntegerField(db_column='Drop4per')  # Nome do campo em minúsculas
    drop5id = models.PositiveSmallIntegerField(db_column='Drop5id')  # Nome do campo em minúsculas
    drop5per = models.PositiveSmallIntegerField(db_column='Drop5per')  # Nome do campo em minúsculas
    drop6id = models.PositiveSmallIntegerField(db_column='Drop6id')  # Nome do campo em minúsculas
    drop6per = models.PositiveSmallIntegerField(db_column='Drop6per')  # Nome do campo em minúsculas
    drop7id = models.PositiveSmallIntegerField(db_column='Drop7id')  # Nome do campo em minúsculas
    drop7per = models.PositiveSmallIntegerField(db_column='Drop7per')  # Nome do campo em minúsculas
    drop8id = models.PositiveSmallIntegerField(db_column='Drop8id')  # Nome do campo em minúsculas
    drop8per = models.PositiveSmallIntegerField(db_column='Drop8per')  # Nome do campo em minúsculas
    drop9id = models.PositiveSmallIntegerField(db_column='Drop9id')  # Nome do campo em minúsculas
    drop9per = models.PositiveSmallIntegerField(db_column='Drop9per')  # Nome do campo em minúsculas
    dropcardid = models.PositiveSmallIntegerField(db_column='DropCardid')  # Nome do campo em minúsculas
    dropcardper = models.PositiveSmallIntegerField(db_column='DropCardper')  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_db2_re'


class MobDbRe(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Nome do campo em minúsculas
    sprite = models.TextField(db_column='Sprite')  # Nome do campo em minúsculas
    kname = models.TextField(db_column='kName')  # Nome do campo em minúsculas
    iname = models.TextField(db_column='iName')  # Nome do campo em minúsculas
    lv = models.PositiveIntegerField(db_column='LV')  # Nome do campo em minúsculas
    hp = models.PositiveIntegerField(db_column='HP')  # Nome do campo em minúsculas
    sp = models.PositiveIntegerField(db_column='SP')  # Nome do campo em minúsculas
    exp = models.PositiveIntegerField(db_column='EXP')  # Nome do campo em minúsculas
    jexp = models.PositiveIntegerField(db_column='JEXP')  # Nome do campo em minúsculas
    range1 = models.PositiveIntegerField(db_column='Range1')  # Nome do campo em minúsculas
    atk1 = models.PositiveSmallIntegerField(db_column='ATK1')  # Nome do campo em minúsculas
    atk2 = models.PositiveSmallIntegerField(db_column='ATK2')  # Nome do campo em minúsculas
    def_field = models.PositiveSmallIntegerField(db_column='DEF')  # Nome do campo em minúsculas Campo renomeado porque era uma palavra reservada do Python.
    mdef = models.PositiveSmallIntegerField(db_column='MDEF')  # Nome do campo em minúsculas
    str = models.PositiveSmallIntegerField(db_column='STR')  # Nome do campo em minúsculas
    agi = models.PositiveSmallIntegerField(db_column='AGI')  # Nome do campo em minúsculas
    vit = models.PositiveSmallIntegerField(db_column='VIT')  # Nome do campo em minúsculas
    int = models.PositiveSmallIntegerField(db_column='INT')  # Nome do campo em minúsculas
    dex = models.PositiveSmallIntegerField(db_column='DEX')  # Nome do campo em minúsculas
    luk = models.PositiveSmallIntegerField(db_column='LUK')  # Nome do campo em minúsculas
    range2 = models.PositiveIntegerField(db_column='Range2')  # Nome do campo em minúsculas
    range3 = models.PositiveIntegerField(db_column='Range3')  # Nome do campo em minúsculas
    scale = models.PositiveIntegerField(db_column='Scale')  # Nome do campo em minúsculas
    race = models.PositiveIntegerField(db_column='Race')  # Nome do campo em minúsculas
    element = models.PositiveIntegerField(db_column='Element')  # Nome do campo em minúsculas
    mode = models.PositiveIntegerField(db_column='Mode')  # Nome do campo em minúsculas
    speed = models.PositiveSmallIntegerField(db_column='Speed')  # Nome do campo em minúsculas
    adelay = models.PositiveSmallIntegerField(db_column='aDelay')  # Nome do campo em minúsculas
    amotion = models.PositiveSmallIntegerField(db_column='aMotion')  # Nome do campo em minúsculas
    dmotion = models.PositiveSmallIntegerField(db_column='dMotion')  # Nome do campo em minúsculas
    mexp = models.PositiveIntegerField(db_column='MEXP')  # Nome do campo em minúsculas
    mvp1id = models.PositiveSmallIntegerField(db_column='MVP1id')  # Nome do campo em minúsculas
    mvp1per = models.PositiveSmallIntegerField(db_column='MVP1per')  # Nome do campo em minúsculas
    mvp2id = models.PositiveSmallIntegerField(db_column='MVP2id')  # Nome do campo em minúsculas
    mvp2per = models.PositiveSmallIntegerField(db_column='MVP2per')  # Nome do campo em minúsculas
    mvp3id = models.PositiveSmallIntegerField(db_column='MVP3id')  # Nome do campo em minúsculas
    mvp3per = models.PositiveSmallIntegerField(db_column='MVP3per')  # Nome do campo em minúsculas
    drop1id = models.PositiveSmallIntegerField(db_column='Drop1id')  # Nome do campo em minúsculas
    drop1per = models.PositiveSmallIntegerField(db_column='Drop1per')  # Nome do campo em minúsculas
    drop2id = models.PositiveSmallIntegerField(db_column='Drop2id')  # Nome do campo em minúsculas
    drop2per = models.PositiveSmallIntegerField(db_column='Drop2per')  # Nome do campo em minúsculas
    drop3id = models.PositiveSmallIntegerField(db_column='Drop3id')  # Nome do campo em minúsculas
    drop3per = models.PositiveSmallIntegerField(db_column='Drop3per')  # Nome do campo em minúsculas
    drop4id = models.PositiveSmallIntegerField(db_column='Drop4id')  # Nome do campo em minúsculas
    drop4per = models.PositiveSmallIntegerField(db_column='Drop4per')  # Nome do campo em minúsculas
    drop5id = models.PositiveSmallIntegerField(db_column='Drop5id')  # Nome do campo em minúsculas
    drop5per = models.PositiveSmallIntegerField(db_column='Drop5per')  # Nome do campo em minúsculas
    drop6id = models.PositiveSmallIntegerField(db_column='Drop6id')  # Nome do campo em minúsculas
    drop6per = models.PositiveSmallIntegerField(db_column='Drop6per')  # Nome do campo em minúsculas
    drop7id = models.PositiveSmallIntegerField(db_column='Drop7id')  # Nome do campo em minúsculas
    drop7per = models.PositiveSmallIntegerField(db_column='Drop7per')  # Nome do campo em minúsculas
    drop8id = models.PositiveSmallIntegerField(db_column='Drop8id')  # Nome do campo em minúsculas
    drop8per = models.PositiveSmallIntegerField(db_column='Drop8per')  # Nome do campo em minúsculas
    drop9id = models.PositiveSmallIntegerField(db_column='Drop9id')  # Nome do campo em minúsculas
    drop9per = models.PositiveSmallIntegerField(db_column='Drop9per')  # Nome do campo em minúsculas
    dropcardid = models.PositiveSmallIntegerField(db_column='DropCardid')  # Nome do campo em minúsculas
    dropcardper = models.PositiveSmallIntegerField(db_column='DropCardper')  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_db_re'


class MobSkillDb(models.Model):
    mob_id = models.SmallIntegerField(db_column='MOB_ID')  # Nome do campo em minúsculas
    info = models.TextField(db_column='INFO')  # Nome do campo em minúsculas
    state = models.TextField(db_column='STATE')  # Nome do campo em minúsculas
    skill_id = models.SmallIntegerField(db_column='SKILL_ID')  # Nome do campo em minúsculas
    skill_lv = models.IntegerField(db_column='SKILL_LV')  # Nome do campo em minúsculas
    rate = models.SmallIntegerField(db_column='RATE')  # Nome do campo em minúsculas
    casttime = models.IntegerField(db_column='CASTTIME')  # Nome do campo em minúsculas
    delay = models.IntegerField(db_column='DELAY')  # Nome do campo em minúsculas
    cancelable = models.TextField(db_column='CANCELABLE')  # Nome do campo em minúsculas
    target = models.TextField(db_column='TARGET')  # Nome do campo em minúsculas
    condition = models.TextField(db_column='CONDITION')  # Nome do campo em minúsculas
    condition_value = models.TextField(db_column='CONDITION_VALUE', blank=True, null=True)  # Nome do campo em minúsculas
    val1 = models.IntegerField(db_column='VAL1', blank=True, null=True)  # Nome do campo em minúsculas
    val2 = models.IntegerField(db_column='VAL2', blank=True, null=True)  # Nome do campo em minúsculas
    val3 = models.IntegerField(db_column='VAL3', blank=True, null=True)  # Nome do campo em minúsculas
    val4 = models.IntegerField(db_column='VAL4', blank=True, null=True)  # Nome do campo em minúsculas
    val5 = models.IntegerField(db_column='VAL5', blank=True, null=True)  # Nome do campo em minúsculas
    emotion = models.TextField(db_column='EMOTION', blank=True, null=True)  # Nome do campo em minúsculas
    chat = models.TextField(db_column='CHAT', blank=True, null=True)  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_skill_db'


class MobSkillDb2(models.Model):
    mob_id = models.SmallIntegerField(db_column='MOB_ID')  # Nome do campo em minúsculas
    info = models.TextField(db_column='INFO')  # Nome do campo em minúsculas
    state = models.TextField(db_column='STATE')  # Nome do campo em minúsculas
    skill_id = models.SmallIntegerField(db_column='SKILL_ID')  # Nome do campo em minúsculas
    skill_lv = models.IntegerField(db_column='SKILL_LV')  # Nome do campo em minúsculas
    rate = models.SmallIntegerField(db_column='RATE')  # Nome do campo em minúsculas
    casttime = models.IntegerField(db_column='CASTTIME')  # Nome do campo em minúsculas
    delay = models.IntegerField(db_column='DELAY')  # Nome do campo em minúsculas
    cancelable = models.TextField(db_column='CANCELABLE')  # Nome do campo em minúsculas
    target = models.TextField(db_column='TARGET')  # Nome do campo em minúsculas
    condition = models.TextField(db_column='CONDITION')  # Nome do campo em minúsculas
    condition_value = models.TextField(db_column='CONDITION_VALUE', blank=True, null=True)  # Nome do campo em minúsculas
    val1 = models.IntegerField(db_column='VAL1', blank=True, null=True)  # Nome do campo em minúsculas
    val2 = models.IntegerField(db_column='VAL2', blank=True, null=True)  # Nome do campo em minúsculas
    val3 = models.IntegerField(db_column='VAL3', blank=True, null=True)  # Nome do campo em minúsculas
    val4 = models.IntegerField(db_column='VAL4', blank=True, null=True)  # Nome do campo em minúsculas
    val5 = models.IntegerField(db_column='VAL5', blank=True, null=True)  # Nome do campo em minúsculas
    emotion = models.TextField(db_column='EMOTION', blank=True, null=True)  # Nome do campo em minúsculas
    chat = models.TextField(db_column='CHAT', blank=True, null=True)  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_skill_db2'


class MobSkillDb2Re(models.Model):
    mob_id = models.SmallIntegerField(db_column='MOB_ID')  # Nome do campo em minúsculas
    info = models.TextField(db_column='INFO')  # Nome do campo em minúsculas
    state = models.TextField(db_column='STATE')  # Nome do campo em minúsculas
    skill_id = models.SmallIntegerField(db_column='SKILL_ID')  # Nome do campo em minúsculas
    skill_lv = models.IntegerField(db_column='SKILL_LV')  # Nome do campo em minúsculas
    rate = models.SmallIntegerField(db_column='RATE')  # Nome do campo em minúsculas
    casttime = models.IntegerField(db_column='CASTTIME')  # Nome do campo em minúsculas
    delay = models.IntegerField(db_column='DELAY')  # Nome do campo em minúsculas
    cancelable = models.TextField(db_column='CANCELABLE')  # Nome do campo em minúsculas
    target = models.TextField(db_column='TARGET')  # Nome do campo em minúsculas
    condition = models.TextField(db_column='CONDITION')  # Nome do campo em minúsculas
    condition_value = models.TextField(db_column='CONDITION_VALUE', blank=True, null=True)  # Nome do campo em minúsculas
    val1 = models.IntegerField(db_column='VAL1', blank=True, null=True)  # Nome do campo em minúsculas
    val2 = models.IntegerField(db_column='VAL2', blank=True, null=True)  # Nome do campo em minúsculas
    val3 = models.IntegerField(db_column='VAL3', blank=True, null=True)  # Nome do campo em minúsculas
    val4 = models.IntegerField(db_column='VAL4', blank=True, null=True)  # Nome do campo em minúsculas
    val5 = models.IntegerField(db_column='VAL5', blank=True, null=True)  # Nome do campo em minúsculas
    emotion = models.TextField(db_column='EMOTION', blank=True, null=True)  # Nome do campo em minúsculas
    chat = models.TextField(db_column='CHAT', blank=True, null=True)  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_skill_db2_re'


class MobSkillDbRe(models.Model):
    mob_id = models.SmallIntegerField(db_column='MOB_ID')  # Nome do campo em minúsculas
    info = models.TextField(db_column='INFO')  # Nome do campo em minúsculas
    state = models.TextField(db_column='STATE')  # Nome do campo em minúsculas
    skill_id = models.SmallIntegerField(db_column='SKILL_ID')  # Nome do campo em minúsculas
    skill_lv = models.IntegerField(db_column='SKILL_LV')  # Nome do campo em minúsculas
    rate = models.SmallIntegerField(db_column='RATE')  # Nome do campo em minúsculas
    casttime = models.IntegerField(db_column='CASTTIME')  # Nome do campo em minúsculas
    delay = models.IntegerField(db_column='DELAY')  # Nome do campo em minúsculas
    cancelable = models.TextField(db_column='CANCELABLE')  # Nome do campo em minúsculas
    target = models.TextField(db_column='TARGET')  # Nome do campo em minúsculas
    condition = models.TextField(db_column='CONDITION')  # Nome do campo em minúsculas
    condition_value = models.TextField(db_column='CONDITION_VALUE', blank=True, null=True)  # Nome do campo em minúsculas
    val1 = models.IntegerField(db_column='VAL1', blank=True, null=True)  # Nome do campo em minúsculas
    val2 = models.IntegerField(db_column='VAL2', blank=True, null=True)  # Nome do campo em minúsculas
    val3 = models.IntegerField(db_column='VAL3', blank=True, null=True)  # Nome do campo em minúsculas
    val4 = models.IntegerField(db_column='VAL4', blank=True, null=True)  # Nome do campo em minúsculas
    val5 = models.IntegerField(db_column='VAL5', blank=True, null=True)  # Nome do campo em minúsculas
    emotion = models.TextField(db_column='EMOTION', blank=True, null=True)  # Nome do campo em minúsculas
    chat = models.TextField(db_column='CHAT', blank=True, null=True)  # Nome do campo em minúsculas

    class Meta:
        managed = False
        db_table = 'mob_skill_db_re'


class Party(models.Model):
    party_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    exp = models.PositiveIntegerField()
    item = models.PositiveIntegerField()
    leader_id = models.PositiveIntegerField()
    leader_char = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'party'


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    class_field = models.PositiveIntegerField(db_column='class')  # Campo renomeado porque era uma palavra reservada do Python.
    name = models.CharField(max_length=24)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField()
    egg_id = models.PositiveSmallIntegerField()
    equip = models.PositiveIntegerField()
    intimate = models.PositiveSmallIntegerField()
    hungry = models.PositiveSmallIntegerField()
    rename_flag = models.PositiveIntegerField()
    incubate = models.PositiveIntegerField()
    autofeed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet'


class Quest(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    quest_id = models.PositiveIntegerField()
    state = models.CharField(max_length=1)
    time = models.PositiveIntegerField()
    count1 = models.PositiveIntegerField()
    count2 = models.PositiveIntegerField()
    count3 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'quest'
        unique_together = (('char_id', 'quest_id'),)


class Ragsrvinfo(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=255)
    exp = models.PositiveIntegerField()
    jexp = models.PositiveIntegerField()
    drop = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ragsrvinfo'


class Sales(models.Model):
    nameid = models.PositiveSmallIntegerField(primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales'


class ScData(models.Model):
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField()
    tick = models.BigIntegerField()
    val1 = models.IntegerField()
    val2 = models.IntegerField()
    val3 = models.IntegerField()
    val4 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sc_data'


class Skill(models.Model):
    char_id = models.PositiveIntegerField(primary_key=True)
    id = models.PositiveSmallIntegerField()
    lv = models.PositiveIntegerField()
    flag = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'skill'
        unique_together = (('char_id', 'id'),)


class SkillHomunculus(models.Model):
    homun_id = models.IntegerField(primary_key=True)
    id = models.IntegerField()
    lv = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'skill_homunculus'
        unique_together = (('homun_id', 'id'),)


class Skillcooldown(models.Model):
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    skill = models.PositiveSmallIntegerField()
    tick = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'skillcooldown'


class Sstatus(models.Model):
    index = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    user = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'sstatus'


class Storage(models.Model):
    account_id = models.PositiveIntegerField()
    nameid = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.PositiveSmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'storage'


class VendingItems(models.Model):
    vending_id = models.PositiveIntegerField()
    index = models.PositiveSmallIntegerField()
    cartinventory_id = models.PositiveIntegerField()
    amount = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'vending_items'


class Vendings(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    account_id = models.PositiveIntegerField()
    char_id = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    map = models.CharField(max_length=20)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=80)
    body_direction = models.CharField(max_length=1)
    head_direction = models.CharField(max_length=1)
    sit = models.CharField(max_length=1)
    autotrade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendings'
