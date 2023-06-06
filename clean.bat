@echo off
for /r %%i in (__pycache__) do (
    if exist "%%i" (
        echo Eliminando "%%i"
        rd /s /q "%%i"
    )
)

if exist .cache (
    echo Eliminando .cache
    rd /s /q .cache
)

if exist .mypy_cache (
    echo Eliminando .mypy_cache
    rd /s /q .mypy_cache
)

if exist schema\.mypy_cache (
    echo Eliminando schema\.mypy_cache
    rd /s /q schema\.mypy_cache
)

if exist .coverage (
    echo Eliminando .coverage
    del .coverage
)

if exist *cover (
    echo Eliminando *cover
    del *cover
)

if exist *cover (
    echo Eliminando *cover
    del *cover
    rd /s /q *cover
)