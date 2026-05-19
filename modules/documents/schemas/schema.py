from pydantic import BaseModel

class DocumentIngestRequest(BaseModel):
    title: str
    content: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    status: str

    model_config = {
        "from_attributes": True
    }