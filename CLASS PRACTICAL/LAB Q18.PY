import re
def tokenize(s): return re.findall(r"->|[A-Za-z_]\w*|[()&|~,.]", s)
class Parser:
    def __init__(self, s): self.t, self.i = tokenize(s), 0
    def peek(self): return self.t[self.i] if self.i < len(self.t) else None
    def eat(self, x=None):
        tok = self.peek()
        if tok is None: raise SyntaxError("unexpected end of input")
        if x and tok != x: raise SyntaxError(f"expected {x!r}, got {tok!r}")
        self.i += 1; return tok
    def formula(self):
        left = self.disj()
        if self.peek() == "->": self.eat(); return ("->", left, self.formula())
        return left
    def disj(self):
        left = self.conj()
        while self.peek() == "|": self.eat(); left = ("|", left, self.conj())
        return left
    def conj(self):
        left = self.unary()
        while self.peek() == "&": self.eat(); left = ("&", left, self.unary())
        return left
    def unary(self):
        tok = self.peek()
        if tok == "~": self.eat(); return ("~", self.unary())
        if tok in ("forall", "exists"):
            self.eat(); var = self.eat(); return (tok, var, self.unary())
        if tok == "(":
            self.eat(); f = self.formula(); self.eat(")"); return f
        name = self.eat()
        if self.peek() == "(":
            self.eat("("); args = [self.eat()]
            while self.peek() == ",": self.eat(","); args.append(self.eat())
            self.eat(")"); return (name, args)
        return name
for f in ["forall x (Student(x) -> Likes(x, Math))", "exists y (Dog(y) & ~Barks(y))",
          "Loves(John, Mary) | Hates(John, Mary)", "Likes(x,"]:
    try: print(f, "\n  ->", Parser(f).formula())
    except SyntaxError as e: print(f, "\n  -> Syntax error:", e)
