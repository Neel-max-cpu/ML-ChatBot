from starlette.middleware.cors import CORSMiddleware


def allow_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",  # Next.js
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )