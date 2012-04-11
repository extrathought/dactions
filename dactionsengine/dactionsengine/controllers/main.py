import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import datetime
import calendar
import os
from xml.parsers.expat import ExpatError

from dactionsengine.model.results import Results
from dactionsengine.lib.base import BaseController, render

log = logging.getLogger(__name__)

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
        path="./dactionsengine/public/results"
        dirList=os.listdir(path)
        results = []
        for name in dirList:
            result = dict(path=path + "/" + name + "/sg/singapore/")
            result['name'] = datetime.datetime(int(name[:4]), int(name[5:]), 1).strftime("%b '%y")
            results.append(result)
        results.reverse()
        return results

    def _parse_results(self):
        """ parse the results.xml files and create a list of results objects """
        path="./dactionsengine/public/results"
        directoryListing=os.listdir(path)
        results = []
        for eventDate in directoryListing:
            try:
                results.append(Results(path+"/"+eventDate+"/sg/singapore/results.xml"))
            except Exception as e:
                raise Exception(e, eventDate)
        return results

    def index(self):
        c.next_date = self._calculate_next_date()
        c.results = self._list_results()
        c.test = self._parse_results()
        return render('/index.mako', )
