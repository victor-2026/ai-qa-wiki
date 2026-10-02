# Win-laptop: включить SSH и прислать 2 строки (инструкция исполнителю)

## Сделать на вин-ноуте (PowerShell as Admin, один раз)

```powershell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd; Set-Service -Name sshd -StartupType Automatic
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

## Прислать маку (в чат) ровно две строки

1. ZT-адрес ноута — из ZeroTier UI или командой:
```powershell
zerotier-cli listnetworks
```
(нужна строка вида `10.24.175.xx`)
2. Вывод команды:
```powershell
whoami
```

## Дальше без тебя

Мак сам зайдет по SSH и снимет инвентаризацию (CPU/RAM/GPU/диски/сеть). Ничего больше на вин-ноуте делать не надо.
