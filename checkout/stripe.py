import stripe

from django.conf import settings

SILVER = 's'
GOLD = 'g'


class SimDriverSchoolSilverPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_SILVER_PLAN
        self.amount = 499


class SimDriverSchoolGoldPlan:
    def __init__(self):
        self.stripe_plan_id = settings.STRIPE_GOLD_PLAN
        self.amount = 999


