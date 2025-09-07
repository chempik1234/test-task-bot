import structlog

structlog.configure(
    processors=[
        structlog.processors.dict_tracebacks,
        structlog.processors.JSONRenderer()
    ]
)
