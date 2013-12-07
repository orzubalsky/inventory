from django.db.models import *


class DecisionProcessType(Mode):
    """
    DecisionProcessType is a way in which a decision is made.
    it is used in relation to ProfitUseType objects.

    Examples of DecisionProcessType objects:
        'Consensus',
        'Majority vote',
        'Plurality vote',
        'Random'
    """
    name = CharField()


class SurplusAppropriationType(Model):
    """
    SurplusAppropriationType is a way of directing surplus.
    It is used in relation to Profit objects, in a m2m relationship.

    Examples of ProfitUseType objects:
        'For the well being of those who labored',
        'For the well being of those controlling the producing entity',
        'For the development of the producing entity',
        'To be added to the commons',
        'Cannot be disclosed'
    """
    name = CharField()
    decision_type = ForeignKey(DecisionProcessType)


class LaborType(Model):
    """
    LaborType is a type of labor that resulted in aquiring a kind of good.

    Examples of LaborType objects:
        'Volunteer',
        'Gift',
        'Barter',
        'Full time',
        'Part time',
        'Temporary',
        'Personal interest',
        'Housework',
        'Family Care',
    """
    name = CharField()
    is_paid = BooleanField()
    is_collective = BooleanField()
    with_joy = BooleanField()
    start_date = DateTimeField()
    end_date = DateTimeField()


class Profit(Model):
    """
    Profit is something that was gained through labor.
    It does not have to be quantitive or acquired through any specific way.
    It is used loosely in order to create a diverse economy.
    """
    name = CharField()
    is_speculative = BooleanField()
    labor_type = ForeignKey(LaborType)
    surplus_uses = ManyToManyField(PurposeTypes)
    tags = TaggableManager()
