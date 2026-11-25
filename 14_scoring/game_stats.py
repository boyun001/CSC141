from pathlib import Path


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.high_score_path = Path(__file__).parent / 'high_score.txt'
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self._load_high_score()

    def _load_high_score(self):
        """Read the saved high score, or return 0 if there isn't one."""
        try:
            return int(self.high_score_path.read_text())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        """Write the high score to a file."""
        self.high_score_path.write_text(str(self.high_score))

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        