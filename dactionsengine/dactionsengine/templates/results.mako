<%inherit file="/base.mako" />

<%def name="head_tags()">
  <!-- add some head tags here -->
</%def>

	<div class="contents_wrapper">
		<div class="contents" id="challenge">
			<h1>Challenges</h1>
			% for challenge in c.result.challenges:
			    <h3>${challenge["type"]} #${challenge["id"]}</h3><p>${challenge["challenge"]}</p>
			% endfor

			<p class="note">
				Tuesday, ${c.result.date} at 19:00 at ${c.result.location["venue"]}, ${c.result.location["address"]}, ${c.result.location["city"]}, ${c.result.location["country"]}.

				% if len(c.result.pictures) > 0:
				    Pictures are
				    % for pics in c.result.pictures:
				        <a href="${pics}" title="Pictures from ${c.result.date}">here</a>
				    % endfor
				    .
				% endif

			</p>
		</div>
	</div>

    % for team in c.result.teams:
        <div class="team">
            <div class="contents_wrapper">
                <div class="contents">
                    <h2>Team ${team["id"]}</h2>
                    <h3>Members</h3>
                    <p>
                        <%
                         m = []
                         for member in team["members"]:
                             m.append(member.name)
                        %>
                        ${u" × ".join(m)}
                    </p>
                    <h3>Challenge</h3>
                    <p>
                        ${challenge["type"]} #${challenge["id"]}
                    </p>
                </div>
            </div>
        </div>
        <div class="contents_wrapper">
            <div id="contents_box">
                <div class="contents">
                    % for i in range(int(team["pages"])):
                        <img class="result" src="/${c.result.path}${team["id"]}${i+1}.png" alt="Solution Team A" />
                    % endfor
                </div>
            </div>
        </div>
    % endfor