import os

class Config:
    # Tenta ler do ambiente, se não achar, avisa com um erro claro
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    
    @classmethod
    def validate(cls):
        if not cls.GOOGLE_API_KEY:
            raise EnvironmentError("A variável GOOGLE_API_KEY não foi encontrada!")
