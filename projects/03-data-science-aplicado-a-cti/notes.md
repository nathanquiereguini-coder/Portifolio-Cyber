# Notas — Data Science aplicado a CTI

## 1. Reconhecimento como fonte de dados

O módulo apresenta a fase de reconhecimento como uma etapa de baixo custo e baixo risco para o atacante, na qual informações públicas podem revelar sistemas, serviços e possíveis pontos de exposição. Em CTI, esses dados podem ser transformados em sinais estruturados para análise.

### Reconhecimento ativo x passivo

- **Passivo:** coleta de informações disponíveis publicamente sem interação direta relevante com o alvo.
- **Ativo:** envolve interação direta com a infraestrutura, devendo respeitar autorização e escopo.

## 2. WHOIS

Perguntas úteis durante a análise:

- Quem registrou o domínio?
- Quando o domínio foi criado?
- Qual registrador foi utilizado?
- Existem contatos administrativos ou técnicos disponíveis?
- Quando ocorre a expiração?

Aplicações de CTI citadas no material:

- identificação de domínios de phishing registrados recentemente;
- rastreamento de infraestrutura associada a grupos APT;
- monitoramento da expiração de domínios sensíveis da organização.

## 3. Automação de WHOIS

O exemplo `whois_universal.py` apresenta uma lógica de normalização e roteamento:

1. normalizar o domínio para minúsculas;
2. separar os componentes do domínio;
3. identificar o TLD;
4. consultar um mapeamento de servidores WHOIS;
5. retornar `None` quando o TLD não for suportado;
6. produzir dados estruturados em JSON.

Exemplo apresentado no material:

```bash
python3 whois_universal.py -l ../dominios.txt -o adint.json
cat adint.json | jq .
```

## 4. DNS

DNS traduz nomes de domínio legíveis por humanos em endereços IP utilizados pelos computadores. Em CTI, registros e relações DNS podem ajudar a identificar infraestrutura, subdomínios e vínculos entre ativos.

O módulo reforça novamente dois objetivos operacionais:

- automatização;
- output em JSON.

## 5. Coleta de domínios e subdomínios

O material demonstra o uso do **theHarvester** e do **Subfinder** para ampliar a superfície de descoberta.

Exemplo conceitual:

```bash
theHarvester -b <fontes> -d <dominio>
```

E:

```bash
subfinder -d <dominio>
```

O valor para CTI está na transformação da descoberta em uma lista que possa ser normalizada, enriquecida e correlacionada.

## 6. Shodan

Shodan é apresentado como fonte para observação de serviços expostos e infraestrutura associada a domínios/IPs. A saída pode ser incorporada a um pipeline de enriquecimento.

## 7. Pipelines ProjectDiscovery

O material apresenta exemplos de encadeamento entre ferramentas:

```bash
subfinder -d <dominio> | httpx -status-code -title -tech-detect -fr -web-server -extract-fqdn
```

E:

```bash
subfinder -d <dominio> | naabu -scan-all-ips -top-ports 1000
```

A ideia central é transformar uma etapa de descoberta em um fluxo contínuo de processamento e enriquecimento.

## 8. Do dado bruto à inteligência

Uma arquitetura útil para o portfólio é:

```text
Coleta → Normalização → Validação → Enriquecimento → Correlação → Análise → Disseminação
```

O ponto mais importante não é simplesmente executar ferramentas, mas construir dados consistentes que possam responder a uma pergunta de inteligência.

## 9. Cuidados

O material contém exemplos de credenciais/chaves em slides. **Esses valores não devem ser reproduzidos no portfólio.** O projeto usa placeholders e não armazena segredos.
