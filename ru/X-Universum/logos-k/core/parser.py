class Parser:
    """Строит AST из токенов."""
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
    
    def parse(self):
        """Парсит программу как последовательность связей."""
        program = []
        while not self._is_at_end():
            program.append(self._parse_relation())
        return program
    
    def _parse_relation(self):
        """Парсит одну связь (relation)."""
        if not self._match('LPAREN'):
            raise SyntaxError("Ожидается '(' в начале связи")
        
        operator = self._consume('SYMBOL', "Ожидается оператор")
        operands = []
        
        while not self._match('RPAREN'):
            if self._peek()[0] == 'LPAREN':
                operands.append(self._parse_relation())
            else:
                operands.append(self._parse_atom())
        
        return {'operator': operator[1], 'operands': operands}
    
    def _parse_atom(self):
        """Парсит атомарное значение."""
        for token_type in ('STRING', 'NUMBER', 'SYMBOL'):
            if self._match(token_type):
                return self.tokens[self.current - 1][1]
        raise SyntaxError(f"Неожиданный токен: {self._peek()}")
    
    # Вспомогательные методы _match, _consume, _peek, _is_at_end и т.д.
    