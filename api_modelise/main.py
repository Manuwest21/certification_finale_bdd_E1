from fastapi import FastAPI
from fastapi.routing import APIRouter
from modelisation_vrai import app as modelisation_router
# from securite import router1 as utils_router
from securite_vrai import router1 as utils_router
router = APIRouter()

router.include_router(utils_router)

#alphonse#
app = FastAPI()
app.include_router(router)
app.include_router(modelisation_router)
from fastapi import FastAPI
from fastapi.routing import APIRouter

from securite import router1 as utils_router


router = APIRouter()

# Inclure les routes de sécurité et de modèle
router.include_router(utils_router)
router.include_router(modelisation_router)

app = FastAPI()

app.include_router(router)