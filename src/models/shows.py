from datetime import datetime
class Show:
    def __init__(self, show_id: int, date: datetime, name: str):
        #Validadores para a ID, nome e data do evento
        if not isinstance(show_id, int):
            raise ValueError('Show_id must be a positive integer.')
        if not isinstance(date, datetime):
            raise ValueError('Date must be a datetime object.')
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Name must be a non-empty string.')


        self.__show_id = show_id
        self.__date = date
        self.__name = name

    def to_dict(self):
        return {
            'show_id': self.__show_id,
            'date': self.__date.strftime('%Y-%m-%d'), #pega o objeto datetime e converte para string para assim armazenar melhor no json
            'name': self.__name
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Show':
        data_obj = datetime.strptime(data['date'], '%Y-%m-%d') #aqui faz o contrário do strftime, retorna a data em srt para o seu formato datetime
        return cls(data['show_id'], data_obj, data['name'])

    @property
    def date(self) -> datetime:
        return self.__date
    @property
    def name(self) -> str:
        return self.__name
    @property
    def show_id(self) -> int:
        return self.__show_id
    
    # Útil para a visualização do usuario no print(objeto). Mais legível
    def __str__(self):
        return f'{self.name} ID: {self.show_id} - {self.date.strftime('%d/%m/%Y')}'

    # Útil para dev em debug. Mais preciso
    def __repr__(self):
        return f'Show(id={self.show_id}, name={self.name}, date={self.date.strftime('%d/%m/%Y')})'