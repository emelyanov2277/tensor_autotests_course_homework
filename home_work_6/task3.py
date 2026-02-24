# 1. Вывести список установленных пакетов в консоли cmd/Pycharm и сделать скрин установленных пакетов
# 2. Установить любую стороннюю библиотеку
# 3. Вывести и сделать скрин нового списка установленных пакетов в консоли cmd/Pycharm
# 4. Удалить установленную библиотеку и проверить, что удалилась
#
# Итогом должно быть три скрина: Первый до установки библиотеки, второй после установки библиотеки, третий после удаления.
import nmap
Initial_Port = 50
Final_Port = 60

Target_Host = '127.0.0.1'
Port_Scanner = nmap.PortScanner()

for i in range(Initial_Port, Final_Port + 1):
    output = Port_Scanner.scan(Target_Host, str(i))
    port_state = output['scan'][Target_Host]['tcp'][i]['state']
    print(f'The port number {i} in the range is {port_state}')