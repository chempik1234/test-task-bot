from .publish import router as publish_router
from .login import router as login_router
from .menu import router as menu_router

routers_list = [login_router, menu_router, publish_router]
