# Setup Instructions

## For Users

1. Follow the virtual environment setup instructions in [docs/venv.md](venv.md)
2. Configure environment variables as described in [docs/env.md](env.md)
3. Run the application:
   ```bash
   uvicorn main:app
   ```

The API will be available at http://localhost:8000

## For Developers

In addition to the user setup steps above:

1. Set up pre-commit hooks following [docs/pre-commit.md](pre-commit.md)
2. Configure package management using [docs/pigar.md](pigar.md)
