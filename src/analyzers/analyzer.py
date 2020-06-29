from pprint import pprint

from syntax_formatters.sample_data import one_x_bet, parimatch
from scrapers.one_x_bet_scraper import OneXBetScraper
from scrapers.parimatch_scraper import ParimatchScraper
from registry import registry


class Analyzer:
    """
    Class for collecting betting info and analyzing it
    """
    _SCRAPERS = [ParimatchScraper(), OneXBetScraper()]

    def __init__(self, sport_type):
        """
        Scrape betting info on a given sport type and store it in a dict

        :param sport_type: sport type name e.g. 'csgo', 'dota 2'
        :type sport_type: str
        """
        # self.bets_list = []
        # for scraper, formatter in registry.items():
        #     bets = scraper.get_bets(sport_type)
        #     formatter.apply_unified_syntax_formatting(bets)
        #     self.bets_list.append(bets)
        self.bets_list = [one_x_bet.bets, parimatch.bets]

        self.all_bets = self.get_all_bets()

    def get_all_bets(self):
        """
        Initializes all_bets dict, with info from all known scrapers
        all_bets[match_title][bet_title] = {odds: bookmaker}
        """
        all_bets = {}
        for bets in self.bets_list:
            for match_title in bets.keys():
                all_bets.setdefault(match_title, {})
                for bet_title, odds in bets[match_title].items():
                    all_bets[match_title].setdefault(bet_title, {}).update(odds)

        return all_bets
