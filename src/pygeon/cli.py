from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(
    name="pygeon",
    help="Generate PDF business letters conforming to DIN 5008",
    no_args_is_help=True,
)


@app.command()
def generate(
    source: Annotated[Path, typer.Argument(help="Path to the source file")],
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Output PDF path"),
    ] = None,
) -> None:
    """Generate a PDF business letter."""

    if not source.is_file():
        typer.echo(f"File not found: {source}", err=True)
        raise typer.Exit(code=1)

    target = output or source.with_suffix(".pdf")
    typer.echo(f"Generating {target}")


@app.command()
def validate(
    source: Annotated[Path, typer.Argument(help="Path to the source file")],
) -> None:
    """Validate a letter and its attachments."""

    typer.echo(f"Validating {source}")


if __name__ == "__main__":
    app()
