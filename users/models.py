from .bases import base_user
from .manager import user_manager
from django.db import models
from nuts.cache.models import cache
from nuts.fields import cache_field


class  user (base_user):
    def get_rooter_model (self):
        from nuts.rooting.rooters.rooters import default_rooter
        return default_rooter

