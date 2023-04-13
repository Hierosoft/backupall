
SET LOG=C:\backup.log
SET BC=%BACKUPS%\c
SET BD=%BACKUPS%\d
IF EXIST %LOG% DEL %LOG%

ECHO Backup-all.bat was written by Jake Gustafson 2023-02-06 > %LOG%
ECHO backupall.py was written by Jake Gustafson 2023-04-12 >> %LOG%
ECHO Started %~dp0 >> %LOG%
ECHO %DATE% >> %LOG%
ECHO %TIME% >> %LOG%

C:\Python32\python C:\backupall.py 2>%LOG%
IF %ERRORLEVEL% NEQ 0 GOTO :END
GOTO ENDSILENT


REM Ignore batch version below. It fails. See "Copy of backup.log".


@ECHO OFF
SET BACKUPS=E:

IF NOT EXIST %BACKUPS%\d GOTO CHECKF
GOTO :DONECHECKF
:CHECKF
IF EXIST F:\d SET BACKUPS=F:
:DONECHECKF



IF NOT EXIST %BC% ECHO Error: The backup drive is set to %BACKUPS% and must contain directory %BC% and %BD% to be considered as a backup, so no backup will occur. >> %LOG%
IF NOT EXIST %BC% GOTO END
IF NOT EXIST %BD% ECHO Error: The backup drive is set to %BACKUPS% and must contain directory %BD% to be considered as a backup, so no backup will occur. >> %LOG%
IF NOT EXIST %BD% GOTO END

ECHO.
ECHO Running backup (avoid closing this window or power off until finished)...
ECHO.

@ECHO ON
REM XCOPY /E /C /H /K /I /D /Y C:\WW390VXX %BC%\WW390VXX 1>>%LOG% 2>>%LOG%
REM IF %ERRORLEVEL% NEQ 0 GOTO :END
XCOPY /E /C /H /K /I /D /Y /EXCLUDE:C:\exclude-from-backup.txt C:\ %BC% 2>>%LOG%
IF %ERRORLEVEL% NEQ 0 GOTO :END
XCOPY /E /C /H /K /I /D /Y /EXCLUDE:C:\exclude-from-backup.txt D:\ %BD% 2>>%LOG%
IF %ERRORLEVEL% NEQ 0 GOTO :END
@ECHO OFF

REM /E           Copies directories and subdirectories, including empty ones.
REM              Same as /S /E. May be used to modify /T.
REM /C           Continues copying even if errors occur.
REM /G (WinXP or higher only!) Copies encrypted files to a destination that does not support encryption.
REM /H           Copies hidden and system files also.
REm /K           Copies attributes. Normal Xcopy will reset read-only attributes.
REM /I  Assume destination is a directory if doesn't exist
REM     (otherwise will create giant invisible file if doesn't exist...thanks Windoze)
REM /D:m-d-y     Copies files changed on or after the specified date.
REM              If no date is given, copies only those files whose
REM              source time is newer than the destination time.

GOTO :ENDSILENT

:END
TYPE %LOG%
ECHO Take note of any errors above. They have been saved to %LOG%.

PAUSE

:ENDSILENT