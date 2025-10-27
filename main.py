from fastapi import FastAPI

from atleta.models import AtletaModel
from categorias.models import CategoriaModel
from centro_treinamento.models import CentroTreinamentoModel
from routers import api_router

app = FastAPI(title="Workoutapi")
app.include_router(api_router)
