from dactionsengine.model.user import User

__author__ = 'wolf'

from xml.dom import minidom

class Results:

    def __init__(self, filename):

        """do the parsing magic"""

        self.date = None
        self.location = None
        self.challenges = []
        self.winners = []
        self.pictures = []
        self.teams = []

        doc = minidom.parse(filename)
        # set date
        self.date =  self._getText(doc.getElementsByTagName("date"))

        # set location
        venue = self._getText(doc.getElementsByTagName("venue"))
        address =  self._getText(doc.getElementsByTagName("address"))
        city = self._getText(doc.getElementsByTagName("city"))
        country = self._getText(doc.getElementsByTagName("country"))
        self.location = {"venue" : venue, "address" : address, "city" : city, "country" : country}

        # set challenges
        for challenge in doc.getElementsByTagName("challenge"):
            id = challenge.getAttribute("id")
            ch = challenge.firstChild.data
            type = challenge.getAttribute("type")
            self.challenges.append({"id": id, "type": type, "challenge" : ch})

        # set winners
        for win in doc.getElementsByTagName("winner"):
            self.winners.append(win.firstChild.data)

        # set pictures
        for pics in doc.getElementsByTagName("pictures"):
            if pics.hasChildNodes():
                self.pictures.append(pics.firstChild.data)

        # set teams
        for team in doc.getElementsByTagName("team"):
            id = team.getAttribute("id")
            challenge = team.getAttribute("challenge")
            pages = 1
            members = []
            name = mail = twitter = ""
            for child in team.childNodes:
                if child.nodeName == "member":
                    for n in child.childNodes:
                        if n.childNodes == []:
                            continue
                        elif n.nodeName == "name":
                            name = n.firstChild.data
                        elif n.nodeName == "mail":
                            mail = n.firstChild.data
                        elif n.nodeName == "twitter":
                            twitter = n.firstChild.data
                    members.append(User(name, mail, twitter))
                if child.nodeName == "pages":
                    #pages = child.firstChild
                    pages = int(child.firstChild.data)
            self.teams.append({"id" : id, "challenge" : challenge, "members" : members, "pages" : pages})


    def _getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.firstChild.nodeType == node.TEXT_NODE:
                rc.append(node.firstChild.data)
        return ''.join(rc)

"""
<destraction>
	<date>2012-03-20</date>
	<location>
		<venue>The Pigeonhole</venue>
		<address>52/53 Duxton Road</address>
		<city>Singapore</city>
		<country>SG</country>
	</location>
	<challenges>
		<challenge id="1" type="Phantasise">Design changes to our public spaces that allow animals from the zoo to roam our urban habitat freely. Find a way that makes it possible to let wild animals roam our city safely next to humans (e.g. Orchard Road area). Bonus: Any solution that allows us to get into arm's reach of a real lion.</challenge>
		<challenge id="2" type="Conceptualise">Design an elegant piece of men's clothing that allows provides warmth in freezing (AC) temperatures and that does not get in the way with hot and humid weather (i.e. does not have to be carried in one's hand or uses lots of space in a bag). Bonus: Style and functionality.</challenge>
		<challenge id="3" type="Visualise">Design icons that clearly visually represent the concepts of today, yesterday and tomorrow without using any text or letters. Bonus: Icons that work independent of culture.</challenge>
	</challenges>
	<winner>D</winner>
	<pictures>https://www.facebook.com/media/set/?set=oa.376111989088608</pictures>
	<teams>
		<team id="A" challenge="1">
			<member><name>Eva Wan</name><mail>eva.wan@possibleworldwide.com</mail></member>
			<member><name>Jai</name><twitter>@gmail</twitter></member>
			<pages>3</pages>
		</team>
		<team id="B" challenge="1">
			<member><name>Ibrahim Iqbal</name><mail>ibrahim13@gmail.com</mail></member>
			<pages>1</pages>
		</team>
	</teams>
</destraction>
"""