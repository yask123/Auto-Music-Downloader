@echo off
cd %~dp0
rem Script goes to System32 if you start it as admin

echo This will copy Music-Downloader to %UserProfile%\music_downloader and set it in PATH.

goto check_Permissions
sss
:back
mkdir "%UserProfile%\music_downloader"
copy ".\music_downloader.py" "%UserProfile%\music_downloader\music_downloader.py"

rem check if already exists in PATH
echo. ";%PATH%;" | findstr /C:";%UserProfile%\music_downloader;" 1>nul
if errorlevel 1 (
    set svar="%PATH%;%UserProfile%\music_downloader;;"
    goto strlen
    :pathok
    @setx PATH "%PATH%;%UserProfile%\music_downloader" /m
    goto end
    rem needed as if-else logic is lost after goto
) ELSE (
	echo Already exists in PATH
)

:end
set /p tempvar="SUCCESS. Press Enter to continue"
exit /B


rem http://stackoverflow.com/a/11995662/2295672

:check_Permissions
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (
        rem echo Success: Administrative permissions confirmed.
        goto back
    ) else (
        echo Failure: Try running as administrator
    	pause >nul
        exit /B
    )

rem http://stackoverflow.com/a/5841587/2295672

:strlen
    rem setlocal EnableDelayedExpansion for changing var and using it in loop
    setlocal EnableDelayedExpansion
    set "s=!%svar%!#"
    set "len=0"
    for %%P in (4096 2048 1024 512 256 128 64 32 16 8 4 2 1) do (
        if "!s:~%%P,1!" NEQ "" ( 
            set /a "len+=%%P"
            set "s=!s:~%%P!"
        )
    )
    if %len% GEQ 1024 (
        set /p tempvar="PATH is more than 1024 characters. This can't be handled by the script. You will have to add that manually."
        exit /b
    ) else (
        goto pathok
    )
