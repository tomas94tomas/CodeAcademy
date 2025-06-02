@echo off
setlocal enabledelayedexpansion

REM --- Check if inside a Git repo ---
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ❌ You are not inside a Git repository!
    pause
    exit /b
)

REM --- Detect remote name ---
set remote_name=

for /f "delims=" %%r in ('git remote') do (
    set remote_name=%%r
    goto :got_remote
)

:got_remote
if "%remote_name%"=="" (
    echo ❌ No Git remote found!
    pause
    exit /b
)

REM --- Ask for commit message ---
set /p commit_msg="Enter commit message: "

REM --- Checkout main branch ---
echo 🔁 Switching to main...
git checkout main

REM --- Stage everything ---
echo 📦 Staging all changes...
git add .

REM --- Commit ---
echo 📝 Committing...
git commit -m "%commit_msg%"

REM --- Push to detected remote ---
echo 🚀 Pushing to %remote_name%/main...
git push %remote_name% main

echo ✅ Done! Changes pushed to %remote_name%/main
pause