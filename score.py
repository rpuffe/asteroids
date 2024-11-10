class Score():
    def __init__(self):
        self.score = 0
        self.nuke_spawn_score = 0
        self.nuke_level = 0

    def scoreadd(self, points, from_nuke):
        self.score += points
        if not from_nuke:
            self.nuke_spawn_score += points
    
    def nuke_spawn(self):
        self.nuke_spawn_score = 0
        self.nuke_level += 1
        
