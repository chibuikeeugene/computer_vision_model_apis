import typing as t
from pydantic import BaseModel


class PredictionResult(BaseModel):
    readable_prediction: list[str]
    version: t.Any

    