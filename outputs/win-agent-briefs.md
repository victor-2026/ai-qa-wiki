# Брифы вин-агенту (релей через человека, SSH не взлетел)

## Бриф 01 (2026-10-02): инвентаризация железа — СТАТУС: выдан, жду ответ

Выполни инвентаризацию этого Windows-ноутбука. Только чтение, ничего не ставить и не менять. Выполни в PowerShell по очереди и верни вывод целиком:

```powershell
systeminfo | findstr /C:"OS Name" /C:"OS Version" /C:"System Model" /C:"System Type" /C:"Total Physical Memory"
wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors /format:list
wmic path win32_videocontroller get name,AdapterRAM /format:list
wmic logicaldisk get caption,size,freespace /format:list
zerotier-cli listnetworks
ipconfig | findstr /C:"IPv4"
```

Верни мне: (1) сырой вывод всех шести команд без сокращений, (2) одной строкой итог: CPU / RAM ГБ / GPU / свободное место на C: / ZT-адрес. Вопросы по ходу — спрашивай до выполнения, не додумывай.
