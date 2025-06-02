@echo off
setlocal

REM Make sure you're inside a Git repo
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ❌ You are not inside a Git repository!
    pause
    exit /b
)

REM Ask for commit message
set /p commit_msg="Enter commit message: "

REM Checkout main (if not already)
echo 🔁 Switching to main branch...
git checkout main

REM Stage all changes
echo 📦 Adding all changes...
git add .

REM Commit with message
echo 📝 Committing with message: "%commit_msg%"
git commit -m "%commit_msg%"

REM Push to origin/main
echo 🚀 Pushing to origin/main...
git push origin main

echo ✅ All changes committed and pushed to main!
pause
