# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1335447455.963388
_template_filename = '/Users/wolf/Sites/engine.dactions.org/dactionsengine/dactionsengine/templates/results.mako'
_template_uri = '/results.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['head_tags']


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
        int = context.get('int', UNDEFINED)
        c = context.get('c', UNDEFINED)
        range = context.get('range', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n\t<div class="contents_wrapper">\n\t\t<div class="contents" id="challenge">\n\t\t\t<h1>Challenges</h1>\n')
        # SOURCE LINE 10
        for challenge in c.result.challenges:
            # SOURCE LINE 11
            __M_writer(u'\t\t\t    <h3>')
            __M_writer(escape(challenge["type"]))
            __M_writer(u' #')
            __M_writer(escape(challenge["id"]))
            __M_writer(u'</h3><p>')
            __M_writer(escape(challenge["challenge"]))
            __M_writer(u'</p>\n')
            pass
        # SOURCE LINE 13
        __M_writer(u'\n\t\t\t<p class="note">\n\t\t\t\tTuesday, ')
        # SOURCE LINE 15
        __M_writer(escape(c.result.date))
        __M_writer(u' at 19:00 at ')
        __M_writer(escape(c.result.location["venue"]))
        __M_writer(u', ')
        __M_writer(escape(c.result.location["address"]))
        __M_writer(u', ')
        __M_writer(escape(c.result.location["city"]))
        __M_writer(u', ')
        __M_writer(escape(c.result.location["country"]))
        __M_writer(u'.\n\n')
        # SOURCE LINE 17
        if len(c.result.pictures) > 0:
            # SOURCE LINE 18
            __M_writer(u'\t\t\t\t    Pictures are\n')
            # SOURCE LINE 19
            for pics in c.result.pictures:
                # SOURCE LINE 20
                __M_writer(u'\t\t\t\t        <a href="')
                __M_writer(escape(pics))
                __M_writer(u'" title="Pictures from ')
                __M_writer(escape(c.result.date))
                __M_writer(u'">here</a>\n')
                pass
            # SOURCE LINE 22
            __M_writer(u'\t\t\t\t    .\n')
            pass
        # SOURCE LINE 24
        __M_writer(u'\n\t\t\t</p>\n\t\t</div>\n\t</div>\n\n')
        # SOURCE LINE 29
        for team in c.result.teams:
            # SOURCE LINE 30
            __M_writer(u'        <div class="team">\n            <div class="contents_wrapper">\n                <div class="contents">\n                    <h2>Team ')
            # SOURCE LINE 33
            __M_writer(escape(team["id"]))
            __M_writer(u'</h2>\n                    <h3>Members</h3>\n                    <p>\n                        ')
            # SOURCE LINE 36

            m = []
            for member in team["members"]:
                m.append(member.name)
                                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['member','m'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 40
            __M_writer(u'\n                        ')
            # SOURCE LINE 41
            __M_writer(escape(u" × ".join(m)))
            __M_writer(u'\n                    </p>\n                    <h3>Challenge</h3>\n                    <p>\n                        ')
            # SOURCE LINE 45
            __M_writer(escape(challenge["type"]))
            __M_writer(u' #')
            __M_writer(escape(challenge["id"]))
            __M_writer(u'\n                    </p>\n                </div>\n            </div>\n        </div>\n        <div class="contents_wrapper">\n            <div id="contents_box">\n                <div class="contents">\n')
            # SOURCE LINE 53
            for i in range(int(team["pages"])):
                # SOURCE LINE 54
                __M_writer(u'                        <img class="result" src="/')
                __M_writer(escape(c.result.path))
                __M_writer(escape(team["id"]))
                __M_writer(escape(i+1))
                __M_writer(u'.png" alt="Solution Team A" />\n')
                pass
            # SOURCE LINE 56
            __M_writer(u'                </div>\n            </div>\n        </div>\n')
            pass
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


