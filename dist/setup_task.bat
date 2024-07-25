
    @echo off
    schtasks /create /tn "Automation" /tr "dist\main.exe" /sc onlogon /rl highest
    pause
    