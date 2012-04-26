# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1335447262.376354
_template_filename = '/Users/wolf/Sites/engine.dactions.org/dactionsengine/dactionsengine/templates/index.mako'
_template_uri = '/index.mako'
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
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n\t<div class="contents_wrapper">\n\t\t<div class="contents">\n\t\t\t<h3>Manifesto</h3>\n\t\t\t<p>\n\t\t\t\tWe &hearts; design meet-ups to mingle and network, to inspire and being inspired. But we miss variety\n\t\t\t\tin topics and activities. In our daily project routines we dread for creative interruptions and small challenges\n\t\t\t\tto keep our minds nimble. Therefore working an evening on out-of-context challenge with new faces is sheer bliss.\n\t\t\t</p>\n\t\t</div>\n\t</div>\n\t\n\t<div id="banner">\n\t\t<div class="contents_wrapper">\n\t\t\t<div class="contents">\n\t\t\t\t<h1>DestrActions</h1>\n\t\t\t\t<h6>Design&nbsp;&nbsp;&times;&nbsp;&nbsp;Distraction&nbsp;&nbsp;&times;&nbsp;&nbsp;Interaction</h6>\n\t\t\t\n\t\t\t\t<h3>Details</h3>\n\t\t\t\t<p>\n\t\t\t\t\tTuesday, ')
        # SOURCE LINE 26
        __M_writer(escape(c.next_date))
        __M_writer(u' at 19:00 (7pm)<br/>\n\t\t\t\t\tAt <a href="http://thepigeonhole.com.sg/" name="link to location">The Pigeonhole</a>, 52/53 Duxton Road. <a href="http://maps.google.com.sg/maps?q=The+Pidgeonhole,+52%2F53+Duxton+Road,+Singapore&hl=en&ll=1.279286,103.843267&spn=0.011563,0.015385&sll=1.278179,103.843328&sspn=0.011563,0.015385&vpsrc=0&hq=The+Pidgeonhole,&hnear=53+Duxton+Rd,+Singapore+089517&t=m&cid=8372603932834912927&z=16&iwloc=A" name="link to location map">(map)</a>\n\t\t\t\t</p>\n\n\t\t\t\t<h3>Signup</h3>\n\t\t\t\t<p><a href="https://www.flickevents.com/destractions-sg-march-2012">Signup via FlickEvents</a></p>\n\t\t\t\n\t\t\t\t<h3>Contact</h3>\n\t\t\t\t<p>\n\t\t\t\t\tTwitter: <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter"> @DActions</a>\n\t\t\t\t\t&nbsp;&nbsp;&times;&nbsp;&nbsp;Facebook: <a href="http://www.facebook.com/groups/DActions.SG" name="Link to DActions on Facebook"> DActions.SG</a>\n\t\t\t\t\t&nbsp;&nbsp;&times;&nbsp;&nbsp;e-Mail:\n\t\t\t\t\t<a href="mailto:info@dactions.org" name="e-mail to DActions"> info@dactions.org</a>\n\t\t\t\t</p>\n\t\t\t\t<h3>Cost</h3>\n\t\t\t\t<p>free but we encourage you to get a drink or two</p>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n\n\t<div class="contents_wrapper">\n\t\t<div id="contents_box">\n\t\t\t<div class="contents">\n\n\t\t\t\t<h3>What</h3>\n\t\t\t\t<p>We meet on the <em>3rd&nbsp;Tuesday every month</em> with fellow designers to <em>collaborate</em> a few hours on <em>small design challenges</em> across the disciplines. We conclude the session with a brief presentation and discussion of the designs before making them available online.</p>\n\t\t\t\t<h3>Who</h3>\n\t\t\t\t<p>\n\t\t\t\t\tThe sessions are <em>open for everybody</em> with interest in designing stuff. You don\'t need to be an architect,\n\t\t\t\t\tindustrial/graphic/fashion/etc. designer, ergonomist or artist to join. The engineer, business girl, accounting guy,\n\t\t\t\t\tkindergarden teacher or hobby inventor is as welcome to join and get their creative juices flow. The goal is to open up to other\n\t\t\t\t\tdesign ideas, get out of the comfort zone and be inspired.<br/><br />\n\t\t\t\t\tWho we don\u2019t want are elitists, design divas and rockstars that can\u2019t collaborate. <em>Keep it simple and down to\n\t\t\t\t\tearth, creative and sharing.</em> It\u2019s to tickle your brain out of the routine.\n\t\t\t\t</p>\n\t\t\t\t<h3>Format</h3>\n\t\t\t\t<table>\n\t\t\t\t\t<tr><th>Challenge</th><td>Pitch and explanation of the different challenges to choose from. If you have proposals please <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter">tweet</a> or <a href="mailto:info@dactions.org" name="e-mail to DActions">e-mail</a> them.</td></tr>\n\t\t\t\t\t<tr><th>Team Lottery</th><td>A simple hat-lottery system to draft the groups to make sure you don\'t always work with your buddies.</td></tr>\n\t\t\t\t\t<tr><th>Team Work</th><td>Group work for 90 minutes to design the proposals (i.e. brainstorming, discussion, sketching, etc.).</td></tr>\n\t\t\t\t\t<tr><th>Presentation</th><td>Each group briefly presents their designs with a short discussion and feedback session.</td></tr>\n\t\t\t\t</table>\n\t\n\t\t\t\t<h3>Supplies</h3>\n\t\t\t\t<p>\n\t\t\t\t\tBring you jolly self, your <em>charm, sharp mind and keen eye</em>, your design instinct and anything else\n\t\t\t\t\tthat has been dulled down. Bringing your <em>favourite designing pen and paper</em> will help to come up with results.\n\t\t\t\t</p>\n\t\n\t\t\t\t<h3>Results</h3>\n\t\t\t\t<p>\n\t\t\t\t\tIn the end the <em>results will be published online as Creative Commons Attribution</em> so you can share and refer to them. The place for this\n\t\t\t\t\thas not yet been decided.\n\t\t\t\t</p>\n\t\t\t\t\t\n\t\t\t</div>\n\t\t\t<div class="right">\n\t\t\t\t<h4>Session Results</h4>\n\n                <ul>\n')
        # SOURCE LINE 86
        for result in c.results:
            # SOURCE LINE 87
            __M_writer(u'                        <li>\n                            ')
            # SOURCE LINE 88
            __M_writer(escape(result.date))
            __M_writer(u': <a href="')
            __M_writer(escape(result.path))
            __M_writer(u'" title="Results from ')
            __M_writer(escape(result.date))
            __M_writer(u'">Results</a>\n')
            # SOURCE LINE 89
            if len(result.pictures) > 0:
                # SOURCE LINE 90
                __M_writer(u'                                -\n')
                # SOURCE LINE 91
                for pics in result.pictures:
                    # SOURCE LINE 92
                    __M_writer(u'                                    <a href="')
                    __M_writer(escape(pics))
                    __M_writer(u'" title="Pictures from ')
                    __M_writer(escape(result.date))
                    __M_writer(u'">Pics</a>\n')
                    pass
                pass
            # SOURCE LINE 95
            __M_writer(u'                        </li>\n')
            pass
        # SOURCE LINE 97
        __M_writer(u'                </ul>\n\n\t\t\t\t<p class="separator">&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;</p>\n\t\t\t\t\n\t\t\t\t<h4>Related Events</h4>\n\t\t\t\t<ul>\n\t\t\t\t\t<li><a href="http://www.creativemixer.co" title="Link to Creative Mixer">Creative Mixer</a></li>\n\t\t\t\t\t<li><a href="http://www.ixdsessions.com" title="Link to IXD Sessions">IXD Sessions</a></li>\n\t\t\t\t\t<li><a href="http://experienceunion.wordpress.com/category/kennel-nights" title="Link to Kennel Nights">Kennel Nights</a></li>\n\t\t\t\t\t<li><a href="http://www.farm.sg/rojak" title="Link to ROJAK">ROJAK</a></li>\n\t\t\t\t\t<li><a href="http://www.pecha-kucha.org" name="Link to Pecha Kucha">Pecha Kucha</a></li>\n\t\t\t\t</ul>\n\n\t\t\t\t<p class="separator">&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;</p>\n\t\t\t\t\n\t\t\t\t<h4>Supporters</h4>\n\t\t\t\t<ul>\n\t\t\t\t\t<li><a href="http://thepigeonhole.com.sg" name="supporter The Pigeonhole">The Pigeonhole</a></li>\n\t\t\t\t\t<li><a href="https://www.flickevents.com" name="supporter FlickEvents">FlickEvents</a></li>\n\t\t\t\t</ul>\n\t\t\t\t\n\t\t\t</div>\n\t\t\t<div class="contents" id="faq">\n\t\t\t\t<h3>F.A.Q.</h3>\n\t\t\t\t<p id="show_faq"><a href="javascript:showFAQ();">read faq</a></p>\n\t\t\t\t<dl id="faq_text">\n\t\t\t\t\t<dt>Can I come up with my own challenge?</dt>\n\t\t\t\t\t<dd>We are open to any kind of interesting topic so yes, please share your challenges. We do moderate topics to avoid inappropriate ones, but at the same time we want variety. So please share your challenges beforehand via mail or twitter or bring them with you to DestrActions. At the end it will be the people present choosing what challenge they pick.</dd>\n\t\t\t\t\t<dt>Who owns the designs made?</dt>\n\t\t\t\t\t<dd>Creativity is all about sharing but the creators shall be acclaimed. So it\u2019s only fair to make the results available as Creative Commons Attribution. What happens afterwards is up to people but we recommend that if you want to take things further you talk to the guys that were in your team. DestrActions is only a facilitator and shall not own any of the contents created.</dd>\n\t\t\t\t\t<dt>Can I work further on the things made at DestrActions?</dt>\n\t\t\t\t\t<dd>Yes, we hope you do find useful nuggets. If you find things useful, please give back to the community.</dd>\n\t\t\t\t\t<dt>Can I have people work on my commercial project?</dt>\n\t\t\t\t\t<dd>You can, if people are willing to choose your challenge. This might be a good way to find new talent for your team or bump you product further. No matter why you would want that, we recommend you to at least buy those guys a drink, it\u2019s only fair. ;)</dd>\n\t\t\t\t\t<dt>Can I have people work on my confidential project?</dt>\n\t\t\t\t\t<dd>As said before, the results of the session will be shared as Creative Commons Attribution, no two ways about it. This is about openness. But if your project has a part that presents an interesting challenge and that\u2019s not crucially confidential, why not crowd-source it?</dd>\n\t\t\t\t\t<dt>Why do you do this?</dt>\n\t\t\t\t\t<dd>We want to mingle and work other creative heads, it\u2019s liberating. We want to stimulate the design scene to share and cross trenches. We believe in openness and that inspiration often comes from fields outside your expertise. And who doesn\u2019t enjoy a nice challenge that distracts from dull routine?</dd>\n\t\t\t\t\t<dt>How about the money?</dt>\n\t\t\t\t\t<dd>This is or volunteer effort and we plan to not make any money or charge anything. However, as we don\u2019t know where this is headed, this is where we stand ideologically:<br />People who give shall receive, people who receive shall give; a community that shares fairly benefits everybody. Meaning, participation shall always be free besides that we encourage you to consume something at the venue. Submitting challenges shall be free unless you have a clear commercial intent with the challenge. Donations and/or free food and drinks are always welcome but shall not be the incentive.</dd>\n\t\t\t\t\t<dt>Can I use DestrActions to meet people and eventually hire them?</dt>\n\t\t\t\t\t<dd>Yes, use the sessions to get to know people and network. Give and take. :)</dd>\n\t\t\t\t\t<dt>Any more questions?</dt>\n\t\t\t\t\t<dd>Get in touch via <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter">Twitter</a> or <a href="mailto:info@dactions.org" name="e-mail to DActions">email</a>.</dd>\n\t\t\t\t</dl>\n\t\t\t</div>\n\t\t</div>\n\t</div>\n')
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


