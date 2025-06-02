@echo off
set /p commit_msg="Enter commit message: "

echo.
echo 📦 Adding all changes...
git add .

echo 📝 Committing with message: "%commit_msg%"
git commit -m "%commit_msg%"

echo 🔁 Switching to main branch...
git checkout main

echo 🚀 Pushing to origin/main...
git push origin main

echo ✅ Changes committed and pushed to main!
pause