@echo off
setlocal enabledelayedexpansion

REM Check if inside a Git repo
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ❌ Not inside a Git repository.
    pause
    exit /b
)

REM Switch to main branch
echo 🔁 Switching to main branch...
git checkout main

REM Ask for commit message
set /p commit_msg=Enter commit message: 

REM Stage all changes
echo 📦 Staging all changes...
git add -A

REM Commit
echo 📝 Committing...
git commit -m "%commit_msg%"

REM Get first available remote (avoiding GOTO for PowerShell compatibility)
set remote_name=
for /f %%r in ('git remote') do (
    if not defined remote_name set remote_name=%%r
)

if not defined remote_name (
    echo ❌ No git remote found. Use: git remote add origin <url>
    pause
    exit /b
)

REM Push to remote
echo 🚀 Pushing to !remote_name!/main...
git push !remote_name! main

echo ✅ Done! All changes pushed to !remote_name!/main
pause
