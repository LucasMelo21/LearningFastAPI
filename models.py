from typing import  Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id : Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.lower().split(' ')
        if len(palavras) < 2:
            raise ValueError('O título deve ter ao menos 2 palavras')
        return value

    @validator('aulas')
    def validar_aulas(cls, value):
        if value <= 1:
            raise ValueError('Deve haver ao menos duas aulas no curso')
        return value


cursos = [
    Curso(
        id=1,
        titulo='Programação para Leigos',
        aulas=42,
        horas=56,
    ),
    Curso(
        id=2,
        titulo='Algoritmos e Lógica de Programação',
        aulas=52,
        horas=66
    )
]