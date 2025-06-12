from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from db import SessionLocal, engine

# Criar todas as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Inicializar o app FastAPI
app = FastAPI(
    title="BioCadastro API",
    description="API para gerenciamento de animais da fazenda experimental",
    version="1.0.0"
)

# Configurar CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency para obter sessão do banco de dados
def get_db():
    """Cria uma sessão de banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ========================================
# ENDPOINTS BÁSICOS
# ========================================

@app.get("/")
def root():
    """Endpoint raiz da API"""
    return {"message": "BioCadastro API funcionando! 🐄"}

@app.post("/animals", response_model=schemas.AnimalResponse)
def create_animal(animal: schemas.AnimalCreate, db: Session = Depends(get_db)):
    """Cria um novo animal"""
    return crud.criar_animal(db=db, animal=animal)

@app.get("/animals", response_model=List[schemas.AnimalResponse])
def get_animals(db: Session = Depends(get_db)):
    """Retorna lista de animais"""
    return crud.obter_todos_animais(db)

@app.get("/animals/{animal_id}", response_model=schemas.AnimalResponse)
def get_animal(animal_id: int, db: Session = Depends(get_db)):
    """Retorna um animal específico pelo ID"""
    return crud.obter_animal_por_id(db, animal_id=animal_id)

@app.put("/animals/{animal_id}", response_model=schemas.AnimalResponse)
def update_animal(animal_id: int, animal_update: schemas.AnimalUpdate, db: Session = Depends(get_db)):
    """Atualiza dados de um animal"""
    return crud.atualizar_animal(db, animal_id=animal_id, animal_update=animal_update)

@app.delete("/animals/{animal_id}")
def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    """Deleta um animal"""
    crud.deletar_animal(db, animal_id=animal_id)
    return {"message": "Animal deletado"}

@app.post("/vaccinations", response_model=schemas.VacinacaoResponse)
def create_vaccination(vaccination: schemas.VacinacaoCreate, db: Session = Depends(get_db)):
    """Registra uma nova vacinação"""
    return crud.criar_vacinacao(db=db, vacinacao=vaccination)

@app.get("/animals/{animal_id}/vaccinations", response_model=List[schemas.VacinacaoResponse])
def get_animal_vaccinations(animal_id: int, db: Session = Depends(get_db)):
    """Retorna histórico de vacinações de um animal"""
    return crud.obter_vacinacoes_por_animal(db, animal_id=animal_id)

@app.delete("/vaccinations/{vaccination_id}")
def delete_vaccination(vaccination_id: int, db: Session = Depends(get_db)):
    """Deleta um registro de vacinação"""
    crud.deletar_vacinacao(db, vacinacao_id=vaccination_id)
    return {"message": "Vacinação deletada"}

@app.post("/weights", response_model=schemas.PesagemResponse)
def create_weight_record(weight: schemas.PesagemCreate, db: Session = Depends(get_db)):
    """Registra uma nova pesagem"""
    return crud.criar_pesagem(db=db, pesagem=weight)

@app.get("/animals/{animal_id}/weights", response_model=List[schemas.PesagemResponse])
def get_animal_weights(animal_id: int, db: Session = Depends(get_db)):
    """Retorna histórico de pesagens de um animal"""
    return crud.obter_pesagens_por_animal(db, animal_id=animal_id)

@app.delete("/weights/{weight_id}")
def delete_weight_record(weight_id: int, db: Session = Depends(get_db)):
    """Deleta um registro de pesagem"""
    crud.deletar_pesagem(db, pesagem_id=weight_id)
    return {"message": "Pesagem deletada"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    





