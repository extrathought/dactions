<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<ul>
% for result in c.test:
<li>
    ${result.date}: ${result.teams} winner: ${result.winners}, pictures: ${result.pictures}
</li>
% endfor
</ul>

	<div class="contents_wrapper">
		<div class="contents">
			<h3>Manifesto</h3>
			<p>
				We &hearts; design meet-ups to mingle and network, to inspire and being inspired. But we miss variety
				in topics and activities. In our daily project routines we dread for creative interruptions and small challenges
				to keep our minds nimble. Therefore working an evening on out-of-context challenge with new faces is sheer bliss.
			</p>
		</div>
	</div>
	
	<div id="banner">
		<div class="contents_wrapper">
			<div class="contents">
				<h1>DestrActions</h1>
				<h6>Design&nbsp;&nbsp;&times;&nbsp;&nbsp;Distraction&nbsp;&nbsp;&times;&nbsp;&nbsp;Interaction</h6>
			
				<h3>Details</h3>
				<p>
					Tuesday, ${c.next_date} at 19:00 (7pm)<br/>
					At <a href="http://thepigeonhole.com.sg/" name="link to location">The Pigeonhole</a>, 52/53 Duxton Road. <a href="http://maps.google.com.sg/maps?q=The+Pidgeonhole,+52%2F53+Duxton+Road,+Singapore&hl=en&ll=1.279286,103.843267&spn=0.011563,0.015385&sll=1.278179,103.843328&sspn=0.011563,0.015385&vpsrc=0&hq=The+Pidgeonhole,&hnear=53+Duxton+Rd,+Singapore+089517&t=m&cid=8372603932834912927&z=16&iwloc=A" name="link to location map">(map)</a>
				</p>

				<h3>Signup</h3>
				<p><a href="https://www.flickevents.com/destractions-sg-march-2012">Signup via FlickEvents</a></p>
			
				<h3>Contact</h3>
				<p>
					Twitter: <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter"> @DActions</a>
					&nbsp;&nbsp;&times;&nbsp;&nbsp;Facebook: <a href="http://www.facebook.com/groups/DActions.SG" name="Link to DActions on Facebook"> DActions.SG</a>
					&nbsp;&nbsp;&times;&nbsp;&nbsp;e-Mail:
					<a href="mailto:info@dactions.org" name="e-mail to DActions"> info@dactions.org</a>
				</p>
				<h3>Cost</h3>
				<p>free but we encourage you to get a drink or two</p>
			</div>
		</div>
	</div>

	<div class="contents_wrapper">
		<div id="contents_box">
			<div class="contents">

				<h3>What</h3>
				<p>We meet on the <em>3rd&nbsp;Tuesday every month</em> with fellow designers to <em>collaborate</em> a few hours on <em>small design challenges</em> across the disciplines. We conclude the session with a brief presentation and discussion of the designs before making them available online.</p>
				<h3>Who</h3>
				<p>
					The sessions are <em>open for everybody</em> with interest in designing stuff. You don't need to be an architect,
					industrial/graphic/fashion/etc. designer, ergonomist or artist to join. The engineer, business girl, accounting guy,
					kindergarden teacher or hobby inventor is as welcome to join and get their creative juices flow. The goal is to open up to other
					design ideas, get out of the comfort zone and be inspired.<br/><br />
					Who we don’t want are elitists, design divas and rockstars that can’t collaborate. <em>Keep it simple and down to
					earth, creative and sharing.</em> It’s to tickle your brain out of the routine.
				</p>
				<h3>Format</h3>
				<table>
					<tr><th>Challenge</th><td>Pitch and explanation of the different challenges to choose from. If you have proposals please <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter">tweet</a> or <a href="mailto:info@dactions.org" name="e-mail to DActions">e-mail</a> them.</td></tr>
					<tr><th>Team Lottery</th><td>A simple hat-lottery system to draft the groups to make sure you don't always work with your buddies.</td></tr>
					<tr><th>Team Work</th><td>Group work for 90 minutes to design the proposals (i.e. brainstorming, discussion, sketching, etc.).</td></tr>
					<tr><th>Presentation</th><td>Each group briefly presents their designs with a short discussion and feedback session.</td></tr>
				</table>
	
				<h3>Supplies</h3>
				<p>
					Bring you jolly self, your <em>charm, sharp mind and keen eye</em>, your design instinct and anything else
					that has been dulled down. Bringing your <em>favourite designing pen and paper</em> will help to come up with results.
				</p>
	
				<h3>Results</h3>
				<p>
					In the end the <em>results will be published online as Creative Commons Attribution</em> so you can share and refer to them. The place for this
					has not yet been decided.
				</p>
					
			</div>
			<div class="right">
				<h4>Session Results</h4>

                <ul>
                    % for result in c.results:
                    <li>
                        ${result['name']}:
                        <a href="${result['path']}results.html" title="Results from ${result['name']}">Results</a>
                    </li>
                    % endfor
                </ul>

				<p class="separator">&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;</p>
				
				<h4>Related Events</h4>
				<ul>
					<li><a href="http://www.creativemixer.co" title="Link to Creative Mixer">Creative Mixer</a></li>
					<li><a href="http://www.ixdsessions.com" title="Link to IXD Sessions">IXD Sessions</a></li>
					<li><a href="http://experienceunion.wordpress.com/category/kennel-nights" title="Link to Kennel Nights">Kennel Nights</a></li>
					<li><a href="http://www.farm.sg/rojak" title="Link to ROJAK">ROJAK</a></li>
					<li><a href="http://www.pecha-kucha.org" name="Link to Pecha Kucha">Pecha Kucha</a></li>
				</ul>

				<p class="separator">&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;&times;&nbsp;&nbsp;</p>
				
				<h4>Supporters</h4>
				<ul>
					<li><a href="http://thepigeonhole.com.sg" name="supporter The Pigeonhole">The Pigeonhole</a></li>
					<li><a href="https://www.flickevents.com" name="supporter FlickEvents">FlickEvents</a></li>
				</ul>
				
			</div>
			<div class="contents" id="faq">
				<h3>F.A.Q.</h3>
				<p id="show_faq"><a href="javascript:showFAQ();">read faq</a></p>
				<dl id="faq_text">
					<dt>Can I come up with my own challenge?</dt>
					<dd>We are open to any kind of interesting topic so yes, please share your challenges. We do moderate topics to avoid inappropriate ones, but at the same time we want variety. So please share your challenges beforehand via mail or twitter or bring them with you to DestrActions. At the end it will be the people present choosing what challenge they pick.</dd>
					<dt>Who owns the designs made?</dt>
					<dd>Creativity is all about sharing but the creators shall be acclaimed. So it’s only fair to make the results available as Creative Commons Attribution. What happens afterwards is up to people but we recommend that if you want to take things further you talk to the guys that were in your team. DestrActions is only a facilitator and shall not own any of the contents created.</dd>
					<dt>Can I work further on the things made at DestrActions?</dt>
					<dd>Yes, we hope you do find useful nuggets. If you find things useful, please give back to the community.</dd>
					<dt>Can I have people work on my commercial project?</dt>
					<dd>You can, if people are willing to choose your challenge. This might be a good way to find new talent for your team or bump you product further. No matter why you would want that, we recommend you to at least buy those guys a drink, it’s only fair. ;)</dd>
					<dt>Can I have people work on my confidential project?</dt>
					<dd>As said before, the results of the session will be shared as Creative Commons Attribution, no two ways about it. This is about openness. But if your project has a part that presents an interesting challenge and that’s not crucially confidential, why not crowd-source it?</dd>
					<dt>Why do you do this?</dt>
					<dd>We want to mingle and work other creative heads, it’s liberating. We want to stimulate the design scene to share and cross trenches. We believe in openness and that inspiration often comes from fields outside your expertise. And who doesn’t enjoy a nice challenge that distracts from dull routine?</dd>
					<dt>How about the money?</dt>
					<dd>This is or volunteer effort and we plan to not make any money or charge anything. However, as we don’t know where this is headed, this is where we stand ideologically:<br />People who give shall receive, people who receive shall give; a community that shares fairly benefits everybody. Meaning, participation shall always be free besides that we encourage you to consume something at the venue. Submitting challenges shall be free unless you have a clear commercial intent with the challenge. Donations and/or free food and drinks are always welcome but shall not be the incentive.</dd>
					<dt>Can I use DestrActions to meet people and eventually hire them?</dt>
					<dd>Yes, use the sessions to get to know people and network. Give and take. :)</dd>
					<dt>Any more questions?</dt>
					<dd>Get in touch via <a href="http://twitter.com/#!/DActions" name="Link to DActions on Twitter">Twitter</a> or <a href="mailto:info@dactions.org" name="e-mail to DActions">email</a>.</dd>
				</dl>
			</div>
		</div>
	</div>
