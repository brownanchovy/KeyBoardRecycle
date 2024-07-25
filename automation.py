import os
import subprocess


def create_exe(script_path):
    # PyInstaller로 파이썬 스크립트를 exe로 변환
    subprocess.run(['pyinstaller', '--onefile', script_path])


def create_task_scheduler_batch(exe_path, batch_file_path):
    # 작업 스케줄러에 추가하는 배치 파일 생성
    batch_content = f"""
    @echo off
    schtasks /create /tn "Automation" /tr "{exe_path}" /sc onlogon /rl highest
    pause
    """
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(batch_content)

def main():
    script_path = 'main.py'  # 자동화할 파이썬 스크립트 경로
    dist_path = 'dist'
    exe_name = 'main.exe'
    batch_file_name = 'setup_task.bat'

    # PyInstaller로 exe 생성
    create_exe(script_path)

    exe_path = os.path.join(dist_path, exe_name)
    batch_file_path = os.path.join(dist_path, batch_file_name)

    # 배치 파일 생성
    create_task_scheduler_batch(exe_path, batch_file_path)

    print(f'Automation is almost Ready')

    #생성되는 bat 파일의 위치 & taskschd.msc에 등록-- 관리자 권한 필요
    batch_file_execute = r'dist\setup_task.bat'
    subprocess.run(['powershell', '-Command', f'Start-Process cmd.exe -ArgumentList "/c {batch_file_execute}" -Verb RunAs'])
    print(f'Automation is Done')

if __name__ == '__main__':
    main()
