# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1335450175.089637
_template_filename = '/Users/wolf/Sites/engine.dactions.org/dactionsengine/dactionsengine/templates/error.mako'
_template_uri = '/error.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['title', 'heading', 'head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n<p>')
        # SOURCE LINE 10
        __M_writer(escape(c.message))
        __M_writer(u'</p>\n\n\n\n\t<div class="contents_wrapper">\n\t\t<div class="contents">\n\t\t\t<h3>Manifesto</h3>\n\t\t\t<p>\n\t\t\t\tWe &hearts; design meet-ups to mingle and network, to inspire and being inspired. But we miss variety\n\t\t\t\tin topics and activities. In our daily project routines we dread for creative interruptions and small challenges\n\t\t\t\tto keep our minds nimble. Therefore working an evening on out-of-context challenge with new faces is sheer bliss.\n\t\t\t</p>\n\t\t</div>\n\t</div>\n\t\n\t<div id="banner">\n\t\t<div class="contents_wrapper">\n\t\t\t<div class="contents">\n\t\t\t\t<h1>')
        # SOURCE LINE 28
        __M_writer(escape(c.error))
        __M_writer(u'</h1>\n\t\t\t\t<h6>We cannot find what you are looking for. Sorry :(</h6>\n\t\t\t\n\t\t\t\t<h3>Next Event</h3>\n\t\t\t\t<p>\n\t\t\t\t\tTuesday, March 20 at 19:00 (7pm)<br/>\n\t\t\t\t\tAt <a href="http://thepigeonhole.com.sg/" name="link to location">The Pigeonhole</a>, 52/53 Duxton Road. <a href="http://maps.google.com.sg/maps?q=The+Pidgeonhole,+52%2F53+Duxton+Road,+Singapore&hl=en&ll=1.279286,103.843267&spn=0.011563,0.015385&sll=1.278179,103.843328&sspn=0.011563,0.015385&vpsrc=0&hq=The+Pidgeonhole,&hnear=53+Duxton+Rd,+Singapore+089517&t=m&cid=8372603932834912927&z=16&iwloc=A" name="link to location map">(map)</a>\n\t\t\t\t</p>\n\n\t\t\t\t<h3>Signup</h3>\n\t\t\t\t<p><a href="https://www.flickevents.com/destractions-sg-march-2012">Signup via FlickEvents</a></p>\n\t\t\t\n\t\t\t\t<h3>Contact</h3>\n\t\t\t\t<p>\n\t\t\t\t\tTwitter: <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter"> @DActions</a>\n\t\t\t\t\t&nbsp;&nbsp;&times;&nbsp;&nbsp;Facebook: <a href="http://www.facebook.com/groups/DActions.SG" name="Link to DActions on Facebook"> DActions.SG</a>\n\t\t\t\t\t&nbsp;&nbsp;&times;&nbsp;&nbsp;e-Mail:\n\t\t\t\t\t<a href="mailto:info@dactions.org" name="e-mail to DActions"> info@dactions.org</a>\n\t\t\t\t</p>\n\t\t\t\t<h3>Cost</h3>\n\t\t\t\t<p>free but we encourage you to get a drink or two</p>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'Server Error ')
        __M_writer(escape(c.code))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'<h1>Error ')
        __M_writer(escape(c.code))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  <!-- add some head tags here -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


