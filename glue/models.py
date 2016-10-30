import vk_api
from django.db import models


class Vkaccount(models.Model):
    name = models.CharField(max_length=300, default="")
    token = models.CharField(max_length=300)
    vk_id = models.IntegerField()
    pic_url = models.CharField(max_length=300, default="")

    @property
    def api(self):
        return vk_api.VkApi(token=self.token)

    def __str__(self):
        return self.name


class Community(models.Model):
    vk_domen = models.IntegerField()
    url = models.CharField(max_length=300, default="")
    name = models.CharField(max_length=300, default="")

    def save(self):
        domen_name = self.url.split("://")[1].split("/")[1]
        if "public" in domen_name:
            domen_name = domen_name.split("public")[1]
        self.vk_domen = vk_api.VkApi().method(
            "groups.getById", {'group_ids': domen_name}
        )[0].get("id")

        super().save()

    def __str__(self):
        return self.name
