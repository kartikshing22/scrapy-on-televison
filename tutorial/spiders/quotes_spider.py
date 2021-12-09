from urllib import parse
import scrapy
import datetime


class QuotesSpider(scrapy.Spider):
    name = "quotes"


    def start_requests(self):
        urls = open("lg.txt","r")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        refresh_rate =  response.css('tr:contains("Refresh Rate") td.spec_des::text').get()
        if refresh_rate==None:
            refresh_rate= response.css('tr:contains("Refresh Rate") td.spec_des::text').get()
        else:
            refresh_rate = refresh_rate.replace('Hz', '').strip()

        brand=response.css('tr:contains("Brand") td.spec_des::text').get().strip().lower()
        brand=brand.replace(" ", "-")+"-tv-price-in-india"

        
        slug= response.css('.h1_pro_head::text').get().strip().lower()
        slug=slug.replace(" ","-")+"-price-in-india"
        sku=slug.replace(" ", "-").replace("-price-in-india", "")
        announced=datetime.date.today()
        price=response.css('span.big_prc::text').getall()
        price=price[1]
        
        
    
        def shortfunc(value):                          
            main_value=response.css(f'tr:contains("{value}") td.spec_des::text').get()
            if main_value!=None:
                return response.css(f'tr:contains("{value}") td.spec_des::text').get().strip()
            else:
                return response.css(f'tr:contains("{value}") td.spec_des::text').get()

        

        def yesno(value):                          
            main_value=response.css(f'tr:contains("{value}") td.spec_des::text').get()
            if main_value==None:
                return response.css(f'tr:contains("{value}") td.spec_des::text').get()
            else:
                main_value= response.css(f'tr:contains("{value}") td.spec_des::text').get().strip()
                if main_value=="Yes":
                    return "1"
                else:
                    return "0"
        
        def display_resolution_filter():
            main_value=response.css('tr:contains("Resolution") td.spec_des::text').get()
            if "Full HD" in main_value:
                return "Full HD"
            elif "4K" or "Ultra HD" or "UHD" or "SUHD" in main_value:
                return "4K"
            elif "HD ready" in main_value:
                return "HD ready"
            elif "2K" in main_value:
                return "2K"
            elif "8K" in main_value:
                return "8K"

        def con_filter():
            l=[]
            main_value=response.css('tr:contains("USB Ports") td.spec_des::text').get()
            main_value=list(main_value)
            for i in main_value:
                if i=="1" or i=="2" or i=="3" or i=="4":
                    l.append(int(i))
            return(sum(l))
            
        def conn_ports_hdmi_ports_filter():
            l=[]
            main_value=response.css('tr:contains("HDMI Ports") td.spec_des::text').get()
            main_value=list(main_value)
            for i in main_value:
                if i=="1" or i=="2" or i=="3" or i=="4":
                    l.append(int(i))
            return(sum(l))

             
        a={
            #basic details
            "web-scraper-start-url":response,
            "announced":announced.today(),
            "market_status":"Available",
            "flipkart_tracking_id":None,
            "amazone_tracking_id":None,
            "status":"1",
            "visible_individually":"1",
            "https":"https:",
            "imageslink":response.css('.overview_lrg_pic_img ::attr(src)').extract(),
            "images":None,
            "attribute_family_name":"television",
            "category_slug":"televisions",
            "brand_slug":brand,
            'name': shortfunc("Model"),
            "sku":sku,
            "slug":slug,
            "price":price,
            "type":"simple",
            
            #general
            "general_warranty":shortfunc("Warranty"),
            'general_box_contents': shortfunc("Box Contents"),

            #display section
            "display_type": shortfunc("Type"),
            "display_size_diagonal":shortfunc("Size(Diagonal)"),
            "display_resolution": shortfunc("Resolution"),
            "display_resolution_filter": display_resolution_filter(),
            "display_led_backlight_type": shortfunc("Backlight Type"),
            'global_display_refresh_rate': refresh_rate,
            "display_brightness": shortfunc("Brightness"),
            "display_contrast_ratio": shortfunc("Contrast Ratio"),
            "display_aspect_ratio": "16:1",
            "display_3d_tv": yesno("3D TV"),
            "display_curved_tv": yesno("Curved TV"),
            "display_horizontal_viewing_angles": shortfunc("Horizontal Viewing Angles"),
            "display_ultra_slim_tv": yesno("Ultra Slim TV"),
            "display_vertical_viewing_angles": shortfunc("Vertical Viewing Angles"),
            "display_local_dimming": shortfunc("Local-Dimming"),
            "display_response_time": shortfunc("Response Time"),
            "display_curvature": shortfunc("Screen Curvature"),
            "display_clear_motion_rate": shortfunc("Clear Motion Rate"),
            "display_perfect_motion_rate":shortfunc("Perfect Motion Rate"),
            "display_other_display_features": shortfunc("Other Display Features"),


            #physical desgin
            "physical_design_colour": shortfunc("Colour"),
            "physical_design_weight_without_stand": shortfunc("Weight Without Stand"),
            "physical_design_weight_with_stand": shortfunc("Weight With Stand"),
            "physical_design_dimen_with_stand_wxhxd": shortfunc("Dimensions With Stand(WxHxD)"),
            "physical_design_dimen_without_stand_wxhxd": shortfunc("Dimensions Without Stand(WxHxD)"),
            "physical_design_wall_mount_dimen_wxhxd": shortfunc("Wall Mount Dimensions(WxHxD)"),
            "physical_design_wall_mount_colour": shortfunc("Wall Mount Colour"),
            "physical_design_stand_colour": shortfunc("Stand Colour"),
            "physical_design_stand_features": shortfunc("Stand Features"),
            "physical_design_stand_material": shortfunc("Stand Material"),
            "physical_design_stand_shape": shortfunc("Stand Shape"),
            "physical_design_stand_weight": shortfunc("Stand Weight"),
            "physical_design_other_design_features": shortfunc("Other Design Features"),
            
            #video
            "video_digital_tv_reception_formats": shortfunc("Digital TV Reception Formats"),
            "video_analog_tv_reception_formats": shortfunc("Analog TV Reception Formats"),
            "video_video_formats_supported": shortfunc("Video Formats Supported"),
            "video_image_formats_supported": shortfunc("Image Formats Supported"),
            "video_upscaling": shortfunc("Upscaling"),
            "video_video_signals": shortfunc("Video Signals"),
            "video_pc_signals": shortfunc("PC Signals"),

            #audio
            "audio_sound_type": shortfunc("Sound Type"),
            "audio_audio_formats_supported": shortfunc("Audio Formats Supported"),
            "audio_no_of_speakers": shortfunc("No. of Speakers"),
            "audio_output_per_speaker": shortfunc("Output per Speaker"),
            "audio_total_speaker_output": shortfunc("Total Speaker Output"),
            "audio_speaker_frequency_range": shortfunc("Speaker Frequency Range"),
            "audio_total_tweeter_output": shortfunc("Total Tweeter Output"),
            "audio_no_of_subwoofers": shortfunc("No. of Subwoofers"),
            "audio_sound_technology": shortfunc("Sound Technology"),
            "audio_no_of_tweeters": shortfunc("No. of Tweeters"),
            "audio_output_per_subwoofer": shortfunc("Output per Subwoofer"),
            "audio_total_subbwoofer_output": shortfunc("Total Subwoofer Output"),
            "audio_other_smart_audio_features": shortfunc("Other Smart Audio Features"),

            #connectivity/ports
            "conn_ports_usb_ports": shortfunc("USB Ports"),
            "conn_ports_usb_ports_filter": con_filter(),
            "conn_ports_usb_supports": shortfunc("USB Supports"),
            "conn_ports_hdmi_ports": shortfunc("HDMI Ports"),
            "conn_ports_hdmi_ports_filter": conn_ports_hdmi_ports_filter(),
            "conn_ports_digital_optical_ao_ports": shortfunc("Digital/Optical Audio output ports"),
            "conn_ports_headphone_speaker_o_ports": shortfunc("Headphone/Speaker output ports"),
            "conn_ports_rf_input_analog_coaxial_ports": shortfunc("RF Input(Analog Coaxial) Ports"),
            "conn_ports_ethernet_sockets": shortfunc("Ethernet Sockets"),
            "conn_ports_mhl_enabled": yesno("MHL Enabled"),
            "conn_ports_vga_input_ports": shortfunc("VGA Input Ports"),
            "conn_ports_composite_input_avc_ports": shortfunc("Composite Input(Audio Video Cable) Ports"),
            "conn_ports_nfc_ports": shortfunc("NFC Ports"),
            "conn_ports_rca_output_ports": shortfunc("RCA Output Ports"),
            "conn_ports_compo_output_rgb_i_ports": shortfunc("Component Output(RGB input) Ports"),

            #smart_tv_features
            "smart_tv_features_smart_tv": yesno("Smart TV"),
            "smart_tv_features_wifi_present": yesno("Wifi Present"),
            "smart_tv_features_band_support": shortfunc("Band Support"),
            "smart_tv_features_bluetooth": yesno("Bluetooth"),
            "smart_tv_features_bluetooth_version": shortfunc("Bluetooth Version"),
            "smart_tv_features_processer_type": shortfunc("Processor Type"),
            "smart_tv_features_inbuilt_apps": shortfunc("Inbuilt Apps"),
            "smart_tv_features_fb_and_social_media_integration": yesno("Facebook and Social Media Integration"),
            "smart_tv_features_games": yesno("Games"),
            "smart_tv_features_camera": yesno("Camera"),
            "smart_tv_features_microphone": yesno("Microphone"),
            "smart_tv_features_voice_recognition": yesno("Voice Recognition"),
            "smart_tv_features_gesture_recognition": yesno("Gesture Recognition"),
            "smart_tv_features_facial_recognition": yesno("Facial Recognition"),
            "smart_tv_features_miracast_screen_mirroring_support": yesno("Miracast/Screen Mirroring Support"),
            "smart_tv_features_wifi_direct_support": yesno("Wifi-Direct Support"),
            "smart_tv_features_maximum_speed": shortfunc("Maximum Speed"),
            "smart_tv_features_android_tv": yesno("Android TV"),
            "smart_tv_features_other_smart_features": shortfunc("Other Smart Features"),

            #remote
            "remote_remote_type": shortfunc("Remote Type"),
            "remote_touch_control_present": yesno("Touch Control Present"),
            "remote_internet_access": yesno("Internet Access"),
            "remote_universal_control_present": yesno("Universal Control Present"),
            "remote_cell_requirement": shortfunc("Cell Requirement"),
            "remote_other_remote_features": shortfunc("Other Remote Features"),

            #power Supply
            "power_supply_voltage_requirement": shortfunc("Voltage Requirement"),
            "power_supply_frequency_requirement": shortfunc("Frequency Requirement"),
            "power_supply_power_consmption_running": shortfunc("Power Consmption Running"),
            "power_supply_power_consmption_standby": shortfunc("Power Consmption Standby"),
            "power_supply_power_saving_mode": yesno("Power Saving Mode"),
            "power_supply_energy_star_compliant": shortfunc("Energy Star Compliant"),        
        }
        """
        data = TutorialItem()
        
        for key,value in a.items():
            data[key] = value
        """    
        yield(a)
  
