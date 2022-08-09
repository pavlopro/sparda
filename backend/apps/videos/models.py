from core.models import BaseModel
from django.db import models

class Video(BaseModel):
    url = models.URLField(max_length=512)
    title = models.CharField(max_length=256, default="No title")

    def __str__(self) -> str:
        return self.title
