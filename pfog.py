import numpy as np

class Grammar:
    def __init__(
                self,
                axiom,
                terminals,
                nonterminals,
                productions,
                ):
        self.axiom = axiom
        self.terminals = terminals
        self.nonterminals = nonterminals
        self.productions = productions

    def generate(self, n_steps=10):
        sentence = list(self.axiom)
        for _ in range(n_steps):
            replace_idx = [ idx for idx, c in enumerate(sentence) if c not in self.terminals ]
            if replace_idx:
                replace_idx = np.random.choice(replace_idx)
                replace_word = sentence[replace_idx]
                sentence[replace_idx] = np.random.choice(self.productions[replace_word])
                sentence = list("".join(sentence))
            else:
                break
        return sentence

g = Grammar(
        axiom="S",
        terminals=["a", "b", "c"],
        nonterminals=["A","B","C"],
        productions={
                "S": ["A", "B", "C"],
                "A": ["a", "AB", "BA", "AC", "CA"],
                "B": ["b", "BA", "AB", "BC", "CB"],
                "C": ["c", "CA", "AC", "CB", "CB"],
            }
        )

g.generate()
