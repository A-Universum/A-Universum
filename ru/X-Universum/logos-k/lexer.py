```python
import re

class Lexer:
    """Разбивает исходный код LOGOS-κ на токены."""
    
    TOKEN_SPEC = [
        ('STRING', r'"[^"]*"'),
        ('NUMBER', r'\d+(\.\d+)?'),
        ('SYMBOL', r'[a-zA-Z_][a-zA-Z0-9_-]*'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('WHITESPACE', r'\s+'),
        ('COMMENT', r';[^\n]*'),
    ]
    
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.pos = 0
    
    def tokenize(self):
        """Возвращает список токенов."""
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.TOKEN_SPEC)
        
        for mo in re.finditer(tok_regex, self.source):
            kind = mo.lastgroup
            value = mo.group()
            
            if kind in ('WHITESPACE', 'COMMENT'):
                continue
            elif kind == 'STRING':
                value = value[1:-1]  # Убираем кавычки
            elif kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)
            
            self.tokens.append((kind, value))
        
        return self.tokens
```        