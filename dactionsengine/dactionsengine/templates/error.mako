<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

<%def name="title()">Server Error ${c.code}</%def>
<%def name="heading()"><h1>Error ${c.code}</h1></%def>

<p>${c.message}</p>



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
				<h1>${c.error}</h1>
				<h6>We cannot find what you are looking for. Sorry :(</h6>
			
				<h3>Next Event</h3>
				<p>
					Tuesday, March 20 at 19:00 (7pm)<br/>
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
