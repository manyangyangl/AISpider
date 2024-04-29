from . import BaseItem
from scrapy import Field


class EcouncilItem(BaseItem):
    app_number = Field()
    description = Field()
    type_of_work = Field()
    date_lodged = Field()
    cost = Field()
    determination_details = Field()
    determination_date = Field()
    application_stages_and_status = Field()
    document = Field()

    class Meta:
        table = 'bayside'
        unique_fields = ['app_number', ]
