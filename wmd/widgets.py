from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class WMDWidget(forms.Textarea):
    def __init__(self, large=False, *args, **kwargs):
        if large:
            attrs = kwargs.setdefault('attrs', {
                'class': 'extraLargeTextField wmd-panel',
            })
        else:
            attrs = kwargs.setdefault('attrs', {
                'class': 'vLargeTextField wmd-panel',
            })
        super(WMDWidget, self).__init__(*args, **kwargs)

    @property
    def media(self):
        return forms.Media(
            css = {'screen': ('wmd/wmd.css',)},
            js = ('wmd/wmd.js',)
        )

    def render(self, name, value, attrs=None):
        rendered = mark_safe(u'<div class="wmd-button-bar wmd-panel" id="wmd-bar-%s"></div>' % (attrs['id']))
        rendered += super(WMDWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''
            <div id="wmd-preview-%s" class="wmd-preview">
                <div class="wmd-preview-label">Preview:</div>
                <div class='wmd-preview-area' class="wmd-panel"></div>
            </div>
            <script type="text/javascript">
                setup_wmd({
                    input: "%s",
                    button_bar: "wmd-bar-%s",
                    preview: "wmd-preview-%s",
                    helpLink: "http://daringfireball.net/projects/markdown/syntax"
            });
            </script>
            ''' % (attrs['id']))
