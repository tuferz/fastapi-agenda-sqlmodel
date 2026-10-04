# src/routers/views.py
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from src.database import get_session
from src.models.agenda import Contacto

templates = Jinja2Templates(directory="src/templates")

router = APIRouter(prefix="/views", tags=["Vistas Web (Jinja2)"])

@router.get("/agenda")
def render_agenda_view(request: Request, session: Session = Depends(get_session)):
    contactos = session.exec(select(Contacto)).all()
    return templates.TemplateResponse(
        request=request,
        name="agenda.html",
        context={"contactos": contactos}
    )

@router.post("/agenda/nuevo")
def crear_contacto_desde_vista(
    nombre: str = Form(...),
    telefono: str = Form(...),
    mail: str = Form(...),
    session: Session = Depends(get_session)
):
    nuevo = Contacto(nombre=nombre, telefono=telefono, mail=mail)
    session.add(nuevo)
    session.commit()
    return RedirectResponse(url="/views/agenda", status_code=303)
