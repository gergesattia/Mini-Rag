from fastapi import APIRouter, File, HTTPException, UploadFile

from src.controllers import DataController


router = APIRouter()


@router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile = File(...)):
    try:
        is_valid = DataController().validate(project_id, file)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {"is_valid": is_valid}
