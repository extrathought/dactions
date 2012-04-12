__author__ = 'wolf'

from xml.dom import minidom

class Results:

    """
    teams.team.id
    teams.team.challenge
    teams.team.users
    """
    date = None
    location = None
    challenges = []
    winners = []
    pictures = []
    teams = []

    def __init__(self, filename):
        """do the parsing magic"""
        doc = minidom.parse(filename)
        # set date
        self.date =  self._getText(doc.getElementsByTagName("date"))
        # ste location
        venue = self._getText(doc.getElementsByTagName("venue"))
        address =  self._getText(doc.getElementsByTagName("venue"))
        city = self._getText(doc.getElementsByTagName("venue"))
        country = self._getText(doc.getElementsByTagName("venue"))
        self.location = {"venue" : venue, "address" : address, "city" : city, "country" : country}
        # set challenges
        for challenge in doc.getElementsByTagName("venue"):
            id = challenge.getAttribute("id")
            type = challenge.getAttribute("type")
            ch = challenge.data
            self.challenges.append({"id": id, "type": type, "challenge" : ch})
        # set winners
        for win in doc.getElementsByTagName("winner"):
        win[0].getAttribute("team")
        # set pictures

        # set teams

        teams = doc.getElementsByTagName("team")
        for team in teams:
            print team.toxml()

    def _getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.childNodes[0].nodeType == node.TEXT_NODE:
                rc.append(node.childNodes[0].data)
        return ''.join(rc)

"""
<destraction>
<date>2011-12-20</date>
<location>
<venue>The Pigeonhole</venue>
<address>52/53 Duxton Road</address>
<city>Singapore</city>
<country>SG</country>
</location>
<challenges>
<challenge id="1" type="Visualise">The effects of the internet on our daily lives is hard to deny. The extent of the impact, however, may be obscured by the gradual introduction into our lives. Visualise the impact the Internet, especially social media (Facebook, Twitter, YouTube, etc.), has had on your life. Bonus for (valid) qualitative data.</challenge>
<challenge id="2" type="Conceptualise">Christmas is probably the most resource-intensive celebration of modern humanity: gifts, gift-wrappings, Christmas trees, decorations and their electricity use, travelling home to see family, etc. Design a resourceful once-a-year holiday tradition representing the values of love, peace and unity. Bonus for transgressing creed and culture.</challenge>
<challenge id="3" type="Remix">"The straight line leads to the downfall of humanity." - Friedensreich Hundertwasser. Envision non-structural modifications that anybody can make to our public concrete environment to make it more humane, natural and alive. Bonus for implementable and legal modifications.</challenge>
</challenges>
<winner team="E" />
<picture>https://plus.google.com/photos/109626465941792614807/albums/56896029947411572814</pictures>
<teams>
<team id="A">
<challenge id="3" />
<member><name>Sami Kizilbash</name><mail>sami@figr.com</mail></member>
<member><name>Prashant Kumar</name><mail>prashant.kumar@iproperty.com</mail></member>
<member><name>Arief Aziz</name><mail>arief@tedxjkt.org</mail></member>
<member><name>Michael Ong</name><mail>michael.ong@iproperty.com</mail></member>
<member><name>Grace Sai</name><mail>gracesai@gmail.com</mail></member>
<member><name>Zuhairah Ariff</name><mail>zuhairah.a@gmail.com</mail></member>
</team>
<team id="B">
<challenge id="3" />
<member><name>Raven Chai</name><mail>raven@uxconsulting.com.sg</mail></member>
<member><name>Elly Lisa</name><mail>ellylisaconnect@gmail.com</mail></member>
<member><name>Rishab Malik</name><mail>rishab@figr.com</mail></member>
<member><name>Shah Widjaja</name><mail></mail></member>
<member><name>Ling Ling</name><mail>linglingn@yahoo.com</mail></member>
<member><name>John Tan</name><mail>johntan@orita-sinclair.edu.sg</mail></member>
</team>
</team>
</teams>
</destraction>

"""