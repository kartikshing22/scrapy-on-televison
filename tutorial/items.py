# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    refresh = scrapy.Field()
    slug = scrapy.Field()
    name = scrapy.Field()
    contrast_ratio=scrapy.Field()
    bluetooth=scrapy.Field()
    #basic things
    name=scrapy.Field()
    slug=scrapy.Field()
    announced=scrapy.Field()
    price=scrapy.Field()
    Warranty=scrapy.Field()
    Box_Contents=scrapy.Field()
    visible_individually=scrapy.Field()
    status=scrapy.Field()
    market_status=scrapy.Field()

    #display
    display_type=scrapy.Field()
    display_size_diagonal=scrapy.Field()
    display_resolution=scrapy.Field()
    display_resolution_filter=scrapy.Field()
    display_led_backlight_type=scrapy.Field()
    global_display_refresh_rate=scrapy.Field()
    display_brightness=scrapy.Field()
    display_contrast_ratio=scrapy.Field()
    display_aspect_ratio=scrapy.Field()
    display_3d_tv=scrapy.Field()
    display_curved_tv=scrapy.Field()
    display_horizontal_viewing_angles=scrapy.Field()
    display_ultra_slim_tv=scrapy.Field()
    display_vertical_viewing_angles=scrapy.Field()
    display_local_dimming=scrapy.Field()
    display_response_time=scrapy.Field()
    display_curvature=scrapy.Field()
    display_clear_motion_rate=scrapy.Field()
    display_curvature=scrapy.Field()
    display_perfect_motion_rate=scrapy.Field()
    display_other_display_features=scrapy.Field()

    
    

    
    pass
