from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from image_filer.models import ImagePublication, ImageFilerTeaser

class ImagePlugin(CMSPluginBase):
    model = ImagePublication
    name = _("Image (image filer)")
    render_template = "cms/plugins/picture.html"
    text_enabled = True
    raw_id_fields = ('image',)
    
    def render(self, context, instance, placeholder):
        if instance.free_link:
            link = instance.free_link
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'picture':instance,
            'link':link, 
            'placeholder':placeholder
        })
        return context
    def icon_src(self, instance):
        return instance.image.file.extra_thumbnails['admin_tiny_icon']
plugin_pool.register_plugin(ImagePlugin)

class ImageFilerTeaserPlugin(CMSPluginBase):
    model = ImageFilerTeaser
    name = _("Teaser (image filer)")
    render_template = "cms/plugins/teaser.html"
    
    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        context.update({
            'object':instance, 
            'placeholder':placeholder,
            'link':link
        })
        return context
plugin_pool.register_plugin(ImageFilerTeaserPlugin)
