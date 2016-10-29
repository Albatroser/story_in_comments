from django.forms import ModelForm
from glue.models import Community, Vkaccount


class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ['vk_domen', 'name', 'url']


class VkaccountForm(ModelForm):
    class Meta:
        model = Vkaccount
        fields = ['token', 'name']
