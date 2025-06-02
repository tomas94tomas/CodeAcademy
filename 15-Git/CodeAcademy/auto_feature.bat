@echo off
set /p feature_name="Enter the feature name: "

echo Creating new branch: feature/%feature_name%
git checkout -b feature/%feature_name%

echo Pushing to origin...
git push -u origin feature/%feature_name%

echo Done!
pause