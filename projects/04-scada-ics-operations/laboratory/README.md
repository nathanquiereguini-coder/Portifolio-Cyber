# Laboratório — DNP3 / SCADA / ICS

## Objetivo

Demonstrar análise defensiva de tráfego DNP3 em um laboratório isolado, conectando arquitetura OT, protocolo, evidência de rede e avaliação de risco.

## Fluxo seguro

1. iniciar somente a VM/lab autorizado;
2. identificar Master SCADA e Outstation/RTU simulada;
3. observar a comunicação DNP3 sem alterar sistemas reais;
4. capturar tráfego autorizado no Wireshark;
5. aplicar o filtro `dnp3`;
6. identificar Data Link, Transport e Application Layer;
7. registrar Function Code, IIN e Object Groups;
8. comparar comportamento observado com o baseline;
9. documentar evidências e confiança;
10. produzir recomendações defensivas.

## Evidências a registrar

- timestamp;
- origem/destino;
- porta TCP;
- function code;
- object group/variation;
- valores observados;
- contexto operacional;
- captura `.pcap` sanitizada, quando apropriado.

## Wireshark

O material instrui a usar captura SSHdump na interface `lo` do laboratório e filtro de captura relacionado à porta TCP/20000. Para o portfólio, não publicar credenciais do ambiente didático nem dados de infraestrutura fora do laboratório.

## Entregáveis

- `pcap` sanitizado, se permitido;
- screenshot do dissector DNP3;
- matriz de análise;
- relatório final;
- avaliação de controles.

## Nota de segurança

Não executar testes de exploração, flood, spoofing, replay ou comandos de controle em infraestrutura real. O objetivo do projeto é análise e detecção em ambiente autorizado e isolado.
