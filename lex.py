import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str

def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """
    grammar = {
        "LPAR": r"\(",
        "NUMBER": r"[-+]?[0-9]*\.?[0-9]+",
        "RPAR": r"\)",
        "COMMENT": r"[;][^\n]*",
        "CHAR": r"[#][\\]([A-Za-z]+|[\d]|[^\s0-9A-Za-z])",
        "STRING": r"('[^\n'\\]*(?:\\.[^\n'\\]*)*'|\"[^\n\"\\]*(?:\\.[^\n\"\\]*)*\")",
        "BOOL": r"([#][t]|[#][f])",
        "QUOTE": r"\'",
        "NAME": r"([-+]|[.]{3}|[A-Za-z|*\/<=>!?:$%_&~^][\w|+-.*\/<=>!?:$%_&~^]*)"
    }
    
    groups = (f"(?P<{k}>{v})" for k, v in grammar.items())
    regex = re.compile('|'.join(groups))
    for m in regex.finditer(code):
        if(m.lastgroup != "COMMENT"):
            yield Token(m.lastgroup, m.group(0))  

    
    return [Token('INVALIDA', 'valor inválido')]