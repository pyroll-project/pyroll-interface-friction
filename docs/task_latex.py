import pytask
from pytask_latex import compilation_steps
from docs.config import BUILD_DIR


@pytask.mark.latex(
    script="docs.tex",
    document="docs.pdf",
    compilation_steps=[
        compilation_steps.latexmk(["--shell-escape", "--cd", "--halt-on-error"])
    ]
)
@pytask.mark.depends_on(BUILD_DIR.rglob("*"))
def task_latex():
    pass
