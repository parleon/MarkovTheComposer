from random import random

class Composer:

    def __init__(self) -> None:

        self.note_dict = {}
        self.chain = {}
        self.cum_chain = {}
        self.generated_patterns = []

    def feed(self, notelist):

        for i in range(len(notelist)-1):
            start = notelist[i]
            end = notelist[i+1]

            if start not in self.note_dict:
                self.note_dict[start] = {'TOTAL':0}

            if end not in self.note_dict[start]:
                self.note_dict[start][end] = 0

            self.note_dict[start][end] += 1
            self.note_dict[start]['TOTAL'] += 1

    def update(self):

        self.note_dict = dict(sorted(self.note_dict.items()))

        for note in self.note_dict:
            self.chain[note] = {}
            self.cum_chain[note] = {}
            cum = 0

            for n in self.note_dict:
                if n in self.note_dict[note]:
                    self.chain[note][n] = self.note_dict[note][n]/self.note_dict[note]['TOTAL']
                    cum += self.chain[note][n]
                    self.cum_chain[note][n] = cum
                else:
                    self.chain[note][n] = 0

    def walk(self, distance):
        length = len(self.chain)
        pattern = []
    
        
        note = list(self.cum_chain.keys())[round(random()*(length-1))]
        pattern.append(note)
        for i in range(distance-1):
            rng = random()
            for n in self.cum_chain[note]:
                if rng < self.cum_chain[note][n]:
                    note = n
                    pattern.append(note)
                    break
        return pattern

    def print_chain(self):
        print(' '*5, end='')
        for i in self.chain:
            print(f'{i:^5}',end='')
        print()
        for n in self.chain:
            print(f'{n:^5}', end = '')
            for nn in self.chain[n]:
                print(f'{round(self.chain[n][nn],2):^5}', end='')
            print()

Carl = Composer()

Carl.feed('D7 Dm7 C D7 Dm7 C G/B Am C Dm G G7 C Em/B Am C Dm G C Em/B Am Em Bb C/G G F G C F G C F G Am D7 F Fm C F C Em/B Am C Dm G G7 C Em/B Am C Dm G C Em/B Am Em Bb C/G G F G C F G C F G Am D7 F Fm C F G C G/B Am Em/G D7 Dm7 G F G C F G C F G Am D7 F Fm C D7 F Fm C'.split(' '))
Carl.update()
Carl.print_chain()
print(Carl.walk(4))