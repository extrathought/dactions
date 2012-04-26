import logging

from pylons import tmpl_context as c
import datetime
import calendar
import os
from pylons.controllers.util import abort

from dactionsengine.model.results import Results
from dactionsengine.lib.base import BaseController, render

log = logging.getLogger(__name__)
BASEPATH = "./dactionsengine/public/results"

class MainController(BaseController):

    def _calculate_next_date(self):
        """ calculate the date of the DestrActions of the current month """
        curYear = datetime.datetime.now().year
        curMonth = datetime.datetime.now().month
        firstDayOfMonth = calendar.weekday(curYear, curMonth, 1)
        firstTueOfMonth = (8 - firstDayOfMonth) % 7 + 15
        newdate = datetime.datetime(curYear, curMonth, firstTueOfMonth)
        return newdate.strftime("%B %d")

    def _list_results(self):
        """ parse the results folder and create a list of links """
        dirList=os.listdir(BASEPATH)
        results = []
        for name in dirList:
            if os.path.isdir(BASEPATH + "/" + name) and os.path.exists(BASEPATH + "/" + name + "/sg/singapore/results.xml"):
                result = dict(path = BASEPATH + "/" + name + "/sg/singapore/")
                result['name'] = datetime.datetime(int(name[:4]), int(name[5:]), 1).strftime("%b '%y")
                results.append(result)
        results.reverse()
        return results

    def _parse_result(self, eventDate=None, country=None, city=None):
        """ parse one results.xml file and return the results object """
        result = None
        datePath = "/".join([BASEPATH, eventDate])
        resourcePath = "/".join([datePath, country, city])
        if os.path.isdir(datePath) and os.path.exists(resourcePath + "/results.xml"):
            result = Results(resourcePath + "/results.xml")
            result.path = "/".join(["results", eventDate, country, city, ""])
        return result

    def _parse_results(self):
        """ parse the results.xml files and create a list of results objects """
        directoryListing=os.listdir(BASEPATH)
        results = []
        for eventDate in directoryListing:
            result = self._parse_result(eventDate, "sg", "singapore")
            if result is not None:
                results.append(result)
        results.reverse()
        return results

    def index(self):
        c.next_date = self._calculate_next_date()
        c.results = self._parse_results()
        if c.results == None:
            abort(404)
        return render('/index.mako')

    def results(self, url=None):
        info = url.split("/")
        c.result = self._parse_result(info[0], info[1], info[2])
        if c.result == None:
            abort(404)
        return render('/results.mako')
