from pydantic import BaseModel, EmailStr

class PessoaBase(BaseModel):
    cpf: str
    nome: str
    email: EmailStr
    telefone: str

class PessoaCreate(PessoaBase):
    senha: str

class PessoaUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    telefone: str | None = None
    senha: str | None = None

class PessoaResponse(PessoaBase):
    class Config:
        from_attributes = True 