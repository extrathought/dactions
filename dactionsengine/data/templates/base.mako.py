# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1335435306.963989
_template_filename = u'/Users/wolf/Sites/engine.dactions.org/dactionsengine/dactionsengine/templates/base.mako'
_template_uri = u'/base.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t  <meta charset="utf-8">\n\t\t<title>DestrActions: Singapore\'s Monthly Design Distraction &amp; Interaction</title>\n\t\t<link rel="shortcut icon" href="/favicon.png" />\n\t\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Arvo">\n\t\t<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Cantarell">\n\t\t<link rel="stylesheet" type="text/css" href="/styles.css">\n\t\t<script type="text/javascript">\n\t\t\tfunction showFAQ() {\n\t\t\t\tdocument.getElementById("show_faq").style.display = "none";\n\t\t\t\tdocument.getElementById("faq_text").style.display = "block";\n\t\t\t}\n\t\t</script>\n\t\t<!-- GOOGLE ANALYTICS //-->\n\t\t<script type="text/javascript">\n\n\t\t\tvar _gaq = _gaq || [];\n\t\t\t_gaq.push([\'_setAccount\', \'UA-30242158-1\']);\n\t\t\t_gaq.push([\'_setDomainName\', \'dactions.org\']);\n\t\t\t_gaq.push([\'_trackPageview\']);\n\n\t\t\t(function() {\n\t\t\t\tvar ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n\t\t\t\tga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n\t\t\t\tvar s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n\t\t\t})();\n\t\t</script>\n\t\t')
        # SOURCE LINE 30
        __M_writer(escape(self.head_tags()))
        __M_writer(u'\n\t</head>\n\n\n\t<body>\n\t\t')
        # SOURCE LINE 35
        __M_writer(escape(self.body()))
        __M_writer(u'\n\n        <div id="footer">\n            <div class="contents_wrapper">\n                <div class="contents">\n                    <p class="note">DestrActions is run by <a href="mailto:wm@njyo.net">Wolfgang Maehr</a> from <a href="http://www.extrathought.com">Extra Thought</a> as an effort to connect designers and enable contacts and inspiration across the fields.</p>\n                </div>\n            </div>\n        </div>\n\n\t</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


