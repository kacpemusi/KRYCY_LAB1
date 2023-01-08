#glowny klient obslugujacy pozostale narzedzia
#w trybie CLI - wypisywanie
#GEN.MGMT.1, GEN.MGMG.2
import os
import click
@click.group()
def cli():
    pass

@cli.command()
@click.option('--path','-p', required=True, help='Path to directory with .pcap file to analyze')
@click.option('--bpf','-b', required=False, help='BPF filter to filter packets')
def pcap_handler(path, bpf):
    if bpf==None:
        bpf = ''
    os.system('python3 pcap_handler.py '+path+' '+bpf)
cli.add_command(pcap_handler)

@cli.command()
@click.option('--path', '-p', required=True, help='Path to directory containing files to analyze')
@click.option('--option', '-o', required=True, help='Option to use for the process: re or grep')
@click.option('--regex', '-r', required=True, help='Regular expression for search')
def files_analyzer(path, option, regex):
    if regex==None:
        regex = ''
    os.system('python3 files_analyzer.py '+path+' '+option+' '+'\''+regex+'\'')
cli.add_command(files_analyzer)

@cli.command()
@click.option('--path','-p',required=True, help='Path to the directory that contains files to scan')
@click.option('--option', '-o', required=True, help='Option used for the process: http, blip or all')
def python_scan(path, option):
    os.system('python3 scanner.py python '+path+' '+option)
cli.add_command(python_scan)

@cli.command()
@click.option('--events','-e',required=True, help='Path to the directory that contains events to scan')
@click.option('--rules','-r',required=True, help='Path to the rules used for scan')
def sigma_scan(events, rules):
    os.system('python3 scanner.py sigma '+events+' '+rules)
cli.add_command(sigma_scan)

@cli.command()
@click.option('--interface','-i',required=True, help='Packets will be captured on this interface')
@click.option('--duration','-d', required=True, help='Duration of the packet capture')
def agent_pcap(interface, duration):
    os.system('python3 agent_command.py pcap '+interface+' '+duration)
cli.add_command(agent_pcap)

@cli.command()
@click.option('--name','-n',required=True, help='Name of the file to be downloaded')
def agent_download(name):
    if name == '':
        name ='*'
    os.system('python3 agent_command.py download \''+name+'\'')
cli.add_command(agent_download)

@cli.command()
@click.option('--command','-c',required=True, help='Command to be executed on the remote agent')
def agent_execute(command):
    os.system('python3 agent_command.py execute \''+command+'\'')
cli.add_command(agent_execute)

@cli.command()
def agent_list():
    os.system('python3 agent_command.py list')
cli.add_command(agent_list)

@cli.command()
def agent_ifconfig():
    os.system('python3 agent_command.py ifconfig')
cli.add_command(agent_ifconfig)

if __name__ == '__main__':
    cli()
