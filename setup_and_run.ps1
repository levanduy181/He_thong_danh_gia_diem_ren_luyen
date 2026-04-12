$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

function Test-Command {
    param([string]$Name)
    return $null -ne (Get-Command $Name -ErrorAction SilentlyContinue)
}

function Try-CreateVenv {
    param(
        [string]$Command,
        [string[]]$Arguments
    )

    if (-not (Test-Command $Command)) {
        return $false
    }

    if (Test-Path ".venv") {
        Remove-Item ".venv" -Recurse -Force
    }

    $nativePrefExists = $null -ne (Get-Variable PSNativeCommandUseErrorActionPreference -ErrorAction SilentlyContinue)
    if ($nativePrefExists) {
        $previousNativePref = $PSNativeCommandUseErrorActionPreference
        $script:PSNativeCommandUseErrorActionPreference = $false
    }

    try {
        & $Command @Arguments *> $null
        if ($LASTEXITCODE -ne 0) {
            return $false
        }
    } catch {
        return $false
    } finally {
        if ($nativePrefExists) {
            $script:PSNativeCommandUseErrorActionPreference = $previousNativePref
        }
    }

    return Test-Path ".venv\Scripts\python.exe"
}

function New-Venv {
    if (Test-Path ".venv\Scripts\python.exe") {
        return
    }

    if (Try-CreateVenv "py" @("-3.13", "-m", "venv", ".venv")) {
        return
    }

    if (Try-CreateVenv "py" @("-3.12", "-m", "venv", ".venv")) {
        return
    }

    if (Try-CreateVenv "py" @("-3", "-m", "venv", ".venv")) {
        return
    }

    if (Try-CreateVenv "python" @("-m", "venv", ".venv")) {
        return
    }

    throw "Khong tao duoc .venv. Hay cai Python 3.12 hoac 3.13, mo terminal moi, roi chay lai."
}

function Ensure-Npm {
    if (Test-Command "npm") {
        return
    }

    $nodejsDir = "C:\Program Files\nodejs"
    if (Test-Path $nodejsDir) {
        $env:PATH = "$nodejsDir;$env:PATH"
    }

    if (-not (Test-Command "npm")) {
        throw "Khong tim thay npm. Hay cai Node.js LTS truoc."
    }
}

function Compile-ReflexApp {
    param([string]$PythonExe)

    @'
from reflex.utils.prerequisites import get_compiled_app
get_compiled_app(check_if_schema_up_to_date=False, dry_run=False, use_rich=False)
'@ | & $PythonExe -
}

function Ensure-Tslib {
    $webDir = Join-Path $projectRoot ".web"
    $packageJson = Join-Path $webDir "package.json"
    $tslibDir = Join-Path $webDir "node_modules\tslib"

    if (-not (Test-Path $packageJson)) {
        return
    }

    if (Test-Path $tslibDir) {
        return
    }

    Push-Location $webDir
    try {
        & npm install tslib --no-save --legacy-peer-deps
    } finally {
        Pop-Location
    }
}

New-Venv
$pythonExe = Join-Path $projectRoot ".venv\Scripts\python.exe"

Ensure-Npm

& $pythonExe -m pip install --upgrade pip
& $pythonExe -m pip install -r requirements.txt

if (-not (Test-Path "data")) {
    New-Item -ItemType Directory -Path "data" | Out-Null
}

$env:REFLEX_USE_NPM = "1"
$env:REFLEX_HOT_RELOAD_EXCLUDE_PATHS = "data"

Compile-ReflexApp -PythonExe $pythonExe
Ensure-Tslib

& $pythonExe main.py
