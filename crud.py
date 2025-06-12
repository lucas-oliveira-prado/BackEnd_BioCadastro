from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas

def criar_animal(db: Session, animal: schemas.AnimalCreate) -> models.Animal:
    db_animal = models.Animal(
        nome=animal.nome,
        sexo=animal.sexo,
        raca=animal.raca,
        data_nascimento=animal.data_nascimento,
        status=animal.status
    )
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

def obter_animal_por_id(db: Session, animal_id: int) -> Optional[models.Animal]:
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()

def obter_todos_animais(db: Session, skip: int = 0, limit: int = 100) -> List[models.Animal]:
    return db.query(models.Animal).offset(skip).limit(limit).all()

def atualizar_animal(db: Session, animal_id: int, animal_update: schemas.AnimalUpdate) -> Optional[models.Animal]:
    db_animal = obter_animal_por_id(db, animal_id)
    if not db_animal:
        return None
    
    update_data = animal_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_animal, field, value)
    
    db.commit()
    db.refresh(db_animal)
    return db_animal

def deletar_animal(db: Session, animal_id: int) -> bool:
    # Deletar primeiro todas as pesagens relacionadas
    db.query(models.Pesagem).filter(models.Pesagem.id_animal == animal_id).delete()
    
    # Deletar todas as vacinações relacionadas
    db.query(models.Vacinacao).filter(models.Vacinacao.animal_id == animal_id).delete()
    
    # Agora deletar o animal
    db_animal = obter_animal_por_id(db, animal_id)
    if not db_animal:
        return False
    
    db.delete(db_animal)
    db.commit()
    return True

def criar_vacinacao(db: Session, vacinacao: schemas.VacinacaoCreate) -> models.Vacinacao:
    db_vacinacao = models.Vacinacao(
        animal_id=vacinacao.animal_id,
        nome=vacinacao.nome,
        data=vacinacao.data
    )
    db.add(db_vacinacao)
    db.commit()
    db.refresh(db_vacinacao)
    return db_vacinacao

def obter_vacinacoes_por_animal(db: Session, animal_id: int) -> List[models.Vacinacao]:
    return db.query(models.Vacinacao).filter(models.Vacinacao.animal_id == animal_id).all()

def deletar_vacinacao(db: Session, vacinacao_id: int) -> bool:
    db_vacinacao = db.query(models.Vacinacao).filter(models.Vacinacao.id == vacinacao_id).first()
    if not db_vacinacao:
        return False
    db.delete(db_vacinacao)
    db.commit()
    return True

def criar_pesagem(db: Session, pesagem: schemas.PesagemCreate) -> models.Pesagem:
    db_pesagem = models.Pesagem(
        id_animal=pesagem.id_animal,
        peso=pesagem.peso,
        data=pesagem.data
    )
    db.add(db_pesagem)
    db.commit()
    db.refresh(db_pesagem)
    return db_pesagem

def obter_pesagens_por_animal(db: Session, animal_id: int) -> List[models.Pesagem]:
    return db.query(models.Pesagem).filter(models.Pesagem.id_animal == animal_id).all()

def deletar_pesagem(db: Session, pesagem_id: int) -> bool:
    db_pesagem = db.query(models.Pesagem).filter(models.Pesagem.id == pesagem_id).first()
    if not db_pesagem:
        return False
    db.delete(db_pesagem)
    db.commit()
    return True
