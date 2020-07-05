from abc import ABC

from esports.abstract_syntax_formatter import AbstractSyntaxFormatter as ASF


class AbstractSyntaxFormatter(ASF, ABC):
    """
    Class that is used for applying unified syntax formatting to all betting
    related information scraped from the websites
    """
    def apply_unified_syntax_formatting(self, bets):
        """
        Apply unified syntax formatting to the given bets dict

        :param bets: bets dictionary to format
        :type bets: dict
        """
        self.bets = bets.copy()

        bets = self._format_before(bets)

        bets = self._update(bets, self._format_total)
        bets = self._update(bets, self._format_maps)
        bets = self._update(bets, self._format_handicap)
        bets = self._update(bets, self._format_win_in_round)
        bets = self._update(bets, self._format_correct_score)
        bets = self._update(bets, self._format_win)
        bets = self._update(bets, self._format_uncommon_chars)
        bets = self._update(bets, self._format_bomb_exploded)
        bets = self._update(bets, self._format_bomb_planted)
        bets = self._update(bets, self._format_overtime)
        bets = self._update(bets, self._format_first_kill)
        bets = self._update(bets, self._format_win_at_least_number_of_maps)
        bets = self._update(bets, self._format_win_number_of_maps)
        bets = self._update(bets, self._format_individual_total_rounds)
        bets = self._update(bets, self._format_first_to_win_number_of_rounds)
        bets = self._update(bets, self._format_total_kills)

        bets = self._format_after(bets)

        bets = self._format_odds(bets)
        bets = self._format_bookmaker_name(bets)
        bets = self._format_titles(bets)

        return bets

    def _format_win_in_round(self):
        return self.bet_title.lower()

    def _format_bomb_exploded(self):
        return self.bet_title.lower()

    def _format_bomb_planted(self):
        return self.bet_title.lower()

    def _format_overtime(self):
        return self.bet_title.lower()

    def _format_individual_total_rounds(self):
        return self.bet_title.lower()

    def _format_first_to_win_number_of_rounds(self):
        return self.bet_title.lower()
